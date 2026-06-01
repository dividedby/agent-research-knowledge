# Agent Integration Architecture

Beads implements a context-efficient, editor-agnostic integration model designed to minimize token overhead while maximizing compatibility across agent platforms.

## Integration Strategy: CLI + Hooks Over MCP

**Primary approach:** CLI commands with git hooks for automatic context refresh
- `bd prime` command for context injection (~1-2k tokens)
- SessionStart hooks for automatic context refresh  
- Direct CLI commands with `--json` flags
- Optional plugin for slash commands and enhanced UX

**Alternative:** MCP Server for constrained environments
- Higher context overhead (MCP tool schemas add 10-50k tokens)
- Use only when CLI unavailable (Claude Desktop without shell)

## Context Efficiency Philosophy

**Core principle:** Context efficiency matters even with large context windows because:

1. **Compute cost scales with tokens** - Every token consumes compute on every inference
2. **Latency increases with context** - Larger prompts take longer to process  
3. **Energy consumption** - Each token has environmental impact
4. **Attention quality** - Models attend better to smaller, focused contexts

**The efficiency math:**
- MCP tool schemas: 10-50k tokens of context overhead
- `bd prime`: ~1-2k tokens of workflow context  
- **Result: 10-50x less context overhead with CLI approach**

## Editor Agnostic Design

**Universal compatibility:** CLI approach works across all agent platforms:
- Claude Code, Cursor, Windsurf, Zed
- Any environment with shell access
- Multi-editor workflows (CLI is universal)

**Why not Claude Skills:**
- Redundant with `bd prime` context injection
- Claude-specific (breaks editor-agnostic philosophy)
- Additional maintenance burden
- More systems = more complexity

## Installation Patterns

### Setup Commands
```bash
# Global Claude Code hooks
bd setup claude

# Project-only installation  
bd setup claude --project

# Stealth mode (no git operations)
bd setup claude --stealth

# Check installation status
bd setup claude --check
```

### Hook Architecture
Installed hooks:
- **SessionStart hook:** Runs `bd prime` when agent starts session
- **Post-compaction hook:** Refreshes context after compaction
- **Pre-commit hook:** Updates `.beads/issues.jsonl` export when `export.auto=true`

## Multi-Platform Support

### MCP Integration (Constrained Environments)
For environments without shell access:
- Single MCP server instance with automatic routing
- Per-project Dolt server routing based on working directory
- Maintains database isolation across projects

### Shared Server Mode
Optional `BEADS_DOLT_SHARED_SERVER=1` configuration:
- All projects use single Dolt server at `~/.beads/shared-server/`
- Database isolation via per-project database names
- Reduces resource overhead for multi-project workflows

## Context Injection Strategy

### Prime Command Design
`bd prime` provides comprehensive workflow context in minimal tokens:
- Current ready work and blocked dependencies
- Persistent project memories
- Workflow command guidance  
- Agent-specific instruction snippets

### Automatic Context Refresh
Hooks ensure context stays current:
- SessionStart: Initial context injection
- Post-merge/checkout: Sync state updates
- Pre-commit: Export refresh for external tools

## Design Philosophy

**Simplicity over features:**
- Workflow fits in simple command set: ready → create → update → close → sync
- Well-documented in ~1-2k tokens
- Complex orchestration handled by external layers

**Compatibility over optimization:**
- Universal CLI works everywhere
- MCP available as fallback
- No editor-specific dependencies

**Efficiency over convenience:**
- Minimal context overhead
- Structured metadata over prose parsing
- Direct database queries over export/import cycles

## Architecture Boundaries

**Integration scope:** Beads handles agent integration at the CLI/context level
**Out of scope:** 
- Editor-specific UX enhancements (handled by optional plugins)
- Complex orchestration workflows (handled by external orchestrators)
- Cross-agent communication (handled by shared Dolt database)

## Sources

- `sources/steveyegge/beads/docs-CLAUDE_INTEGRATION.md-772005ab.md` (lines 8-122)
- `sources/steveyegge/beads/docs-MULTI_REPO_AGENTS.md-82567446.md` (lines 12-43)
- `sources/steveyegge/beads/AGENTS.md.md` (lines 149-242)