# Tmux Instead Of Background Bash

pi's bash tool runs strictly **synchronously** — no background processes, dev servers, or REPL interaction. The reasoning is subtractive: background process management drags in process tracking, output buffering, cleanup, and input plumbing, and the feature tends to produce *poor* observability anyway. Claude Code's agent once forgot its own background processes after a compaction.

The substitute is **tmux**. The agent drives long-running servers, debuggers (LLDB), and log-watching through a tmux session it can query — and the human can attach to the same session to co-drive. This keeps the harness minimal while yielding *better* observability than a bespoke background-bash feature would: the session is a real, inspectable, shared surface rather than hidden process state ([[observability-is-the-feature]]).

The slogan is "bash is all you need." Because tmux is just another shell command, the approach works in any harness with a shell — nothing about it is pi-specific. The agent gets persistent interactive processes without the harness having to grow a process manager, and the human gets a window into exactly what the agent is doing. See [[minimal-harness-by-subtraction]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-08-15-mcp-vs-cli-c4a760c5.md — https://mariozechner.at/posts/2025-08-15-mcp-vs-cli
