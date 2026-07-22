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

## Renaming the chain: `to-prd` → `to-spec`, `to-issues` → `to-tickets`

Matt later renamed both hand-off skills — `/to-prd` to `/to-spec`, `/to-issues`
to `/to-tickets` — "apologies for the churn, but I've been wanting to make this
change for a while." The rename is cosmetic, not a behavior change: `/to-prd`
already produced a spec document, and "tickets and issues are basically
interchangeable" — the new names just say what the artifact already was. With
the rename the full chain reads: `/wayfinder → /to-spec → /to-tickets →
/implement → /code-review`, with `/grill-with-docs` feeding `/to-spec` once a
shared understanding is reached — the same alignment gate
`align-before-building-grilling` describes, now named as one step in a longer,
explicitly-ordered pipeline rather than left as an implicit hand-off.

## A hand-off pointer is dead weight once the sequence becomes structural

A skill's closing "now call skill X" instruction earns its place only as long
as the pipeline order isn't yet established elsewhere; once it is, restating it
burns instruction budget for no new information. `to-tickets` originally closed
by pointing at the next skill explicitly — *"Work the frontier one ticket at a
time with `/implement`, clearing context between tickets"* — naming both which
skill runs next and how (per-ticket, fresh context). A later revision drops
that closing sentence, keeping only the frontier-selection rule ("any ticket
whose blockers are all done"). By then the pipeline was already a fixed,
separately-documented sequence (`/wayfinder → /to-spec → /to-tickets →
/implement → /code-review`, above), so the in-skill pointer to `/implement` had
become pure duplication — the same instruction-economy discipline this repo
applies to root config files (see `claude-md-is-an-instruction-budget`), here
aimed at trimming one individual skill's own closing line.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-triage-SKILL.md-c4a91ff1.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/triage/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-diagnose-SKILL.md-82a24dd7.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/diagnose/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-handoff-SKILL.md-c846b3b5.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/handoff/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2059576485111808071-85921d94.md` — origin: https://x.com/mattpocockuk/status/2059576485111808071
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072623114219835733-97d6fcff.md` — origin: https://x.com/mattpocockuk/status/2072623114219835733
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072625252144730215-a927e57f.md` — origin: https://x.com/mattpocockuk/status/2072625252144730215
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072629917779439875-dff4a19f.md` — origin: https://x.com/mattpocockuk/status/2072629917779439875
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072638587267387803-25530ac9.md` — origin: https://x.com/mattpocockuk/status/2072638587267387803
- `sources/mattpocock/skills-repo/skills-engineering-to-tickets-SKILL.md-d6e52aba.md` — origin: https://github.com/mattpocock/skills/blob/d574778f94cf620fcc8ce741584093bc650a61d3/skills/engineering/to-tickets/SKILL.md (revision 2026-07-22, origin https://github.com/mattpocock/skills/blob/57a5add86bfc5e9058dd94c512c4012b3c014336 — drops the closing "one ticket at a time with `/implement`, clearing context between tickets" pointer, leaving only the frontier-selection rule)
