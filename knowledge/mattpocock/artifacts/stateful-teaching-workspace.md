# Stateful teaching workspace with progressive knowledge capture

The `teach` skill implements learning as a stateful, file-backed workspace where knowledge acquisition happens through structured documents that persist across sessions. Rather than treating each teaching interaction as isolated, the workspace accumulates context through four key files that track mission, terminology, resources, and learning progress.

## The workspace file structure

- **`MISSION.md`** — captures the *reason* the user wants to learn, grounding all instruction in real-world goals rather than abstract study
- **`GLOSSARY.md`** — builds shared terminology incrementally, compressing knowledge into language so complex concepts become building blocks for harder ones  
- **`RESOURCES.md`** — catalogs high-quality, trusted sources for knowledge acquisition, with agent instruction to "never trust your parametric knowledge" before this is populated
- **`learning-records/*.md`** — numbered ADR-style records (`0001-concept-name.md`) capturing non-obvious lessons and key insights that drive future sessions and help calculate the zone of proximal development

## Knowledge-Skills-Wisdom progression

Teaching follows a three-phase model: **Knowledge** (gathered from trusted resources, taught via beautiful HTML explainers saved to disk), **Skills** (acquired through interactive exercises with tight feedback loops), and **Wisdom** (gained by directing users to real-world communities for authentic practice). The workspace files support this progression by providing context for each phase.

## Zone of proximal development calculation

The `learning-records/` directory functions as memory for optimal challenge level — the agent reads prior records to understand what the user already knows, then teaches "the most relevant thing that fits in their zone of proximal development" based on their mission. This prevents both overwhelming beginners and boring advanced learners.

## Mission-grounded instruction

Every teaching session ties back to the mission file. If unclear or missing, the first task is questioning the user about their "why" — failing to understand purpose means knowledge acquisition becomes untethered from real goals, making exercises feel abstract and providing no guidance for what to teach next.

## Progressive glossary building

Terms get added to the glossary only after the agent feels confident the user understands them. This creates a living vocabulary that all workspace files adhere to, enabling more sophisticated discussions as the shared language grows. The glossary becomes fuel for increasingly complex instruction.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-teach-SKILL.md-993c30ee.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-MISSION-FORMAT.md-a060ea4c.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/MISSION-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-GLOSSARY-FORMAT.md-40a3046d.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/GLOSSARY-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-RESOURCES-FORMAT.md-270f7fbb.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/RESOURCES-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-LEARNING-RECORD-FORMAT.md-0e2d7095.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/LEARNING-RECORD-FORMAT.md