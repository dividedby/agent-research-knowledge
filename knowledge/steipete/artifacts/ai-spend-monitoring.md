# AI Spend Monitoring

When a provider exposes no API for cost or usage — Cursor, Claude Code subscriptions — reconstruct visibility from whatever local signal exists. Unmetered agent spend is a real operational risk, and approximate visibility you build yourself beats flying blind.

Vibe Meter reverse-engineers Cursor's web endpoints for usage data. For Claude Code, where there's no endpoint at all, it goes to the source: parse the multi-hundred-megabyte JSON-L session logs and count tokens with a BPE tokenizer. A `tiktoken`-style tokenizer approximates Anthropic's billing closely enough to be useful, and the counting is SIMD-accelerated so chewing through huge logs doesn't bog the CPU. The principle is that an honest approximation, computed locally, is worth more than an exact number you can't get.

Because the data sources are unofficial and each account is shaped differently, design for graceful degradation rather than correctness guarantees. Cache last-known values so a transient failure doesn't blank the display; back off exponentially on errors instead of hammering an endpoint that's already failing; and when fresh data can't be fetched, show the stale value *with an indicator* rather than crashing. A monitor that dies whenever the unofficial source shifts is worse than no monitor, because you stop trusting it.

This is another instance of building the infrastructure agents and their operators need — see [[close-the-loop-with-purpose-built-tools]] — and like [[agent-status-in-terminal-titles]] it turns an invisible aspect of running a fleet into something you can watch at a glance.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-vibe-meter-monitor-your-ai-cost-e7465ad6.md — https://steipete.me/posts/2025/vibe-meter-monitor-your-ai-costs/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-vibe-meter-2-claude-code-usage--c1968274.md — https://steipete.me/posts/2025/vibe-meter-2-claude-code-usage-calculation/
