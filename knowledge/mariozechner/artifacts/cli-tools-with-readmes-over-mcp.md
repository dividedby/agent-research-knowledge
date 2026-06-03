# Cli Tools With Readmes Over Mcp

When the agent already has a shell, prefer small CLI scripts documented by a README over an MCP server. MCP servers dump **all** their tool descriptions into context every session — Playwright MCP costs 21 tools / 13.7k tokens, Chrome DevTools MCP 26 tools / 18k tokens, so 7–9% of the window is gone before any work starts. They also aren't composable (every result must pass back through the agent's context) and are awkward to extend.

A CLI-plus-README inverts all three properties. It is **progressively disclosed**: the agent reads the ~225-token README only when it needs the tool. It is **composable**: outputs pipe and chain, can be saved to disk, and reformatted for token efficiency without round-tripping the model. It is **trivially extensible**: add a script, add a README line. And it is **portable** across any harness with code execution. This is effectively ad-hoc, agent-agnostic "skills" — the pattern existed before Anthropic shipped skills as a feature.

So pi has **no MCP support and no built-in web tools** by design. Instead Zechner maintains a personal agent-tools collection wired in via a `PATH` alias plus an `@README` pointer the agent can follow. The decision of *when* a capability genuinely warrants an MCP server versus a CLI tool is its own design call — see [[mcp-vs-cli-tool-design-decides]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-02-what-if-you-dont-need-ab16af09.md — https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
