# Tune the routine, not the PR

An autonomous routine that opens PRs all day only stays useful if reviewing
each one is cheap — so the routine has to manufacture the evidence a reviewer
would otherwise have to derive by hand, and when a PR comes back wrong, the fix
belongs in the routine's prompt, not in that one PR.

Boris ran eleven daily maintenance routines unattended against Anthropic's own
apps for weeks — crash fuzzer, ant-only shipper, logic simplifier, logic
bugfixer, dup unifier, dead-code removal, useless-test pruner, shipped-feature
inliner, flaky-test fixer, abstraction improver, abstraction police — one
instance per surface (iOS, Android, Desktop, web, CLI, Agent SDK). Every job is
mechanical, verifiable, and endless: the maintenance backlog nobody gets to,
never feature work. This is the receipt for [[automation-as-leverage]]'s claim
that moving fixes out of prompts and into infrastructure is the highest-leverage
move available — and it's the operating model for making that infrastructure
trustworthy enough to run without anyone watching.

**Evidence in, not confirmation out.** Unlike [[safe-maintenance-audits]]'s
`/checkup` — which earns trust by pausing and asking before it touches
anything — these routines never pause; they earn trust by making their own
output self-checking. The prompt demands proof directly: *"each pr must run
`/verify` and post a repro and truth table to the pr."* Logic-heavy routines go
further — *"formally model the logic also to spot gaps and duplication and to
make sure all edge cases are well tested"* before touching it. A truth table
does double duty: it turns "trust me, this refactor is equivalent" into
something a reviewer checks in seconds, and enumerating every case is how the
routine *finds* the gaps and duplication it's supposed to fix — the
verification artifact and the discovery method are the same work. This also
means running against real, running apps, never mocks — a crash fuzzer against
a mock only finds mock bugs, extending [[verification-is-the-number-one-tip]]
to autonomous, no-human-in-the-loop runs.

**Probe, then act, when you can't derive the fact statically.** The dead-code
routine shows the pattern for any irreversible cleanup: static analysis only
proves the easy half (code nothing references) — reachable-but-never-run code
is the stuff that accumulates for years, and no analyzer can tell you it's safe
to cut. So the routine doesn't guess: day one adds instrumentation and gathers
evidence, day two deletes whatever never fired. A routine on a daily cadence
can afford that patience. The design wasn't specified — the whole ask was eight
words, *"also do one for dead code removal"* — Claude worked out the two-phase
shape was necessary on its own, the production form of "give judgement, not
rules" ([[context-engineering-judgement-over-rules]]).

**The debugging habit that makes it compound.** When a PR comes back wrong, the
instinct is to fix that PR. Boris fixes the routine instead — he doesn't rewrite
the prompt himself, he asks Claude to tune its own routine — and lets tomorrow's
run produce a better PR unattended: *"Claude generally gets these PRs right on
the first shot, and if it doesn't, we ask Claude to tune its routines so it's
better the next day. Sometimes it takes a few days of tuning."* One-off fix
buys one better PR; fixing the routine buys every future PR — [[automation-as-leverage]]'s
"fix the class, not the instance" applied to the maintenance system's own
feedback loop. The corollary: judge a routine on its trend across a week, not
its first output.

**Set expectations with the actual number, and keep both review gates.** Over a
few weeks across six surfaces: 388 PRs opened, 180 merged — 46%. Not a
validation of "ship on trust": roughly half is an excellent return on code
nobody was going to write, and a bad one if you assumed higher. Nothing merges
unreviewed — every PR still passes Claude Code Review, then human review;
automation generates the work, it doesn't approve it. With generation nearly
free, the real bottleneck moves downstream to review throughput, not routine
output.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
