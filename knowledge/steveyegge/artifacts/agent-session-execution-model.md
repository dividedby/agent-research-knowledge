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

A project can drop a `.beads/PRIME.md` to override the *workflow-text* portion
of `bd prime`'s output, but persistent memories are still appended on top of a
custom template — a project-specific priming doc can't accidentally silence
memory injection. Two flags tune how much of that output an agent actually
wants in context: `--memories-only` returns just the memories section (for
hook contexts that only need that), and `--no-memories` omits it (for when
accumulated memories have grown large enough to threaten the context budget);
`--memories-only` wins if both are set.

### Memory Persistence
```bash
bd remember \"insight\"               # Store project memory across sessions
bd remember \"...\" --key dolt-phantoms  # Keyed, updates in place if re-stored
bd remember dolt-phantoms            # Bare existing key: reads it (= bd recall)
bd recall dolt-phantoms             # Retrieve full content by key
bd memories \"race flag\"             # List / keyword-search stored memories
```

Allows agents to accumulate knowledge that survives session boundaries — and,
explicitly, **account rotations** (a new agent identity inherits the accumulated
insights). Memories are auto-injected at prime time, so they reappear in every
session without manual loading; a key makes a memory addressable and idempotent
(re-`remember`ing the same key updates in place rather than duplicating).
`bd remember` also collapses into `bd recall` when its positional argument is a
bare string that names an existing memory key — one command serves both write
and read, disambiguated by whether the key already exists, rather than forcing
the agent to remember (and pick correctly between) two verbs for the same
concept.

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

### Claim Recovery
If an agent crashes mid-work while holding a claim, `bd unclaim <id>` releases
it back to the ready pool so another agent (or the restarted same one) can pick
it up — the explicit escape hatch for the atomic-claim invariant when the
claiming process itself is gone, not just its work state. Plain `bd unclaim`
covers self-recovery; releasing a claim held by a *different* actor needs
`--force`, scoped to admin/reaper use — so an orchestrator sweeping stuck
claims across a fleet has an explicit, named override rather than being able
to silently steal another agent's in-flight work. Even with `--force`
available, the documented etiquette is to coordinate with the holder first —
an issue can look idle while its claim is still live — and to prefer letting
lease expiry (`bd reclaim`) recover genuinely abandoned work over an admin
force-release, since expiry is a mechanical, no-judgment-call signal that the
holder is actually gone.

### Claim Pools: Dispatching to a Pseudo-Assignee
A dispatcher can pre-assign issues to a pool alias (e.g. `fable-crew`) instead
of a specific agent, then list that alias in the `claim.pools` config
(`bd config set claim.pools "fable-crew,night-crew"`). Any actor can then take
a pool-assigned issue with `--claim` — the anti-steal protection that normally
guards an issue assigned to a *real* actor (or to an alias not in the list) is
deliberately waived for listed pool aliases, since the point of a pool is
first-come-first-served pickup, not reservation. The pool identity doesn't
travel with the claim, though: if a pool take's lease expires, `bd reclaim`
returns the issue to the general unassigned pool, not back to the pool alias
it was originally dispatched to — so a stalled pool item re-enters ordinary
triage instead of silently re-queuing into the same pool unattended.

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
4. Handle git/sync **per the active context profile** (see below)
5. Clean up git state
6. Provide next-session prompt

### Quality Gates
- Run tests: `make test`
- Check linting: `golangci-lint run ./...`
- File P0 issues if gates fail

### Agent Context Profiles — the managed block is subordinate, not sovereign
The managed bd instruction block carries a version+profile marker
(`v:1 profile:full hash:…`) and an explicit disclaimer: it is *task-tracking
guidance, not permission to override repository, user, or orchestrator
instructions*. The earlier unconditional "you MUST `git push`" mandate is now
**gated by a context profile**, because a managed block injected into an arbitrary
repo cannot assume it has authority to commit/push/sync:

- **Conservative (default)** — use bd for tracking; **do not** run git commits,
  pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed
  files, validation, and the proposed commands — then wait.
- **Minimal** — instruction files stay pointers to `bd prime`; same conservative
  git policy.
- **Team-maintainer** — only when the repo explicitly opts in may the agent close
  beads, run quality gates, commit, and push at session close. A live "do not
  commit/push" instruction still wins.

The profile is a selectable runtime setting, not just descriptive prose:
`bd config set agent.profile team-maintainer` (or `BD_AGENT_PROFILE=team-maintainer`
per-session, which takes precedence over the persisted config) actually switches
which git/commit-authority wording the injected instruction block carries.

The precedence rule is absolute: explicit user/orchestrator instructions override
the block, and a blocked sync/push is a **stop-and-report**, not a silent skip.
This reframes the "land the plane" push mandate — once a universal imperative
designed for a single dedicated repo — into a default-safe stance for a tracker
meant to be embedded across many repos with differing authority.

### Agent attribution: signed commits and comments
Agent-prepared commits carry an `Agent-Signature:` trailer (alongside the
`(bd-xxx)` issue-ID convention), falling back to `unknown-model` /
`unknown-reasoning` when reliable runtime metadata is unavailable; agent-written
GitHub comments and reviews are signed the same way. This extends the commit-ID
convention from *which issue* a commit closes to *which agent identity* produced
it — attribution that survives into the audit trail and the PR thread, so a fleet
of agents stays accountable, not anonymous.

**Sources:**
- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` (session workflow; "landing the plane"; `Agent-Signature:` commit/comment trailer, 2026-06-21 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/AGENT_INSTRUCTIONS.md
- `sources/steveyegge/beads/AGENTS.md.md` (Agent Context Profiles + instruction-precedence, profile-gated session-completion git policy, 2026-06-21 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/AGENTS.md
- `sources/steveyegge/beads/docs-MOLECULES.md-d06ec0d4.md` (lines 57-72, multi-day execution)
- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (`bd remember`/`bd recall`/`bd memories` — keyed memory, persistence across account rotations; bare-existing-key-recalls-instead-of-stores overload, 2026-07-03 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (`bd config set agent.profile` / `BD_AGENT_PROFILE` — explicit runtime selector for the conservative/minimal/team-maintainer profile, 2026-07-08 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
- `sources/steveyegge/beads/docs-QUICKSTART.md-ef67bedb.md` (`bd unclaim` — releasing a stuck claim after an agent crash, 2026-07-07 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/QUICKSTART.md
- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (`bd unclaim --force` — admin/reaper override to release another actor's claim, 2026-07-13 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (`bd prime --no-memories`/`--memories-only` and the PRIME.md-override-keeps-memories clarification, 2026-07-14 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (`bd unclaim` — coordinate-with-holder etiquette and prefer-lease-expiry guidance; `bd config` — `claim.pools` pool-aware claiming, anti-steal waiver, `bd reclaim` returns expired pool takes to the unassigned pool, 2026-07-17 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md