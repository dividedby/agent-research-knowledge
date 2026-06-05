# Working past the context window: compaction, notes, sub-agents

Long-horizon tasks — codebase migrations, multi-hour research — generate more
tokens than fit in a single context window, and waiting for bigger windows won't
save you (windows of any size suffer pollution and relevance decay where peak
performance matters). Three techniques let an agent maintain coherence across the
limit; they compose.

- **Compaction.** When the conversation nears the window limit, summarize it and
  reinitialize a fresh window with the summary. It's the first lever and preserves
  continuity for the *same* agent. The art is in what to keep vs. discard:
  preserve architectural decisions, unresolved bugs, implementation details;
  discard redundant tool outputs. Tune the compaction prompt on real traces —
  maximize recall first, then trim for precision. The lightest, safest form is
  **tool-result clearing**: once a tool's result is deep in history, the agent
  rarely needs the raw output again.
- **Structured note-taking (agentic memory).** The agent writes notes to memory
  *outside* the context window — a `NOTES.md`, a to-do list, a file-based memory
  tool — and pulls them back later. This gives persistent state with minimal
  overhead: progress, dependencies, and tallies survive across dozens of tool
  calls and across context resets, enabling multi-hour strategies (Claude playing
  Pokémon maintains maps and objectives across thousands of steps this way).
- **Sub-agent architectures.** Specialized sub-agents each work a focused task in
  a *clean* context window, exploring with tens of thousands of tokens but
  returning only a distilled 1,000–2,000-token summary. The detailed search
  context stays isolated in the sub-agent; the lead agent keeps a clean high-level
  view to synthesize. This separation of concerns is the same lever that lets a
  Claude Code subagent absorb a heavy codebase read without polluting the main
  session.

A heavier variant is the **context reset** (see the long-running harness concept):
unlike compaction, it clears the window entirely and hands off via a structured
artifact, which also cures "context anxiety" that compaction alone leaves intact.
The choice among these depends on the task; all rest on treating context as a
finite resource to curate.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-effective-context-engine-42516bb9.md` — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-multi-agent-research-sys-37ed91c9.md` — https://www.anthropic.com/engineering/multi-agent-research-system
