# Agents don't just speed up building — they lower the threshold for what gets finished

The visible effect of coding agents on personal software isn't "the same projects,
built faster" — it's a different, larger set of projects clearing the bar to exist
at all. Two separate costs drop at once: the cost of *exploring* more variations,
and the cost of the unfamiliar, mechanical plumbing that stands between a working
prototype and something actually shipped.

- **Exploration gets cheap enough to do exhaustively.** Building a small game by
  hand, Goedecke would have had time to try two or three visual themes before
  shipping whichever wasn't obviously bad. With an agent doing the iteration, he
  tried fifteen or twenty before picking one he actually liked. The build-cost
  reduction doesn't just save time on the theme he would have picked anyway — it
  changes which theme gets picked, by making the search space affordable.
- **Unfamiliar plumbing stops being the reason a project dies.** A project he
  "might have built anyway" (the core logic) stayed unshipped for a different
  reason: setting up a database and Stripe felt like too much overhead for
  something uncertain. Scraping an undocumented, inconsistently-structured
  upstream API was "possible with enough effort" but not worth that effort on its
  own. In both cases the blocker wasn't the interesting part of the problem — it
  was the boring part that agents absorb without complaint.

This is why "if AI writes code so well, where's the flood of AI-built products"
undersells what's happening. Writing code was never the only bottleneck to
shipping — the missing flood shows up where the bottleneck actually *was* code:
in speculative personal and side projects that would otherwise have stalled out
as "a GitHub repo with a few commits." A list of things you specifically would
not have built without an agent is a sharper way to measure this than a list of
things an agent helped you build faster.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-weird-projects-i-shipped-with-ai-c200f795.md` — origin: https://seangoedecke.com/weird-projects-i-shipped-with-ai/
