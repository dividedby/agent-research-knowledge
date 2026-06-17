# Controlling when a skill fires

Two frontmatter mechanisms decide whether the agent may auto-load a skill or
whether the human must invoke it deliberately. The choice encodes how much the
skill should be allowed to fire on its own judgement.

## `disable-model-invocation: true`

`setup-matt-pocock-skills` set this early, for a reason that still holds: it's a
**destructive/once-per-repo setup** that edits `CLAUDE.md`/`AGENTS.md` and writes
config, so you don't want the model deciding to re-scaffold mid-task — it's a
deliberate, human-initiated act. (`zoom-out`, an earlier example of a pure
imperative nudge that only made sense when the *human* felt lost, was later
removed from the repo as unused.)

This flag has since been promoted from a per-skill exception to the repo's
primary organising axis: **every** orchestrator a human types deliberately
(`grill-me`, `grill-with-docs`, `to-prd`, `to-issues`, `triage`, `prototype`,
`handoff`, `teach`, `improve-codebase-architecture`, `ask-matt`) now sets it,
while the reusable-discipline skills (`grilling`, `domain-modeling`,
`codebase-design`, `diagnosing-bugs`, `tdd`) stay model-invoked. The mechanism is
the same; what changed is that the presence-or-absence of `disable-model-invocation`
*is* the taxonomy — see `invocation-axis-user-vs-model` for the full shape and the
one-way invocation rule it enforces.

## The description *is* the auto-trigger

For everything else, autoload is governed entirely by the `description`'s "Use
when…" clause. The triggers are written as the literal phrases a user is likely
to say: `diagnosing-bugs` lists "diagnose this", "debug this", "something is
broken/throwing/failing/slow". This makes skill selection a string-matching
problem the agent can do reliably, which is why `writing-great-skills` (the
successor to `write-a-skill`) treats trigger phrasing as a top predictability
lever — one trigger per genuinely-distinct branch, synonyms collapsed.

## Argument hints

A skill that expects an argument declares `argument-hint` (e.g. `handoff`:
"What will the next session be used for?"), and the body branches on whether an
argument was passed — tailoring output when given, falling back to a default
when not.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-SKILL.md-5dba7935.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/setup-matt-pocock-skills/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-zoom-out-SKILL.md-4adec2ab.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/zoom-out/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-caveman-SKILL.md-3d901941.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/caveman/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-handoff-SKILL.md-c846b3b5.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/handoff/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/docs-invocation.md-1ce78905.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/docs/invocation.md
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
