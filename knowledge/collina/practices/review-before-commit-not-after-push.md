# Move the review checkpoint before commit, not after push

When an agent can generate more code than you can meaningfully review in a
terminal diff, move the review checkpoint earlier — to before commit, not
after push. PR-based review was designed for human-paced, incrementally
written code, and it assumes the reviewer is checking a deliberate,
already-considered change. Agent-generated code arrives in bulk and fast, so
waiting until PR time means the review happens only after the expensive
decisions — the approach, the architecture — are already locked in; by the
time there's a branch and an open PR, you've committed to whatever the agent
chose.

Matteo Collina validated this by dogfooding it to an extreme: he built
GitHuman — entirely with Claude Code — specifically to review staged,
uncommitted AI-generated diffs from his phone over SSH and Tailscale, and
used it to review 83 commits over 12 days. The tight mobile feedback loop
caught real bugs that automated tests missed. The lesson isn't "build a
diff-viewer app" — it's that the checkpoint-shift itself, catching AI output
before it becomes a committed decision rather than after, is what mattered;
the tool was just what made that discipline practical to sustain daily.

## Sources

- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-building-githuman-an-a-f62a48d8.md` — origin: https://adventures.nodeland.dev/archive/building-githuman-an-ai-coded-tool-for-reviewing/
