# Two-Layer Data Architecture

Beads uses a two-layer architecture that enables distributed, Dolt-powered issue tracking while maintaining the feel of a centralized database.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLI Layer                                 │
│                                                                  │
│  bd create, list, update, close, ready, show, dep, sync, ...    │
│  - Cobra commands in cmd/bd/                                     │
│  - All commands support --json for programmatic use              │
│  - Direct DB access (server mode via dolt sql-server)            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               v
┌─────────────────────────────────────────────────────────────────┐
│                      Dolt Database                               │
│                      (.beads/dolt/)                               │
│                                                                  │
│  - Version-controlled SQL database with cell-level merge         │
│  - Server mode via dolt sql-server (multi-writer capable)        │
│  - Fast queries, indexes, foreign keys                           │
│  - Issues, dependencies, labels, comments, events                │
│  - Automatic Dolt commits on every write                         │
│  - Native push/pull to Dolt remotes                              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                        Dolt push/pull
                               │
                               v
┌─────────────────────────────────────────────────────────────────┐
│                     Remote (Dolt or Git)                          │
│                                                                  │
│  - Dolt remotes (DoltHub, S3, GCS, filesystem)                   │
│  - All collaborators share the same issue database               │
│  - Cell-level merge for conflict resolution                      │
│  - Protected branch support via separate sync branch             │
└─────────────────────────────────────────────────────────────────┘
```

## Design Rationale

**Dolt for versioned SQL:** Queries complete in milliseconds with full SQL support. Dolt adds native version control — every write is automatically committed to Dolt history, providing a complete audit trail. Cell-level merge resolves conflicts automatically.

**Dolt for distribution:** Native push/pull to Dolt remotes (DoltHub, S3, GCS). No special sync server needed. Issues travel with your code. Offline work just works.

## Operating Modes

### Embedded Mode (Default)
- Dolt runs in-process — no external server needed
- Data lives in `.beads/embeddeddolt/`
- Single-writer only (file locking enforced)
- Recommended mode for most users

### Server Mode
- Connects to an external `dolt sql-server`
- Data lives in `.beads/dolt/`
- Supports multiple concurrent writers
- Configurable connection parameters

## Data Flow Patterns

### Write Path
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CLI Command   │───▶│   Dolt Write    │───▶│  Dolt Commit    │
│   (bd create)   │    │  (immediate)    │    │  (automatic)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Read Path
```
┌─────────────────┐    ┌─────────────────┐
│   CLI Query     │───▶│   Dolt Query    │
│   (bd ready)    │    │   (SQL)         │
└─────────────────┘    └─────────────────┘
```

## Two-Tier History: Structural Audit vs. Opt-In Interaction Log

Every write's automatic Dolt commit is the *structural* history — always on,
queryable per-issue via `bd history <id> --events`, and not something an
operator chooses to enable. `bd audit` is a separate, deliberately opt-in
layer on top of it: an append-only JSONL sidecar (`.beads/interactions.jsonl`,
disabled by default, turned on with `bd config set audit.enabled true`) for
recording explicit agent/tool interaction entries — not "what changed" but
"what the agent did and why." The stated use cases are diagnostic ("why did
the agent do that?") and, notably, **dataset generation for SFT/RL
fine-tuning** — the same tracker an agent works through doubles as training-
data capture infrastructure when the sidecar is switched on, without that
cost being paid by installations that don't need it.

## Storage Backend Pluralism: Dolt Is Default, Not Exclusive

The database layer was originally Dolt-only (the legacy SQLite backend had
been removed outright). It has since widened into a genuine driver-interface
boundary: `--backend=<postgres|mysql|sqlite>` selects an alternative to Dolt,
each with its own connection surface (`--pg-url`/`--pg-schema` for Postgres,
`--mysql-url`/`--mysql-database` for MySQL, `--sqlite-path` for SQLite; a
password may be supplied at `init` but is never persisted — later commands
read it from an env var instead). **Dolt remains the default and the only
backend with version control** (commit history, branching, native
push/pull sync) — the alternative backends trade that away for a plainer,
more familiar operational surface. This is the concrete payoff of the
project's Storage Boundary design (see `project-scope-charter.md`): the
driver interface was kept narrow enough on purpose that swapping the backend
underneath the CLI layer didn't require touching beads' core logic, only
widening the interface at the boundary.

## Upgrade Discipline: One Clone Owns the Migration

Because the Dolt store is shared history, not just a binary each collaborator
happens to run, "replace the `bd` binary" and "upgrade the database" are two
separate steps. A release can carry a schema migration, and a database that
syncs to a Dolt remote must be migrated by **exactly one designated clone** —
every other collaborator pulls the already-migrated state instead of each
independently re-running the migration against their own copy, which would
fork the shared history the same way an uncoordinated multi-writer push would.
Back up first (`bd export --all`) before migrating, since the migration is a
write against shared state, not a local, reversible config change.

This discipline is a mechanically enforced gate, not just a documented
convention: on a remote-backed database with pending schema migrations, `bd`
refuses to migrate in place. The refusal exists because two clones each
independently migrating fork the schema until `bd dolt pull` can no longer
merge — a break that is silent and unrecoverable, not one that surfaces as an
ordinary conflict. `--force` (or `BD_ALLOW_REMOTE_MIGRATE=1` for scripted/CI
use) is the explicit override for the one clone confirming it is the
designated migrator, who is then expected to `bd dolt push` the migrated
schema so every other clone just pulls the already-migrated state. Concretely,
every non-designated clone's catch-up path is a single command — install the
new binary and run `bd bootstrap` — rather than independently invoking
`bd migrate` against its own copy.

**Sources:**
- `sources/steveyegge/beads/docs-ARCHITECTURE.md-fd45feca.md` (lines 8-95)
- `sources/steveyegge/beads/README.md.md` (lines 110-177, storage modes; "Upgrading?" migration-ownership note, 2026-07-02 revision; non-migrator clones catch up via `bd bootstrap`, 2026-07-10 revision; "Prefer a different database?" storage-backends teaser, 2026-07-11 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/README.md
- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (remote-migrate refusal gate, `--force`/`BD_ALLOW_REMOTE_MIGRATE`, 2026-07-08 revision; `--backend=<postgres|mysql|sqlite>` and connection flags, Dolt-only-versioned framing, `bd audit`/`bd history --events` two-tier history, 2026-07-11 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md