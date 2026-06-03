# Engineer The Codebase For Agents

Stop designing a codebase to be navigable for *you* and start engineering it so an agent works efficiently. Fighting the model's trained-in conventions wastes time and tokens; the winning move is to shape the codebase's surface so the agent's known weak spots never get triggered.

Concretely: cap source files small. Steinberger targets under ~300 LOC and treats 500 as a hard ceiling, because agents make fewer editing mistakes in small files and the limit forces loose coupling and testability as a side effect. Let the model pick conventional doc filenames rather than imposing your own taxonomy — it already knows where things "should" live. Keep per-subsystem docs in a `docs/` folder and force-load them via global config so the agent always opens with engineered context instead of rediscovering the architecture each session.

Start everything as a CLI so the agent can call it and read the output to verify its own work — that closes the loop (see [[close-the-loop-with-purpose-built-tools]] and [[cli-over-mcp]]). Choose languages and dependencies for agent-friendliness, not just for you: popular, well-maintained libraries carry more world knowledge into the model, fast compilers keep the edit-run loop tight, and tools hostile to the command line are a real, recurring tax. Generate gnarly machine files (Xcode's `.pbxproj`) with tooling the agent can drive rather than asking it to hand-edit them.

The throughline: every structural choice either plays to the model's strengths or stumbles into its weaknesses. Pick the former on purpose.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-shipping-at-inference-speed-f7e15b10.md — https://steipete.me/posts/2025/shipping-at-inference-speed/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-vibe-meter-monitor-your-ai-cost-e7465ad6.md — https://steipete.me/posts/2025/vibe-meter-monitor-your-ai-costs/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-mcp-best-practices-500319cb.md — https://steipete.me/posts/2025/mcp-best-practices/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-poltergeist-ghost-keeps-builds--36395e11.md — https://steipete.me/posts/2025/poltergeist-ghost-keeps-builds-fresh/
