# Prompt at the right altitude: heuristics, not rigid rules

System prompts and agent instructions should sit at a deliberate **altitude** —
the Goldilocks zone between two failure modes. Too low: engineers hardcode
complex, brittle if-this-then-that logic to force exact behavior, which is fragile
and expensive to maintain. Too high: vague, hand-wavy guidance that gives no
concrete signal or falsely assumes shared context. The target is specific enough
to steer behavior, flexible enough to leave the model strong heuristics to act on.

For multi-agent and long-horizon systems this becomes the primary lever, because
the best prompts are **frameworks for collaboration, not strict instructions** —
they define the division of labor, the problem-solving approach, and the effort
budget, then trust the model to navigate. Anthropic's research agents improved by
encoding how *skilled humans* approach the task (decompose hard questions,
evaluate source quality, judge depth-vs-breadth) as heuristics, and by adding
explicit guardrails against runaway behavior (early agents spawned 50 subagents
for trivial queries). In multi-agent systems small prompt changes to a lead agent
cascade unpredictably into subagent behavior, so what you're really tuning is the
interaction pattern, not any one agent.

Concrete handles that follow from this:
- **Examples are pictures worth a thousand words.** Few-shot is strongly
  advised — but curate a *small set of diverse, canonical* examples that portray
  the expected behavior, rather than stuffing in a laundry list of every edge
  case (which bloats context and crowds out the signal).
- **Structure for legibility.** Distinct sections (background, instructions, tool
  guidance, output spec) via XML tags or Markdown headers — though exact
  formatting matters less as models improve.
- **Test minimal-first.** Start with the smallest prompt on the best model, see
  where it fails, then add instructions and examples targeted at the observed
  failure modes — not speculative ones.
- **Right home for the instruction.** When usage guidance for a tool is long or
  complex, it belongs in the system prompt (broader context) rather than buried
  in the tool description.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-effective-context-engine-42516bb9.md` — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-multi-agent-research-sys-37ed91c9.md` — https://www.anthropic.com/engineering/multi-agent-research-system
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-think-tool-962c879d.md` — https://www.anthropic.com/engineering/claude-think-tool
