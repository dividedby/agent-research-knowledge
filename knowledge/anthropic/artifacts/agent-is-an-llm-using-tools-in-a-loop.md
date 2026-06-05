# An agent is an LLM using tools in a loop

Anthropic's settled, deliberately minimal definition of an agent: **an LLM
autonomously using tools in a loop**, driven by environmental feedback. The
implementation is usually straightforward even when the task is sophisticated —
the agent begins from a command or discussion, plans, then operates
independently, gaining "ground truth" from each tool result or code execution to
assess progress, pausing for human input at checkpoints, and terminating on
completion or a stopping condition (e.g. a max-iterations cap) for control.

This sits at the top of a complexity ladder built from composable patterns, all
resting on one building block — the **augmented LLM** (an LLM with retrieval,
tools, and memory it actively drives). The intermediate rungs are *workflows*,
where LLM calls are orchestrated along predefined code paths:
- **Prompt chaining** — decompose into a fixed sequence of steps, each processing
  the prior output, with optional programmatic gates. For cleanly decomposable
  tasks; trades latency for accuracy.
- **Routing** — classify the input and dispatch to a specialized follow-up,
  letting each path be optimized separately.
- **Parallelization** — run subtasks concurrently (sectioning) or run the same
  task multiple times for higher-confidence aggregation (voting).
- **Orchestrator–workers** — a central LLM dynamically decomposes a task,
  delegates to workers, and synthesizes results. Unlike parallelization, the
  subtasks aren't predefined — the orchestrator decides them from the input
  (e.g. which files a code change touches).
- **Evaluator–optimizer** — one call generates, another evaluates and feeds back
  in a loop; fits tasks with clear criteria where iterative refinement
  measurably helps.

The distinction between *workflow* (predictable, code-defined paths) and *agent*
(model-driven decisions, dynamic tool use) is the load-bearing architectural
choice — workflows for predictability on well-defined tasks, agents for
flexibility on open-ended ones where you can't hardcode the path and can trust
the model's decisions in a sandboxed environment. These are not prescriptive
boxes but patterns to combine; add a rung only when it demonstrably improves
outcomes.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-building-effective-agent-7d24e5fa.md` — https://www.anthropic.com/engineering/building-effective-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-effective-context-engine-42516bb9.md` — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
