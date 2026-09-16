# Collaborative planning editor (Chopin)

Chopin is GitHub Next's concrete answer to "what would a thick boundary object
actually look like" (see practices/boundary-objects-must-serve-human-legibility):
a multiplayer, real-time planning prototype where humans and agents co-edit a
plan as a rich MDX document — Markdown that embeds interactive visual
components — instead of exchanging walls of static text. It's a distinct GitHub
Next research project from Ace (the broader multiplayer coding workspace, see
collaborative-multiplayer-agent-workspace): Ace is the general session/workspace
layer; Chopin is specifically the planning-document experience, built to test
whether the plan itself can become the shared, manipulable alignment surface
rather than a private wall of Markdown one person approves alone.

Build decisions worth lifting:

- **The plan document is the interactive surface, not a chat log.** Coworkers
  and agents write the plan together in an MDX editor, so a plan can carry
  live, interactive visuals (the shadow-manipulation, state-machine, or
  multi-option-comparison interfaces described in
  practices/boundary-objects-must-serve-human-legibility) directly inline, not
  as attachments or separate demos.
- **Decisions are recorded with provenance.** Answering an embedded decision in
  the plan logs who decided what, and when — turning the plan into an audit
  trail of judgment calls, not just a final spec.
- **Multiplayer by default.** Everyone's cursors are visible and the document is
  collaboratively editable in real time, so a plan can be debated and decided as
  a group instead of being produced by one person in isolation and handed to
  others as a yes/no approval.
- **Deliberately rough.** It's an early proof-of-concept and exploration space,
  not a shipped product — consistent with GitHub Next's stated research
  philosophy of treating agent labor as if it were already free in order to
  explore the design space it will eventually unlock.

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-planning-agents-1b47b34a.md` — origin: https://maggieappleton.com/planning-agents/
