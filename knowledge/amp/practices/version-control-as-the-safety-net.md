# Version control is the safety net, not approval gates

The right protection against an agent's mistakes is **version control**, not
edit-by-edit approval. Most people no longer worry about file edits, because git
makes the cost of a wrong edit negligible — restrictions aren't necessary for any
tool with an easy undo. Errors happen for models and humans alike; an
environment that *acknowledges* error and makes it cheap to reverse beats one
that tries to prevent all error up front.

Why approval gates are the wrong default:

- Edit-by-edit approval **traps you in a local maximum** by impeding the agentic
  feedback loop — you never give the agent the chance to iterate on its first
  draft through review, diagnostics, compiler output, and test runs. (If the
  agent rarely produces good-enough code, the fix is a better prompt and
  `AGENTS.md`, not micromanaging.)
- The checkpoint / apply-reject model is rejected in favor of letting the agent
  run, with VCS always in the background as the safety net you never want to mess
  with.

How it shows up:

- **Lean on the git staging area as your accept/reject UI.** Ask for something,
  see it's good, `git add` it; ask for the next thing, see it's bad, wipe the
  *unstaged* changes. Staged work is your known-good floor.
- **The agent doesn't touch VCS on its own.** It can run commands and edit files
  freely, but Amp deliberately won't stage/commit unprompted — you keep that
  control, while still being able to *tell* it to commit or open a PR.
- **Build one to throw one away.** Cheap reversal kills sunk-cost: have the agent
  implement something, look at it in five minutes, keep or discard. Often the
  most valuable output is learning how you *don't* want to build it.

The same logic answers the "but it could `rm -rf` prod!" objection: backups and
version control reduce the damage of accidents to near zero, so let the model
commit — commits drop and amend easily.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-permissions-b6eba13f.md` — origin: https://ampcode.com/notes/permissions
- `sources/amp/chronicle/https-ampcode.com-notes-fif-dc1eb004.md` — origin: https://ampcode.com/notes/fif
- `sources/amp/chronicle/https-ampcode.com-notes-how-i-use-amp-60b3bca7.md` — origin: https://ampcode.com/notes/how-i-use-amp
