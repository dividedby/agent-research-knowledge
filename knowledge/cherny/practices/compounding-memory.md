# Compounding memory: the agent writes its own rules

A recurring Cherny practice is to make the agent's mistakes *pay forward* by
capturing each correction back into durable memory the agent reloads next time.
He calls the team's version of this **"Compounding Engineering"** (after Dan
Shipper): every interaction should leave the system a little smarter.

The mechanics, in order of how he applies them:

- **One shared CLAUDE.md, checked into git.** The whole Claude Code team
  contributes to a single repo-level CLAUDE.md multiple times a week — it is a
  living, collectively-owned artifact, not a per-developer scratch file.
- **Self-writing rules.** The habit-forming move: after every correction, end with
  *"Update your CLAUDE.md so you don't make that mistake again."* Claude is "eerily
  good at writing rules for itself" — the human supplies the correction once, the
  agent encodes the general rule.
- **Capture in the PR loop.** During code review, tag `@claude` on PRs to fold
  learnings into CLAUDE.md *as part of the PR itself* (via the Claude Code GitHub
  Action), so knowledge accrues exactly where the mistake surfaced.
- **Notes directories.** For larger work, have Claude maintain a notes directory
  per task/project, updated after every PR, and point CLAUDE.md at it — keeping the
  always-loaded file lean while preserving deeper context on demand.

The principle: **memory is an asset you compound, and the cheapest time to write
a rule is the moment a mistake is corrected.** This is the inverse pressure to
[[context-hygiene]] — context-rot discipline keeps the *working window* lean,
while compounding memory keeps the *durable* store growing. Note the later
context-minimalism turn (see [[plan-first-then-context-minimalism]]) tempers how
much you front-load CLAUDE.md, but not the habit of capturing corrections.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
