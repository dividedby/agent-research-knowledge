# Tools must be fast, observable, and idiot-proof

The dominant inefficiency in agentic coding is inference cost and *suboptimal
tool usage*. Since the agent burns a full inference round-trip on every tool
interaction, the quality of your tooling sets the ceiling on the whole loop.
Ronacher's rules for a tool — where "anything the agent can interact with or
observe is a tool": a shell script, an MCP server, a log file:

- **Fast.** The quicker the response and the less useless output, the better.
  Crashes are tolerable; *hangs* are the real problem. The difference between a
  tool that runs in 3ms and one that compiles for 5s then boots for a minute is
  the difference between a productive loop and a stalled one — especially for
  the "emergent" tools the agent writes for itself mid-task. If your real
  system is slow, vibe-code a hot-reloading daemon the agent can dump code into.
- **User-friendly.** Tools must clearly report misuse and errors so the agent
  can make forward progress instead of giving up or wandering to another tool.
- **Chaos-monkey-proof.** Assume the LLM will use the tool completely wrong;
  there is "no such thing as user error or undefined behavior." Example: a
  process manager that writes a pidfile and *errors* ("services already
  running") on a second spawn, because the agent otherwise happily binds two
  servers to the same port.
- **Observable and debuggable.** Always log to a file, not just the terminal, so
  the agent can `tail` it to diagnose. Logging *is* a tool: a debug-mode app
  that prints sign-in emails to stdout lets the agent complete a full email
  confirmation flow unaided, once a `CLAUDE.md` line tells it the link is there.

The ideal: useful observability as a *natural byproduct* of the agent writing
code, so the first generation already emits good logs — beating the
write-it, run-it, fail, then bolt-on-debug-logging loop. Balance verbosity:
informative but concise logs save tokens and inference time; if you can't strike
the balance, give the agent knobs to turn verbosity up and down.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-6-12-agentic-coding-92334255.md — https://lucumr.pocoo.org/2025/6/12/agentic-coding/
