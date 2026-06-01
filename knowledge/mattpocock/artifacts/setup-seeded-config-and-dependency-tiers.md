# Setup-seeded config and hard/soft dependency tiers

The engineering skills are not standalone; several read per-repo configuration
that a dedicated setup skill, `/setup-matt-pocock-skills`, scaffolds once. That
config is three things: the **issue tracker** (GitHub, GitLab, local markdown,
or freeform "other"), the **triage label vocabulary** (the real label strings
behind five canonical roles), and the **domain doc layout** (single `CONTEXT.md`
+ `docs/adr/`, or a multi-context `CONTEXT-MAP.md`). Setup writes these into an
`## Agent skills` block in the repo's `CLAUDE.md`/`AGENTS.md` plus
`docs/agents/*.md`, seeded from bundled templates.

This is how a generic skill becomes repo-aware without hard-coding: the skill
reads the config the user's repo already declares, rather than guessing or
prompting every run.

## The dependency split (ADR 0001)

The skills depend on this config at two different strengths, and the repo
encodes the difference explicitly rather than treating all consumers alike:

- **Hard dependency** (`to-issues`, `to-prd`, `triage`) — cannot function
  correctly without the config. They publish to a *specific* tracker and apply
  *specific* label strings; without the mapping the output is wrong, not just
  fuzzy. These carry an explicit one-liner: *"…should have been provided to you
  — run `/setup-matt-pocock-skills` if not."*
- **Soft dependency** (`diagnose`, `tdd`, `improve-codebase-architecture`,
  `zoom-out`) — only *sharpen* their output with the config (use the glossary
  for naming, respect ADRs in the area). They degrade gracefully: missing docs
  means less sharp output, not wrong output. These reference "the project's
  domain glossary" and "ADRs in the area you're touching" in vague prose only.

The reasoning is token economy and honesty: the loud setup pointer is reserved
for places where it is genuinely load-bearing, so it isn't cargo-culted into
skills that work fine without it.

## Setup is prompt-driven, not scripted

The setup skill is itself an example of the explore → present → confirm → write
loop (see `explore-then-confirm-loop`): it inspects `git remote`, existing
agent-config files, and `.scratch/`, proposes a default posture from what it
finds (GitHub remote → propose GitHub), walks the user through the three
decisions one at a time, and edits the *existing* `CLAUDE.md`/`AGENTS.md` in
place rather than creating a competing file.

## Sources

- `sources/mattpocock/skills-repo/docs-adr-0001-explicit-setup-pointer-only-for-hard-dependenc-071cb663.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/docs/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-SKILL.md-5dba7935.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/setup-matt-pocock-skills/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-to-issues-SKILL.md-04f1cc54.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/to-issues/SKILL.md
