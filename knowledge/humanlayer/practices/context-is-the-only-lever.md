# Context is the only lever

An LLM is a stateless function: weights frozen at inference time, no memory across
calls. A turn in a coding agent is just `context window in, next step out`. Nothing
the model "knows" about your codebase survives between sessions — it knows only the
tokens you put in front of it this turn.

The consequence HumanLayer keeps returning to: **the contents of the context window
are the only thing you can change to affect output quality** (short of training the
model yourself). So context engineering isn't one technique among many — it's the
whole game. Everything else (CLAUDE.md, sub-agents, compaction, forking, harness
config) is in service of getting the right tokens into that window and keeping the
wrong ones out.

This reframes two intuitions:

- **"The agent forgot" is a category error.** It never knew. If something matters
  every session, it has to be re-supplied every session — that is exactly what
  CLAUDE.md is for, and why memory must be managed explicitly.
- **Optimize the window along four axes**, in priority order of what hurts most:
  *correctness* (wrong information is worst), *completeness* (missing information),
  then *size / noise* (too much irrelevant context). A window full of focused,
  relevant context beats a larger window padded with the irrelevant — every time.

This is the premise the rest of HumanLayer's practices build on. If you accept that
the model is a stateless reducer over its context, then instruction budgets, small
focused agents, sub-agent isolation, and compaction all follow as ways to defend the
one lever you actually have.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-12-factor-agents-00e2e139.md`
  — origin: https://www.humanlayer.dev/blog/12-factor-agents (Factor 3: Own Your Context Window)
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-writing-a-good-claude-md-2fad0803.md`
  — origin: https://www.humanlayer.dev/blog/writing-a-good-claude-md
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-advanced-context-engineering-cf42508e.md`
  — origin: https://www.humanlayer.dev/blog/advanced-context-engineering
