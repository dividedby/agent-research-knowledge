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

## Keep the answer — and now, keep the scaffolding too

The code is disposable *from main*; the *verdict* is the only thing worth
keeping there. Once a prototype settles its question, the answer gets captured
somewhere durable — a commit message, an ADR, an issue — paired with the
question it answered, and any validated decision is folded into the real code.
"A prototype left rotting in the repo has outlived its purpose": the failure
mode this guards against is treating the scaffolding as the deliverable when
the deliverable was always the decision.

The rule for the scaffolding itself changed from *delete* to *demote and keep*.
Earlier revisions deleted or absorbed the prototype once its question was
answered; now the prototype is captured as a **primary source** — the runnable
evidence the answer came from — on a throwaway branch, out of main, never
merged, with a context pointer to that branch left on the implementation
issue. Main stays clean (no tests, no error handling to maintain), but the raw
exploration stays one click away for anyone who wants to re-run it rather than
re-derive it from a paraphrase. The UI branch spells out the same split
concretely: fold the winning variant into the real page, but move the losing
variants and the switcher to the throwaway branch, not the bin — "the full set
of variants is the primary source."

## The test for whether a prototype earned its keep

Pushed back on by a user who found wayfinder's prototype tickets "mostly noise"
during a big planning effort, Matt doesn't defend the prototype step
unconditionally — he names the question that decides whether one was worth
building: "Did the prototypes help you answer any particular question? If
raising the fidelity of the conversation is not useful, then you probably have
to be in charge of saying 'I don't need this prototype.'" The prototype's job
is narrowly to raise the fidelity of a stalled conversation (see
`align-before-building-grilling`'s fidelity split) — not to exist by default —
and he concedes the weakness the critique surfaced rather than dismissing it:
a prototype that doesn't clarify anything is noise, and the user, not the
skill, is the one who has to notice and opt out.

## A mismatched target stack is a known failure mode

A prototype answers questions fastest in the stack it's *written in* — but
Matt's default skews toward web/JS regardless of what the real target is:
asked why AI-built game-dev prototypes diverge so sharply from the shipped
result, a correspondent observed that "for whatever reason it uses JavaScript
to create sims... That's why the end results differ from the prototypes so
much." Matt agrees the mismatch is a real gap and names the fix as a rule the
skill should carry explicitly: "use the same language as the target" —
prototyping in a different stack than the one you'll actually ship in isn't a
neutral shortcut, it quietly answers a different question than the one that
was asked.

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
- `sources/mattpocock/skills-repo/docs-engineering-prototype.md-ccedcc07.md` — origin: https://github.com/mattpocock/skills/blob/d574778f94cf620fcc8ce741584093bc650a61d3/docs/engineering/prototype.md (revision 2026-07-11, origin https://github.com/mattpocock/skills/blob/57f045c45f4805c112985f8f54372cd39d264c55 — prototype kept as a primary source on a throwaway branch instead of deleted)
- `sources/mattpocock/skills-repo/skills-engineering-prototype-SKILL.md-aae38256.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/prototype/SKILL.md (revision 2026-07-11, origin https://github.com/mattpocock/skills/blob/1cdd5933be58639a9b9e60fbb6ea32668d000466 — "capture it when done" replaces "delete or absorb")
- `sources/mattpocock/skills-repo/skills-engineering-prototype-LOGIC.md-48cd948d.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/prototype/LOGIC.md (revision 2026-07-11 — the TUI shell rides to the throwaway branch, the validated reducer/machine lifts into the real module)
- `sources/mattpocock/skills-repo/skills-engineering-prototype-UI.md-0de0c866.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/prototype/UI.md (revision 2026-07-11 — losing variants and the switcher move to the throwaway branch, not the bin)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083290662544285858-8839d197.md` — origin: https://x.com/mattpocockuk/status/2083290662544285858
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083541121980932301-d0bf9e56.md` — origin: https://x.com/mattpocockuk/status/2083541121980932301
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083530330565226635-84dcba9a.md` — origin: https://x.com/mattpocockuk/status/2083530330565226635
