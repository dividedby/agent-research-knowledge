# Two sub-types of skill: procedures and abilities

In a terminology debate over whether agent-invoked markdown files are "skills" or
user-invoked "prompts," Matt offers a cleaner cut than the invocation axis. He
splits skills into two sub-types by *what they encode*:

- A **procedure** is a fixed sequence the agent walks through — `/grill-me` is his
  example. It has a defined shape (the interview, one question at a time) and runs
  largely the same way every time.
- An **ability** is a competence the agent applies with judgement — `/tdd` is his
  example. It is not a script to step through but a capacity the agent exercises
  contextually.

The distinction matters for authoring because the two demand different shapes. A
procedure can be written as ordered steps with checkpoints (the `explore → present
→ confirm → write` skeleton, the grilling state machine). An ability is closer to
a principle plus the discipline to apply it — encoding *when* and *how* to bring a
competence to bear, not a fixed path. Naming the split is itself the design value:
it tells the author whether they are writing a recipe or installing a habit, which
changes everything about how the skill body is structured.

This *what-it-encodes* split is largely orthogonal to the *who-can-invoke-it*
split the repo later adopted (`invocation-axis-user-vs-model`), but the two
correlate in practice: the extracted reusable abilities (`grilling`, `tdd`,
`codebase-design`, `domain-modeling`) are the model-invoked primitives, while the
fixed-sequence orchestrators a human drives (`to-prd`, `to-issues`, the thin
grilling wrappers) are user-invoked. Both cuts answer authoring questions — one
asks *recipe or habit*, the other asks *who reaches it* — and a skill is placed by
both.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065687128797749294-79ffa2e8.md` — origin: https://x.com/mattpocockuk/status/2065687128797749294
- `sources/mattpocock/skills-repo/skills-productivity-grilling-SKILL.md-84a3ca23.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/productivity/grilling/SKILL.md
- `sources/mattpocock/skills-repo/docs-invocation.md-1ce78905.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/docs/invocation.md
