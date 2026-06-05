# Artifacts — anthropic

How the team that *trains the model* builds agents and harnesses, distilled from
the in-scope `anthropic.com/engineering` field reports — the vendor-side
counterpart to the external harness builders the corpus already tracks
(mariozechner's `pi`, steipete's OpenClaw, amp). Expect harness-internals
material: the initializer-agent / coding-agent split for long-running work,
sub-agent token-return discipline, tool-response namespacing and caps. One
concept per file; this index lists them, one line each.

Scope: synthesize the agent-engineering field reports only. Out of scope:
safety/alignment, security containment, postmortems, eval/benchmark, and
model-release posts (topical filter — see the practices index).

- [agent-is-an-llm-using-tools-in-a-loop](./agent-is-an-llm-using-tools-in-a-loop.md) — the minimal agent definition and the workflow-vs-agent pattern ladder.
- [tool-writing-for-agents](./tool-writing-for-agents.md) — design the agent-computer interface: few high-impact tools, consolidation, namespacing, token budgets.
- [on-demand-tool-discovery](./on-demand-tool-discovery.md) — defer tool loading and search on demand; tool-use examples teach usage schema can't.
- [code-execution-over-tool-calls](./code-execution-over-tool-calls.md) — let the agent orchestrate tools by writing code; filter data before it reaches context.
- [the-think-tool](./the-think-tool.md) — a mid-loop scratchpad for reasoning over fresh tool results, and when it earns its tokens.
- [long-horizon-context-techniques](./long-horizon-context-techniques.md) — compaction, structured note-taking, and sub-agents to work past the context window.
- [long-running-harness-initializer-and-handoff](./long-running-harness-initializer-and-handoff.md) — initializer + coding agent, JSON feature list, per-session git/progress handoff.
- [generator-evaluator-harness](./generator-evaluator-harness.md) — GAN-inspired planner/generator/evaluator loop for autonomous multi-hour building.
- [multi-agent-orchestrator-worker](./multi-agent-orchestrator-worker.md) — parallel subagents compressing into a lead agent; token budget as the driver.
- [agent-teams-parallel-loop](./agent-teams-parallel-loop.md) — many Ralph-loop agents on a shared repo with locks, no orchestrator; the C-compiler build.
- [agent-skills-progressive-disclosure](./agent-skills-progressive-disclosure.md) — SKILL.md folders loaded in levels; unbounded bundled context; code as deterministic tools.
- [meta-harness-decouple-brain-hands-session](./meta-harness-decouple-brain-hands-session.md) — virtualize brain/hands/session as replaceable interfaces; tokens unreachable from the sandbox.
- [claude-code-extension-surface](./claude-code-extension-surface.md) — CLAUDE.md, hooks, skills, subagents, MCP/CLI/plugins, and horizontal scaling, and when to use each.
- [packaging-mcp-servers-as-desktop-extensions](./packaging-mcp-servers-as-desktop-extensions.md) — bundle an MCP server + deps into a one-click .mcpb via manifest.json and user_config.
