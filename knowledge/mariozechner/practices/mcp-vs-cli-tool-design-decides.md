# Mcp Vs Cli Tool Design Decides

Empirically, the MCP-vs-CLI protocol choice barely matters. Across 120 runs (3 terminal-control tasks × 4 tools × 10 reps, with Claude Code as both driver and judge), the same `terminalcp` logic hit 100% success as an MCP and as a CLI, landing within ~2.5% on cost. The protocol is plumbing.

What actually decides outcomes is **tool design**: token-efficient, cleanly-rendered output and clear, example-rich documentation. A well-designed *novel* tool's in-context docs matched the training-data advantage that standard tools like `tmux` and `screen` get for free — and `terminalcp`'s clean output gave it a 39% cost edge over `tmux` on the most complex task. Good design beats familiarity.

Two sharp mechanics are worth carrying forward. First, under Claude Code every bash call triggers a Haiku malicious-command check, which for the CLI variants burned 1.3–2M Haiku tokens versus ~35k for the MCP — MCP quietly skips that scan, an invisible cost asymmetry that has nothing to do with the protocol's merits. Second, the CLI's piping and composability let you post-filter output for token savings the MCP can't match, since you can shape what re-enters context.

The practical rule: build a good, token-efficient CLI first. It is composable, observable, and cheap to iterate on; wrapping an MCP around it afterward is trivial if you ever need one. Reach for MCP only when its narrower advantages (like skipping the bash scan) actually pay off. See [[cli-tools-with-readmes-over-mcp]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-08-15-mcp-vs-cli-c4a760c5.md — https://mariozechner.at/posts/2025-08-15-mcp-vs-cli
