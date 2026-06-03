# Scrollback Native Tui Differential Rendering

Because a coding agent is fundamentally a **linear chat transcript**, the TUI should *append* to the terminal's native scrollback — like a normal CLI — rather than seize the viewport as a pixel buffer (the full-screen approach of Amp and opencode). Appending gets the terminal's built-in scrolling and search for free, and the constraint itself keeps the program minimal.

`pi-tui` is a simple retained-mode tree. A `Component` is just `render(width) -> string[]` plus an optional `handleInput`. Components **cache their rendered lines**, so a streamed assistant message needn't re-parse markdown on every tick. The TUI **diffs** the new line set against a remembered backbuffer and redraws only from the first changed line — "differential rendering." Full clears happen only on a width change or when an edit lands above the scrolled viewport.

All rendering is wrapped in **synchronized-output escapes** (`CSI ?2026h` / `?2026l`) so each update is atomic and near-flicker-free. The memory cost — a few hundred KB of remembered lines — is trivial, and the payoff is a dead-simple programming model: render a tree to strings, diff, paint. The whole design follows from taking the "it's just a transcript" observation seriously instead of reaching for a full-screen UI framework. See [[minimal-harness-by-subtraction]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
