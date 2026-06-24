# Dynamic workflows: the agent writes its own harness

The most architecturally distinctive artifact in the corpus from the harness
author: a **dynamic workflow** is the agent building its own execution harness on
the fly, custom-built for the task — "Claude can now write its own harness on the
fly." It is the answer to a specific failure mode, not a general upgrade.

**Why it exists.** The default Claude Code harness plans *and* executes in one
context window — highly effective for most coding. It breaks down on
**long-running, massively parallel, or adversarial** tasks: the longer a single
window runs, the more three failure modes (the post names context rot among them)
creep in. A dynamic workflow escapes the single window by spawning and
coordinating subagents.

**What it is, concretely.** A JavaScript file with a few special functions, plus
ordinary `JSON`/`Math`/`Array` for data processing. The two core composition
primitives:

- **`parallel([fns])`** — fan out, run at once.
- **`pipeline(items, ...stages)`** — each item streams through every stage
  independently.

Claude mixes and nests these (and `agent`, `claude -p`, schema/model/isolation
options). The contrast with a *static* workflow is the key insight: a static
workflow must handle every edge case, so it ends up generic; a **dynamic** one is
generated for the task at hand, so it can be specific. Building a mental model of
the primitives lets you nudge Claude's orchestration via prompts.

**The activation trigger drifted** — worth recording as provenance: launch said
the bare word "workflow" in a prompt; Cherny later corrected it to **"use a
workflow"**. (Opus 4.8 era: "mention 'workflow' and Claude builds the
orchestration plan automatically.") Treat the exact trigger as
version-dependent — it's a research preview, "best practices are still
developing," and workflows often use more tokens, so reach for one deliberately.

**Where it pays off.** The built team uses it for migrations, refactors, perf,
batch bug fixes, and catalogue-and-categorize sweeps — and, notably, often for
*non-coding* work ("workflows are sometimes even more useful for non-technical
work"). The orchestrator → implementer → verifiers → fixer pattern is the
canonical shape; `/batch` interviews you then fans out to dozens/hundreds/thousands
of worktree-isolated agents; `/deep-research` is itself a workflow.

**The lower-level primitive** is **nested subagents** — any agent delegating to a
child to keep its own context clean (capped at depth=5 to start), with experimental
`fork: true` skill frontmatter. Where a dynamic workflow is an *orchestrated*
harness, nested subagents are the raw delegation primitive underneath it.

This is the build-side engine under [[autonomous-unattended-operation]]: it is
*how* hundreds of subagents run and self-verify in one session. It composes with
`/goal` (exit condition) and `/loop` (keep going), and reusable workflows are
saved (`~/.claude/workflows`) or distributed as a [[skills-as-the-unit-of-reuse]].

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
