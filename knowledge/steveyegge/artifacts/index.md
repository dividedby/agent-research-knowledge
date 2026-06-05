# Artifacts — steveyegge

How `beads` is built as a dependency-aware agent task tracker: its work-graph
model, dependency/gate system, and how it decomposes and sequences agent work.
One concept per file; this index lists them, one line each.

- `hash-based-collision-prevention.md` — Content-based hashing for distributed ID generation preventing merge collisions
- `two-layer-data-architecture.md` — CLI + Dolt database architecture enabling distributed issue tracking  
- `dependency-aware-work-sequencing.md` — Blocking relationships and ready work detection for agent execution control
- `molecular-work-decomposition.md` — Chemistry metaphor for structuring complex workflows into executable graphs
- `agent-session-execution-model.md` — Patterns for agent work pickup, execution, and cross-session coordination
- `safety-invariant-architecture.md` — Systematic safety guards preventing destructive operations in distributed workflows
- `multi-remote-distribution-model.md` — Multi-remote sync architecture for backup redundancy and data sovereignty
- `agent-integration-architecture.md` — Context-efficient, editor-agnostic integration model via CLI + hooks over MCP
- `multi-repo-routing-architecture.md` — Auto-routing system for OSS contributors with role detection and issue hydration
- `project-scope-charter.md` — Product boundaries and design principles maintaining focus on issue tracking primitives
- `cli-visual-design-system.md` — Visual design principles prioritizing cognitive efficiency over decoration
- `async-coordination-gates.md` — Beads (gates, merge-slot) that block work on external async conditions and serialize conflict resolution
- `human-in-the-loop-escalation.md` — A `human` label/queue turning "an agent needs a person" into trackable, answerable work
