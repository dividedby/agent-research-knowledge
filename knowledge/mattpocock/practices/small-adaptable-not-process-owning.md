# Small and adaptable, not process-owning

Matt frames these skills against process-owning frameworks (GSD, BMAD,
Spec-Kit): those try to help by *owning the process*, but in doing so they take
away your control and make bugs *in the process itself* hard to resolve. His
skills are deliberately the opposite — "small, easy to adapt, and composable…
Hack around with them. Make them your own." The design value is keeping the
human in control of the workflow, with each skill small enough to read, edit,
and rewire.

This philosophy explains several recurring shapes in the repo:

- **Model-agnostic.** Skills are designed to "work with any model" — they encode
  engineering discipline in prose and structure, not provider-specific features.
- **Checkpoints over autonomy.** The heavy skills keep handing control back:
  `grill` waits for an answer per question; `to-issues` and `to-prd` get user
  approval on the module/slice breakdown before publishing; `diagnose` shows its
  ranked hypotheses to the user before testing (a "cheap checkpoint, big time
  saver") but proceeds if the user is AFK. Control is offered, not forced.
- **Prototypes are throwaway, and only the answer survives.** `prototype` builds
  code purely to answer one question, marks it as throwaway from day one, skips
  tests/error-handling/abstractions, and insists the only durable output is *the
  answer* (captured to a commit, ADR, issue, or `NOTES.md`) — then delete or
  absorb the code. Speed of learning over artifact preservation. Crucially **the
  question chooses the shape**: a state/logic question gets a tiny runnable
  terminal app, a UI question gets several visible variations on one throwaway
  route. The prototype "is not the product, it is a flashlight" — and it's how you
  answer the high-fidelity questions grilling can't (AI "has no taste for UI", so
  ask for five options and pick, rather than one-shotting). It slots into the
  bigger loop as `grill-with-docs → handoff to prototype → handoff back → to-prd`,
  with the resolved design committed so the agent sees concrete examples by the
  time the PRD is written.
- **Compression as a deliberate mode.** `caveman` exists to cut token usage ~75%
  while keeping technical substance exact — with an auto-clarity exception that
  drops compression for security warnings and destructive-action confirmations.
  Even the terseness knows when control and clarity matter more than economy.

The throughline: the skills supply discipline and leave judgement — and the
steering wheel — with the human.

## The skills are stages of one pipeline, not a framework

Matt is explicit that this composes into a repeatable seven-phase flow — idea →
(research) → (prototype) → PRD → kanban breakdown → execution → QA — that "applies
whether you're using Ralph loops, GSD, Spec Kit, or any other approach." The
distinction from the process-owning frameworks holds: he supplies the *phases and
the discipline within each* (grill to refine the idea, prototype to impose taste,
PRD for the destination, vertical-slice issues for the journey, TDD for quality,
QA looping back into more issues) but you assemble and re-run them yourself,
HITL or AFK, rather than surrendering control to an orchestrator. Research and
prototype assets are deliberately *temporary* — cached in the repo for one sprint
and then removed, because kept too long they go stale and steer the agent wrong
(the same doc-rot logic as `claude-md-is-an-instruction-budget`).

## Sources

- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/skills-repo/skills-engineering-prototype-SKILL.md-aae38256.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/prototype/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-caveman-SKILL.md-3d901941.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/caveman/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-diagnose-SKILL.md-82a24dd7.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/diagnose/SKILL.md
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-prototype-43e38695.md` — origin: https://www.aihero.dev/skills-prototype
- `sources/mattpocock/aihero/https-www.aihero.dev-my-7-phases-of-ai-development-8d95cfb2.md` — origin: https://www.aihero.dev/my-7-phases-of-ai-development
