# Multi-Repo Routing Architecture

Beads implements intelligent routing to solve the OSS contributor problem: enabling local planning without polluting upstream repositories with planning issues.

## Auto-Routing System

The routing system automatically detects user role and directs issues to appropriate repositories based on contributor vs maintainer status.

### Role Detection Strategy

**Priority order:**
1. **Explicit git config** (highest priority):
   ```bash
   git config beads.role maintainer
   git config beads.role contributor
   ```

2. **Push URL inspection** (automatic detection):
   - SSH URLs (`git@github.com:user/repo.git`) → Maintainer
   - HTTPS with credentials → Maintainer  
   - HTTPS without credentials → Contributor
   - No remote → Contributor (fallback)

### Routing Behavior

**Auto mode configuration:**
```yaml
routing:
  mode: auto
  maintainer: "."                    # Current repo
  contributor: "~/.beads-planning"   # Separate planning repo
```

**Execution patterns:**
```bash
# Maintainer (SSH access)
bd create "Fix bug" -p 1
# → Creates in current repo (source_repo = ".")

# Contributor (HTTPS fork) 
bd create "Fix bug" -p 1  
# → Creates in planning repo (source_repo = "~/.beads-planning")
```

## Multi-Repo Hydration

**Critical requirement:** When routing separates issues across repos, hydration must aggregate them into unified views.

### The Integration Problem

Auto-routing writes issues to separate repositories, but `bd list` by default only shows current repository's database. Without hydration, routed issues become "invisible."

### Hydration Architecture

```yaml
routing:
  mode: auto
  contributor: ~/.beads-planning
repos:
  primary: "."
  additional:
    - ~/.beads-planning
```

**How it works:**
1. **Dolt database as source of truth:** Each repo maintains its own database
2. **Periodic sync:** Beads syncs from `repos.additional` every sync cycle
3. **Source tracking:** Each issue tagged with `source_repo` field
4. **Unified view:** Commands show aggregated issues from all configured repos

### Automatic Setup Integration

`bd init --contributor` configures both routing AND hydration automatically:
- Sets `routing.mode=auto`
- Configures `routing.contributor=~/.beads-planning`  
- Adds `repos.additional=[~/.beads-planning]`

## Discovered Issue Inheritance

Issues with `discovered-from` dependencies automatically inherit parent's repository:

```bash
# Parent in current repo
bd create "Implement auth" -p 1
# → Created as bd-abc (source_repo = ".")

# Discovered issue inherits parent's repo
bd create "Found bug in auth" -p 1 --deps discovered-from:bd-abc
# → Created with source_repo = "." (same as parent)
```

This ensures discovered work stays co-located with parent task.

## Common Workflow Patterns

### OSS Contributor Pattern
**Setup:** `bd init --contributor` (wizard handles configuration)

**Runtime behavior:**
- All planning issues auto-route to `~/.beads-planning`
- Never appears in upstream PRs
- `bd ready` shows unified view of upstream + planning work
- Git operations remain clean

### Team Collaboration Pattern  
**Setup:** `bd init --team` (shared repository planning)

**Runtime behavior:**
- Issues committed to shared repository  
- Visible to all team members
- Optional personal planning in separate repos

### Multi-Phase Development
**Setup:** Multiple repositories for different project phases

**Runtime behavior:**
- Planning repo for design work
- Implementation repo for code work  
- Dependencies can span repos via `blocks` relationships
- Unified views via hydration

## Server Architecture Integration

### Single MCP Server Approach
**Recommended:** One MCP server instance with automatic routing
- Detects workspace from working directory
- Routes to correct per-project Dolt server
- Auto-starts servers as needed
- Maintains complete database isolation

### Dolt Server Coordination
**Per-project mode (default):**
```
MCP Server (one instance)
    ↓
Per-Project Dolt Servers (one per workspace)
    ↓
Dolt Databases (complete isolation)
```

**Shared server mode (optional):**
- `BEADS_DOLT_SHARED_SERVER=1`
- All projects use single Dolt server at `~/.beads/shared-server/`
- Database isolation via per-project database names

## Explicit Override Capabilities

Routing can always be overridden:
```bash
# Force creation in specific repo (overrides auto-routing)
bd create "Fix bug" -p 1 --repo /path/to/repo
bd create "Add feature" -p 1 --repo ~/my-planning
```

## Backward Compatibility

- **Single-repo workflows unchanged:** No multi-repo config = current repo only
- **Explicit --repo always wins:** Flag overrides any auto-routing  
- **No schema changes:** Pure config-based, no database migrations
- **Graceful degradation:** Missing hydration config detected by `bd doctor`

## Implementation Architecture

**Key components:**
- `internal/routing/routing.go` - Role detection and routing logic
- Repository aggregation via hydration layer
- Config-driven routing tables
- Source provenance tracking via `source_repo` field

**API patterns:**
- `DetectUserRole(repoPath)` - Git-based role detection
- `DetermineTargetRepo(config, userRole, repoPath)` - Routing decision
- Multi-database query aggregation for unified views

## Sources

- `sources/steveyegge/beads/docs-ROUTING.md-52ffe97f.md` (lines 4-246)  
- `sources/steveyegge/beads/docs-MULTI_REPO_AGENTS.md-82567446.md` (lines 44-353)