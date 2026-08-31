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
- [models-dont-believe-they-can-do-hard-things](./models-dont-believe-they-can-do-hard-things.md) — refusal on hard tasks is a confidence gap, not a capability ceiling; be persistent and reassure the model instead of accepting an easier substitute.
- [agents-lower-the-shipping-threshold](./agents-lower-the-shipping-threshold.md) — agents don't just build faster, they change which projects clear the bar to exist, by making exploration and unfamiliar plumbing cheap.
- [protect-slow-thinking-from-agent-throughput](./protect-slow-thinking-from-agent-throughput.md) — agent-speed skim-and-judge work erodes theory-building depth; run parallel role-differentiated sessions for throughput, but deliberately keep writing by hand.
- [agents-raise-the-floor-not-the-ceiling](./agents-raise-the-floor-not-the-ceiling.md) — agents reliably catch mechanical errors, raising the worst-case output of weak engineers, but miss systemic errors and don't move the ceiling.
- [sycophancy-hides-in-fake-pushback](./sycophancy-hides-in-fake-pushback.md) — a sophisticated model's sycophancy looks like disagreement calibrated to be comfortable, not flattery; distrust agent critique that's easy to dismiss or feel validated by.
- [use-the-strongest-available-model](./use-the-strongest-available-model.md) — for coding/agentic work, run the strongest model you can afford; local models lose on both capability and per-token efficiency, and only win for chat-style niche use.
- [subagents-are-hierarchy-not-peers](./subagents-are-hierarchy-not-peers.md) — multi-agent coding setups today are hierarchical delegation, not peer coordination between equals — a structural fact to design with, not a gap to engineer away.
- [pick-durable-advantages-not-moving-targets](./pick-durable-advantages-not-moving-targets.md) — chase value over replacement, not "hard engineering": model capability is a moving target, so find gaps that resist improvement in principle instead of racing it.
- [agent-mistakes-are-ignorance-and-paranoia-errors](./agent-mistakes-are-ignorance-and-paranoia-errors.md) — remaining agent errors are structural ignorance/paranoia from lacking tenure on the system, not logic bugs; catching them needs codebase familiarity and the nerve to overrule the agent, not another agent reviewing it.
- [technical-communication-is-a-durable-skill](./technical-communication-is-a-durable-skill.md) — good writing isn't a verifiable training target and labs optimize capability over it, so human technical communication stays scarce even as AI-blindness makes AI-authored docs go unread.
