# An agent is a durable workflow with one self-repeating step

Building a good agent revives an old problem: **durable execution** — long-lived
functions that survive crashes, restarts, and network failures without losing
state or duplicating work. Ronacher's take is that you don't need a heavyweight
third-party durable-execution service; you can get remarkably far on just
Postgres, which is what his library **Absurd** (`absurd.sql`, a single SQL file +
a thin SDK) demonstrates. Durable execution = a queue (Postgres does this via
`SELECT … FOR UPDATE SKIP LOCKED`) + a state store that remembers the last seen
execution state.

The model: a *task* dispatches onto a *queue*; a *worker* picks it up; tasks are
split into *steps* run in sequence; each step's result is a *checkpoint* stored
in the DB. On failure or suspend the task re-runs, but checkpoints are reloaded
so completed steps aren't redone — crash at step 5 and steps 1–4 come back from
the store. Steps are never retried, only tasks. Tasks can also `sleep` (come back
in 7 days) or `waitForEvent` (events are cached, so it's race-free).

The insight that ties this to agents: a human-authored workflow is a DAG fixed
ahead of time, but **an agent defines its own adventure as it goes** — so it's a
workflow with essentially *one step that iterates over changing state* until it
decides it's done. Absurd supports this by auto-incrementing the checkpoint name
on repetition: the agent loop's step is `iteration`, then `iteration#2`,
`iteration#3`, and each checkpoint stores only the *new* messages it generated,
not the whole history. So a crashed agent resumes mid-conversation from the
durable log rather than starting over.

The thesis is deliberate minimalism — "durable workflows are absurdly simple but
have been overcomplicated": just a queue and a state store, no compiler plugin,
no separate runtime, especially appealing for software meant to be self-hosted.
It's the same write-your-own-over-a-stable-substrate instinct as
[[build-your-own-agent-abstraction]] and [[own-your-tools-as-skills]], and it
gives the agent loop the replay-from-log property that [[llm-apis-as-state-sync]]
wishes the provider APIs had.

**What five months in production validated.** The core abstractions (tasks,
steps, checkpoints, events, suspend) never had to change — features accreted
around them rather than forcing a rethink. The bets that aged well:

- **Checkpoint replay beats deterministic replay.** Absurd reloads cached step
  results and skips completed work, so code need only be deterministic *inside*
  a step — `Math.random()` or `now()` between steps is fine because only step
  boundaries matter. Far easier to reason about than systems that demand the
  whole workflow function replay deterministically.
- **Thin SDK, fat SQL.** Putting the complexity in `absurd.sql` keeps the SDKs
  tiny (TS ~1,400 LOC; Python ~1,900, mostly colored-function support) vs
  Temporal's ~170k-line Python SDK — you can read the whole SDK in an afternoon
  and debug it. The same minimalism that makes the agent loop legible.
- **Pull-based scheduling.** Workers pull from Postgres as they have capacity —
  no coordinator, no push, no callbacks — which is what makes it trivially
  self-hostable.

Two additions sharpen the fit for *agent* workloads specifically: `beginStep()`/
`completeStep()` (a handle you can inspect *before* committing a result, so you
can model intentional failures and "before/after call" hook APIs — exactly the
shape of an agent turn), and spawn-then-await task results (a parent workflow can
fork child tasks and wait), plus an `absurdctl` CLI (`dump-task --task-id=…`
shows precisely where a run stopped) and a bundled *skill* coding agents
discover to debug workflow state — so the durable substrate is itself
agent-debuggable, the [[fast-observable-tools]] principle applied to its own
internals.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-11-3-absurd-workflows-74b6e133.md — https://lucumr.pocoo.org/2025/11/3/absurd-workflows/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-4-4-absurd-in-production-95bf2818.md — https://lucumr.pocoo.org/2026/4/4/absurd-in-production/
