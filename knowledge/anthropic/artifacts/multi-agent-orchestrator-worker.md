# Multi-agent orchestrator–worker: parallel subagents that compress

For breadth-first, open-ended work that exceeds a single context window, an
orchestrator–worker multi-agent system outperforms a single agent (Opus 4 lead +
Sonnet 4 subagents beat single-agent Opus 4 by 90.2% on Anthropic's internal
research eval). A lead agent analyzes the query, develops a strategy, and spawns
subagents that explore different aspects **in parallel**, each in its own context
window, returning condensed results the lead synthesizes.

Why it works is almost mechanical: **the essence of search is compression**. Each
subagent burns its own context exploring one facet, then distills the most
important tokens back — separation of concerns (distinct tools, prompts,
trajectories) reduces path-dependency and lets investigations run independently.
The deeper driver is token budget: in the BrowseComp analysis, token usage alone
explained 80% of performance variance, and distributing work across agents with
separate windows is how you spend enough tokens on a problem that overflows one
agent.

The cost is steep and bounds where it applies. Multi-agent systems use ~15× the
tokens of a chat (vs ~4× for a single agent), so they need high-value tasks to be
economical. They fit work that is **heavily parallelizable**, exceeds single-
context limits, and interfaces with many complex tools — and *misfit* domains
needing shared context or tight inter-agent dependencies. Most coding is a misfit:
fewer truly parallel subtasks, and agents aren't yet good at real-time delegation.

Engineering notes that make it production-grade:
- **Prompt the lead to scope subagent effort** — early agents spawned 50
  subagents for trivial queries; the lead's prompt must define division of labor
  and effort budgets, and small lead-prompt changes cascade unpredictably into
  subagent behavior.
- **Subagents write to a filesystem, pass back references** — direct artifact
  output avoids the "game of telephone" of copying large results through the
  coordinator, preserving fidelity and cutting token overhead.
- **State is durable; errors compound.** Long-running agents need checkpoints,
  retry logic, and the ability to *resume* (not restart) from failure; letting the
  agent know a tool is failing and adapt works well.
- **Evaluate by end state, not by prescribed steps** — agents take different valid
  paths, so judge whether the correct final state was reached, and use full
  production tracing (decision patterns, not message contents) to debug the
  non-determinism. The current lead↔subagent execution is synchronous, which
  bottlenecks coordination — an acknowledged limitation.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-multi-agent-research-sys-37ed91c9.md` — https://www.anthropic.com/engineering/multi-agent-research-system
