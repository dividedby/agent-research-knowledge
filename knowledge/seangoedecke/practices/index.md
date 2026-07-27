# Practices — seangoedecke

Sean Goedecke is a staff engineer writing firsthand, hype-free essays on
coding-agent architecture decisions and engineering discipline — "Build agents,
not pipelines", "agents and code review", "programming with AI agents as
theory-building", "how I use LLMs as a staff engineer". The additive vantage:
the practitioner-essay layer (steipete/thorstenball) fused with
architecture-decision framing (ronacher/simonw), from a production
staff-engineer lens — not a harness builder, not a minimalist solo practitioner.
Corpus-anchored: thorstenball cites him across five "Joy & Curiosity" roundups.
Material skews here (practices — architecture decisions, engineering discipline,
working-with-agents essays); `artifacts/` is expected to stay sparse. One
concept per file; this index lists them, one line each.

- [agents-over-pipelines](./agents-over-pipelines.md) — when in doubt build an agent, not a pipeline; pipelines only win on bounded cost/context/local-models.
- [the-theory-is-the-artifact](./the-theory-is-the-artifact.md) — the engineer's mental model is the real output; high agent-rejection rate proves the theory is still yours; agents can't retain theories across runs.
- [shift-work-onto-agents-without-going-too-far](./shift-work-onto-agents-without-going-too-far.md) — the 2026 core skill: hand maximum work to agents, single editing pass, but keep public comms and UI human.
- [generate-skills-after-solving-not-before](./generate-skills-after-solving-not-before.md) — ask the agent to write the skill after it solves the problem the hard way, so it distills hard-won knowledge instead of baking in wrong assumptions.
- [prompts-are-technical-debt](./prompts-are-technical-debt.md) — prompts decay silently per model release; stay as unconfigured as possible, keep AGENTS.md to concrete facts.
- [you-cant-eyeball-prompt-quality](./you-cant-eyeball-prompt-quality.md) — an elaborate prompt rides on a model already good at the task; build a benchmark, don't ask the model to grade itself.
- [domain-expertise-is-the-prompting-skill](./domain-expertise-is-the-prompting-skill.md) — the real prompting skill is domain expertise, not technique; expertise is what lets you push a model hard instead of just cling to it.
