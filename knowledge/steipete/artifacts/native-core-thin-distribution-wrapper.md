# Native Core Thin Distribution Wrapper

Split an agent tool into a fast native engine and a thin wrapper in whatever ecosystem agents and package managers already prefer. Peekaboo is a Swift CLI — using ScreenCaptureKit for focus-free screen capture — sitting behind a thin TypeScript layer that grants npm distribution and MCP support. The native side does the real work and speaks JSON back to the wrapper; errors travel as proper `errno`/exit codes; a single build-injected version number is shared across both layers so they can never drift.

The point of the split is to refuse the usual trade-off where the CLI is a second-class port of the "real" product. Put the actual capability in the native core so it's first-class and fast. Keep the wrapper deliberately thin so that distribution, installability, and agent-friendliness come almost for free, without dragging logic into a layer that's hard to test and slow to ship.

The directionality is load-bearing: build CLI-first with a thin MCP wrapper over the *same* engine, never an MCP server with a CLI bolted on afterward — see [[cli-over-mcp]]. A clean CLI is usable by humans, scripts, and agents alike; an MCP-first design strands all that capability behind one protocol.

Native binaries should be multi-arch, size-optimized, complete under `--help`, and built on a real argument-parser framework rather than hand-rolled flag parsing. Those properties are what make the core trustworthy to wrap. The wrapper then inherits the standards in [[agent-tool-build-best-practices]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-peekaboo-2-freeing-the-cli-from-007a12df.md — https://steipete.me/posts/2025/peekaboo-2-freeing-the-cli-from-its-mcp-shackles/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-peekaboo-mcp-lightning-fast-mac-9aac2401.md — https://steipete.me/posts/2025/peekaboo-mcp-lightning-fast-macos-screenshots-for-ai-agents/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-mcp-best-practices-500319cb.md — https://steipete.me/posts/2025/mcp-best-practices/
