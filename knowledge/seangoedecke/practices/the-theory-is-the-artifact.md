# The engineer's theory of the system is the real artifact

Following Naur's *Programming as Theory Building*, the primary output of an
engineer is not the code but the **theory** — the mental model of what the program
does and how — held in the engineer's mind. The code is a by-product. You cannot
change a program from the code alone: you first build a theory, change the theory,
then change the code to match.

This reframes what working with agents actually is. Two objections to AI coding
fall out of it, and Goedecke answers both:

- **"AI lets you skip theory-building."** Partly true — offloading work to an agent
  necessarily yields a *less detailed* theory than writing every line by hand. But
  every mental model already glosses over detail (you don't model the assembly your
  code compiles to), so giving up *some* fidelity is not a disaster. The deeper
  point: working with agents *teaches* you how load-bearing your theory is. In
  Goedecke's loop he spins up two or three parallel agents, snap-judges each
  output against his model of the system (rejecting ~80% on sight), carefully
  reviews the plausible ~20%, and only ~10% of agent output reaches his PR. If the
  theory weren't his, he'd be accepting most of what the agents produced — the high
  rejection rate is the evidence the theory is intact.
- **"LLMs can't build theories."** You can watch them do it: agent logs are full of
  explicit hypothesis-forming, testing, and revision, and agents do successfully
  debug million-line codebases (sometimes beating him to it). Whether it's a "real"
  theory or a synthetic equivalent is a metaphysical question he sets aside — if the
  model tests hypotheses and answers correctly about the system, the distinction
  doesn't matter in practice. The caveat: agents are reliable on well-represented
  patterns (CRUD servers, proxies) and shakier on genuinely weird systems.

The real limitation is **retention**: an agent cannot keep its theory of the
codebase: it rebuilds from scratch every spin-up, and documentation provably can't
fully capture a theory (Naur). That agents work at all under this handicap is "a
minor miracle." The next big leap in coding agents is whatever lets them retain a
theory across runs — weight updates, or contexts long enough to hold weeks of work
in one run.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-programming-with-ai-agents-as-theory--34e4468e.md` — origin: https://seangoedecke.com/programming-with-ai-agents-as-theory-building/
