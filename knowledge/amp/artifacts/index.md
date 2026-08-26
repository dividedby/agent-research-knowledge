# Artifacts — amp

How Amp's team builds agents, documented from the inside: the canonical
line-by-line agent build (*How to Build an Agent* — an LLM + loop + four
read/list/create/edit tools), and the structural patterns the Chronicle draws
out for shaping a codebase *for* an agent (a codebase by an agent for an agent,
feedback-loopable design). Amp is a harness builder writing from the builder's
side, so agent-design material lands here as readily as in `practices/` — let the
concept decide. One concept per file; this index lists them, one line each.

Scope: synthesize the Chronicle's practitioner-guide notes only; the `/news/*`
product-changelog/marketing stream is out of scope.

- [an-agent-is-llm-loop-tools](./an-agent-is-llm-loop-tools.md) — an agent is an LLM, a loop, and tools defined as plain-text contracts; three tools (read/list/edit) are enough for the model to compose its own plan.
- [subagents-as-context-isolated-tools](./subagents-as-context-isolated-tools.md) — subagents are agents-as-tools with their own context window; generic mini-Amps beat specialized ones, gated by what the model wants.
- [codebase-by-an-agent-for-an-agent](./codebase-by-an-agent-for-an-agent.md) — let the agent pick names and layout (the statistically probable ones) and it navigates the codebase far faster.
- [make-it-feedback-loopable](./make-it-feedback-loopable.md) — shape the environment (playground, URL-encoded experiments, headless text CLI) so the agent can validate its own work.
- [permission-system-design](./permission-system-design.md) — sequential allow/ask/reject/delegate rules over irreversible actions; never file-ignore lists.
- [skills-and-task-queue-for-large-migration](./skills-and-task-queue-for-large-migration.md) — CLI-wrapper skills + semantic graph + task-queue handoff + hard definition-of-done gates to run a migration as a factory.
- [dont-make-the-agent-guess](./dont-make-the-agent-guess.md) — idempotent bootstrap, on-demand docs, machine-readable state, and dev-only auth endpoints so a headless remote agent never has to guess or ask.
- [mode-dial-not-model-selector](./mode-dial-not-model-selector.md) — expose agent modes as a "how hard is this task" difficulty dial, not a model picker; Amp wires the model/prompt/tools/effort behind each mode and can rewire it as models improve.
- [orb-is-a-collaboration-surface-not-just-a-vm](./orb-is-a-collaboration-surface-not-just-a-vm.md) — portals, shareable multiplayer threads, schedule-driven wake, and agents spawning/messaging peer orbs turn a disposable remote sandbox into an addressable, orchestrable surface.
