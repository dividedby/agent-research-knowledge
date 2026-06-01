# Safety Invariant Architecture

Beads implements systematic safety invariants to prevent destructive operations, particularly around initialization and remote synchronization.

## Core Safety Problem

Distributed version control creates scenarios where local and remote state can diverge, leading to data loss if not carefully managed. The system must prevent:

- Silent overwrites of team data
- Orphaned local work that can't sync
- Agent actions that destroy issue history
- Race conditions during multi-agent initialization

## Safety Invariant System

### Invariant 1: Single-Source Identity Resolution

Every `bd init` invocation resolves `project_id` from exactly **one** explicitly-named source:
- (a) mint fresh
- (b) adopt from remote (automatic bootstrap when origin has `refs/dolt/data`)  
- (c) reuse remote identity with local reinit

When two disjoint candidate sources exist (local data + remote Dolt history) and no flag names the winner, `bd init` refuses.

### Invariant 2: Scope-Bound Force Flags

`--force` (and its replacement `--reinit-local`) bypasses the **local** data-safety guard only. It never authorizes silent divergence of remote history. When origin advertises `refs/dolt/data`, `bd init --force` refuses unless `--discard-remote` is also passed.

### Invariant 3: Central Chokepoint Pattern

Every flag on `bd init` that can interact with remote history routes through `CheckRemoteSafety` in `cmd/bd/init_safety.go`. Adding a new flag requires extending the guard matrix test - if the table doesn't exhaustively cover `(dataSource × flagSet) → outcome`, the safety system has a gap.

### Invariant 4: Error-Text-No-Echo

No runtime error output may contain a complete invocation of a destructive command. This prevents AI agents from copy-pasting destructive commands from error messages.

Flag identifiers (`--discard-remote`, `--destroy-token`) and safe-tool names are permitted; token values and hashes live only in help documentation.

### Invariant 5: Race-Safety

When `--discard-remote` is authorized, `bd init` re-verifies `refs/dolt/data` on origin between prompt/confirm and execute. If remote state changed during the confirmation window, the operation aborts.

## Guard Matrix Testing

The safety system uses comprehensive table-driven tests covering every permutation:

```go
TestCheckRemoteSafety_GuardMatrix  // All flag combinations × remote state
TestCheckRemoteSafety_RefusalTextNoEcho  // Ensures no destructive echoing  
TestInitForceRefusesWhenRemoteHasDoltData  // Regression protection
```

New flags must extend this matrix or coverage is incomplete.

## Exit Code Stability

Stable, grep-safe exit codes for automation:

```
10   ExitRemoteDivergenceRefused   --force without --discard-remote
11   ExitLocalExistsRefused        existing local data, declined destroy  
12   ExitDestroyTokenMissing       --discard-remote without valid token
```

## Flag Surface Design

```bash
bd init                         # mint, or auto-bootstrap if remote exists
bd init --reinit-local          # local reinit; refuses remote divergence  
bd init --reinit-local \        # local reinit, overwrite remote on push
    --discard-remote            # (requires interactive confirm or token)
bd bootstrap                    # adopt remote - signposted by init refusal
```

## Historical Context

The safety system emerged from systematic analysis of eight prior commits that each patched one surface of initialization safety without encoding the underlying invariant. Each commit added a guard for one data source but the `--force` flag lived in global scope, creating a pattern where safety bypasses inherited to all future guards.

The centralized chokepoint pattern prevents this anti-pattern by ensuring all safety decisions route through explicit, tested logic.

## Review Discipline

`.github/CODEOWNERS` points `cmd/bd/init*.go` at maintainers and references the safety ADR in review comments. Future reviewers are reminded to walk the guard matrix when new flags or data sources are added.

**Sources:**
- `sources/steveyegge/beads/docs-adr-0002-init-safety-invariants.md-fd3c98c2.md` (lines 4-168)
- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` (lines 33-68, testing isolation)