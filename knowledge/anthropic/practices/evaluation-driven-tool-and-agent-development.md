# Build tools and agents against evals, with the agent as your collaborator

Tools and agent behaviors should be improved through a measured, evaluation-driven
loop, not hand-tuned by intuition. The cycle: stand up a quick prototype, write a
comprehensive eval, then iterate on the implementation until the agent performs
well on realistic tasks — measuring each change rather than guessing at it. Even
small refinements to a tool description can yield dramatic gains (Anthropic's
SWE-bench results moved on precise tool-description edits alone); without an eval
you can't see them.

What makes the evals good:
- **Ground tasks in real-world usage.** Build them on real data sources and
  services; avoid superficial "sandbox" tasks that don't stress the tools.
  Strong tasks may require many tool calls. Pair each with a verifiable
  outcome — but avoid over-strict verifiers that reject correct answers over
  formatting, and avoid overfitting to one expected tool path when several are
  valid. Hold out a test set to catch overfitting.
- **Start immediately with small samples.** In early development, effect sizes
  are huge (a prompt tweak can move success 30%→80%), so ~20 real-usage queries
  already show you the impact of a change. Don't delay evals waiting to build
  hundreds of cases.
- **Instrument beyond accuracy.** Track tool-call counts, token consumption,
  runtime, and error rates — redundant calls hint at pagination/limit
  rightsizing; invalid-parameter errors hint at unclear descriptions.

The distinctive move is treating **the agent as a collaborator in the loop**.
Have it generate evaluation tasks, analyze transcripts, and refactor tools for
you — paste eval transcripts back into the agent and it will spot contradictory
descriptions, confusing schemas, and inefficiencies, then fix many tools at once
while keeping implementations and descriptions self-consistent. But read its
*reasoning and feedback* (turn on interleaved/CoT output), and read between the
lines: what an agent omits often matters more than what it says, and it doesn't
always say what it means. Most of Anthropic's own tool-writing guidance came out
of repeatedly running this loop with Claude Code against their internal workspace.

This is also how a "think" step or any prompt change should be justified: the
"think" tool's value was established on τ-bench and SWE-bench, not asserted — and
the same benchmarks revealed exactly *when* it helps and when it's dead weight.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-writing-tools-for-agents-4f67b063.md` — https://www.anthropic.com/engineering/writing-tools-for-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-think-tool-962c879d.md` — https://www.anthropic.com/engineering/claude-think-tool
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-multi-agent-research-sys-37ed91c9.md` — https://www.anthropic.com/engineering/multi-agent-research-system
