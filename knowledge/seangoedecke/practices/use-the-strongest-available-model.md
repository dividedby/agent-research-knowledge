# Use the strongest available model, not a local one

For agentic coding work, default to the strongest model you can afford, not a
weaker local one — the capability gap dominates whatever cost or control a
local model is supposed to buy you.

This isn't just a preference: it's what people actually do once they have a
choice. Everyone's revealed preference is to use the strongest available model
in their price range, and agentic systems make that gap worse than it looks —
as models get more capable, expectations rise with them, and a weaker model
doesn't just perform worse, it stalls out or gets confused mid-loop, which is
far more frustrating than a merely-slower response. A model good enough to do
frontier mathematical work can still be too weak to refactor a large codebase
as well as a strong model would, so "smaller but local" is rarely a good trade
for coding or research use.

Local models also aren't the cost-saver they're assumed to be. Datacenter
inference is cheaper per token because it batches many users' requests on the
same GPU cycles a single local session leaves idle — a datacenter GPU built for
batched inference gets roughly 30x the effective throughput of a consumer GPU
running one user's requests. So a local setup isn't "free compute," it's a
personal, badly-utilized datacenter running at a fraction of the efficiency.

Local models still have a real niche — steerability, offline reliability, or
just wanting to own your own infrastructure — but that niche is chat-style use,
not coding or research, where you want the smartest model available.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-local-models-will-not-win-eea32071.md` — origin: https://seangoedecke.com/local-models-will-not-win/
