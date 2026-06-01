# Molecular Work Decomposition

Beads uses a \"molecular chemistry\" metaphor to structure and execute complex workflows, decomposing large work items into graphs of dependent sub-work.

## Core Insight: Molecules Are Epics

**There's no fundamental difference between molecules and epics.** A molecule is just an epic (parent + children) with execution intent:

| Term | Meaning | When to Use |
|------|---------|-------------|
| **Epic** | Parent issue with children | General term for hierarchical work |
| **Molecule** | Epic with execution intent | When discussing workflow traversal |
| **Proto** | Epic with `template` label | Reusable pattern (optional) |

## The Execution Model

The fundamental model is simple:

1. **Work = issues with dependencies.** No special types needed.
2. **Dependencies control execution.** `blocks` = sequential, no dep = parallel.
3. **Molecules are just epics.** Any epic with children is a molecule. Templates are optional.
4. **Bonding = adding dependencies.** Connect work graphs.
5. **Agents execute until blocked.** When all ready work is done, workflow is complete.

### How Work Flows

An agent picks up a molecule (epic with children) and executes ready children in parallel until everything closes:

```
epic-root (assigned to agent)
├── child.1 (no deps → ready)      ← execute in parallel
├── child.2 (no deps → ready)      ← execute in parallel  
├── child.3 (needs child.1) → blocked until child.1 closes
└── child.4 (needs child.2, child.3) → blocked until both close
```

**Ready work:** `bd ready` shows issues with no open blockers.
**Blocked work:** `bd blocked` shows what's waiting.

### Dependency Types That Block

| Type | Semantics | Use Case |
|------|-----------|----------|
| `blocks` | B can't start until A closes | Sequencing work |
| `parent-child` | If parent blocked, children blocked | Hierarchy (children parallel by default) |
| `conditional-blocks` | B runs only if A fails | Error handling paths |
| `waits-for` | B waits for all of A's children | Fanout gates |

**Non-blocking types:** `related`, `discovered-from`, `replies-to` - link issues without affecting execution.

### Default Parallelism

**Children are parallel by default.** Only explicit dependencies create sequence:

```bash
# These three tasks run in PARALLEL (no deps between them)
bd create "Task A" -t task
bd create "Task B" -t task  
bd create "Task C" -t task

# Add dependency to make B wait for A
bd dep add <B-id> <A-id>   # B depends on A (B needs A)
```

### Multi-Day Execution

An agent works through a molecule by:
1. Getting ready work (`bd ready`)
2. Claiming it (`bd update <id> --claim`)
3. Doing the work
4. Closing it (`bd close <id>`)
5. Repeat until molecule is done

If blocked by another molecule:
- Agent either waits, or
- Agent continues into the blocking molecule (compound execution)

**Bonding enables compound execution:** When you bond molecule A to molecule B, the agent can traverse both as one logical unit of work.

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
Epic with ordered steps where each step blocks the next:

```bash
bd create "Pipeline" -t epic
bd create "Step 1" -t task --parent <pipeline>
bd create "Step 2" -t task --parent <pipeline>
bd create "Step 3" -t task --parent <pipeline>
bd dep add <step2> <step1>
bd dep add <step3> <step2>
```

### Parallel Fanout with Gate
Epic with multiple parallel tasks feeding into an aggregation step:

```bash
bd create "Process files" -t epic
bd create "File A" -t task --parent <epic>
bd create "File B" -t task --parent <epic>
bd create "File C" -t task --parent <epic>
bd create "Aggregate" -t task --parent <epic>
# Aggregate needs all three (waits-for gate)
bd dep add <aggregate> <fileA> --type waits-for
```

### Dynamic Bonding (Christmas Ornament)
Runtime discovery of workers with dynamic attachment of work arms:

```bash
# In a survey step, discover workers and bond arms dynamically
for worker in $(bd agent list); do
  bd mol bond mol-worker-arm $PATROL_ID --ref arm-$worker --var name=$worker
done
```

Creates:
```
patrol-x7k (wisp)
├── preflight
├── survey-workers
│   ├── patrol-x7k.arm-ace (dynamically bonded)
│   ├── patrol-x7k.arm-nux (dynamically bonded)
│   └── patrol-x7k.arm-toast (dynamically bonded)
└── aggregate (waits for all arms)
```

## Agent Pitfalls

### 1. Temporal Language Inverts Dependencies

**Wrong:** "Phase 1 comes before Phase 2" → `bd dep add phase1 phase2`
**Right:** "Phase 2 needs Phase 1" → `bd dep add phase2 phase1`

Use requirement language. Verify with `bd blocked`.

### 2. Assuming Order = Sequence

Numbered steps don't create sequence. Dependencies do:

```bash
# These run in PARALLEL despite names
bd create "Step 1" ...
bd create "Step 2" ...
bd create "Step 3" ...

# Add deps to sequence them
bd dep add step2 step1
bd dep add step3 step2
```

### 3. Forgetting to Close Work

Blocked issues stay blocked forever if their blockers aren't closed:

```bash
bd close <id> --reason "Done"
```

### 4. Orphaned Wisps

Wisps accumulate if not squashed/burned:

```bash
bd mol wisp list        # Check for orphans
bd mol squash <id>      # Create digest
bd mol burn <id>        # Or discard
bd mol wisp gc          # Garbage collect old wisps
```

## Layer Cake Architecture

For reference, how the layers stack:

```
Formulas (JSON compile-time macros)      ← optional, for complex composition
    ↓
Protos (template issues)                  ← optional, for reusable patterns
    ↓
Molecules (bond, squash, burn)            ← workflow operations
    ↓
Epics (parent-child, dependencies)        ← DATA PLANE (the core)
    ↓
Issues (Dolt, version-controlled)         ← STORAGE
```

**Most users only need the bottom two layers.** Protos and formulas are for reusable patterns and complex composition.

**Sources:**
- `sources/steveyegge/beads/docs-MOLECULES.md-d06ec0d4.md` (lines 4-295)
- `sources/steveyegge/beads/docs-ARCHITECTURE.md-fd45feca.md` (lines 311-361, wisps section)