# Verification as the new bottleneck

Creation is now near-free; verification and understanding are not. Once an LLM
can generate code faster than any human, the constraint on shipping reliable
software stops being "can we write it" and becomes "can we trust it" — so the
discipline worth investing in shifts from generation speed to verification
depth.

## Why this is forcing a chasm-crossing

Huntley's hypothesis is that formal verification and deterministic system
testing — long a niche, specialist discipline — are about to go mainstream,
because two curves crossed at once: the volume of code and code-change any
team now produces has exploded (an "infinite software crisis" where
traditional code review no longer scales), while the supply of practitioners
skilled in formal verification has not grown to match. Manual review that
worked at hand-written-code volumes cannot be the check on AI-generated
volumes.

## The mechanism: forced determinism, not more reviewers

The response isn't hiring more reviewers — it's removing the need for
reviewers to hold the whole system in their head by making failures
reproducible. Building or retrofitting a deterministic simulator for a system
is now cheap enough to be practical, and it's the only technique that
surfaces entire classes of bugs that never show up under nondeterministic
real-world execution, because it makes *anything* about the system's
behavior reproducible on demand.

Huntley names a three-part "software factory" stack that operationalizes this
for teams that don't have in-house formal-verification expertise:
deterministic/simulation-based system testing, adversarial code review
performed by an LLM, and language analyzers wired into pre-commit hooks. The
point of combining them is that people *and* agents can ship reliable
software without themselves mastering the specialized theory — the stack
substitutes for that expertise rather than requiring the team to acquire it.

This sharpens the developer/engineer split (see
`software-engineering-vs-development.md`): if engineering means failures are
unacceptable, verification infrastructure — not typing speed — is what makes
that standard achievable at AI-generation volumes.

## Sources

- `sources/ghuntley/blog/https-ghuntley.com-slop-cdf1e385.md` — origin: https://ghuntley.com/slop/
