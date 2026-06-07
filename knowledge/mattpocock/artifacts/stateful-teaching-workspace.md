# Stateful teaching workspace with progressive knowledge capture

The `teach` skill implements learning as a stateful, file-backed workspace where knowledge acquisition happens through structured documents that persist across sessions. Rather than treating each teaching interaction as isolated, the workspace accumulates context through four key files that track mission, terminology, resources, and learning progress.

## The workspace file structure

- **`MISSION.md`** — captures the *reason* the user wants to learn, grounding all instruction in real-world goals rather than abstract study
- **`RESOURCES.md`** — catalogs high-quality, trusted sources for knowledge acquisition, with agent instruction to "never trust your parametric knowledge" before this is populated
- **`learning-records/*.md`** — numbered ADR-style records (`0001-concept-name.md`) capturing non-obvious lessons and key insights that drive future sessions and help calculate the zone of proximal development
- **`lessons/*.html`** — the *primary unit of teaching*: numbered (`0001-name.html`), self-contained HTML files that each teach ONE tightly-scoped thing tied to the mission (see the lesson/reference split below)
- **`reference/*.html`** — durable, compressed cheat sheets (syntax, algorithms, glossaries, yoga poses) designed for quick re-reference
- **`NOTES.md`** — a scratchpad for user teaching preferences and working notes

## Knowledge-Skills-Wisdom progression

Teaching follows a three-phase model: **Knowledge** (gathered from trusted resources, taught via beautiful, citation-littered HTML lessons saved to disk), **Skills** (acquired through interactive lessons with tight, ideally automatic feedback loops), and **Wisdom** (gained by directing users to real-world communities for authentic practice). The workspace files support this progression by providing context for each phase.

## The lesson/reference split: disposable teaching vs durable reference

The output structure hardened over revisions from a single undifferentiated "HTML explainer" into two distinct HTML artifact types with opposite lifespans, codifying that *teaching* and *reference* are different jobs:

- A **lesson** is the primary unit — one self-contained HTML file teaching ONE thing, quickly completable for a tangible win, opened via a single CLI command. Lessons are knowledge-as-skill: only the knowledge required for the target skill, then an interactive feedback loop. They are treated as largely *disposable* — "lessons will rarely be revisited later."
- A **reference document** is the *durable* counterpart — the compressed essence of lessons, formatted for quick lookup and meant to be returned to. Glossaries (previously a top-level `GLOSSARY.md`) folded into reference docs, and the glossary remains the canonical one: "once one is created, it should be adhered to in every lesson."

The distinction is the design lesson — separating the throwaway pedagogical scaffold from the long-lived artifact the learner keeps, rather than conflating both in one document.

## Zone of proximal development calculation

The `learning-records/` directory functions as memory for optimal challenge level — the agent reads prior records to understand what the user already knows, then teaches "the most relevant thing that fits in their zone of proximal development" based on their mission. This prevents both overwhelming beginners and boring advanced learners.

## Mission-grounded instruction

Every teaching session ties back to the mission file. If unclear or missing, the first task is questioning the user about their "why" — failing to understand purpose means knowledge acquisition becomes untethered from real goals, making exercises feel abstract and providing no guidance for what to teach next.

## Progressive glossary building

A glossary compresses knowledge into language so complex concepts become building blocks for harder ones, and all lessons adhere to it once created — making it fuel for increasingly sophisticated instruction. Originally a dedicated top-level `GLOSSARY.md`, it was later folded into the `reference/` documents, consistent with the lesson/reference split: the glossary is durable, lookup-oriented reference material, not transient lesson content.

## Validated on a non-code mission, still in the in-progress bucket

Matt road-tests `/teach` against a deliberately non-software mission — whether it
can teach him to solve a Rubik's cube — which is the workspace design eating its
own dog food: a real-world "why" (the MISSION), tight interactive feedback loops
(SKILL phase), and a confidence signal so concrete he ordered a speed cube. The
skill is invoked as `/teach me about this codebase` and still lives in the
`in-progress/` bucket — consistent with the buckets-and-promotion discipline,
where a draft skill is fully hidden (unadvertised) until it earns promotion.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-teach-SKILL.md-993c30ee.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-MISSION-FORMAT.md-a060ea4c.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/MISSION-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-GLOSSARY-FORMAT.md-40a3046d.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/GLOSSARY-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-RESOURCES-FORMAT.md-270f7fbb.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/RESOURCES-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-LEARNING-RECORD-FORMAT.md-0e2d7095.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/LEARNING-RECORD-FORMAT.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062973868344524834-0d3780ae.md` — origin: https://x.com/mattpocockuk/status/2062973868344524834
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063002181305868492-1108dcdd.md` — origin: https://x.com/mattpocockuk/status/2063002181305868492