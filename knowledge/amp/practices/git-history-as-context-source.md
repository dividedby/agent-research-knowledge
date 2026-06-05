# Git history as a context source

A single commit carries an enormous amount of meta-information: who changed what,
how they described it, which files changed *together*, the paths, and partly the
contents. "Show me a commit and I shall know enough to build something similar."
Rather than hand-assembling context for a prompt, point the agent at the git
record and let it mine the context itself.

How it shows up:

- **Inject context by reference.** Tell the agent to look at a specific commit
  before doing anything (`This test was broken by commit <sha> … examine the
  commit, then tell us how to fix it`), or have it find the relevant commit
  itself (`Look at the git history of <file>; at some point I removed the vscode
  implementation — find it and explain how we did X`). After that, all the
  context needed is in the thread.
- **`git diff` as a review and cleanup handle.** Ask the agent to `git diff` and
  review "the code someone else wrote" (it's the agent's own work; it doesn't
  know that) and report bugs. Or, in a fresh thread with no files open, `Run git
  diff … then remove the debug statements` — the diff *is* the context, so you
  don't need to know where the changes are.
- **Code discovery via the agent, not grep.** `Find the code that ensures
  unauthenticated users can view /how-to-build-an-agent` — the agent is usually
  faster than coming up with keywords, and once it locates the code everything is
  already in context for the change that follows.

This pairs with carrying context *between* short threads by referencing git
state instead of accumulating it in one conversation.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-how-i-use-amp-60b3bca7.md` — origin: https://ampcode.com/notes/how-i-use-amp
