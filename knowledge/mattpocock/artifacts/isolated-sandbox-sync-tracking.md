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

## Sources

- `sources/mattpocock/sandcastle/docs-adr-0017-sandbox-owned-sync-base-ref.md-792c3e43.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0017-sandbox-owned-sync-base-ref.md