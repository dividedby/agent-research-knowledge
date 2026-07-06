# Reference-Aware Pruning

A deletion/garbage-collection command over an agent's persistent work graph
should not key eligibility on age or status alone — it should first check
whether any live node still *cites* the candidate, and skip deletion if so.
Age-based sweeps are blind to meaning: a closed issue can be simultaneously
"done" and "still load-bearing," if other open work points back at it.

## Why this matters for agent memory

In beads, closed issues aren't only completed tasks — some are durable memory
nodes: ADR records, decisions, verification receipts that other beads cite by
ID in free-text description/notes/comments (not a structural foreign key, so
the database can't enforce the reference). A naive `bd prune --older-than 90d`
would silently delete an ADR bead the moment it crosses the age threshold, even
while an open task's description still says "see bd-a3f8 for why we chose
this" — severing the audit trail the agent (or a human) needs to trace a
decision back to its origin.

## The mechanism

`bd prune` (for regular, non-ephemeral beads) scans the description, notes,
and comments of every open/in-progress bead for the candidate's ID before
deleting it, and skips any match. `--ignore-references` is an explicit escape
hatch for deliberate bulk cleanup (e.g., retiring a whole label across the
rig) — the override exists, but it isn't the default, so accidental
citation-breaking requires an extra, named step.

`bd purge` (for ephemeral beads — wisps, transient molecules) carries **no**
such check: ephemeral work is ephemeral by construction, created with the
understanding that it has no downstream citation value, so there's nothing to
protect. The same age/pattern-based deletion is safe there without the scan.

## Transferable takeaway

Any agent memory-compaction tool that lets records cite each other in free
text — not just structural links a schema can enforce — needs a reference
scan before deletion, or its own garbage collector will quietly corrupt the
provenance trail that other records depend on. Whether that check is needed
at all is itself decidable from how the record was created: work marked
ephemeral at creation time can skip the scan; anything else can't.

## Sources

- `sources/steveyegge/beads/README.md.md` (2026-07-06 revision, "Maintenance — `bd prune` and `bd purge`" section) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/README.md
- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (2026-07-06 revision, `bd prune`/`bd purge` sections — reference-aware protection, `--ignore-references`) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
