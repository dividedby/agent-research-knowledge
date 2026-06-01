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

**Sources:**
- `sources/steveyegge/beads/docs-ARCHITECTURE.md-fd45feca.md` (lines 8-95)
- `sources/steveyegge/beads/README.md.md` (lines 110-177, storage modes)