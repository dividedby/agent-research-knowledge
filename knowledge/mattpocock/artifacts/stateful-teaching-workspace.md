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

The distinction is the design lesson — separating the throwaway pedagogical scaffold from the long-lived artifact the learner keeps, rather than conflating both in one document. A later refinement wires the two output types into a navigable web: each lesson links via HTML anchors out to other lessons and reference documents, so the disposable scaffold still threads the learner back to the durable material it distilled from.

## Fluency vs storage strength: difficulty is asymmetric across the two jobs

A later revision sharpens the Knowledge-vs-Skills distinction into an explicit
learning-science frame and makes the two phases pull in opposite directions on
*difficulty*. The skill names two kinds of learning — **fluency strength**
(in-the-moment retrieval) and **storage strength** (long-term retention) — and
warns that fluency gives "an illusory sense of mastery" while storage strength is
the real goal. The design consequence is a deliberate split:

- **For knowledge acquisition, difficulty is the enemy** — it "eats working
  memory you need for understanding," so lessons stay short (lessons are sized to
  the learner's small working memory, "Think Tufte") and each recommends a single
  primary source to read or watch.
- **For skill acquisition, difficulty is the tool** — effortful retrieval is what
  builds storage strength. Skills lessons engineer *desirable difficulty* via
  retrieval practice (recall from memory), spacing (distributing practice over
  time), and interleaving (mixing related topics — for skills practice only).

This is why the workspace separates teaching knowledge from drilling skills rather
than treating "a lesson" as one undifferentiated thing: easing cognitive load is
correct for the first and self-defeating for the second. A small but telling
enforcement of the same principle: quiz answers must be the same length (words and
characters) so formatting leaks no clue — the difficulty has to live in the recall,
not the presentation.

## Zone of proximal development calculation

The `learning-records/` directory functions as memory for optimal challenge level — the agent reads prior records to understand what the user already knows, then teaches "the most relevant thing that fits in their zone of proximal development" based on their mission. This prevents both overwhelming beginners and boring advanced learners.

The learning-record format hardened into an explicit decision-grade-only discipline that mirrors ADRs. A record is written *only* on one of four triggers: demonstrated (not merely-exposed) understanding of something non-trivial, disclosed prior knowledge, a corrected misconception, or a mission shift. "Coverage is not learning. Wait for evidence." Material already in the glossary is not duplicated here, and the file is explicitly *not* a session journal. Crucially, supersession is non-destructive: when a later record contradicts an earlier one, the old one is marked `Status: superseded by LR-NNNN` rather than deleted — "the history of how understanding evolved is itself useful signal." The same one-direction-only revision posture governs the mission: a changed mission updates `MISSION.md` *and* writes a learning record capturing the change (confirmed with the user first).

## Mission-grounded instruction

Every teaching session ties back to the mission file. If unclear or missing, the first task is questioning the user about their "why" — failing to understand purpose means knowledge acquisition becomes untethered from real goals, making exercises feel abstract and providing no guidance for what to teach next.

## The user-facing loop: interview, then report-back-driven lesson selection

From the learner's seat the workspace is driven by a single conversational loop, not a one-shot generation. The skill opens any new mission with a clarifying *interview* before writing anything — why you want to learn this, your current level, what success looks like, and how you prefer to learn — and the answers' specificity directly determines lesson quality. Thereafter each cycle is the same: the learner completes a lesson, returns to the agent, and *reports back* what they learned, what was confusing, and what to focus on next; the agent then writes the next lesson, updates the learning records, and extends the reference material. The intended posture is "talking to a real teacher who knows everything about your progress" — the report-back is the input that re-anchors the agent's zone-of-proximal-development calculation each turn, so the persisted records and the human's spoken-aloud feedback are the *same* steering signal arriving through two channels. This is what makes the file-backed state pay off: state alone is inert; it's the recurring report-back that keeps the next lesson aimed.

## Progressive glossary building

A glossary compresses knowledge into language so complex concepts become building blocks for harder ones, and all lessons adhere to it once created — making it fuel for increasingly sophisticated instruction. Originally a dedicated top-level `GLOSSARY.md`, it was later folded into the `reference/` documents, consistent with the lesson/reference split: the glossary is durable, lookup-oriented reference material, not transient lesson content.

## Promoted out of in-progress, validated on a non-code mission

Matt road-tests `/teach` against a deliberately non-software mission — whether it
can teach him to solve a Rubik's cube — which is the workspace design eating its
own dog food: a real-world "why" (the MISSION), tight interactive feedback loops
(SKILL phase), and a confidence signal so concrete he ordered a speed cube. The
skill is invoked as `/teach me about this codebase`. Having begun life hidden in
the `in-progress/` bucket, it has since earned promotion to `productivity/` — it
now appears in both the top-level and the productivity README listings as a
shipped skill — a worked example of the buckets-and-promotion discipline: a draft
skill stays fully unadvertised until it proves out, then graduates into the
advertised set.

## Why it isn't just a chat: the four design pillars

Asked directly why `/teach` beats "just a ChatGPT conversation," Matt names the
four properties that justify the file-backed workspace over a stateless chat: it
is **stateful across arbitrarily many conversations**, **opinionated about
teaching style** (the pedagogy is baked in, not improvised per session),
**focused on quality, high-trust resources** (the `RESOURCES.md` "never trust
parametric knowledge" discipline), and **built around rich HTML lesson outputs**
rather than ephemeral chat text. This is the designer's own compression of the
whole artifact: each pillar maps onto a workspace mechanism above, and together
they are the argument that durable, mission-grounded structure is what a chat
session structurally cannot supply. The teaching is explicitly turn-by-turn —
"small, incremental lessons towards a much larger mission," with the skill asking
for a specific mission first and structuring everything around it — not a single
big one-shot teaching dump.

## Domain-agnostic by design

The mission-grounded structure is deliberately subject-neutral: Matt road-tests
it not only on codebases but on solving a Rubik's cube (with printable flashcards
generated for retention), introducing a toddler to new foods, and orchestrating
folk-music vocal harmonies — and judges it to work "super well for each one."
He affirms it generalizes to learning to code and (probably) to remodeling a
house, fixing a car, or running local AI inference. Nothing in the workspace
files is software-specific; the same mission → resources → lessons → records loop
carries any skill-acquisition domain, which is why the artifact lives in
`productivity/` rather than a code-tooling bucket.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-teach-SKILL.md-993c30ee.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-MISSION-FORMAT.md-a060ea4c.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/MISSION-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-GLOSSARY-FORMAT.md-40a3046d.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/GLOSSARY-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-RESOURCES-FORMAT.md-270f7fbb.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/RESOURCES-FORMAT.md
- `sources/mattpocock/skills-repo/skills-in-progress-teach-LEARNING-RECORD-FORMAT.md-0e2d7095.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/teach/LEARNING-RECORD-FORMAT.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062973868344524834-0d3780ae.md` — origin: https://x.com/mattpocockuk/status/2062973868344524834
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063002181305868492-1108dcdd.md` — origin: https://x.com/mattpocockuk/status/2063002181305868492
- `sources/mattpocock/skills-repo/skills-productivity-teach-SKILL.md-553d1784.md` — origin: https://github.com/mattpocock/skills/blob/2bf70051928429983de3b5718d277150926f8c89/skills/productivity/teach/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-teach-MISSION-FORMAT.md-0b4bd6fa.md` — origin: https://github.com/mattpocock/skills/blob/2bf70051928429983de3b5718d277150926f8c89/skills/productivity/teach/MISSION-FORMAT.md
- `sources/mattpocock/skills-repo/skills-productivity-teach-GLOSSARY-FORMAT.md-4d0fa89b.md` — origin: https://github.com/mattpocock/skills/blob/2bf70051928429983de3b5718d277150926f8c89/skills/productivity/teach/GLOSSARY-FORMAT.md
- `sources/mattpocock/skills-repo/skills-productivity-teach-RESOURCES-FORMAT.md-86d24ac9.md` — origin: https://github.com/mattpocock/skills/blob/2bf70051928429983de3b5718d277150926f8c89/skills/productivity/teach/RESOURCES-FORMAT.md
- `sources/mattpocock/skills-repo/skills-productivity-teach-LEARNING-RECORD-FORMAT.md-9f6a6596.md` — origin: https://github.com/mattpocock/skills/blob/2bf70051928429983de3b5718d277150926f8c89/skills/productivity/teach/LEARNING-RECORD-FORMAT.md
- `sources/mattpocock/skills-repo/skills-productivity-README.md-8510d914.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/README.md
- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/aihero/https-www.aihero.dev-learn-anything-with-my-teach-skill-887a2686.md` — origin: https://www.aihero.dev/learn-anything-with-my-teach-skill
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063725040252715125-2c79cedc.md` — origin: https://x.com/mattpocockuk/status/2063725040252715125
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063892029470380103-ca01083e.md` — origin: https://x.com/mattpocockuk/status/2063892029470380103
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063691032470978973-4bff2cc5.md` — origin: https://x.com/mattpocockuk/status/2063691032470978973
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063681047770919248-0fc5a82d.md` — origin: https://x.com/mattpocockuk/status/2063681047770919248
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063724639415578954-587ced1f.md` — origin: https://x.com/mattpocockuk/status/2063724639415578954
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063724667613876291-41881487.md` — origin: https://x.com/mattpocockuk/status/2063724667613876291
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063915648711852164-7521b816.md` — origin: https://x.com/mattpocockuk/status/2063915648711852164
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2063682032077562117-5ccdd4fd.md` — origin: https://x.com/mattpocockuk/status/2063682032077562117