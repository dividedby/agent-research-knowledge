# Practices — humanlayer

How HumanLayer approaches building and working with coding agents: stated
principles, process, and the reasoning behind them. One concept per file; this
index lists them, one line each.

- [context-is-the-only-lever](./context-is-the-only-lever.md) — the LLM is stateless; its context window is the only thing you can change to affect output
- [instruction-budget](./instruction-budget.md) — models follow a finite number of instructions (~150–200 for frontier); adherence degrades uniformly as you add more
- [long-context-is-not-capability](./long-context-is-not-capability.md) — bigger windows don't raise the fixed instruction budget; adherence rots, so stay in the smart zone
- [small-focused-agents](./small-focused-agents.md) — scope agents to 3–10 steps; use micro-agents in a deterministic DAG and sub-agents as context firewalls
- [context-efficient-backpressure](./context-efficient-backpressure.md) — verify the agent's work but surface only errors (a single ✓ on success) to protect context
- [harness-engineering](./harness-engineering.md) — agent failures are usually a config problem, not a model problem; tune CLAUDE.md, MCP, skills, sub-agents, hooks — start simple
- [claude-md-highest-leverage-surface](./claude-md-highest-leverage-surface.md) — CLAUDE.md hits every session; keep it concise, universally applicable, progressive-disclosure, hand-crafted
- [claude-md-is-not-a-linter](./claude-md-is-not-a-linter.md) — never make an LLM enforce style; use deterministic linters/formatters and a Stop hook
- [frequent-intentional-compaction](./frequent-intentional-compaction.md) — design the whole workflow around context: research→plan→implement, distilling to artifacts at 40–60% utilization
- [review-research-and-plans-not-code](./review-research-and-plans-not-code.md) — focus human review upstream where leverage is highest, and use it for mental alignment
- [agents-are-mostly-software](./agents-are-mostly-software.md) — 12-factor agents: own your prompts, context, tools, and control flow around a stateless model
- [context-forking](./context-forking.md) — the context window is a stack you can only push/pop; fork it to course-correct, explore, or salvage
- [ralph-dumb-loops-and-declarative-specs](./ralph-dumb-loops-and-declarative-specs.md) — a dumb while-loop works if the spec is good: declarative specs, carved context, small changesets
