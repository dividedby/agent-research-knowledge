# Multi-Remote Distribution Model

Beads implements a sophisticated multi-remote architecture for distributed synchronization, enabling backup redundancy, data sovereignty, and hybrid sync patterns.

## Architecture Overview

The system supports multiple Dolt remotes while maintaining clear authority relationships:

```yaml
federation:
  remote: \"dolthub://org/beads\"     # primary, Dolt remote name: \"origin\"
  additional-remotes:
    - name: backup
      url: \"az://account.blob.core.windows.net/container/path\"
    - name: archive  
      url: \"gs://bucket/path\"
```

## Design Principles

### Pull Authority
The primary remote (`federation.remote`) is always authoritative for pulls. Additional remotes are **push-only mirrors**.

**Rationale:**
- Backup remotes may be stale due to partial push failures
- Mirrors must not diverge independently - pulling from mirrors creates split-brain ambiguity  
- Single source of truth simplifies conflict resolution

**Disaster Recovery:** If primary remote is permanently lost, operator manually promotes a mirror by updating `federation.remote` to point to mirror URL. This is explicit, auditable action - not automatic failover.

### Push Semantics

**Sequential Push:** Primary (`origin`) first, then additional remotes in list order. This gives clear error semantics - primary success is the minimum bar.

**Partial Failure:** If primary succeeds but backup fails:
- Command reports success with warnings
- Operator responsible for retrying failed backup push (`bd dolt push --remote backup`)
- Exit code reflects primary success (0) with diagnostic output for backup failures
- Future `--strict` mode could fail on any mirror push failure for CI requiring confirmed redundancy

### Credential Routing

Phase 1 relies on ambient environment variables - user sets appropriate credentials before invoking `bd dolt push --remote <name>`. This matches how Dolt itself handles credentials.

Phase 2 may introduce per-remote credential configuration within the `additional-remotes` object structure.

## Implementation Phases

### Phase 1: Dolt-Native Flags
Expose Dolt's native multi-remote capability:
- Add `--remote <name>` flag to `bd dolt push`
- Users manage additional remotes via `bd dolt remote add <name> <url>`
- No config changes, minimal code
- Pull remains single-remote only (primary/`origin`)

### Phase 2: Config-Managed Remotes  
Add config-driven additional remotes:
- Keep `federation.remote` as primary (backwards compatible)
- Add `federation.additional-remotes` as ordered list
- Introduce **SyncOrchestrator** component for multi-remote coordination
- Integrate with existing drift/apply infrastructure

## SyncOrchestrator Component

Dedicated component following Single Responsibility Principle:
- Iterates configured remotes in order
- Handles per-remote push with appropriate credential routing
- Aggregates results (success/warning/failure) 
- Keeps `DoltStore` focused on single-remote operations

## Out of Scope

### Selective Filtering
Routing subsets of issues to specific remotes based on metadata requires fundamentally different architecture - application-level filtering at Dolt row/branch level rather than remote-level push.

### Automatic Failover
No automatic primary-to-mirror promotion. Failover is explicit operator action.

### Parallel Push
Sequential push for simplicity and clear error ordering. Parallel push is potential future optimization but adds complexity to error aggregation and credential isolation.

## Use Cases Enabled

- **Backup redundancy:** Push to primary (DoltHub) + backup (Azure Blob Storage) simultaneously
- **Data sovereignty:** Route data to region-specific remotes for compliance
- **Hybrid sync:** Push to DoltHub for collaboration + Azure for enterprise backup
- **Incremental risk:** Avoid big-bang changes to working federation system

**Sources:**
- `sources/steveyegge/beads/docs-adr-0001-multi-remote-approach.md-3ff37fd9.md` (lines 4-242)