# Artifacts — mariozechner

How Mario Zechner's agent tooling is built: the concrete structure of his `pi`
coding-agent harness (the 4-tool minimal core, the TypeScript extension model,
the TUI and unified-LLM layers) and related reverse-engineering tools, where his
writing shows the runtime internals. One concept per file; this index lists them,
one line each.

Unlike the corpus's other subjects, Zechner is a harness *builder*, so material
lands here as readily as in `practices/` — the posts document runtime internals,
not just usage.

- [four-tool-coding-agent-core](./four-tool-coding-agent-core.md) — read/write/edit/bash plus a sub-1000-token prompt is enough, because frontier models are RL-trained on coding harnesses and already know the role.
- [cli-tools-with-readmes-over-mcp](./cli-tools-with-readmes-over-mcp.md) — small CLI scripts documented by a README are progressively-disclosed, composable, extensible, portable "skills before skills"; MCP servers burn 7–9% of the window before work starts.
- [tmux-instead-of-background-bash](./tmux-instead-of-background-bash.md) — keep bash synchronous and drive long-running servers/debuggers through an attachable tmux session, gaining better observability than a bespoke background-process feature.
- [unified-llm-api-leaky-abstraction](./unified-llm-api-leaky-abstraction.md) — a thin layer over four real provider APIs, built directly on their SDKs, with first-class abort, partial-JSON streaming, cross-provider handoff, and a typesafe model registry.
- [split-tool-results-llm-vs-ui](./split-tool-results-llm-vs-ui.md) — a tool returns two channels — a minimal `output` string for the model and a `details` object for the UI — so neither pays for the other's needs.
- [loop-until-done-agent-scaffold](./loop-until-done-agent-scaffold.md) — the loop just runs tool calls until a turn has none, with no max-steps knobs; a thin Agent class adds state, events, message queuing, and a transport abstraction.
- [scrollback-native-tui-differential-rendering](./scrollback-native-tui-differential-rendering.md) — append to native terminal scrollback instead of seizing the viewport; a retained-mode component tree diffs against a backbuffer and redraws from the first changed line.
- [interpreter-as-sandbox-and-csp-bypass](./interpreter-as-sandbox-and-csp-bypass.md) — ship a bundled JS interpreter to run agent code: bypasses CSP and sandboxes by construction, but is honestly not a security boundary against a prompt-injected agent.
- [patch-the-agent-binary](./patch-the-agent-binary.md) — a JS-distributed agent is patchable via string-anchor + brace-match no-ops (strip anti-debug, re-enable /cost, bypass version guards); package as a reusable patch/restore tool.
- [prompts-are-code-state-on-disk](./prompts-are-code-state-on-disk.md) — serialize workflow state to JSON/Markdown files (PLAN.md, TODO.md, a notes scratchpad) for resumability across fresh contexts, not into the ephemeral conversation or a plan mode.
- [local-models-for-private-agents](./local-models-for-private-agents.md) — a fully local voice agent (llama.cpp + STT + TTS) is worth it for privacy; the hard part is the speech-to-speech UX (sentence-chunked streaming, custom barge-in), not the LLM.
