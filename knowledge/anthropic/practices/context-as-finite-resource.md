# Context is a finite resource with diminishing returns

The single constraint most agent practice descends from: an LLM's context window
is not free storage. As tokens accumulate, recall and reasoning degrade — a
phenomenon Anthropic names **context rot**. It is a gradient, not a cliff:
the model stays capable but loses precision on retrieval and long-range
reasoning as the window fills.

Why it happens is architectural, not incidental. Transformers compute n² pairwise
attention relationships over n tokens; every new token dilutes that attention and
depletes a fixed **attention budget**. Models are also trained mostly on shorter
sequences, so they have fewer specialized parameters for context-wide
dependencies. Bigger context windows do not dissolve the problem — for the
foreseeable future, windows of any size are subject to pollution and relevance
decay where peak performance matters.

The operative consequence: treat context as precious. The guiding principle of
all context engineering is to find the **smallest set of high-signal tokens that
maximize the likelihood of the desired outcome**. "Minimal" does not mean
"short" — it means no token that isn't earning its place. This is why bloated
tool sets, laundry-list edge cases in prompts, raw tool dumps, and over-stuffed
`CLAUDE.md` files actively *hurt*: noise crowds out the instructions that matter,
and the model starts ignoring them or making mistakes. The working test for any
piece of standing context (an instruction, a doc line): "would removing this
cause the agent to make mistakes?" If not, cut it.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-effective-context-engine-42516bb9.md` — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-code-best-practic-4d249e2a.md` — https://www.anthropic.com/engineering/claude-code-best-practices
- `sources/anthropic/best-practices/https-code.claude.com-docs-en-best-practices-fb8dc53b.md` — https://code.claude.com/docs/en/best-practices
