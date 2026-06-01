# Controlling when a skill fires

Two frontmatter mechanisms decide whether the agent may auto-load a skill or
whether the human must invoke it deliberately. The choice encodes how much the
skill should be allowed to fire on its own judgement.

## `disable-model-invocation: true`

`setup-matt-pocock-skills` and `zoom-out` set this. It means the model may not
trigger the skill from a description match — the user must run it explicitly.
The two cases show the two reasons:

- **Destructive/once-per-repo setup** (`setup-matt-pocock-skills`) — it edits
  `CLAUDE.md`/`AGENTS.md` and writes config; you don't want the model deciding
  to re-scaffold mid-task. It's a deliberate, human-initiated act.
- **A pure imperative nudge** (`zoom-out`) — the skill body is two sentences
  ("Go up a layer of abstraction. Give me a map…"). It only makes sense when the
  *human* feels lost; the model auto-firing it would be noise.

## The description *is* the auto-trigger

For everything else, autoload is governed entirely by the `description`'s "Use
when…" clause. The triggers are written as the literal phrases a user is likely
to say: `caveman` lists "caveman mode", "less tokens", "be brief"; `diagnose`
lists "diagnose this", "debug this", "something is broken/throwing/failing".
This makes skill selection a string-matching problem the agent can do reliably,
which is why `write-a-skill` treats the trigger list as the single most
important part of a skill to get right.

## Argument hints

A skill that expects an argument declares `argument-hint` (e.g. `handoff`:
"What will the next session be used for?"), and the body branches on whether an
argument was passed — tailoring output when given, falling back to a default
when not.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-SKILL.md-5dba7935.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/setup-matt-pocock-skills/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-zoom-out-SKILL.md-4adec2ab.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/zoom-out/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-caveman-SKILL.md-3d901941.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/caveman/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-handoff-SKILL.md-c846b3b5.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/handoff/SKILL.md
