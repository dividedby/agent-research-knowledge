# Agent Session Execution Model

Beads defines specific patterns for how AI agents should pick up, execute, and sequence work across multiple sessions.

## Session Workflow Pattern

The canonical agent session follows this loop:

```bash
# 1. Query for ready work
bd ready --json

# 2. Claim a task atomically  
bd update <id> --claim

# 3. Execute the work (implementation-specific)

# 4. Close with reason
bd close <id> --reason \"Completed\"

# 5. Repeat until no ready work remains
```

## Multi-Session Persistence

Agents work through complex molecules over multiple sessions by following the dependency graph:

1. **Session start:** Query `bd ready` for available work
2. **Session work:** Execute all available ready work  
3. **Session end:** Some work may still be blocked by dependencies
4. **Next session:** New work becomes ready as blockers close
5. **Completion:** All work done when molecule has no open issues

## Execution Metadata Handling

Before using description text, agents must inspect structured execution metadata:

```bash
bd show <id> --json | jq '.[0] | {id,title,metadata,description,notes}'
```

Key metadata fields that control execution:
- `execution_agent_type` - Which type of agent should handle this
- `execution_suggested_model` - Recommended model for the work
- `execution_reasoning_effort` - How much reasoning is needed
- `execution_mode` - Execution approach
- `execution_parallel_group` - Parallel execution grouping

## Agent Coordination Primitives

### Atomic Claiming
```bash
bd update <id> --claim  # Sets assignee + in_progress atomically
```

Prevents multiple agents from picking up the same work.

### Session Context Loading
```bash
bd prime  # Loads workflow context and persistent memories
```

Provides agents with project context and accumulated insights.

### Memory Persistence
```bash
bd remember \"insight\"  # Store project memory across sessions
```

Allows agents to accumulate knowledge that survives session boundaries.

## Cross-Session Data Flow

### Write Operations Auto-Commit
Every write operation automatically commits to Dolt history:
- Creates audit trail for agent actions
- Enables rollback if needed
- Provides change attribution

### Sync Coordination
```bash
bd dolt push   # Share changes with team
bd dolt pull   # Get updates from team
```

Agents coordinate through shared Dolt database state.

## Agent Failure Handling

### Hanging Process Recovery
Beads includes completion timeout mechanisms to handle hanging agent processes, preventing deadlock in automated workflows.

### Issue Resurrection
Issues with hash-based IDs can be recovered from Dolt history even after deletion, providing resilience against agent errors.

### Orphaned Work Detection
The system can detect work that was committed to git but never closed in the issue tracker, surfacing incomplete agent sessions.

## Compound Workflow Traversal

When agents encounter blocked work, they can:

1. **Wait:** End session, resume when dependencies clear
2. **Traverse:** Continue into blocking molecules (compound execution)
3. **Delegate:** Create sub-work for other agents

**Bonding enables seamless traversal** - agents follow dependency edges across multiple work graphs as one logical unit.

## Session Boundary Practices

### Land the Plane Protocol
When completing work, agents must:
1. File follow-up issues for remaining work
2. Run quality gates if code changes were made
3. Update and close finished issues
4. **Push all changes to remote** (mandatory)
5. Clean up git state
6. Provide next-session prompt

### Quality Gates
- Run tests: `make test`
- Check linting: `golangci-lint run ./...`
- File P0 issues if gates fail

### Never Stop Before Push
The session is NOT complete until `git push` succeeds. Unpushed work breaks coordination with other agents.

**Sources:**
- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` (lines 247-304, session workflow)
- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` (lines 164-246, \"landing the plane\")
- `sources/steveyegge/beads/docs-MOLECULES.md-d06ec0d4.md` (lines 57-72, multi-day execution)