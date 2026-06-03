# Artifacts — steipete

How Peter Steinberger's agent tooling is built, where his writing shows concrete
structures or conventions. One concept per file; this index lists them, one line
each.

`steipete` still skews toward `practices/`, but his 2025 build-logs (Peekaboo,
VibeTunnel, Vibe Meter, Poltergeist, Demark) document real agent-tooling patterns
worth capturing here.

- [agent-file-as-organizational-scar-tissue](./agent-file-as-organizational-scar-tissue.md) — the AGENTS.md is grown, not authored: the model appends a note per failure and you delete entries as models improve; persona prompts are poison.
- [close-the-loop-with-purpose-built-tools](./close-the-loop-with-purpose-built-tools.md) — any manual babysitting step becomes a tool the agent calls itself (an "oracle" escalation CLI, screenshot-vision, detached servers); building agent infra is cheap and compounds.
- [agent-tool-build-best-practices](./agent-tool-build-best-practices.md) — design for the agent caller: small powerful tool set, lenient input parsing, self-describing/recoverable tools, clean stdout, offload bulk to a sub-model.
- [native-core-thin-distribution-wrapper](./native-core-thin-distribution-wrapper.md) — fast native engine behind a thin TS/npm wrapper with MCP support; build CLI-first and wrap MCP over the same engine, never the reverse.
- [agent-driven-release-automation](./agent-driven-release-automation.md) — encode the release pipeline as plain debuggable shell scripts so an agent ships from one English instruction; fail-fast pre-release checks beat opaque frameworks.
- [remote-terminal-supervision](./remote-terminal-supervision.md) — expose the agent's terminal to a browser (file stdout + named-pipe stdin, Xterm.js over SSE) so you can observe and redirect a long run from anywhere.
- [ai-spend-monitoring](./ai-spend-monitoring.md) — reconstruct unmetered agent cost from local signal (reverse-engineered endpoints, JSON-L log token-counting) with graceful degradation; unmetered spend is an operational risk.
- [invisible-build-watcher](./invisible-build-watcher.md) — a background file-watcher keeps a fresh binary ready so the agent never debugs stale code; the best such tooling is invisible and agent-aware.
- [compose-battle-tested-libraries](./compose-battle-tested-libraries.md) — wire proven libraries together and let the agent write the glue; rolling your own at the hard edges (ANSI, malformed HTML) costs weeks for worse results.
- [agent-status-in-terminal-titles](./agent-status-in-terminal-titles.md) — have each fleet agent self-report its current action into the terminal title; the status line is the orchestration dashboard for parallel agents.
