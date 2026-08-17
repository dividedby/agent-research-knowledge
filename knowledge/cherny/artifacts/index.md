# Artifacts — cherny

How Cherny builds or designs the Claude Code harness, where the fan-curated site
documents internals firsthand. Boris Cherny is Claude Code's lead engineer, so
harness-design material (tool design, context management, agent loop internals)
may land here as readily as in `practices/` — let the concept decide. One
concept per file; this index lists them, one line each.

- [customization-checked-into-git](./customization-checked-into-git.md) — vanilla by default; every customization is committed config (settings.json, commands, agents, skills) the team shares.
- [hooks-deterministic-lifecycle-integration](./hooks-deterministic-lifecycle-integration.md) — hooks are the deterministic escape hatch for invariants you refuse to leave to the model.
- [skills-as-the-unit-of-reuse](./skills-as-the-unit-of-reuse.md) — skills package reusable agent knowledge; the 9 production-tested types and progressive disclosure.
- [dynamic-workflows](./dynamic-workflows.md) — the agent writes its own JS harness (parallel/pipeline + nested subagents) for tasks too big for one window.
- [layered-permission-system](./layered-permission-system.md) — safety as defense-in-depth (allowlists, sandbox, classifier auto mode), where the human is the weakest routine layer.
- [safe-maintenance-audits](./safe-maintenance-audits.md) — `/checkup` audits your whole setup for drift but proposes a plan and waits, never mutating silently.
- [context-engineering-judgement-over-rules](./context-engineering-judgement-over-rules.md) — the harness's own system prompt shed 80% of its rules for model judgement; the same shift applies to tool examples and just-in-time loading.
- [tune-the-routine-not-the-pr](./tune-the-routine-not-the-pr.md) — daily autonomous maintenance routines earn trust with evidence-carrying PRs, a probe-then-act pattern for facts you can't derive statically, and fixing the routine instead of the PR.
