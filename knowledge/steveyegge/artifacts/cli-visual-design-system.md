# CLI Visual Design System

Beads implements a disciplined visual design system for CLI output that prioritizes cognitive efficiency and consistency over decoration.

## Core Design Principle: Minimize Cognitive Overload

**Every new command, flag, or option adds cognitive burden.** The design system actively works to reduce visual noise and decision fatigue.

### Anti-Pattern: Emoji-Style Icons

**NEVER use large emoji-style icons** (🔴🟠🟡🔵⚪) in CLI output:
- Cause cognitive overload
- Break visual consistency  
- Add unnecessary visual weight
- Distract from actual information

### Preferred: Small Unicode Symbols

**ALWAYS use small Unicode symbols** with semantic colors applied via lipgloss:

**Status Icons:**
```text
○ open        - Available to work (white/default)
◐ in_progress - Currently being worked (yellow)
● blocked     - Waiting on dependencies (red)
✓ closed      - Completed (muted gray)
❄ deferred    - Scheduled for later (blue/muted)
```

**Priority Icons:**
Format as `● P0` (filled circle icon plus label, colored by priority):
- `● P0`: Red + bold (critical)
- `● P1`: Orange (high)
- `● P2-P4`: Default text (normal)

**Revision: dropping the priority glyph to fix symbol overload.** The `●`
filled circle originally did double duty — it's also the *status* icon for
`blocked` (see Status Icons above). Reusing one glyph for two unrelated
semantic axes (lifecycle status vs. priority level) meant a bare `●` in
output was ambiguous without reading the surrounding label. The fix wasn't a
new glyph, it was removing the glyph from priority entirely: priority now
renders as a **text label only, colored by level, with no icon** (`P0`
red+bold, `P1` orange, `P2` amber, `P3`–`P4` default) — freeing `●` to mean
"blocked" unambiguously everywhere it appears. The general lesson: when a
CLI's visual vocabulary reuses a symbol across two independent semantic
categories, resolve the collision by dropping the icon from the
*lower-signal* axis rather than inventing a second, similar-looking symbol.

## Semantic Color Strategy

**Color only actionable items** - Don't color everything:

**Issue Type Colors:**
- `bug`: Red (problems need attention)
- `epic`: Purple (larger scope)  
- Others: Default text

**Status Colors:**
- Critical status (blocked, P0): Red for immediate attention
- Active work (in_progress): Yellow for ongoing activity
- Completed work: Muted gray to fade into background

**Principle:** Use color to guide attention to what needs action, not for decoration.

## Visual Hierarchy Principles

### 1. Small Unicode Symbols Only
Avoid emoji blobs. Use precise, minimal symbols that scan quickly.

### 2. Semantic Colors Only  
Color should indicate actionability or urgency, not just categorization.

### 3. Closed Items Fade
Use muted gray for completed work so it doesn't compete for attention.

### 4. Icons Over Text Labels
Prefer `●` over "PRIORITY" for scanability and space efficiency.

### 5. Consistent Cross-Command
Use same icons/colors across list, graph, show, and related commands.

### 6. Tree Connectors for Hierarchy
Use proper tree characters (`├──`, `└──`, `│`) for hierarchical display.

### 7. Reduce Cognitive Noise
Don't show redundant information like `needs:1` when it's just the parent epic.

## CLI Architecture Principles

### Command Consolidation Strategy

**Before adding new commands:**

1. **Recovery/fix operations → `bd doctor --fix`**  
   Don't create separate commands like `bd recover` or `bd repair`. Doctor detects problems; `--fix` handles remediation.

2. **Prefer flags on existing commands**  
   Ask: "Can this be a flag on an existing command?" Example: `bd list --stale` instead of `bd stale`.

3. **Consolidate related operations**  
   Related operations live together. Version control uses `bd vc {log,diff,commit}`, not separate top-level commands.

4. **Count the commands**  
   If approaching 30+ commands, there's a discoverability problem. Consider subcommand grouping.

5. **Strong justification for new commands**  
   New commands should represent fundamentally different operations, not convenience wrappers.

### Command Design Standards

**Every command that agents use must have `--json` flag** for programmatic consumption.

**Non-interactive by default:**
- Never hang waiting for user input
- Use explicit flags for confirmation (`--force`, `--yes`)
- Fail fast with clear error messages

**Consistent flag patterns:**
- `--json` for machine-readable output
- `--quiet` for minimal output  
- `--force` to skip confirmations
- `--dry-run` to preview operations

## Implementation Architecture

### Style System Organization

Use exported styles from `internal/ui/styles.go`:

```go
// Status styles
ui.StatusInProgressStyle  // Yellow - active work
ui.StatusBlockedStyle     // Red - needs attention  
ui.StatusClosedStyle      // Muted gray - done

// Priority styles
ui.PriorityP0Style        // Red + bold
ui.PriorityP1Style        // Orange

// Type styles  
ui.TypeBugStyle           // Red
ui.TypeEpicStyle          // Purple

// General styles
ui.PassStyle, ui.WarnStyle, ui.FailStyle
ui.MutedStyle, ui.AccentStyle
ui.RenderMuted(text), ui.RenderAccent(text)
```

### Example Implementation

```go
switch issue.Status {
case types.StatusOpen:
    icon = "○"
case types.StatusInProgress:
    icon = ui.StatusInProgressStyle.Render("◐")
case types.StatusBlocked:
    icon = ui.StatusBlockedStyle.Render("●")
case types.StatusClosed:
    icon = ui.StatusClosedStyle.Render("✓")
}
```

## Accessibility Considerations

**Color is supplementary:** Don't rely solely on color to convey information. Icons and text should work in monochrome.

**High contrast:** Ensure sufficient contrast for accessibility.

**Consistent symbols:** Use the same Unicode symbols consistently so users can learn the visual language.

## Design Review Criteria

**Before adding visual elements:**

1. **Does this reduce cognitive load?** If it adds visual noise, reconsider.
2. **Is the color semantic?** Color should indicate actionability or urgency.
3. **Is it consistent?** Use existing symbols and colors when possible.
4. **Does it scan quickly?** Users should be able to parse output at a glance.
5. **Is it accessible?** Works without color, sufficient contrast.

**Red flags:**
- Large emoji icons
- Decorative colors that don't indicate action
- Inconsistent symbols across commands
- Visual elements that don't reduce cognitive burden

## Sources

- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` (lines 313-417)
- `sources/steveyegge/beads/AGENTS.md.md` (lines 53-60)
- `sources/steveyegge/beads/AGENTS.md.md` (Priority Labels and Colors — dropping the `●` glyph from priority, P-label-only with color, new P2 amber tier, 2026-08-11 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/AGENTS.md
- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` (same Priority Labels and Colors revision, 2026-08-11 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/AGENT_INSTRUCTIONS.md