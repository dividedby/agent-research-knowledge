# Manage the working session's context actively

Within a single interactive session, the human's job is to keep the context
window clean, because performance degrades as it fills with irrelevant
conversation, file contents, and failed attempts. Conversations are persistent
and reversible — use that.

The named failure patterns and their fixes:
- **The kitchen-sink session** — mixing unrelated tasks pollutes context. Fix:
  reset between unrelated tasks (`/clear`). A clean session with a sharper prompt
  almost always beats a long one with accumulated corrections.
- **Correcting over and over** — after two failed corrections the context is full
  of dead approaches. Fix: clear and rewrite the initial prompt incorporating
  what you learned, rather than piling on more corrections.
- **The infinite exploration** — an unscoped "investigate this" makes the agent
  read hundreds of files into your main context. Fix: scope it narrowly, or push
  it into a subagent whose separate context window absorbs the reading and reports
  back only a summary.

Beyond reset, the controls are: **course-correct early** (interrupt mid-action
with `Esc`, context preserved, and redirect — tight feedback loops beat hoping the
first attempt lands; or just say `"undo that"` to have it revert changes);
**rewind** (`Esc Esc` / `/rewind`) to a prior conversation/code checkpoint to try
a risky approach and undo it if it fails — checkpoints are auto-snapshotted before
each change and *persist across sessions*, so you can close the terminal and still
rewind later; and **steer compaction** with `/compact <instructions>` (e.g.
`/compact Focus on the API changes`) or a standing CLAUDE.md rule, so the summary
keeps the modified-files list, test commands, and key decisions you care about.
Rewind also offers *partial* compaction: select a checkpoint and **summarize from
here** (condense forward, keep earlier context) or **summarize up to here**
(condense earlier, keep recent in full). For a one-off question that shouldn't
grow context at all, `/btw` returns the answer in a dismissible overlay that never
enters history. And conversations are durable: `claude --continue` resumes the
latest, `claude --resume` picks from a list, and descriptive session names (e.g.
`oauth-migration`) make a multi-sitting task findable. Develop intuition over
rules: sometimes you *should* let context
accumulate because you're deep in one problem and the history is valuable —
notice what you did when output was great, and when it struggled ask whether the
context was too noisy.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-code-best-practic-4d249e2a.md` — https://www.anthropic.com/engineering/claude-code-best-practices
- `sources/anthropic/best-practices/https-code.claude.com-docs-en-best-practices-fb8dc53b.md` — https://code.claude.com/docs/en/best-practices
