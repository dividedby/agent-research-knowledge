# Rules-Corpus Hygiene

The same fleet that bloats an issue tracker also bloats its own standing
instructions. An agent's rules directory (`.claude/rules/`) accumulates rules
written at different times by different sessions, and that corpus rots the same
way a backlog does: rules that contradict each other, and near-duplicate rules
saying the same thing in three places. A contradictory or redundant rule set
degrades the agent reading it. Beads extends its hygiene philosophy from the
*issue* corpus to the *instruction* corpus with `bd rules`.

## What it does

- **`bd rules audit`** scans `.claude/rules/` for contradictions and merge
  opportunities — pairs of rules similar enough to consolidate, keyed on a
  Jaccard token-similarity threshold (default 0.6).
- **`bd rules compact`** merges related rules into composites — `--dry-run` to
  preview, `--auto` to apply the audit's suggestions, `--group` to merge a named
  set by hand.

## Why it's built this way

- **The same engine, a different corpus.** This reuses the Jaccard-similarity
  mechanism that powers `bd find-duplicates` on issues, pointed at the rules
  directory instead. The insight is that *any* agent-written, append-mostly text
  corpus suffers the same near-duplicate rot, so the dedup tool generalizes.
- **Rules are a steering surface, not documentation.** Contradictory rules are
  worse than redundant ones: the agent can't tell which instruction wins, so the
  audit flags contradictions first. Compaction keeps the rule set small enough
  that the agent actually attends to all of it — the same context-economy
  argument that keeps `bd prime` lean, applied to the standing instructions.

This is the maintenance counterpart to backlog hygiene aimed one layer up: where
`bd lint`/`bd find-duplicates`/`bd stale` keep the *work corpus* legible, `bd
rules` keeps the *instruction corpus* the agent reads from non-contradictory.

## Sources

- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (`bd rules audit`, `bd rules compact` — Jaccard-threshold contradiction/merge detection over `.claude/rules/`) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
