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
- [token-economics-as-a-cost-lever](./token-economics-as-a-cost-lever.md) — input (history + system prompt + tool defs) is re-billed every turn and output is the dearer half; shape prompts for fewer output tokens, and canonical vocab tokenizes cheaper.
- [claude-md-is-an-instruction-budget](./claude-md-is-an-instruction-budget.md) — never run `/init`; keep CLAUDE.md to what's undiscoverable AND global, push the rest into progressive-disclosure docs and skills.
- [deterministic-hooks-over-prose-rules](./deterministic-hooks-over-prose-rules.md) — enforceable constraints become PreToolUse hooks (exit 2 blocks) rather than prose rules that only lower the odds and cost budget.
- [autonomous-loops-ralph](./autonomous-loops-ralph.md) — run the agent in a fresh-context bash loop that picks its own backlog task; HITL→AFK, sandboxed, feedback-gated, reshapeable to any "improve one thing, commit" task.
- [plan-mode-and-the-plan-loop](./plan-mode-and-the-plan-loop.md) — explore-only plan mode primes context before coding; plan→execute→test→commit, always dictate, configure the planner for legible plans.
- [treat-the-agent-as-an-amnesiac-engineer](./treat-the-agent-as-an-amnesiac-engineer.md) — the agent is a competent engineer with no memory; give it human engineering discipline, design around the amnesia, never delegate your thinking.
- [enforced-vocabulary-as-agent-alignment](./enforced-vocabulary-as-agent-alignment.md) — precise terminology with explicit "avoid" lists prevents concept drift; vocabulary as coordination mechanism ensuring agents, maintainers and users share exact language for exact concepts.
- [agent-feedback-loops-as-quality-gates](./agent-feedback-loops-as-quality-gates.md) — fast, deterministic feedback loops as non-negotiable constraints; agents excel with clear pass/fail signals that prevent progress until issues are resolved.
- [tracer-bullets-over-horizontal-layers](./tracer-bullets-over-horizontal-layers.md) — small end-to-end functionality slices combat agents' tendency toward "slop"; validates assumptions early through vertical cuts across system layers.
- [prefactor-before-the-easy-change](./prefactor-before-the-easy-change.md) — PRD-decomposition makes prefactoring its own leading slice ("make the change easy, then make the easy change"); ordered list + fresh-session-per-slice means cleanup only happens if it's first.
- [seven-phase-development-methodology](./seven-phase-development-methodology.md) — structured approach from idea through QA that scales across different AI coding tools; enables consistent progress toward shipping quality work.
- [deep-modules-and-gray-box-architecture](./deep-modules-and-gray-box-architecture.md) — restructure codebases into modules with simple interfaces controlling complex implementations; humans own interfaces, agents own internals, tests ensure correctness.
- [personal-software-optimized-integration](./personal-software-optimized-integration.md) — build bespoke applications that integrate deeply with personal workflows; leverage AI for grunt work while preserving human thinking and judgment.
