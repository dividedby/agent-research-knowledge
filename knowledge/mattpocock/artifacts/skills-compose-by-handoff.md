# Skills compose by handoff

The skills are designed to be small and composable rather than one monolithic
"do everything" process. Composition happens two ways: skills *invoke* each
other inline, and skills *hand off* to each other across a session boundary by
naming the next skill to run.

## Inline invocation

A skill drops into another mid-process when it needs that capability:

- `triage` runs a `/grill-with-docs` session (step 4) when an issue needs
  fleshing out before it can be marked ready.
- `improve-codebase-architecture` drops into a grilling loop once the user picks
  a candidate, and reuses `grill-with-docs`'s `CONTEXT-FORMAT.md` and
  `ADR-FORMAT.md` rather than restating them — a bundled resource shared across
  skills by relative path (`../grill-with-docs/CONTEXT-FORMAT.md`).
- `diagnose` ends by handing the architectural finding off to
  `improve-codebase-architecture` *with specifics*, but only after the fix is in
  — when it has the most information.

## Cross-session handoff and suggested-skills pointers

Several skills end by pointing at the *next* skill rather than doing that work
themselves. `handoff` writes a continuation document that includes an explicit
"suggested skills" section telling the next agent what to invoke. `diagnose`
recommends `improve-codebase-architecture`. This keeps each skill scoped to one
job while still threading a multi-skill workflow together.

## Two-tier architecture: now realized as the invocation axis

What Matt earlier framed as *future potential* — dividing skills into top-level
user-run "commands" and atomic model-invocable "skills" the commands compose — is
now the repo's organising principle, renamed **user-invoked vs model-invoked** and
enforced in `CLAUDE.md` and `docs/invocation.md`. The compound workflows he
predicted shipped: `grill-with-docs` now composes the model-invoked `domain-modeling`,
and `improve-codebase-architecture` composes `codebase-design`. Commands became the
orchestrators; the primitives became composable model-invoked skills. The full
shape of that taxonomy — the one-way invocation rule, the router skill, and the
fleet-wide refactor it drove — is its own concept: see
`invocation-axis-user-vs-model`.

## The data spine: the issue tracker

The engineering skills compose around a shared artifact — the issue tracker.
`to-prd` produces a PRD issue; `to-issues` breaks a plan/PRD into slice issues;
`triage` moves issues through states and writes agent briefs onto them. None of
them owns the others' output; they read from and write to the same tracker, so
the workflow is assembled by the *data* they pass rather than by a controlling
orchestrator. This is why "what's the issue tracker?" is the first thing
`setup-matt-pocock-skills` resolves.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-triage-SKILL.md-c4a91ff1.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/triage/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-diagnose-SKILL.md-82a24dd7.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/diagnose/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-handoff-SKILL.md-c846b3b5.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/handoff/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2059576485111808071-85921d94.md` — origin: https://x.com/mattpocockuk/status/2059576485111808071
