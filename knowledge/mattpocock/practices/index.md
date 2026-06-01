# Practices — mattpocock

How Matt Pocock works with coding agents: process, workflow sequencing, and
agent/LLM principles. One concept per file; this index lists them, one line each.

- [align-before-building-grilling](./align-before-building-grilling.md) — interview the human one question at a time to alignment before any code; a reusable primitive other skills drop into.
- [shared-language-as-agent-fuel](./shared-language-as-agent-fuel.md) — a `CONTEXT.md` glossary captured live cuts tokens and sharpens naming; ADRs reserved for hard-to-reverse trade-offs.
- [adrs-as-agent-memory](./adrs-as-agent-memory.md) — ADRs are the thinnest layer of what code can't say; one stack per bounded context, agent-authored, explored by filename — kill stale design docs and write ADRs instead.
- [feedback-loop-is-the-work](./feedback-loop-is-the-work.md) — building a fast deterministic pass/fail signal is the skill; red-green via vertical slices, never horizontal.
- [design-as-continuous-defense-against-mud](./design-as-continuous-defense-against-mud.md) — agents accelerate entropy, so deep-module design is built into every stage, not saved for cleanup.
- [durable-briefs-for-afk-agents](./durable-briefs-for-afk-agents.md) — specs for away-from-keyboard agents are behavioural and path-free so they outlive a moving codebase.
- [small-adaptable-not-process-owning](./small-adaptable-not-process-owning.md) — skills supply discipline and keep the human in control, unlike process-owning frameworks; model-agnostic, checkpointed.
- [keep-the-agent-in-the-smart-zone](./keep-the-agent-in-the-smart-zone.md) — quality decays as context fills (~40%/120k dumb zone); fresh-context loops, handoff vs compact, and a visible context-budget beat filling the window.
- [claude-md-is-an-instruction-budget](./claude-md-is-an-instruction-budget.md) — never run `/init`; keep CLAUDE.md to what's undiscoverable AND global, push the rest into progressive-disclosure docs and skills.
- [deterministic-hooks-over-prose-rules](./deterministic-hooks-over-prose-rules.md) — enforceable constraints become PreToolUse hooks (exit 2 blocks) rather than prose rules that only lower the odds and cost budget.
- [autonomous-loops-ralph](./autonomous-loops-ralph.md) — run the agent in a fresh-context bash loop that picks its own backlog task; HITL→AFK, sandboxed, feedback-gated, reshapeable to any "improve one thing, commit" task.
- [plan-mode-and-the-plan-loop](./plan-mode-and-the-plan-loop.md) — explore-only plan mode primes context before coding; plan→execute→test→commit, always dictate, configure the planner for legible plans.
- [treat-the-agent-as-an-amnesiac-engineer](./treat-the-agent-as-an-amnesiac-engineer.md) — the agent is a competent engineer with no memory; give it human engineering discipline, design around the amnesia, never delegate your thinking.
- [enforced-vocabulary-as-agent-alignment](./enforced-vocabulary-as-agent-alignment.md) — precise terminology with explicit "avoid" lists prevents concept drift; vocabulary as coordination mechanism ensuring agents, maintainers and users share exact language for exact concepts.
