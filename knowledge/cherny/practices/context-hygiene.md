# Context hygiene: rewind over correcting

The team's stated tell for *good* context management is **rewind, not
correction** (Thariq). The unifying idea across several session-management tips:
the working context window is a scarce, degrading resource, and the skilled move
is to keep failed work *out* of it rather than to talk your way past mistakes.

- **Rewind, don't correct.** When Claude goes down a wrong path, don't type "that
  didn't work, try X instead" — that keeps the failed attempt *in* your context and
  pollutes the window. Instead rewind (`/rewind`) and re-prompt with what you
  learned. Optionally use "summarize from here" first, so Claude writes a handoff
  message — "a message from the next iteration of Claude to its past self" — before
  you rewind.
- **`/clear` vs `/compact`.** They feel similar but behave very differently. Rule
  of thumb: a genuinely *new* task → new session with `/clear`; a *related* task
  where you still need some context → `/compact` with a hint.
- **Context rot is real and has a threshold.** On the 1M-context model, degradation
  kicks in around **300–400k tokens**. You can set the autocompact threshold lower
  to force earlier compaction and effectively shrink your usable window — and fire
  `/compact <hint>` proactively when you sense bad-compact risk (autocompact firing
  mid-task can summarize the wrong things).
- **Context minimalism over context engineering.** Cherny frames keeping the
  window lean as "the single most important idea for long-running work — and the
  whole reason agents can run for hours." Subagents and worktrees exist partly to
  *protect* the main context: offload a task to a subagent to keep the main agent's
  window clean and focused.

The principle: **treat context as a budget you actively defend, not a log you let
accumulate.** This is the working-window counterpart to [[compounding-memory]]
(durable store) and the precondition for [[autonomous-unattended-operation]] —
hours-long runs are only possible because the window doesn't rot.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
