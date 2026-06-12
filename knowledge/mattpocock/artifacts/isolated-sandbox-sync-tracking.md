# Isolated sandbox sync: tracking patch base with sandbox-owned refs

For isolated sandbox providers where the agent works in a separate filesystem, Sandcastle must extract commits via `git format-patch` and apply them on the host with `git am`. Since `git am` always rewrites commit SHAs, the host ends up with different SHAs than the sandbox for the same changes. Tracking the sync baseline becomes a coordination problem — Sandcastle solves this with a sandbox-owned ref that never reaches the host.

## The SHA rewrite coordination problem

On the first sync-out, using the host's HEAD as the patch base works perfectly — right after sync-in, both host and sandbox have identical HEAD. But `git am --3way` always re-commits, giving the host new SHAs the sandbox has never seen. On subsequent syncs, using the host's HEAD as the base fails with "fatal: Invalid revision range" because that SHA doesn't exist in the sandbox.

This creates a data loss scenario: the second sync-out fails entirely, and when the sandbox tears down, all the agent's work vanishes because it was never successfully extracted.

## Sandbox-owned ref as sync bookmark

Sandcastle tracks the last-successfully-synced sandbox commit in `refs/sandcastle/sync-base`, a reference kept entirely within the sandbox's git repo. The sync-out logic resolves the patch base by checking this ref first, falling back to host HEAD only when the ref is absent (exactly when no prior `git am` has run).

After successfully applying commits to the host, the ref advances to the sandbox's HEAD. This creates a moving baseline that tracks what the host has already seen, independent of the SHA rewrites `git am` introduced.

## Safe fallback through coupled conditions

The ref is absent exactly when no `git am` has run yet — and `git am` is the only operation that rewrites host HEAD. These conditions are coupled: whenever the ref is missing, host HEAD has not been rewritten and therefore remains a valid base that still exists in the sandbox.

This coupling makes the fallback safe without requiring coordination between host and sandbox. The presence or absence of the sandbox ref perfectly predicts whether the host HEAD is still a usable base.

## Invisible bookkeeping

The `refs/sandcastle/` namespace keeps the sync bookmark invisible to `git log`, `git branch`, and `git tag`. It's pure infrastructure that doesn't appear in the user's view of the repository. The ref never reaches the host — the sandbox→host channel (`format-patch`/`am`) carries commits, not references.

This keeps the sync tracking mechanism out of the user's mental model while solving the coordination problem invisibly in the background.

## The worktree, not sync, is now the spine of the architecture

The sync-in/sync-out machinery above is the **isolated-provider** path, and the
README's "How it works" has been rewritten around a **worktree-based** model rather
than that sync model as the headline architecture. The current framing is three
*branch strategies* over a git worktree: `head` (agent writes the host working
directory directly, no worktree), `merge-to-head` (temp branch in a worktree,
merged back to HEAD), and `branch` (commits land on a named branch in a worktree).
For the common bind-mount providers (Docker, Podman) the worktree directory is
simply *bind-mounted into the container* — the agent writes the host filesystem
through the mount, so **no sync is needed at all**. The `format-patch`/`am` sync
dance described above is now the fallback specific to *isolated* providers whose
sandbox can't reach the host filesystem, not the general mechanism.

The worktree is also promoted to a **first-class, standalone concept** via
`createWorktree()` — a worktree independent of any sandbox. The motivating workflow
is hand-off: run an *interactive* session in the worktree first (to explore and
understand), then hand the *same* worktree to a sandboxed AFK agent. Ownership
splits accordingly — when a sandbox is created via `wt.createSandbox()`,
`sandbox.close()` tears down the container only and the worktree survives;
`wt.close()` owns worktree cleanup (preserving it if dirty). This differs from the
top-level `createSandbox()`, where one `close()` owns both.

## Sources

- `sources/mattpocock/sandcastle/docs-adr-0017-sandbox-owned-sync-base-ref.md-792c3e43.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0017-sandbox-owned-sync-base-ref.md
- `sources/mattpocock/sandcastle/README.md.md` — origin: github.com/mattpocock/sandcastle (README.md)
- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: github.com/mattpocock/sandcastle (CHANGELOG.md)