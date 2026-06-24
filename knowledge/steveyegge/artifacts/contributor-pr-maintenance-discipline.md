# Contributor-PR Maintenance Discipline

Beads' agent instructions encode an explicit policy for how an AI agent should
maintain an open-source project's pull-request queue. The problem it solves: an
agent told to "implement feature X" will, by default, start coding — and silently
duplicate or clobber a human contributor's open PR on the same topic, discarding
volunteer work and damaging community trust. The fix is to make
contributor-awareness a **read-only gate that runs before any build or merge
work**, not a courtesy the agent might remember.

## The preflight gate

Before implementing related work, opening a PR, or merging/closing one, the agent
runs a read-only preflight that searches the open-PR set for the same topic:

```bash
scripts/pr-preflight.sh --search "<topic keywords>" --repo <org>/beads
scripts/pr-preflight.sh <pr-number> --repo <org>/beads
```

The instructions are explicit that the agent must **not rely on auto-discovery**
of `CONTRIBUTING.md` — the preflight is the *enforced* gate, because "the agent
will read the contributing guide if relevant" is exactly the kind of soft
expectation an agent skips under load. Encoding it as a command to run turns a
norm into a checkable step.

## Contributor work gets priority

When an external PR already exists on the topic, the agent's order of operations
is fixed: review it first, **build on it rather than rewrite it** (checkout the
branch, fix/adapt), preserve the contributor's tests as signal, attribute with
`Co-authored-by:` and a PR reference, and **never auto-close a contributor PR by
merging a rewrite**. A full rewrite is permitted only when fundamentally
necessary, and then only with an explanation on the original PR crediting the
contributor's design and tests.

This inverts the usual agent default (produce the cleanest possible diff from
scratch). The maintainer policy is to *maximize community throughput* — find the
useful value in a contribution, absorb or transform it locally when practical,
and use request-changes only as a last resort. The agent is steered toward
the human's contribution as the substrate, not toward its own from-scratch
solution.

## PR-by-default and signed agent presence

Work lands via a feature branch + `gh pr create` against `main`; direct push to
`main` is reserved for releases and narrow operational fixes ("prefer a PR when
unsure"). External contributor PRs are handled with **fix-merge** — checkout the
branch locally, fix/rebase onto main, merge via PR, then close. Every
agent-written GitHub comment and review is signed (per the same
`Agent-Signature:` convention used on commits), so a fleet of agents maintaining
the queue stays attributable rather than anonymous in the PR thread.

A small hygiene rule rounds it out: GitHub PR/issue/comment/review bodies are
written to a file and passed with `gh ... --body-file`, linted first by
`scripts/gh-body-lint` to catch literal `\n` sequences and non-linking `GH#123`
references — guarding against the characteristic ways an agent mangles Markdown
when shelling out.

## Sources

- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` ("Git Workflow: PR by Default", "External Contributor PRs: Check Before You Build", maintainer PR guidelines, `pr-preflight.sh` gate, fix-merge, `gh-body-lint` body hygiene; 2026-06-21/06-23 revisions) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/AGENT_INSTRUCTIONS.md
