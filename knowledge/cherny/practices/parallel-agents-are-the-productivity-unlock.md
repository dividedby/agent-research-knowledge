# Parallel agents are the productivity unlock

Cherny's single most-repeated claim is that the leap from one agent to *many*
agents — not any prompting trick — is the largest productivity gain available in
Claude Code. The same idea recurs across every thread, each iteration replacing
the previous mechanism with a more first-class one. Treat them as one evolving
concept, not separate tips:

- **Manual checkouts (Jan 2026).** Run 5 instances in numbered terminal tabs over
  5 separate git checkouts of the same repo, plus 5–10 web sessions on
  claude.ai/code; system notifications signal which one needs input.
- **Worktrees + aliases.** Spin up 3–5 git worktrees at once, each its own
  session, hopping between them with one-keystroke shell aliases (`za`, `zb`,
  `zc`). A dedicated "analysis" worktree is kept read-only for logs / BigQuery.
- **Built-in worktree support (`claude --worktree`).** Isolation becomes a flag —
  parallel sessions in one repo without edits clobbering each other; subagents can
  isolate too (`isolation: worktree` in agent frontmatter; depth-capped nested
  subagents let agents kick off agents to keep context clean).
- **Agent view (`claude agents`).** The productized control plane — "tmux built
  for CC" — that groups every session by *needs-your-input / working / done*. This
  is explicitly the productized version of the original manual-tabs pattern.
- **The finest-grained rung: one request, not one session.** Append "use
  subagents" to any single prompt to fan extra compute into that one request —
  the same one-to-many move, scoped down to a task instead of a whole workflow.
- **Ergonomics for telling sessions apart.** Once you're juggling several at
  once, invest in visual distinction: a customized `/statusline` (context usage,
  branch, at a glance), color-coded and named terminal tabs — one per
  task/worktree — optionally grouped under tmux. The team's terminal of choice,
  Ghostty, earns its place for exactly this: synchronized rendering, 24-bit
  color, and proper unicode support are what make color and name cues actually
  legible at a glance.

The throughline: **the bottleneck is the human cycling between tabs, not the
model.** Each step removes a manual coordination tax. Cherny: "The best way to
level up is from 1 agent to many agents. No more cycling between terminal tabs."
He keeps "dozens of Claudes running at all times." Worktrees are what make this
safe — parallel work in one repo without interference — which is why they recur
as the substrate under every later orchestration feature (agent view, `/batch`,
dynamic workflows).

See also [[verification-is-the-number-one-tip]] (each parallel agent must be able
to verify itself to run unattended) and [[autonomous-unattended-operation]].

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
