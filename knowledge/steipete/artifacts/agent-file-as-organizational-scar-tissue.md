# Agent File As Organizational Scar Tissue

The agent instruction file (`AGENTS.md`/`CLAUDE.md`) is grown, not authored. Steipete's ~800-line file was written largely *by the model itself*: every time something goes wrong, the model appends a concise note so it won't repeat the mistake. The file accretes like organizational scar tissue — each line is a healed-over failure.

It works *despite* its size because the entries are reactive corrections to real failures, not aspirational instructions. Good entries capture the gap between the model's defaults and your project's reality: git operation gotchas, naming and API patterns, framework rules, and anything newer than the model's training cutoff. Worthless entries are persona prompts ("you are an expert Swift engineer...") — context-poison that consumes tokens without changing output. What actually improves results is documentation, concrete examples, and explicit do/don'ts.

The discipline is bidirectional: you also *delete* entries as models improve and absorb that knowledge into their defaults. A note that fights a problem the new model no longer has is dead weight. So the file stays a living record of the current delta, not a growing archive — pruning matters as much as appending.

Because vendors won't agree on a filename, he keeps one canonical `AGENTS.md` and symlinks `CLAUDE.md` to it, so every tool reads the same source of truth.

This is the file-level expression of [[engineer-the-codebase-for-agents]]: instead of re-explaining context every session, you encode hard-won corrections once and let them persist. It pairs naturally with [[less-is-more-tooling]] — keep only what earns its tokens.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
