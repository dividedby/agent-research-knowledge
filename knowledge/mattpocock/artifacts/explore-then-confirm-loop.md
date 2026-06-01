# The explore → present → confirm → write loop

The stateful skills share a near-identical control skeleton: **explore** the
repo's current state, **present** what you found plus a proposal, **confirm**
with the user (often editing the draft), then **write**. Side effects are
deferred behind a human checkpoint rather than fired eagerly. Recognising it as
one reused shape — not coincidence — is the point.

- `setup-matt-pocock-skills`: explore (`git remote`, existing
  `CLAUDE.md`/`AGENTS.md`, `docs/agents/`, `.scratch/`) → present findings and
  ask the three decisions one at a time → show a draft to edit → write, editing
  the *existing* config file in place.
- `to-prd` / `to-issues`: explore the codebase → draft modules / vertical slices
  → get user approval on the breakdown → publish to the issue tracker.
- `improve-codebase-architecture`: explore for friction → present candidates
  (as an HTML report written to the OS temp dir, never the repo) → grill on the
  chosen one → side effects inline.

## Conventions the loop enforces

- **Lazy, idempotent writes.** Create files only when there's something to write
  (`CONTEXT.md`/`docs/adr/` spring into existence at the first term/decision).
  Update an existing block in place rather than appending a duplicate; never
  overwrite a competing file (`CLAUDE.md` vs `AGENTS.md`) or the user's
  surrounding edits.
- **Keep generated noise out of the repo.** `improve-codebase-architecture`
  writes its report to `$TMPDIR`; `handoff` saves to the OS temp dir; `prototype`
  is throwaway and clearly marked. Durable output goes to the right home (issue
  tracker, ADR, `CONTEXT.md`); scratch output stays out of version control.
- **Defer the irreversible.** Publishing issues, closing tickets, editing config
  all sit behind an explicit confirmation; the agent proposes, the human commits.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-SKILL.md-5dba7935.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/setup-matt-pocock-skills/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-to-prd-SKILL.md-c9420806.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/to-prd/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-handoff-SKILL.md-c846b3b5.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/handoff/SKILL.md
