# Metadata-First Execution Routing

Steve Yegge's beads system embodies a key agent workflow principle: structured metadata should drive execution decisions before natural language descriptions.

## Core Principle: Inspect Metadata Before Prose

When enacting a beads issue, agents must inspect structured metadata before using description or notes to choose execution mode, delegation, model, reasoning level, or parallel group:

```bash
bd show <id> --json | jq '.[0] | {id,title,metadata,description,notes}'
```

## Execution Metadata Keys

The authoritative execution hints:

- `execution_agent_type` — Which type of agent should handle this work
- `execution_suggested_model` — Recommended model for the work  
- `execution_reasoning_effort` — How much reasoning is needed
- `execution_mode` — Execution approach (autonomous, supervised, etc.)
- `execution_parallel_group` — Parallel execution grouping

## Routing Logic

When these keys are present, treat them as authoritative execution hints:

- Use `metadata` for execution routing decisions
- Use `description` for work scope understanding  
- Use `notes` for rationale or fallback context

## Parent/Orchestrator Responsibility

Parent/orchestrator agents **must** read these fields before spawning subagents because a running subagent cannot change its model or reasoning effort after launch.

This creates a clear separation of concerns:
- **Planning phase:** Parent reads metadata and makes routing decisions
- **Execution phase:** Subagent executes within predetermined constraints

## Implementation Pattern

```bash
# 1. Read metadata first
METADATA=$(bd show <id> --json | jq -r '.[0].metadata')

# 2. Route based on metadata, not description
if [[ \"$METADATA\" =~ execution_agent_type.*specialized ]]; then
  # Route to specialized agent
elif [[ \"$METADATA\" =~ execution_reasoning_effort.*high ]]; then  
  # Use high-reasoning model
fi

# 3. Pass description as context to chosen execution path
DESCRIPTION=$(bd show <id> --json | jq -r '.[0].description')
```

## Rationale

This pattern prevents the common anti-pattern where:
1. Natural language descriptions contain implicit execution hints
2. Agents must parse prose to understand how to execute
3. Execution routing becomes unreliable and inconsistent
4. Model/reasoning decisions are made reactively during execution

By encoding execution metadata explicitly, the system enables:
- **Deterministic routing:** Same metadata always routes the same way
- **Parallel orchestration:** Parent can dispatch multiple agents with appropriate models
- **Resource optimization:** Right-sized models for different reasoning levels
- **Execution traceability:** Clear audit trail of routing decisions

**Sources:**
- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` (lines 257-278)