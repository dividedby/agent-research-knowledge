# A bigger context window is not more capability

When Claude Code's default jumped to a 1M-token window, the obvious move was to use
it: fit the whole codebase in, stop compacting, solve bigger problems in one shot.
HumanLayer tested this and **switched back to the smaller-window model**, because
instruction adherence degraded badly — and not only near the limit, but across the
*whole* range, even at token counts that should have been comfortable.

The mechanism is that the window grew but the model's capacity to attend did not.
Extended-context variants are typically stretched with mathematical tricks (e.g.
YaRN) that lengthen the sequence without adding parameters, so the *instruction
budget stays fixed while the window expands*. More room to put things in, no more
ability to act on them.

Two framings make this concrete:

- **Needle in a haystack.** Context is a haystack of tool calls, docs, and
  instructions. A 5× larger haystack with no improvement in retrieval makes finding
  the relevant needle dramatically harder, not easier.
- **Context rot.** Models perform worse at longer context lengths, and *worse still*
  when the semantic similarity between the query and the surrounding context is low.
  Every irrelevant tool result is a distractor, and the effect compounds.

The practical correction HumanLayer made was to **stop scaling the budget with the
window**. They moved their context warning from "40% of usable window" to a fixed
~100k-token threshold across all models — which on a 1M window is only 10%. The
target isn't "fill the window," it's **stay in the zone where the model is sharp**
(they cite roughly 75k tokens as the smart zone) and aggressively manage everything
else out.

So the answer to "the model isn't keeping up — should we give it more context?" is
usually no. The answer is *less, and better*: sub-agent isolation, compaction, and
focused scope (see *context-is-the-only-lever*, *instruction-budget*,
*small-focused-agents*, and *frequent-intentional-compaction*).

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-long-context-isnt-the-answer-dc10c427.md`
  — origin: https://www.humanlayer.dev/blog/long-context-isnt-the-answer
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-context-efficient-backpressure-38259122.md`
  — origin: https://www.humanlayer.dev/blog/context-efficient-backpressure
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-skill-issue-harness-engineerin-313aa20b.md`
  — origin: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
