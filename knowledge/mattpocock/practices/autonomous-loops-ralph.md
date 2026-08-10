# Autonomous loops (Ralph)

Ralph is Matt's term for running a coding agent in an unsupervised loop: a bash
script feeds the *same* prompt to the agent over and over, and the agent works a
backlog to completion while you're away. It sits at the end of an evolution —
vibe coding → planning (one context window) → multi-phase plans (a new prompt per
phase) → Ralph — and its defining move is that **the agent picks the next task,
not you.** You define the end state (a PRD); the loop converges on it.

## The loop is the whole idea — keep it simple

Each iteration reads the plan and a progress file, decides the highest-priority
task, explores, implements *one* thing, runs its feedback loops, and commits. The
power is structural, not clever: every iteration starts in a **fresh context
window**, which is precisely why a dumb bash `for` loop outperforms a clever
in-session plugin (see `keep-the-agent-in-the-smart-zone`). A completion sigil
(`<promise>COMPLETE</promise>`) lets the script detect "done" and exit; an
iteration cap prevents runaway cost with a stochastic system. The simplicity is
load-bearing: because Ralph is "just a loop", it's endlessly reshapeable.

## HITL first, then AFK

Matt's strong sequencing advice: start **human-in-the-loop** (`ralph-once.sh` —
run one iteration, watch, rerun) to learn the behaviour and refine the prompt,
then go **away-from-keyboard** (`afk-ralph.sh` — loop with a cap) only once you
trust it. Even pure HITL Ralph beats multi-phase planning, because rerunning one
prompt is nicer than writing a fresh prompt per phase. Risky, architecture-shaping
work stays HITL (those decisions cascade forever); AFK is reserved for the
low-risk remainder. A notification (e.g. WhatsApp ping on completion) removes the
need to babysit.

## What makes a loop safe and good

- **Feedback loops are non-negotiable** — types, tests, lint, and a pre-commit
  hook that blocks on red so the loop *can't* declare false victory. The more
  loops, the higher the quality (see `feedback-loop-is-the-work`).
- **Explicit scope + stop condition** — a living PRD (Anthropic's
  `passes: false`-per-item JSON works well) editable mid-flight, with the files,
  edge cases, and definition of "done" pinned so the agent can't quietly redefine
  the goal (see `durable-briefs-for-afk-agents`).
- **A committed progress file** — short-circuits re-exploration each fresh
  iteration; deleted when the sprint ends.
- **Docker sandbox** — essential insurance for unattended runs: it isolates the
  filesystem so a rogue command can't escape the project (the complement to the
  in-project guardrails in `deterministic-hooks-over-prose-rules`). Trade-off: it
  won't load your global config or user skills.

## The "happy hour" prompt: a deliberate exception to explicit scope

The scoped, converge-on-a-PRD discipline above is Matt's default, but he
carves out one recurring exception on purpose. At the end of each working day
he runs a "happy hour" prompt with none of Ralph's guardrails: "Fuck the
rules, I'm about to finish for the day, just make me something cool." He
checks the result the next morning and either merges it or throws it away —
one example produced an auto-zoom feature for his video editor that he kept.
The move only works *because* it inverts the usual stakes: with the loop's
scope-and-stop-condition discipline reserved for AFK work that has to land
safely unattended, a low-cost, easily-discarded slot is where he can afford to
drop that discipline entirely and let the agent free-associate — the same
autonomy that would be reckless mid-project is fine when the downside is
"delete the branch."

## The loop generalises past features

Anything expressible as "look at the repo, improve one thing, commit" fits the
same machinery — only the prompt changes. Matt runs coverage loops (took a CLI
from 16% to 100%), linting loops, duplication loops (jscpd → extract shared
utilities), and entropy loops (clean up dead code and smells). The task source is
equally swappable — local PRD, GitHub Issues, Linear, beads — and the output can be
PRs rather than commits to main, which turns Ralph into a backlog-triaging engine.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-tips-for-ai-coding-with-ralph-wiggum-440a70a9.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-getting-started-with-ralph-7f6ee75f.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-why-the-anthropic-ralph-plugin-sucks-60344c9c.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-heres-how-to-stream-claude-code-with-af-8595552d.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086206733521695001-dc80f9af.md` — origin: https://x.com/mattpocockuk/status/2086206733521695001
