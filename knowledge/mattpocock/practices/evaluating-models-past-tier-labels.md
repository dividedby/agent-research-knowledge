# Model tiers are collapsing; evaluate on effort and price-efficiency, not the brand name

Matt's working shorthand for choosing a model used to be a simple three-bucket
tier: "Opus-like, Sonnet-like, or Haiku-like" — pick the bucket that matches the
task's difficulty and move on. He now says plainly that **"categorising models
got harder recently"** and the bucket has stopped being a reliable proxy: a new
brand (Fable) doesn't obviously slot into any of the three, "Sonnet 5 behaves
like Opus," and a competitor model (GLM 5.2) is genuinely ambiguous — "Opus-like,
or Sonnet 5-like?" The tier label was never the real variable; it was a stand-in
for "how capable is this for the money," and once naming and capability stop
lining up, the stand-in breaks first while the underlying question is still
answerable.

## Two variables the label was hiding

Pressed on why the shorthand broke specifically now, Matt points at two axes
that used to move together with the tier name and now move independently of it
and of each other:

- **Price-efficiency, not just list price.** Sonnet 5 shipped at "a lower price
  but also extremely inefficient" — its token consumption for the same task runs
  fast enough that it ends up "even more expensive than Opus" in practice. A
  cheaper sticker price is not the same claim as a cheaper bill; judging a model
  by its per-token rate alone, without checking how many tokens it burns to do
  the job, gets the comparison backwards.
- **Reasoning effort.** The effort parameter (low/medium/high/xhigh) "has an
  enormous impact too, making everything a lot harder [to evaluate]" — the same
  model name at a different effort setting can behave like a different tier
  entirely, so "which model" and "what effort" are now two separate decisions
  that both need setting, not one bucket choice.

## The practical corollary

Because tier-by-name no longer predicts capability or cost, the only honest
evaluation is empirical and per-task: run the actual candidate models (and
effort settings) against the work you have, and compare real token spend and
output quality rather than reasoning from the brand tier a model is presumed to
sit in. Matt frames this as an open question rather than a settled answer — "so,
I'm asking, how are you evaluating models?" — which is itself the tell that the
old shorthand no longer does the job it used to.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072996604018143557-01bc560b.md` — origin: https://x.com/mattpocockuk/status/2072996604018143557
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072999535068983359-502d9cb9.md` — origin: https://x.com/mattpocockuk/status/2072999535068983359
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072999606749720606-bfad223b.md` — origin: https://x.com/mattpocockuk/status/2072999606749720606
