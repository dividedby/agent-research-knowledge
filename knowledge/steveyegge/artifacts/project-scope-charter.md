# Project Scope Charter

Beads implements strict product boundaries to remain reliable, understandable, and composable as a focused issue tracker for AI-supervised development.

## Core Scope Definition

Beads owns issue tracking primitives:

- **Issues and issue lifecycle** - Creation, status, priority, assignment management
- **Dependency relationships and readiness** - Blocking relationships, ready work detection
- **Labels, comments, metadata** - Tagging, discussion, extensible data attachment
- **Local CLI workflows** - Command-line operations around core concepts
- **Import, export, sync, backup** - Data movement and recovery operations
- **Tracker integrations** - Translation from external tracker data into beads concepts

**Absorption principle:** Within these boundaries, the project should absorb useful contributor work when practical. If a contribution has value but doesn't fit as submitted, prefer preserving the value by simplifying it, moving it to metadata, routing it to an integration/plugin, or reimplementing the use case in a smaller design.

## Orchestration Boundary

**Strict separation:** Beads should not know about orchestration layers built on top of it.

**Systems out of scope:**
- Gastown, Gas City, schedulers, swarms, release coordinators
- Future workflow engines that use beads as substrate
- Agent routing, task assignment strategy, model choice, retry plans
- Scheduling, workflow semantics, cross-system coordination

**Exposed interfaces:** Core beads can expose stable issue data, metadata, CLI output, and documented extension points. The orchestration layer owns orchestration policy.

**When orchestration needs extra per-issue data:** Prefer issue metadata before adding first-class fields or commands.

## Storage Boundary

**Core principle:** Beads should not become a storage engine.

**Dolt provides:** Storage, versioning, sync, merge behavior, concurrency, crash safety. Beads puts data in and pulls data out through the storage boundary.

**Forbidden patterns:**
- Storage-engine details leaking into beads packages (unless part of deliberate storage interface)
- Beads-side flocks, engine introspection, storage-specific retry loops
- Crash-recovery workarounds, schema poking that belongs in Dolt or Dolt driver

**When storage interface is inadequate:** Widen the interface or route the issue to the driver instead of embedding storage-engine logic in core.

**Mechanically enforced:** a `depguard` rule in `.golangci.yml` denies
`github.com/dolthub/` imports outside `internal/storage/` and
`internal/doltserver/` for non-test code, with the rule's exception list
documenting (and justifying) the only sanctioned crossings. This turns the
Storage Boundary from a review-time convention that depends on a maintainer
noticing a drift into a build-time check that fails the same way every time.

**The boundary also disciplines rollout pace, not just import graphs:** `bd
doctor` support for embedded mode is being enabled one subcommand at a time,
each change human-vetted, rather than lifting the embedded-mode gate in
`cmd/bd/doctor.go` wholesale — database-layer checks and fixes stay
server-gated until the driver interface actually covers them. A boundary that
constrains *what* can cross it turns out to constrain *how fast* new surface
area crosses it too.

## Schema Boundary

**Stability principle:** The database schema is considered stable. Schema changes are allowed when there's a pressing product or correctness need, but they should not be the first answer to extension requests.

**Use issue metadata first when:**
- Data is specific to one integration, orchestrator, or team workflow
- Data is advisory rather than part of beads' core issue model  
- Data can be represented as JSON without harming queryability
- Shape may evolve before it deserves a stable CLI or schema contract

**Promote to first-class schema only when:** Field has broad, durable meaning for beads itself and migration cost is justified.

## Integration Boundary

**Purpose definition:** Tracker integrations are adoption bridges, not a second product surface.

**In scope:**
- Map external tracker data into beads concepts
- Keep the dependency graph useful
- Provide migration and sync capabilities

**Out of scope:**
- Replicate tracker UIs, notification systems
- Credential vaults, webhook gateways  
- Cross-tracker automation beyond basic sync

**Reference:** See Integration Charter for detailed policy for GitHub, GitLab, Jira, Linear, Azure DevOps integrations.

## Review Posture

**Fences, not bounce messages:** These boundaries are guidance for transformation, not rejection criteria.

**For pull requests and proposals:**
1. **Identify contributor value first** - What problem are they solving?
2. **Keep the part that belongs in core** when possible
3. **Move boundary-crossing behavior** to metadata, integrations, plugins, or external tools when that preserves the use case
4. **Preserve attribution** when transforming, cherry-picking, or reimplementing contributor work
5. **Explain clearly** when a feature belongs outside beads

**Last resort:** Use request-changes or rejection only after considering whether the project can absorb, transform, or reroute the useful part.

## Design Philosophy

**Small and focused:** Stay small enough to remain reliable, understandable, and composable.

**Clear boundaries:** Each layer has well-defined responsibilities:
- **Core beads:** Issue tracking primitives
- **Storage layer:** Dolt handles persistence, versioning, sync
- **Integration layer:** External tracker bridges  
- **Orchestration layer:** Workflow policy, agent coordination (external)

**Extensibility through metadata:** Prefer extensible metadata over schema changes for most extension needs.

**Contributor-friendly:** Transform and preserve contributor value rather than reject it outright.

## Enforcement Strategy

**Boundary violations are transformation opportunities:**
- Core logic that belongs in storage → Route to Dolt driver interface
- Orchestration logic in core → Move to metadata or external orchestrator
- Schema additions → Evaluate if metadata suffices first
- Integration complexity → Simplify to bridge-only functionality

**Maintainer responsibility:** Actively look for ways to preserve contributor value while maintaining boundaries.

## Sources

- `sources/steveyegge/beads/docs-PROJECT_CHARTER.md-cd654e43.md` (lines 4-114) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/PROJECT_CHARTER.md
- `sources/steveyegge/beads/docs-PROJECT_CHARTER.md-cd654e43.md` (Storage Boundary — `depguard` mechanical enforcement, 2026-07-08 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/PROJECT_CHARTER.md
- `sources/steveyegge/beads/AGENTS.md.md` (Storage Boundary — `bd doctor` embedded-mode gate lifted one subcommand at a time, human-vetted, 2026-07-15 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/AGENTS.md