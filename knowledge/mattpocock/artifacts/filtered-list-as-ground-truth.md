# An empty filtered list means "done", not "go re-query unfiltered"

Sandcastle's loop templates (`simple-loop`, `sequential-reviewer`) feed the agent a
**pre-expanded, already-filtered** task list — e.g. open issues carrying the
configured label, expanded into the prompt via a `` !`gh issue list … --label …` ``
block. A failure mode emerges when that list comes back empty: a capable agent,
seeing `[]`, infers the snapshot must be stale and runs its *own* unfiltered
`gh issue list`, picking up work outside the configured filter and breaking the
operator's intended scope.

## The prompt hardening: make the filtered list the sole ground truth

The fix is entirely in prompt wording, not code. Two complementary instructions:

- A **"do not re-query"** hint that frames the pre-expanded list as the *single
  source of truth* — not a possibly-stale cache the agent should refresh, but the
  authoritative set of work for this iteration.
- A **completion criterion** that explicitly equates an empty list with done:
  `# Done` when the list is `[]`. This removes the agent's incentive to go looking
  for more — emptiness is the success signal, not a problem to route around.

## Why this is a general pattern, not a one-off

The agent is doing something locally reasonable — distrusting a stale-looking
snapshot — that is globally wrong, because it can't see that the emptiness is the
*result of a deliberate filter*. Whenever a harness hands an agent a curated subset
and also gives it the tools to fetch the full set, the prompt must state which one
is authoritative and what an empty curated set *means*. Pre-expanding context into
the prompt (so the agent reads a snapshot rather than querying live) only contains
the agent if the prompt also forbids the agent from going around it. This is
prompt-side scope enforcement for the dogfooded loop, complementing the structural
filters baked into the scaffolded commands.

## Sources

- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: github.com/mattpocock/sandcastle (CHANGELOG.md)
