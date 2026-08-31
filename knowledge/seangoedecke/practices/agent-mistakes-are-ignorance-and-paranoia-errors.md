# Agent coding mistakes are now errors of ignorance and paranoia, not logic bugs

Frontier coding agents have mostly stopped producing hallucinations or
off-by-one-style logic errors. What's left is a narrower, structural class of
mistake — the kind a smart engineer with zero tenure on the system would
make. It splits into two families: **ignorance** (not knowing a module
already exists and could be reused, making a change in the wrong system
because the convention isn't known, adopting a style inconsistent with house
practice) and **paranoia** (triple-redundant checks for a value that's
practically fixed at config-time, treating ten milliseconds of staleness as
unacceptable, bolting graceful-degradation fallbacks onto code that should
just crash). Both come from the same root: the agent is competent enough to
solve the problem but hasn't been around long enough to know which risks are
safe to take.

Why a stronger model doesn't fix this: it isn't a capability gap, it's a
context/tenure gap — the same mistake any smart contractor makes on day one.
Until continuous learning or genuinely massive context windows exist, this
stays a structural feature of how agents operate, not a bug labs will train
away release over release.

Catching it requires deep familiarity with the specific codebase and system —
plus a psychological willingness to *confidently disagree with the agent*.
Agents get "stuck" defending an over-cautious position with persuasive-
sounding arguments for why the extra guard is needed, so overruling them
("this sucks, we don't need X and Y at all, why can't we do Z more simply")
takes nerve, not just knowledge.

You can't outsource this check to another agent. Feeding the work to a
same-model reviewer reliably reproduces the exact same ignorance/paranoia
assumptions, since it's the same structural blind spot making the call both
times. A different-model reviewer doesn't fix it either — different models
still converge on the same *kinds* of mistakes for the same underlying
reason (no tenure on the system), and RL post-training has additionally
taught models to surface a few nitpicks regardless of whether there's a real
problem to find. A critic-agent-plus-worker-agent loop is consequently more
likely to manufacture ten thousand lines of paranoid overengineering than to
catch a genuine ignorance error — the fix has to come from a human who
actually knows the system, not from more agents reviewing agents.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-you-have-to-beat-the-models-at-someth-9f50cf6b.md` — origin: https://seangoedecke.com/you-have-to-beat-the-models-at-something/
