# Naive interventionism: weigh the whole delivery, not the nitpick you can point to

People whose job is to *do X* are structurally biased toward believing that
doing X matters more than not doing X — Taleb's "naive interventionism," coined
from doctors over-recommending tonsillectomies because recommending surgery is
what the job rewards, independent of what the evidence supports. Ball applies
the same bias to how engineers judge agent output: a reviewer is primed to find
something to flag, so a throwaway comment or an odd variable name becomes the
verdict — "it writes bad code, it leaves dumb comments" — while the actual
delivery goes unweighed: a feature built end-to-end, frontend and backend,
with internal and external docs and tests, verified in a headless browser with
a recorded walkthrough as proof it works.

The failure isn't that the flaw is imaginary; it's that critique is always
available and always rewarded, so it gets produced regardless of whether it's
proportionate to what shipped. The tell: if your read of agent output is a list
of things you found wrong, check whether that list is weighed against the size
and completeness of the delivery it rode in on — or whether you'd have found
something to flag no matter how good the work was, because finding something is
the job you're already primed to do.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-98-c70ec820.md` — *Joy & Curiosity #98* opening: naive interventionism from Taleb's *Antifragile*, applied to engineers dismissing agent output on surface nits ("dumb comments") while ignoring a feature shipped end-to-end with tests and a recorded proof-of-work video (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-98)
