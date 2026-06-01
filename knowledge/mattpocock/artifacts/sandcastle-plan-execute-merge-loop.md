# Sandcastle's batch loop: plan → parallel execute+review → merge

`.sandcastle/main.ts` is the "software factory" form of the autonomous loop
([[autonomous-loops-ralph]]): a bounded outer `for` loop (`MAX_ITERATIONS = 10`)
where each iteration runs three phases against the live issue backlog, each phase a
discrete Claude Code agent in a Docker sandbox.

1. **Plan.** An orchestrator agent reads the open issues and emits a `<plan>` tag
   carrying JSON — the parallelizable issues it chose, each with a `number`,
   `title`, and a `branch`. No `<plan>` tag is a hard error; an empty issue list
   ends the whole run. The agent picks the work, exactly as in Ralph — the loop
   just bounds and parallelizes it.
2. **Execute + review, bounded-parallel.** Up to `MAX_PARALLEL = 4` issues run
   concurrently (a hand-rolled acquire/release semaphore over `Promise.allSettled`,
   so one issue's failure is logged but never sinks the batch). Each gets its **own
   Docker sandbox** on its branch, `npm install` on sandbox-ready, then the
   implementer agent; and *only if it produced commits* a reviewer agent runs on
   the same branch. Sandbox isolation per branch is what makes the parallelism safe.
3. **Merge.** A single merger agent takes all branches that produced commits and
   merges them together in one pass (`maxIterations: 10`), given the branch list
   and the issues they close.

Branches with zero commits are dropped before merge; an iteration that produced
nothing to merge just continues to the next.

## Why this shape

It keeps every agent in a fresh, single-purpose context (the smart-zone discipline
of [[keep-the-agent-in-the-smart-zone]]) while getting throughput from fanning out
independent issues — the orchestrator's whole job is choosing work that's *actually*
parallelizable so the per-branch sandboxes don't collide. The bounded iteration and
parallelism caps are the runaway-cost guard Ralph loops always carry, made explicit
as constants. Each phase's prompt is paired with a structured-output contract
([[structured-output-with-session-retry]]) — the planner's `<plan>` tag is parsed
the same disciplined way the review phase's `<output>` is.

This is the **batch** topology. The same repo also drives one-issue-per-event work
through the [[label-driven-agent-ci-pipeline]]; the two coexist — the loop chews a
backlog unattended, the CI workflows handle individually-labelled issues and PRs.

## Sources

- `sources/mattpocock/course-video-manager/.sandcastle-main.ts-9fc6dc1c.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/main.ts
