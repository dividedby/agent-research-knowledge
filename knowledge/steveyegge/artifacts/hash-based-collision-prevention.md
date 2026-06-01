# Hash-Based Collision Prevention

Beads uses content-based hashing for distributed ID generation to prevent merge collisions in multi-agent workflows.

## The Core Problem

Sequential IDs (bd-1, bd-2, bd-3) cause collisions when multiple agents create issues concurrently across branches:

```
Branch A: bd create "Add OAuth"   → bd-10
Branch B: bd create "Add Stripe"  → bd-10 (collision!)
```

## The Solution

Hash-based IDs derived from random UUIDs ensure uniqueness without central coordination:

```
Branch A: bd create "Add OAuth"   → bd-a1b2  
Branch B: bd create "Add Stripe"  → bd-f14c (no collision)
```

## Implementation Details

1. **Issue creation:** Generate random UUID, derive short hash as ID
2. **Progressive scaling:** IDs start at 4 chars, grow to 5-6 chars as database grows
3. **Content hashing:** Each issue has a content hash for change detection
4. **Merge logic:** Same ID + different content = update, same ID + same content = skip

## Merge Resolution

The system handles distributed convergence through deterministic merge rules:

```
For each issue in incoming data:
  1. Compute content hash
  2. Look up existing issue by ID
  3. Compare hashes:
     - Same hash → skip (already present)
     - Different hash → update (newer version) 
     - No match → create (new issue)
```

This eliminates the need for central coordination while ensuring all machines converge to the same state.

**Sources:**
- `sources/steveyegge/beads/docs-ARCHITECTURE.md-fd45feca.md` (lines 96-142)
- `sources/steveyegge/beads/README.md.md` (lines 61, "Zero Conflict" feature)