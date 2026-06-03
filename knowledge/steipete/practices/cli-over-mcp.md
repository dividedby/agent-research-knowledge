# Cli Over Mcp

Almost every MCP should have been a CLI. A CLI costs zero context until the moment it is invoked, whereas an MCP is a constant tax — "garbage in your context" sitting there whether or not the agent ever calls it. A CLI is also self-documenting: the agent runs it, hits `--help`, and now has full information on demand; it composes through pipes; and the model already carries world knowledge of standard tools like `gh`, `psql`, and `vercel`, so there is nothing to teach.

The corollary for your own services is direct. Give the agent a CLI, or curl-able endpoints behind an API key, plus one line in the agent file — "logs: axiom or vercel cli" — rather than standing up a bespoke tool server. Steinberger says this as someone who wrote five MCPs himself, so it is hard-won, not reflexive. Reserve MCP only for what a CLI genuinely cannot do, such as rich browser automation where structured bidirectional state matters.

This is [[less-is-more-tooling]] made specific: the context tax and the visibility argument both point to the terminal as the right surface. When you do build the thing the agent calls, the construction discipline lives in [[agent-tool-build-best-practices]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-live-coding-session-building-ar-6d007535.md — https://steipete.me/posts/2025/live-coding-session-building-arena/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-peekaboo-2-freeing-the-cli-from-007a12df.md — https://steipete.me/posts/2025/peekaboo-2-freeing-the-cli-from-its-mcp-shackles/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-mcp-best-practices-500319cb.md — https://steipete.me/posts/2025/mcp-best-practices/
