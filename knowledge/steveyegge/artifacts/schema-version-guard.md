# Schema Version Guard

A distributed store that multiple binaries can open — synced clones, agent
worktrees, CI runners — must detect version skew explicitly at open time,
not let a stale binary discover it by issuing queries that fail with cryptic
errors partway through a task.

Beads checks the database schema version against the running binary's known
migrations every time it opens the store. It fires in exactly one direction:
schema *ahead of* binary — a newer binary elsewhere already migrated the
shared, Dolt-synced database, and this binary predates those migrations.
(The reverse — this binary migrating an older database forward — is a normal
upgrade and is unaffected.) On mismatch it exits with an actionable error
naming the exact version gap (e.g. "database is at v45, binary knows up to
v42"), the concrete failure mode being averted ("queries for dropped or
renamed columns will fail with cryptic SQL errors"), and the fix (rebuild or
reinstall latest). An escape hatch (`BD_IGNORE_SCHEMA_SKEW=1` /
`--ignore-schema-skew`) exists for the narrow case where the operator already
knows the pending migrations are additive-safe for their read pattern.

Why this matters for a fleet of agents sharing one synced store: an agent
mid-task has no way to notice "the schema changed under me" on its own — it
would just see a confusing SQL error and could misattribute it to its own
logic. Front-loading the check into a single, named failure mode turns a
silent-corruption risk into a legible, actionable one, the same shape as
Beads' other safety invariants (fail loud with a specific diagnosis rather
than let a distributed-state mismatch surface as an opaque downstream error).

## Sources

- `sources/steveyegge/beads/README.md.md` (2026-07-24 revision, "Schema Version Guard" section) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/README.md
