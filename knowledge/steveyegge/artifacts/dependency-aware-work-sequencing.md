# Dependency-Aware Work Sequencing

Beads implements a sophisticated dependency system that controls work execution through explicit blocking relationships, enabling agents to pick up ready work automatically.

## Core Concept: Ready Work Detection

The key insight is that agents execute work by querying for issues with no open blocking dependencies:

```bash
bd ready    # Shows issues with no blockers
bd blocked  # Shows what's waiting and why
```

An issue is "ready" when ALL of its blocking dependencies are closed.

## Dependency Types

### Blocking Types (Affect `bd ready`)

| Type | Meaning | Agent Impact |
|------|---------|--------------|
| `blocks` (default) | Issue B cannot start until A closes | Sequential execution |
| `parent-child` | Children blocked when parent blocked | Hierarchical control |
| `conditional-blocks` | B runs only if A fails | Error handling paths |
| `waits-for` | B waits for all of A's children | Fanout aggregation |

### Non-Blocking Types (Graph annotations only)

| Type | Purpose |
|------|---------|
| `related` | Informational link |
| `tracks` | Progress tracking |
| `discovered-from` | Found during other work |
| `caused-by` | Root cause link |
| `validates` | Test or verification link |
| `supersedes` | Replacement link |

## Work Execution Model

### Default Parallelism

**Children are parallel by default.** Only explicit dependencies create sequence:

```bash
# These three tasks run in PARALLEL (no deps between them)
bd create \"Task A\" -t task
bd create \"Task B\" -t task  
bd create \"Task C\" -t task

# Add dependency to make B wait for A
bd dep add <B-id> <A-id>   # B depends on A
```

### Multi-Day Agent Execution

Agents work through complex workflows by:

1. Getting ready work (`bd ready`)
2. Claiming it (`bd update <id> --claim`)
3. Doing the work
4. Closing it (`bd close <id>`)
5. Repeat until all work is done

### Layered Execution

The dependency system organizes work into layers:

- **Layer 0**: No dependencies (can start immediately)
- **Layer 1**: Depends on layer 0
- **Higher layers**: Depend on lower layers
- **Same layer**: Can run in parallel

## Cross-System Integration: Gates

Gates bridge external conditions into the dependency graph:

| Gate Type | Condition | Auto-Resolution |
|-----------|-----------|-----------------|
| `gh:pr` | PR merged | `gh pr view` returns MERGED |
| `gh:run` | CI passes | `gh run view` returns completed + success |
| `timer` | Time elapsed | Current time exceeds timeout |
| `bead` | Cross-rig issue closed | Remote bead status checked |
| `human` | Manual approval | `bd gate resolve <id>` |

Gates are wired into dependencies like any other issue, allowing agents to wait for external systems naturally.

## Compound Workflow Execution

**Bonding enables compound execution:** When molecule A blocks molecule B, agents can traverse both as one logical unit of work, continuing seamlessly from A into B across multiple sessions.

**Sources:**
- `sources/steveyegge/beads/docs-DEPENDENCIES.md-ccda48ce.md` (lines 4-330)
- `sources/steveyegge/beads/docs-MOLECULES.md-d06ec0d4.md` (lines 16-72)
- `sources/steveyegge/beads/README.md.md` (lines 62-73, essential commands)