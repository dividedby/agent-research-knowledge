# Practices — anthropic

How the team that *trains the model* teaches **working with** coding agents,
distilled from the in-scope `anthropic.com/engineering` field reports and the
living Claude Code best-practices guide. This is the primary source the rest of
the corpus reacts to secondhand (the ghuntley/Ralph anchoring logic): named,
numbered techniques from internal practice — context engineering ("context rot",
just-in-time context), tool-writing-with-agents, and the workflow discipline the
best-practices guide codifies. One concept per file; this index lists them, one
line each.

Scope: synthesize the agent-engineering field reports only (how to build/work
with coding agents) plus the best-practices guide. Out of scope, left
unsynthesized: safety/alignment, security containment, postmortems,
eval/benchmark, and model-release posts — a topical filter, since the
`/engineering` listing carries no URL signal separating them.

- [context-as-finite-resource](./context-as-finite-resource.md) — context rot and the attention budget: why every standing token must earn its place.
- [just-in-time-context](./just-in-time-context.md) — hold references, retrieve data at runtime; metadata is signal; progressive disclosure.
- [start-simple-add-complexity-only-when-needed](./start-simple-add-complexity-only-when-needed.md) — the simplest thing that works; harness components encode stale assumptions to stress-test.
- [give-the-agent-a-way-to-verify](./give-the-agent-a-way-to-verify.md) — a machine-readable pass/fail closes the loop; the near-perfect verifier is the work.
- [separate-the-doer-from-the-judge](./separate-the-doer-from-the-judge.md) — agents praise their own work; a separate skeptical evaluator/reviewer fixes it.
- [explore-plan-then-code](./explore-plan-then-code.md) — separate exploration from execution; spend planning where it pays; prompt specifically.
- [evaluation-driven-tool-and-agent-development](./evaluation-driven-tool-and-agent-development.md) — improve tools/agents against real-world evals, with the agent as collaborator in the loop.
- [prompt-heuristics-not-rigid-rules](./prompt-heuristics-not-rigid-rules.md) — prompt at the right altitude; frameworks for collaboration; curated canonical examples.
- [manage-the-session-context-actively](./manage-the-session-context-actively.md) — keep the window clean: clear, rewind, scope, steer compaction; the named failure patterns.
