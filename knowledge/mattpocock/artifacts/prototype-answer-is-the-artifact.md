# Prototype: the answer is the artifact, not the code

`/prototype` builds throwaway code whose only job is to answer one design
question that talking couldn't settle — a flashlight, not the product. The
question decides everything about the exercise: pick the wrong shape and the
prototype answers something nobody asked, wasting the whole exercise.

## The question picks one of two shapes

- **Logic prototype** — a tiny interactive terminal app that pushes a state
  machine or business rule through its awkward cases, printing the full state
  after every action, for "does this state model feel right?" questions.
- **UI prototype** — several visibly different variations on one route,
  switchable from a small control, for "what should this look like?" questions
  — real renders to compare instead of imagined ones.

Both branches keep state in memory and run from one command; the skill
identifies which question it's answering before it writes any code.

## Disposable by design, not by neglect

A good prototype carries no tests, no error handling beyond what makes it run,
no abstractions, and no persistence — polish is explicitly out of scope. The
rule is sharp: "the moment you start hardening it, you've stopped
prototyping." This isn't corner-cutting; it's the point. An artifact whose only
job is to answer one question fast and then disappear gets nothing from being
made durable — durability is effort spent on the wrong deliverable.

## Keep the answer, delete the scaffolding

The code is disposable; the *verdict* is the only thing worth keeping. Once a
prototype settles its question, the answer gets captured somewhere durable — a
commit message, an ADR, an issue, a `NOTES.md` next to it — paired with the
question it answered. Only then does the code get deleted or absorbed. "A
prototype left rotting in the repo has outlived its purpose": the failure mode
this guards against is treating the scaffolding as the deliverable when the
deliverable was always the decision.

## Where it sits: an anytime escape hatch, not a pipeline stage

`/prototype` is a reach-for-it-anytime standalone rather than a fixed step in
the build chain — the escape hatch a stalled grilling session reaches for when
a question is too high-fidelity for conversation to resolve (the "grill →
prototype → grill again" loop; see `align-before-building-grilling`). It is not
for figuring out why something already built is broken — that's
`diagnosing-bugs`'s job; prototyping explores what to build, not why the built
thing is broken. Its answer typically feeds forward: a validated state model or
UI direction becomes settled input for `to-prd` to write up, or an
architectural decision worth recording via `domain-modeling`.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-prototype-43e38695.md` — origin: https://www.aihero.dev/skills-prototype
