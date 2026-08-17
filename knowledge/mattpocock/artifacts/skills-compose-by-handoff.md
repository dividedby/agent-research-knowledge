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

## Inline invocation moved from prose slash-commands to an explicit tool call

Across an August 2026 revision wave, nearly every skill that delegates to
another rewrote its delegation from telling the model to "run `/grilling`" or
"run the `/domain-modeling` skill" into an explicit instruction to **call the
Skill tool** with that skill's name — `grill-with-docs` becomes "Call the
Skill tool twice, for 'grilling' and 'domain-modeling'"; `grill-me` becomes
"Call the Skill tool with 'grilling'"; `handoff`/`claude-handoff` name "which
skills the next agent should call the Skill tool for" instead of "which
skills the agent should invoke"; `wayfinder`, `triage`,
`improve-codebase-architecture`, and `tdd` all follow the same substitution
wherever they'd previously written a bare `/command` reference. The wording
change is uniform and mechanical enough to read as a fleet-wide convention
shift, not an independent choice made once per skill.

The motivation lines up with a known failure elsewhere in this collection:
`grill-with-docs`'s one-line delegation to `grilling` and `domain-modeling`
is the single most commonly reported source of trouble, precisely because
*naming* a skill in prose doesn't reliably cause a model to load it (see
`align-before-building-grilling`'s "A skill naming another skill doesn't
reliably load it"). Rewriting the delegation as a literal tool call swaps an
instruction the model has to correctly interpret as "go run that command" for
one that maps directly onto a concrete tool invocation — the same shift from
convention to mechanism this repo repeats elsewhere (deterministic hooks over
prose rules, linted architecture boundaries over a documented convention).
Whether it actually closes the partial-loading gap isn't confirmed in these
captures; what's confirmed is that the fleet standardised on the more
literal instruction as its default composition idiom.

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
- `sources/mattpocock/skills-repo/skills-engineering-grill-with-docs-SKILL.md-1015ebf3.md` — origin: https://github.com/mattpocock/skills/blob/9aad5d190aa87d659f82e68fdb0ee13636541c48/skills/engineering/grill-with-docs/SKILL.md (revision 2026-08-16 — "Call the Skill tool twice, for 'grilling' and 'domain-modeling'")
- `sources/mattpocock/skills-repo/skills-productivity-grill-me-SKILL.md-5d73b98f.md` — origin: https://github.com/mattpocock/skills/blob/ffae54adff84ac14e24bc2418f479b664d02773f/skills/productivity/grill-me/SKILL.md (revision 2026-08-16 — "Call the Skill tool with 'grilling'")
- `sources/mattpocock/skills-repo/skills-productivity-handoff-SKILL.md-c846b3b5.md` — origin: https://github.com/mattpocock/skills/blob/404b84f562bf8f8a934314668f088c07651cebef/skills/productivity/handoff/SKILL.md (revision 2026-08-16 — "suggested skills" section now names which skills to call the Skill tool for)
- `sources/mattpocock/skills-repo/skills-in-progress-claude-handoff-SKILL.md-f0e12f6d.md` — origin: https://github.com/mattpocock/skills/blob/2a2324225de032f7efdc37700f20293b61f88e4d/skills/in-progress/claude-handoff/SKILL.md (revision 2026-08-16 — same wording change)
- `sources/mattpocock/skills-repo/skills-engineering-wayfinder-SKILL.md-fda0505b.md` — origin: https://github.com/mattpocock/skills/blob/dbda61e60513a04387605089043bd03bf3889930/skills/engineering/wayfinder/SKILL.md (revision 2026-08-16 — every ticket-type resolution step rewritten to "call the Skill tool")
- `sources/mattpocock/skills-repo/skills-engineering-triage-SKILL.md-c4a91ff1.md` — origin: https://github.com/mattpocock/skills/blob/733481eb2e94d874b9b31fb1fd32534b7c0ddebc/skills/engineering/triage/SKILL.md (revision 2026-08-16 — grilling step rewritten to "call the Skill tool twice")
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/6fc6607afb7ca35af99524957a85a33e41cfc2bc/skills/engineering/improve-codebase-architecture/SKILL.md (revision 2026-08-16 — same wording change across all three grilling-loop side effects)
- `sources/mattpocock/skills-repo/skills-engineering-tdd-SKILL.md-29d824ee.md` — origin: https://github.com/mattpocock/skills/blob/ea9d9ddb2675429026a318b898b0d8b4ed383674/skills/engineering/tdd/SKILL.md (revision 2026-08-16 — "call the Skill tool with 'codebase-design'")
