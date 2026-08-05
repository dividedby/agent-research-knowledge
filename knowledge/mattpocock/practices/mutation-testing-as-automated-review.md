# Mutation testing flushes out tests that don't actually check anything

Floated as an open question rather than a settled workflow, Matt raises
mutation testing as a technique worth wiring into automated agent review:
"Anyone using agents/tools to do mutation testing? Seems like it would ROCK
during automated review for flushing out which branches of the code are
actually covered by tests." The mechanism, stated plainly: it "mutates the
source code and checks if the tests catch it" — deliberately corrupt a branch
and see whether the test suite fails. A test suite that stays green against a
mutated line was never actually exercising that line, no matter what a
coverage report says.

## Why this is a different signal than coverage or property-based testing

Coverage tells you a line *executed* during a test run; it says nothing about
whether the test would notice if that line's logic were wrong. Mutation
testing targets exactly that gap, which is why Matt calls out that it "doesn't
necessarily check for test coverage/utility" the same way plain coverage does
— it's a check on whether tests are *doing work*, not on whether they ran. He
also draws a boundary against a different technique that's sometimes conflated
with it: "Property-based is different" — property-based testing generates
inputs to find cases that violate an invariant, whereas mutation testing
corrupts the implementation and checks the existing suite catches it. Both are
ways of finding weak tests, but from opposite directions (vary the input vs.
vary the code under test).

## The case for wiring it into agent review specifically

The appeal for an agent-driven workflow is that an agent can generate the
mutants and re-run the suite cheaply and repeatedly — the kind of mechanical,
high-volume verification pass agents are well suited to, surfacing exactly the
branches a human reviewer would otherwise have to eyeball for "does this test
really test anything." This is still an idea Matt is floating, not a skill or
workflow he's shipped — worth recording as a named technique and an open
question about tooling, not as an established practice.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083807120886038716-ab8de83b.md` — origin: https://x.com/mattpocockuk/status/2083807120886038716
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083808542960623834-9525345b.md` — origin: https://x.com/mattpocockuk/status/2083808542960623834
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083828027599761546-a9f1add9.md` — origin: https://x.com/mattpocockuk/status/2083828027599761546
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083828169677607074-22f3080e.md` — origin: https://x.com/mattpocockuk/status/2083828169677607074
