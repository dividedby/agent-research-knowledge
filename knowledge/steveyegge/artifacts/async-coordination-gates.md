# Async Coordination Gates

Beyond the blocking dependency types between *issues*, beads models a distinct
primitive for blocking on **external, asynchronous conditions** the issue graph
can't express: a gate. A gate is itself a bead that blocks another issue from
becoming ready until something *outside* beads resolves — a human decision, a
clock, a CI run, a PR merge, or a bead in a different repository. The blocked
issue simply stays out of `bd ready` until the gate closes.

## Gate types are a typed escalation of "what are we waiting on"

The gate's `type` encodes *who or what* resolves it, and the types form a
deliberate progression from manual to fully automated:

| Type | Resolves when | Resolution mechanism |
|------|---------------|----------------------|
| `human` | A person decides | manual `bd gate resolve` |
| `timer` | A timeout elapses | auto: `now > created_at + timeout` |
| `gh:run` | A GitHub Actions run completes successfully | poll `gh run view` |
| `gh:pr` | A PR is merged | poll `gh pr view`, state=MERGED |
| `bead` | A bead in the same rig closes | poll same-rig bead status |

`bead` gates originally could target `<rig>:<bead-id>` to await a bead in a
*different* repository, but multi-rig routing has since been removed from
beads — that cross-rig form can no longer be evaluated. A gate created before
the removal, or one mistakenly given a cross-rig `await_id`, simply stays
pending forever until a human resolves it manually (`bd gate resolve`); it
does not error at creation time. New `bead` gates must target an ID already in
the local rig's database. The lesson: a coordination primitive that spans
process boundaries (here, separate repos) is a bigger commitment than it looks
— removing the routing layer it depended on silently strands any gate built on
it, so the failure mode of a removed cross-cutting capability is "wedged
forever," not "loud error."

Gates are created automatically when a workflow-formula step declares a `gate`
field, or ad-hoc via `bd gate create --blocks <id>`. The same command surface
covers all types — only the resolution path differs.

## Resolution is a poll-and-close loop, not a callback

`bd gate check` is the engine: it evaluates open gates and **closes the resolved
ones**, which is what unblocks downstream work. It can run scoped (`--type=gh`)
and supports `--dry-run`. Crucially it also handles the *failure* branch — a
`gh:run` that completed with `failure`/`canceled`, or a PR that closed without
merging, is **escalated** (`--escalate`) rather than silently resolved, so a
broken upstream condition surfaces instead of unblocking work that shouldn't
proceed. For GitHub gates the await target (a run ID) may not be known at
creation; `bd gate discover` heuristically matches open `gh:run` gates to recent
workflow runs by branch, commit SHA, and time proximity, then fills in the
`await_id` so polling can begin.

Agents that need to be told when a gate clears register as **waiters**
(`bd gate add-waiter <gate-id> <waiter>`, where the waiter is a worker address);
on close they get a wake notification. This is how a phase-completing agent
parks itself against an async condition instead of busy-waiting.

## Merge-slot: a gate specialized into a one-holder mutex

The merge slot is the same gate idea narrowed to a single purpose — **serializing
conflict resolution** so multiple agents don't race to resolve merge conflicts
and cascade new ones (the "monkey knife fights" failure mode). Each rig has one
`<prefix>-merge-slot` bead acting as an exclusive lock:

- `status=open` means available; `status=in_progress` means held.
- `metadata.holder` records who holds it; `metadata.waiters` is a
  priority-ordered queue.
- `acquire` takes it if open, else fails unless `--wait` enqueues the requester;
  `release` reopens it and the highest-priority waiter acquires next.

The design lesson: rather than build a separate lock subsystem, beads expresses
mutual exclusion as *yet another bead with a status and a waiter queue* — the
same data model that powers issues and gates, reused as a coordination
primitive. Async waits and mutexes both reduce to "a bead that blocks until it
closes."

## Sources

- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (lines 610-807, `bd gate`; lines 948-1036, `bd merge-slot`) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (`bd gate` — multi-rig routing removed, `bead` gates now same-rig only, historical cross-rig `await_id` stays pending, 2026-07-17 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
