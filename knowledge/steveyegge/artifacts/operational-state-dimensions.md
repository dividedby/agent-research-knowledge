# Operational State Dimensions

Beads tracks the live operational status of long-running agents/workers as
**structured, multi-dimensional, event-sourced state** carried on a bead —
distinct from an issue's `status` (open/in-progress/closed). Where `status`
describes *the work item*, state dimensions describe *the actor*: an agent bead
like `agent-abc` or `witness-abc` carries independent dimensions such as
`patrol`, `mode`, and `health` (`patrol:active`, `mode:degraded`,
`health:healthy`), each settable and queryable on its own.

## Two-tier representation: event as truth, label as cache

`bd set-state <issue> <dimension>=<value>` is deliberately not a single mutation.
It does three things atomically:

1. **Creates an event bead** recording the state change — this is the *source of
   truth*, giving every transition an auditable, timestamped, reasoned history.
2. **Removes the prior `dimension:value` label** for that dimension.
3. **Adds the new `dimension:value` label** — a *fast-lookup cache* over the
   authoritative event stream.

The `--reason` flag (recommended) annotates the event bead
(`patrol=muted --reason "Investigating stuck worker"`), so the *why* of an agent
going degraded is recoverable, not just the current value.

Reads go against the cheap label cache: `bd state <issue> <dimension>` extracts a
single dimension's value, and `bd state list <issue>` enumerates every
`dimension:value` label on a bead. The convention `<dimension>:<value>` is what
lets a generic label store double as a typed state machine without new schema.

## Why this shape matters for agent decomposition

This is the primitive that turns a fleet of autonomous workers into something
*observable and steerable* through the same tracker that holds their work. An
orchestrator (or a human) can flip `agent-abc patrol=muted` to quiet a
misbehaving worker, or read `health` across the fleet — all as ordinary bead
operations, with the event log providing the after-the-fact account of how each
agent's operational posture evolved. Multi-dimensionality keeps orthogonal
concerns independent: muting patrol doesn't disturb `mode` or `health`.

## Sources

- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (`bd set-state`, `bd state`, `bd state list`) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
