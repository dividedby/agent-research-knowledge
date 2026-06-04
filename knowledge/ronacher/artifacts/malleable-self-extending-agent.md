# A malleable agent that extends itself (Pi)

Pi (Mario Zechner's minimal coding agent, the engine under OpenClaw) is the
harness Ronacher uses almost exclusively, and it embodies one design philosophy:
**software malleable like clay**. When you want a capability the agent lacks, you
don't download an extension or a community skill — you *ask the agent to extend
itself*. It celebrates code writing and running code. (You *can* download
extensions, but the encouraged move is "build it like that one over there, with
these changes.")

The deliberate omission is **MCP**. There's no MCP support — not laziness but
philosophy. MCP tools must load into the system context at session start, which
makes it near-impossible to reload what a tool does without trashing the cache or
confusing the model about how prior invocations worked ([[manual-prompt-cache-points]],
[[skills-over-deferred-tool-loading]]). If you must, you bridge via `mcporter`,
but the native path is self-built skills — Ronacher replaced all his
browser-automation MCPs/CLIs with a skill that just drives CDP, "because this is
just easy and natural" ([[own-your-tools-as-skills]]).

Architectural constraints that self-extension *forces* into the core:

- **Provider-portable sessions.** Pi's AI SDK lets one session hold messages
  from many model providers and avoids leaning into any provider-specific
  feature that can't transfer — the [[build-your-own-agent-abstraction]]
  instinct, made a core requirement.
- **Custom messages in the session.** Beyond model messages, sessions store
  custom messages extensions use for state — some never sent to the model, or
  only partially.
- **Hot reloading.** The agent writes extension code, reloads, tests, loops until
  it works; ships with docs/examples the agent itself reads to extend itself.
- **Sessions are trees.** You can branch and rewind — e.g. side-quest to fix a
  broken tool in a fresh branch without wasting main-session context, then rewind
  and have Pi summarize what happened on the branch ([[isolate-failures-in-subagents]]).

Extensions span registered LLM-callable tools (he loads exactly one — a local
to-do tracker the agent built, where a tool felt right over a CLI despite his
[[cli-over-mcp]] default) and rich TUI components (spinners, file pickers, data
tables — flexible enough to run Doom). His own are agent-built to his spec:
`/answer` (reformats the agent's questions into an input box — he prefers prose
Q&A over structured question tools, so no [[plan-via-a-file-on-disk]] plan mode),
`/review` (branch into a fresh review context — "it makes little sense to throw
unfinished work at humans before an agent has reviewed it"), `/todos`, `/control`
(one Pi prompting another — minimal multi-agent), `/files`. Skills are
disposable — thrown away when unneeded. Taken to its extreme — strip the UI,
wire it to a chat channel — this *is* OpenClaw: software that builds more
software.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-1-31-pi-e44c11e9.md — https://lucumr.pocoo.org/2026/1/31/pi/
