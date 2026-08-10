# domain-modeling: the active build-the-glossary discipline

`domain-modeling` is the model-invoked skill that *actively builds and sharpens* a
project's domain model — and its first design decision is to draw a hard line
between active and passive work. Merely **reading** `CONTEXT.md` for vocabulary is
a one-line prose pointer any skill can do; it is explicitly *not* this skill. The
skill fires only when you are **changing the model** — challenging terms,
inventing edge-case scenarios, recording decisions — not when you are consuming
it. (This is why `grill-with-docs`, which builds docs as it interviews, runs
`domain-modeling`, while a skill that only respects existing vocabulary just
references `CONTEXT.md` in passing.)

This is the synthesis-time complement to `shared-language-as-agent-fuel`
(why a glossary pays off) and `adrs-as-agent-memory` (what ADRs are for): this
doc captures the *skill mechanics* that produce them.

## The five in-session moves

The discipline is a set of interventions the agent makes mid-conversation, written
to capture decisions *the moment they crystallise* rather than batching:

- **Challenge against the glossary** — when a term conflicts with `CONTEXT.md`,
  call it out immediately ("your glossary defines 'cancellation' as X, but you
  seem to mean Y").
- **Sharpen fuzzy language** — propose a precise canonical term for an overloaded
  word ("'account' — do you mean Customer or User?").
- **Discuss concrete scenarios** — stress-test relationships with invented
  edge-case scenarios that force precision about boundaries.
- **Cross-reference with code** — when the user states how something works, check
  the code agrees and surface contradictions.
- **Update `CONTEXT.md` inline** — write the resolved term down right there, never
  later.

## CONTEXT.md is a glossary, nothing else

The skill is emphatic that `CONTEXT.md` is "totally devoid of implementation
details" — not a spec, scratch pad, or decision log. The `CONTEXT-FORMAT.md`
companion gives the shape: per-term `**Name**: one-or-two-sentence definition` with
an opinionated `_Avoid_:` list of rejected synonyms, define what a thing *is* not
what it *does*, and only include terms *specific to this project's context* (general
programming concepts like timeouts don't belong). Files are created **lazily** —
the root `CONTEXT.md` appears only when the first term is resolved. Multi-context
repos carry a `CONTEXT-MAP.md` at the root listing each context, where it lives,
and how the contexts relate (event flows, shared types); the skill infers
single-vs-multi from which files exist and asks if unclear.

## ADRs offered sparingly, behind a three-part gate

The `ADR-FORMAT.md` companion makes the ADR deliberately minimal — title plus 1–3
sentences of context/decision/why is a complete ADR; sections like Status,
Considered Options, Consequences are optional and added only when they earn their
place. The discipline is in *when* to offer one: all three must hold —
**hard to reverse**, **surprising without context**, and **the result of a real
trade-off**. Miss any one and you skip it (easy-to-reverse decisions get reversed;
unsurprising ones nobody questions; no-alternative ones record nothing). Worth-
recording cases are spelled out: architectural shape, cross-context integration
patterns, lock-in technology choices, boundary/scope no-s, deliberate deviations
from the obvious path, invisible constraints, and non-obvious rejected
alternatives. This is the exact bar this repo's own `CLAUDE.md` adopts for its
ADRs.

The gate is meant to bite hard in practice, not just in theory: "most sessions
produce a sharper glossary and few or no ADRs, and that's the intended shape."
A session that mints an ADR every time is a sign the gate isn't being applied —
the glossary is the expected steady output, the ADR the rare exception.

## When the glossary itself has drifted, re-run the discipline on it

The five moves above assume a live interview building the glossary forward.
Matt also names the fix for the opposite problem — a glossary that's already
been written but has since become confusing to its own owner. Told by a user
that they were "having a hard time even understand[ing] my own glossary now,"
his answer treats it as the same discipline applied retroactively rather than
a new tool: "go back through it and use the domain-modeling skill to make sure
it's aligned with what you want." A `CONTEXT.md` isn't a write-once artifact —
if it stops being legible, the fix is to re-run the same challenge-and-sharpen
moves against the existing file, not to abandon it or start a fresh one.

## Not deprecated — absorbed and expanded

Asked whether the standalone `ubiquitous-language` skill had been dropped,
Matt corrects the framing: "Opposite - moved into `/domain-modelling`,
integrated more deeply with every part of the process." The skill didn't
disappear when it was folded in (see `shared-language-as-agent-fuel`); it
became a discipline other skills invoke rather than a thing you run on its
own — going from one narrow entry point to something woven through the whole
`grill-with-docs`/`wayfinder` chain is a promotion, not a removal.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-domain-modeling-SKILL.md-afe6b5a2.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/domain-modeling/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-domain-modeling-CONTEXT-FORMAT.md-d4513441.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/domain-modeling/CONTEXT-FORMAT.md
- `sources/mattpocock/skills-repo/skills-engineering-domain-modeling-ADR-FORMAT.md-0fcfff53.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/domain-modeling/ADR-FORMAT.md
- `sources/mattpocock/skills-repo/docs-invocation.md-1ce78905.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/docs/invocation.md
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
- `sources/mattpocock/aihero/https-www.aihero.dev-grill-with-docs-d376dfd1.md` — origin: https://www.aihero.dev/grill-with-docs (revision 2026-07-02 — "most sessions produce a sharper glossary and few or no ADRs")
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2084255866543390766-29f40882.md` — origin: https://x.com/mattpocockuk/status/2084255866543390766
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085674908051275993-c3c44927.md` — origin: https://x.com/mattpocockuk/status/2085674908051275993
