# Worktree Sync Decoupled From Git Refs

A sync mechanism layered on top of git should keep its own state in a ref
namespace git does not treat as checkout state — never an ordinary branch —
or every worktree the tool creates becomes a git worktree, and git worktrees
lock the branch they have checked out.

## The failure mode this design avoids

Beads originally implemented cross-machine sync via a dedicated "sync branch"
(`bd config set sync.branch <name>`). To commit issue updates to that branch
without disturbing the user's working directory, beads silently created its
own git worktree at `.git/beads-worktrees/<branch>/`. Because git refuses to
check the same branch out in two worktrees at once, a beads-created sync
worktree pinned to `main` made the user's own `git checkout main` fail with
`fatal: 'main' is already checked out at '.git/beads-worktrees/beads-sync'` —
an internal implementation detail of the tracker surfacing as a mysterious
git error with no visible link back to beads.

## The fix: store sync state outside git's ref-checkout model

Current beads stores issue data in Dolt under `refs/dolt/data` — a ref
namespace git tracks but never checks out. Sync (`bd dolt push`/`bd dolt
pull`) updates that ref directly, so there is no sync branch, no
beads-managed git worktree, and no checkout collision to hit. Every linked
worktree in a repository transparently shares one `.beads` workspace by
discovery, with no special configuration required.

## Transferable takeaway

If you're building a tool that layers its own versioned state on top of git
(for sync, locking, or history), don't reuse git's branch-and-checkout
mechanism as if it were free storage — a branch is a checkout target, and
anything that creates worktrees against it inherits git's one-worktree-per-
branch constraint. Put the tool's own state in a ref namespace git manages
but never checks out, so the two subsystems can't collide.

## Sources

- `sources/steveyegge/beads/docs-WORKTREES.md-495554ba.md` (2026-07-08 revision — sync-branch removal, `refs/dolt/data` storage replacing the beads-managed worktree) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/WORKTREES.md
