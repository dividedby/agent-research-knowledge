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

**Sources:**
- `sources/steveyegge/beads/docs-ARCHITECTURE.md-fd45feca.md` (lines 8-95)
- `sources/steveyegge/beads/README.md.md` (lines 110-177, storage modes; "Upgrading?" migration-ownership note, 2026-07-02 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/README.md