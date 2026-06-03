# Agent As Universal Computer

The mental shift that unlocks the most value is reframing the coding agent from "a smarter command line for code" to a *universal computer interface* that happens to run in text. Once it clicks, you stop scripting and start stating intent at a higher level of abstraction: "organize these files by date, compress anything older than 30 days." You describe the outcome; the agent figures out the commands.

A CLI-first agent has full filesystem access, can execute, read its own output, and iterate — so it absorbs whole categories of work that were never "coding" at all: OS configuration, machine migration, release engineering. The terminal is the substrate precisely because everything on the machine is reachable from it (see [[cli-over-mcp]]). The developer becomes an orchestrator: syntax fades into the background, system thinking moves to the front.

The enabler is removing flow-shattering friction. Pre-authorizing execution (the `--dangerously-skip-permissions` alias) means the agent doesn't stop to ask before every command. Crucially, this is made safe not by caution but by *infrastructure*: hourly snapshots and a working clone make any rogue command recoverable. You buy speed with a safety net, not with hesitation — the same trade that underwrites a [[parallel-agent-fleet-on-main]].

This reframe is upstream of most other practices. If the agent is just a code generator, you sandbox it narrowly; if it's your computer's universal interface, you provision it generously, wire it into everything, and steer it actively. See [[stay-in-the-loop-active-steering]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-claude-code-is-my-computer-eb7a3371.md — https://steipete.me/posts/2025/claude-code-is-my-computer/
