# Agent Experience as a Design Target

Matt names a counterpart to developer experience (DX): **agent experience (AX)** —
how well an environment is set up for an *agent* to do good work, measured in
checks, architecture, and free context. The pairing is the point. DX asks how
easy a codebase and toolchain make it for *humans* to do good work (docs,
feedback speed, error quality); AX asks the same of the agent. Treating AX as a
first-class, deliberately-engineered property — not an accident of whatever DX
you happened to build — is what separates a codebase an agent thrives in from one
it thrashes in.

The three levers of AX are concrete:

- **Checks** — deterministic pass/fail signals (types, tests, lints, build,
  pre-commit hooks) the agent can run itself. These are the agent's only honest
  window onto whether its work is correct.
- **Architecture** — structure the agent can navigate and reason about: deep
  modules with simple interfaces, clear boundaries, discoverable layout.
- **Free context** — information the environment surfaces *for free* (a
  `CONTEXT.md` glossary, an `AGENTS.md`/`CLAUDE.md` standing brief, ADRs) so the
  agent doesn't burn turns or tokens rediscovering it.

The framing reframes existing practices as a single discipline: feedback loops,
shared-language glossaries, deep-module architecture, and progressive-disclosure
docs are all *AX investments*. Where DX and AX diverge — an agent doesn't need a
pretty error message but does need a machine-checkable one — design for the agent
explicitly rather than assuming good human ergonomics transfer.

## AX doesn't retire DX

Asked point-blank whether developer experience still matters "now that we're
generating code via agents," Matt refuses the implied trade-off: "AX is
important, but don't underestimate DX. Tools that prioritise both are the
goal." The naming of AX earlier in this doc could read as DX being superseded
— it isn't. Coding tools are still used by humans who read the errors, run the
build, and hold the codebase's shape in their head even when an agent writes
most of the diff; a tool that optimises only for the agent's three levers while
letting human ergonomics rot has just moved the neglect from one axis to the
other. The goal is a tool good for both, not a hierarchy where one retires the
other.

## Codebase size and required context window are a false dichotomy

Asked whether a larger codebase forces a larger working context window, Matt
rejects the premise outright: **"larger code bases don't require more context
window. You just need to structure your codebase in a way that the agent can
navigate it easily."** Size and navigability are independent variables that get
conflated because an *unstructured* large codebase does force the agent to hold
more in its head at once — but the fix is Architecture, not a bigger window.
The concrete levers he names are the AX architecture lever made specific:
**smaller files**, a **more descriptive file system**, and **better context
pointers in `AGENTS.md` files** — each one lets the agent find and load only the
relevant slice on demand instead of front-loading the whole codebase's shape into
context. Treating "big codebase, therefore big context budget" as inevitable
skips the actual fix and pays for it in tokens and smart-zone budget instead (see
`keep-the-agent-in-the-smart-zone`).

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md` — origin: https://www.aihero.dev/ai-coding-dictionary
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079154519556944281-3a12ac20.md` — origin: https://x.com/mattpocockuk/status/2079154519556944281
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088275402292654472-bb05122b.md` — origin: https://x.com/mattpocockuk/status/2088275402292654472
