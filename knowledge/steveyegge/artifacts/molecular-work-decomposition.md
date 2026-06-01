# Molecular Work Decomposition

Beads uses a \"molecular chemistry\" metaphor to structure and execute complex workflows, decomposing large work items into graphs of dependent sub-work.

## Core Insight: Molecules Are Epics

**There's no fundamental difference between molecules and epics.** A molecule is just an epic (parent + children) with execution intent:

| Term | Meaning | When to Use |
|------|---------|-------------|
| **Epic** | Parent issue with children | General term for hierarchical work |
| **Molecule** | Epic with execution intent | When discussing workflow traversal |
| **Proto** | Epic with `template` label | Reusable pattern (optional) |

## Work = Issues + Dependencies

The fundamental model is simple:

1. **Work = issues with dependencies.** No special types needed.
2. **Dependencies control execution.** `blocks` = sequential, no dep = parallel.
3. **Agents execute until blocked.** When all ready work is done, workflow is complete.

## Phase Metaphor (Templates)

For reusable workflows, beads uses chemistry phases:

| Phase | Name | Storage | Synced | Purpose |
|-------|------|---------|--------|---------|
| **Solid** | Proto | `.beads/` | Yes | Frozen template |
| **Liquid** | Mol | `.beads/` | Yes | Active persistent work |
| **Vapor** | Wisp | `.beads/` (Wisp=true) | No | Ephemeral operations |

### Phase Commands

```bash
bd mol pour <proto>              # Proto → Mol (persistent instance)
bd mol wisp <proto>              # Proto → Wisp (ephemeral instance) 
bd mol squash <id>               # Mol/Wisp → Digest (permanent record)
bd mol burn <id>                 # Wisp → nothing (discard)
```

### When to Use Each Phase

| Use Case | Phase | Rationale |
|----------|-------|-----------|
| Feature work | Mol (pour) | Persists across sessions, audit trail |
| Patrol cycles | Wisp | Routine, no audit value |
| One-shot ops | Wisp | Scaffolding, not the work itself |
| Important discovery | Mol (--pour) | \"This matters, save it\" |

## Bonding: Connecting Work Graphs

**Bond = create a dependency between two work graphs.**

```bash
bd mol bond A B                    # B depends on A (sequential)
bd mol bond A B --type parallel    # Organizational link, no blocking
bd mol bond A B --type conditional # B runs only if A fails
```

### Bonding Effects

| Operands | Result |
|----------|--------|
| epic + epic | Creates dependency edge between them |
| proto + epic | Spawns proto as new issues, attaches to epic |
| proto + proto | Creates compound template |

## Wisp Lifecycle and Isolation

Wisps are intentionally **local-only**:

- Exist only in the spawning agent's local database
- **Never exported or synced**
- Cannot resurrect from other clones (they were never there)
- **Hard-deleted** when squashed (no tombstones needed)

This design enables:
- **Fast local iteration:** No sync overhead during execution
- **Clean history:** Only the digest (outcome) enters git
- **Agent isolation:** Each agent's execution trace is private
- **Bounded storage:** Wisps don't accumulate across clones

### Wisp vs Regular Issue Deletion

| Aspect | Regular Issues | Wisps |
|--------|---------------|-------|
| Synced to remotes | Yes | No |
| Tombstone on delete | Yes | No |
| Can resurrect | Yes (without tombstone) | No (never synced) |
| Deletion method | `CreateTombstone()` | `DeleteIssue()` (hard delete) |

## Common Decomposition Patterns

### Sequential Pipeline
Epic with ordered steps where each step blocks the next.

### Parallel Fanout with Gate
Epic with multiple parallel tasks feeding into an aggregation step that waits for all.

### Dynamic Bonding (Christmas Ornament)
Runtime discovery of workers with dynamic attachment of work arms:

```bash
for worker in $(bd agent list); do
  bd mol bond mol-worker-arm $PATROL_ID --ref arm-$worker --var name=$worker
done
```

**Sources:**
- `sources/steveyegge/beads/docs-MOLECULES.md-d06ec0d4.md` (lines 4-295)
- `sources/steveyegge/beads/docs-ARCHITECTURE.md-fd45feca.md` (lines 311-361, wisps section)