# Context forking: the context window as a stack

A useful mental model: a coding agent's context window is a **downward-growing stack**,
like an OS call stack. Each user-message / assistant-message turn is a frame pushed on
the end. You can push (send a message) or pop from the newest end — but you **can't
randomly access the middle.** Agents forbid that for good reasons: editing the middle
causes expensive inference-cache misses, mangles accumulated context, and desyncs the
harness's internal state (e.g. its record of which files were read before an edit is
allowed). Surgically rewriting the window *and* that hidden state isn't supported.

**Context forking** is the one sanctioned form of non-linear editing: pop one or more
turns off the end to restore an earlier state, usually only at user-message
boundaries (whole frames, not mid-tool-call), and you can fork the same window many
different ways. Implementations vary — some agents also rewind the disk/code state,
some create a branch or worktree. The names vary too: rewind, time-travel, branching.

Three high-value uses, all in service of protecting good context (see
*context-is-the-only-lever*):

- **Course-correct.** Rewind mid-implementation when the agent missed something,
  instead of arguing with a polluted window.
- **Explore design paths.** Once you've built up high-quality context about the
  problem, fork from that point to try several architectures in parallel, then keep
  the session whose result you like (or decide you need more research).
- **Salvage after a context-inefficient operation.** When the agent dumps 40k tokens
  by reading a huge file or command output one chunk at a time, fork back to the
  state *before* the dump — rescuing the expensive, high-quality context you'd built
  rather than starting over.

Forking is the interactive cousin of *frequent-intentional-compaction*: compaction
distills context forward into a fresh window, forking rewinds it to a known-good
point. Both treat the window as something you actively curate, not a transcript you're
stuck appending to.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-context-forking-to-save-time-t-a5d6680c.md`
  — origin: https://www.humanlayer.dev/blog/context-forking-to-save-time-trouble-and-tokens
