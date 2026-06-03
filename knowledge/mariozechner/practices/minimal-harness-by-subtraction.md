# Minimal Harness By Subtraction

A coding-agent harness should be sized to its author's actual workflow, not a feature checklist. Zechner builds `pi` by **subtraction**: every feature must be justified by a concrete personal need, and absent that need it isn't built. No to-dos, no plan mode, no sub-agents, no background bash, no MCP, no compaction — each was considered and cut because he had no real use for it.

The payoff is full observability and control over what enters the model's context ([[observability-is-the-feature]]), which he treats as the paramount lever for code quality. Mature harnesses lose exactly this: they inject context behind your back and quietly change system prompts, tools, and behavior every release, so you can no longer reason about why output shifted. A tiny surface also stays forkable and easy to build alternative UIs on top of.

The generalizable claim is that most "creature comfort" agent features add tracked state and hidden behavior that hurt more than they help. A to-do list is mutable state the model can desync from; compaction silently rewrites history; sub-agents are black boxes ([[context-gathering-before-implementation]]). Stripping them out costs convenience but buys a system you can fully predict.

The minimal core ([[four-tool-coding-agent-core]]) plus a thin extension layer is the structural counterpart: it lets you build entirely different agents without touching the core. Subtraction is not minimalism for its own sake — it is a discipline for keeping the context window, and therefore the model's behavior, legible.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-12-22-year-in-review-2025-cbb5c6d1.md — https://mariozechner.at/posts/2025-12-22-year-in-review-2025
