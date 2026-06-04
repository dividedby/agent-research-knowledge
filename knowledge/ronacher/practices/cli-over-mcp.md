# Prefer CLIs over MCP

Ronacher's persistent, evidence-backed stance: for an agent that can already run
shell, a command-line tool almost always beats an MCP server. Run the same
GitHub task through the GitHub MCP and through the `gh` CLI — the CLI uses
context far more efficiently and reaches the result quicker. He uses MCP "only
if the alternative is too unreliable," because MCP servers are an extra thing
that can break, and they cost tokens just by existing (the Sentry MCP burns ~8k
tokens loaded eagerly, before doing anything).

The two structural flaws he names:

1. **MCP relies on inference at every step.** Every tool call is an inference
   round-trip; proposals for scaling to many tools all add a *filtering* LLM
   pass on top, which only compounds the problem. This is the same argument as
   [[code-over-inference-for-repeatable-work]] — inference per step doesn't
   scale to automation.
2. **MCP can't compose without inference.** The command line isn't one tool;
   it's a series of tools composed *through a programming language* (bash). The
   agent chains `tmux send-keys`, `sleep`, `tmux capture-pane`, falls back to
   `base64 -d` when encoding fails, and builds up reusable scripts from
   one-liners. None of that composition is available through MCP today.

CLIs aren't free of friction — they're platform-, version-, and
documentation-dependent, can fail on first use, suffer Claude Code's per-command
Haiku security preflight, and force the agent to manage *stateful sessions* it
isn't reliably good at (it loses track of a tmux session, renames it, forgets to
kill it). Those failure modes are what push Ronacher toward two refinements
rather than back to MCP: have the agent [[own-your-tools-as-skills]], and where
statefulness genuinely helps, expose a programming language *through* a single
MCP tool — [[code-as-the-mcp-interface]]. His verdict is that MCP "is actually
pretty great when it works," but in its current form is a dead end that can't
scale to automation because it leans on inference too heavily.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-7-3-tools-d973b4d4.md — https://lucumr.pocoo.org/2025/7/3/tools/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-6-12-agentic-coding-92334255.md — https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-8-18-code-mcps-7d9f20ae.md — https://lucumr.pocoo.org/2025/8/18/code-mcps/
