# Don't send an LLM to do a linter's job

One of the most common things people stuff into CLAUDE.md is code-style guidelines.
HumanLayer's position is blunt: **never make an LLM do what a deterministic tool does
better.** A linter or formatter is faster, cheaper, and exact; an LLM applying style
rules is slow, expensive, and unreliable. Style guidelines also drag a pile of
instructions and soon-stale code snippets into the context window, spending
instruction budget and degrading adherence on the work that actually matters.

You usually don't even need the rules in context, because **LLMs are in-context
learners**. Armed with a few searches of the codebase (or a good research doc), the
agent tends to match existing patterns and conventions on its own — no explicit style
section required.

When you do care about enforcement, **make it deterministic and keep it out of the
prompt**:

- A `Stop` hook that runs your formatter and linter and feeds only the *errors* back
  to the agent to fix — so the model never hunts for formatting issues itself (this
  is *context-efficient-backpressure* applied to style).
- A linter that auto-fixes (e.g. Biome), with rules carefully tuned for what's safe
  to fix automatically, for maximum safe coverage.
- A slash command carrying the guidelines and pointed at `git status` / the diff, so
  implementation and formatting are handled in separate passes — both come out better.

The general principle, stated elsewhere as "determinism over delegation": if a
deterministic tool can do it, it should — and it should report only what the agent
needs to act on.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-writing-a-good-claude-md-2fad0803.md`
  — origin: https://www.humanlayer.dev/blog/writing-a-good-claude-md
