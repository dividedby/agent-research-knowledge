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

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md (origin: https://www.aihero.dev/ai-coding-dictionary, revision 2026-06-05)
