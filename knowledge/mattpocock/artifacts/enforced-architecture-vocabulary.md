# Enforced architecture vocabulary

`improve-codebase-architecture` ships a `LANGUAGE.md` that defines a small, fixed
set of architecture terms and **forbids substitutes**. Every suggestion the
skill makes must use these words exactly — never "component", "service", "API",
or "boundary". The consistency is treated as the point, not a side effect: a
stable vocabulary is what lets the agent reason about structure and lets a human
read a hundred suggestions without re-decoding each one.

## The terms (and what each rejects)

- **Module** — anything with an interface and an implementation; scale-agnostic
  (function, class, package, slice). Rejects "unit/component/service".
- **Interface** — *everything a caller must know*: types, invariants, ordering,
  error modes, config, perf — not just the type signature. Rejects "API" and
  "signature" as too narrow.
- **Depth** — leverage at the interface: lots of behaviour behind a small
  interface. **Deep** = high leverage; **shallow** = interface nearly as complex
  as the implementation. Notably this rejects Ousterhout's own
  implementation-lines-to-interface-lines ratio as "rewards padding"; depth is
  redefined as *leverage*.
- **Seam** (Feathers) — where an interface lives; a place behaviour can be
  altered without editing in place. Deliberately replaces "boundary" because
  that collides with DDD's bounded context.
- **Adapter** — a concrete thing satisfying an interface at a seam (role, not
  substance). **Implementation** (the body of code inside a module) is held
  separate from Adapter on purpose: a module can be a *small adapter with a large
  implementation* (a Postgres repo) or a *large adapter with a small
  implementation* (an in-memory fake). Conflating the two is exactly the
  imprecision the vocabulary guards against.
- **Leverage** / **Locality** — the two payoffs of depth: leverage is what
  *callers* get (capability per unit of interface learned); locality is what
  *maintainers* get (change/bugs/knowledge concentrated in one place).

## Operational tests, not just definitions

The vocabulary comes with falsifiable heuristics so the agent can apply it:

- **Deletion test** — imagine deleting the module. If complexity vanishes it was
  a pass-through; if complexity *reappears across N callers* it was earning its
  keep. This is the primary signal for "shallow".
- **The interface is the test surface** — callers and tests cross the same seam;
  wanting to test *past* the interface means the module is the wrong shape.
- **One adapter = hypothetical seam; two adapters = real seam** — don't
  introduce a seam until something actually varies across it.

The skill explicitly layers two vocabularies: this `LANGUAGE.md` for *structure*
and the repo's own `CONTEXT.md` for *domain* ("the Order intake module", not
"the FooBarHandler"). Mixing them is mandated; drifting out of either is the
failure mode it guards against.

## The vocabulary was later promoted to its own shared skill

This term-set no longer lives inside `improve-codebase-architecture`'s
`LANGUAGE.md`. It was extracted — "generalized for reuse across skills" — into a
standalone model-invoked `codebase-design` skill, and `improve-codebase-architecture`
now *runs* `/codebase-design` for the vocabulary rather than carrying it inline (as
does `tdd` for its interface-design guidance). The terms, the deletion test, and
the seam rules are unchanged; what changed is that the language became shared
infrastructure many skills point at instead of one orchestrator's private appendix.
The full skill, plus its DEEPENING dependency-category model and DESIGN-IT-TWICE
parallel-sub-agent pattern, is covered in `codebase-design-deep-module-vocabulary`.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-LANGUAGE.md-d7d1e1c1.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/LANGUAGE.md
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/skills-engineering-codebase-design-SKILL.md-533bf87d.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/codebase-design/SKILL.md
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
- `sources/mattpocock/skills-repo/skills-engineering-tdd-deep-modules.md-31fec91f.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/tdd/deep-modules.md
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-changelog-ubiquitous-language-gr-ec926d6c.md` — origin: https://www.aihero.dev/skills-changelog-ubiquitous-language-grill-with-docs
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-improve-codebase-architecture-23b24b6b.md` — origin: https://www.aihero.dev/skills-improve-codebase-architecture
