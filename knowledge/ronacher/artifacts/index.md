# Artifacts — ronacher

How Ronacher builds agents, from firsthand agent-design experience: the concrete
internals he documents from the inside — prompt-cache point placement,
reinforcement messaging in tool responses, failure isolation in subagents, a
shared filesystem across inference tools, and why high-level SDKs break so you
must build your own agent abstraction. Like mariozechner, Ronacher writes from
the builder's side, so agent-design material lands here as readily as in
`practices/` — let the concept decide. One concept per file; this index lists
them, one line each.

- [build-your-own-agent-abstraction](./build-your-own-agent-abstraction.md) — high-level SDKs break on real tool use; drive the loop on the provider SDK yourself.
- [manual-prompt-cache-points](./manual-prompt-cache-points.md) — explicit cache-point placement makes cost predictable; the static prefix shapes the whole design.
- [reinforcement-in-tool-responses](./reinforcement-in-tool-responses.md) — every tool response re-steers the loop: re-anchor goals, hint failures, self-reinforce, force the output tool.
- [isolate-failures-in-subagents](./isolate-failures-in-subagents.md) — absorb messy iteration in a subagent and report only success plus a failure digest.
- [shared-filesystem-across-tools](./shared-filesystem-across-tools.md) — a common (virtual) filesystem so tools compose by path and have no dead ends.
- [llm-apis-as-state-sync](./llm-apis-as-state-sync.md) — message APIs are the wrong abstraction; it's a distributed state-sync problem, borrow from local-first.
- [durable-agent-loop](./durable-agent-loop.md) — an agent is a durable workflow with one self-repeating, checkpointed step (Absurd, on just Postgres).
- [code-as-the-mcp-interface](./code-as-the-mcp-interface.md) — one MCP tool whose input is code: a stateful interpreter the model already knows (pexpect-mcp).
- [skills-over-deferred-tool-loading](./skills-over-deferred-tool-loading.md) — why skills beat Anthropic's deferred MCP loading, from the model internals.
- [malleable-self-extending-agent](./malleable-self-extending-agent.md) — Pi: an agent that extends itself, no MCP, provider-portable tree sessions, hot reload.
- [design-a-language-for-agents](./design-a-language-for-agents.md) — local reasoning, no LSP-split, effect markers, diff stability: designing a language agents read well.
- [agent-driven-issue-triage](./agent-driven-issue-triage.md) — Pi's `.pi` `/is`+`prompt-url-widget`+`/wr` setup: feed issues to the agent but instruct it to distrust the issue.
- [local-models-as-a-first-class-provider](./local-models-as-a-first-class-provider.md) — pick one model+stack and polish it end-to-end inside the harness; tool-param streaming is a product bug (pi-ds4).
