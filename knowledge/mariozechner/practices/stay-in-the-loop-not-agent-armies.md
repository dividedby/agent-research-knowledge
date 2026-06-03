# Stay In The Loop Not Agent Armies

There are two camps in agentic coding: keep agents on a tight leash and stay in the loop, or orchestrate armies of autonomous agents. Zechner argues the in-the-loop camp is right and the agent-army camp is unproven. There's little evidence that agent-army workflows produce maintainable software anyone actually uses in anger, and its champions rarely ship open, inspectable work to back the claim.

The deeper argument is mechanical: a human is a natural rate-limiter. You can only introduce so many small mistakes per day, and your own aversion to pain means you eventually stop and clean up. An orchestrated army of agents removes that bottleneck. Tiny, individually harmless "booboos" — dead code, nonsensical types, quiet duplication — now compound at a rate no one can absorb. Worse, because you took yourself out of the loop, you feel the pain only when it's far too late, at which point the codebase (and the agent-written tests meant to guard it) can no longer be trusted.

The reframe: the human bottleneck is a feature, not a bug. Deliberately cap how much code you let agents generate per day, sized to your actual ability to review it. Throughput you can't audit isn't throughput — it's deferred collapse. This connects to [[manual-testing-only-trustworthy-oracle]] (the eventual oracle when tests rot) and [[friction-builds-understanding-and-taste]] (slowing down on purpose).

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-12-22-year-in-review-2025-cbb5c6d1.md — https://mariozechner.at/posts/2025-12-22-year-in-review-2025
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-03-25-thoughts-on-slowing-t-e9b43800.md — https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down
