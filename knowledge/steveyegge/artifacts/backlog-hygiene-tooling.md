# Backlog-Hygiene Tooling

A tracker that an agent fleet writes into faster than humans read will rot:
malformed issues, near-duplicate reports, and in-progress work nobody finished.
Beads treats backlog *quality* as a first-class, command-backed concern — not a
human chore — so the corpus of work an agent generates stays legible enough to
keep sequencing from.

## The hygiene commands

| Command | What it polices |
|---------|-----------------|
| `bd lint` | Issues missing the recommended sections for their type — bugs need *Steps to Reproduce* + *Acceptance Criteria*, tasks/features need *Acceptance Criteria*, epics need *Success Criteria*. Defaults to all open issues. |
| `bd find-duplicates` | *Semantically* similar issues (not exact matches — that's `bd duplicates`). Two methods: `mechanical` (Jaccard token similarity, fast, no API key) and `ai` (mechanical pre-filter, then Claude judges the surviving pairs). |
| `bd stale` | In-progress issues with no recent activity (default 30d) — abandoned, forgotten, or no-longer-relevant work. |
| `bd status` | A `git status`-style one-shot snapshot: counts by state, ready work, lead time, last-24h activity. Built for project health checks, onboarding, and shell-prompt/CI integration. |

## Why it's built this way

- **Schema-by-type, enforced not assumed.** `bd lint` encodes that an issue type
  *implies* a contract (a bug without repro steps is incomplete). Acceptance
  criteria are precisely what an agent needs to know when a task is *done* — so
  the lint rules double as the agent's done-definition discipline.
- **Two-tier duplicate detection mirrors the cost gradient.** The free mechanical
  pass runs always; the LLM pass is gated behind a pre-filter so the expensive
  semantic judgement only fires on candidate pairs. A fleet that files issues
  cheaply needs dedup that scales without an API call per pair.
- **Staleness is operational, not editorial.** `bd stale` keys on *activity*, not
  age — it surfaces work that started and stalled, the failure mode of
  long-running agent sessions, distinct from old-but-deliberately-open issues.

Together these are the maintenance counterpart to dependency-aware sequencing:
sequencing decides *what runs next*, hygiene tooling keeps the issue corpus those
decisions read from from degrading as the fleet writes into it.

## Sources

- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md (`bd lint`, `bd find-duplicates`, `bd stale`, `bd status` sections)
