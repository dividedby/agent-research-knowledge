# codebase-design: a shared deep-module vocabulary skill

The architecture vocabulary that once lived inside
`improve-codebase-architecture`'s `LANGUAGE.md` was extracted into a standalone
**model-invoked** `codebase-design` skill, "generalized for reuse across skills."
This is the same fixed term-set described in `enforced-architecture-vocabulary`
(module / interface / depth / seam / adapter / leverage / locality, with
forbidden substitutes and the deletion test) — but promoting it to its own skill
is itself the design move: a vocabulary becomes shared infrastructure that any
skill can reach (`tdd` now points at it for interface-design guidance instead of
bundling its own notes), rather than a private appendix to one orchestrator.

The aim is stated as a triple payoff: **leverage** for callers, **locality** for
maintainers, **testability** for everyone — "a lot of behaviour behind a small
interface, placed at a clean seam, testable through that interface."

## Testability is a first-class part of the vocabulary

Beyond the definitions, the skill bakes in three testability rules that turn
"deep module" into something an agent can act on while writing code:

- **Accept dependencies, don't create them** — inject the gateway, don't `new` it
  inside.
- **Return results, don't produce side effects** — `calculateDiscount(cart):
  Discount` over `applyDiscount(cart): void`.
- **Small surface area** — fewer methods and params mean fewer tests and simpler
  setup.

It also distinguishes **internal seams** (private to a module's implementation,
used by its own tests) from the **external seam** at its interface, and warns not
to expose internal seams through the interface just because tests use them.

## DEEPENING: dependency category decides the test strategy

A companion `DEEPENING.md` answers "how do I safely deepen a cluster of shallow
modules, given what it depends on?" by classifying each dependency into one of
four categories, and the category dictates the seam:

1. **In-process** (pure computation, in-memory) — always deepenable; merge and
   test through the new interface, no adapter.
2. **Local-substitutable** (PGLite for Postgres, in-memory FS) — deepenable if the
   stand-in exists; the seam stays internal.
3. **Remote but owned** (your own services across a network) — define a *port* at
   the seam; inject an HTTP/gRPC adapter in prod, an in-memory adapter in tests.
4. **True external** (Stripe, Twilio) — inject a port; tests provide a mock.

The testing rule is **replace, don't layer**: once tests exist at the deepened
module's interface, delete the old unit tests on the shallow pieces. Tests assert
observable outcomes through the interface and must survive internal refactors —
"if a test has to change when the implementation changes, it's testing past the
interface."

## DESIGN-IT-TWICE: parallel sub-agents to explore alternative interfaces

A second companion operationalises Ousterhout's "design it twice" with sub-agents.
The agent first writes a user-facing framing of the problem space (constraints,
dependency categories, an illustrative sketch) so the human reads while work
proceeds, then spawns **3+ parallel sub-agents**, each handed a *different design
constraint* — minimise the interface; maximise flexibility; optimise the common
caller; design around ports & adapters — and each required to produce a
**radically different** interface (with usage example, what it hides, dependency
strategy, trade-offs). The orchestrator presents them sequentially, compares them
on **depth, locality, and seam placement**, and gives an opinionated
recommendation (or a hybrid). The briefs carry both the `codebase-design`
vocabulary and the project's `CONTEXT.md` vocabulary so every variant names things
consistently. This is the same fan-out-then-compare structure used elsewhere in
the repo (the `review` skill's two-axis parallel sub-agents), applied to interface
design.

## Enforcing the boundary mechanically, not just by convention

An in-progress `setup-ts-deep-modules` skill takes the vocabulary a step
further than description and review: it wires `dependency-cruiser` into a
TypeScript repo so each package's deep-module boundary is a **linted rule**,
not a convention an agent (or reviewer) has to remember to check. A package's
implementation lives hidden in subfolders, reachable only through its
entry-point files, and tests exercise it only through those entry points —
the same "don't expose internal seams through the interface" rule above, now
enforced structurally instead of relying on the agent reading the vocabulary
correctly every time. Where `codebase-design`'s testability rules teach an
agent to *design* a deep module, this is the complementary move of making a
violation *fail the build* rather than pass silent review.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-07-11, origin https://github.com/mattpocock/skills/blob/85804e72bbb83120b3becba0edd22b91abf3aa52/skills/in-progress/README.md — `setup-ts-deep-modules` listed)
- `sources/mattpocock/skills-repo/skills-engineering-codebase-design-SKILL.md-533bf87d.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/codebase-design/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-codebase-design-DEEPENING.md-6d2223b2.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/codebase-design/DEEPENING.md
- `sources/mattpocock/skills-repo/skills-engineering-codebase-design-DESIGN-IT-TWICE.md-7e0e561e.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/codebase-design/DESIGN-IT-TWICE.md
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/skills-engineering-tdd-SKILL.md-29d824ee.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/tdd/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
