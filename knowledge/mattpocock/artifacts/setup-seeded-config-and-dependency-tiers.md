# Setup-seeded config and hard/soft dependency tiers

The engineering skills are not standalone; several read per-repo configuration
that a dedicated setup skill, `/setup-matt-pocock-skills`, scaffolds once. That
config is three things: the **issue tracker** (GitHub via `gh`, GitLab via `glab`,
local markdown, or freeform "other"), the **triage label vocabulary** (the real
label strings behind five canonical roles), and the **domain doc layout** (single
`CONTEXT.md` + `docs/adr/`, or a multi-context `CONTEXT-MAP.md`). Setup writes these
into an `## Agent skills` block in the repo's `CLAUDE.md`/`AGENTS.md` plus
`docs/agents/*.md`, seeded from bundled templates. Each tracker backend ships its
own template (`issue-tracker-github.md`, `issue-tracker-gitlab.md`,
`issue-tracker-local.md`) recording the CLI shape the skills shell out to — the
GitLab one is a near-isomorphic remap of the GitHub one (`glab mr` for `gh pr`,
GitLab's "notes" for comments, separate issue/MR number spaces vs GitHub's shared
one).

For GitHub and GitLab only, setup also records one extra flag: **whether external
PRs/MRs are a request surface** (default no). When on, the config tells `triage`
to pull contributors' external PRs into the same queue as issues and how to tell
them apart from maintainers' in-flight work (`gh`'s `authorAssociation`, or
filtering GitLab MR authors against project members). Local-markdown and "other"
trackers skip the question — they have no PRs.

This is how a generic skill becomes repo-aware without hard-coding: the skill
reads the config the user's repo already declares, rather than guessing or
prompting every run.

## The dependency split (ADR 0001)

The skills depend on this config at two different strengths, and the repo
encodes the difference explicitly rather than treating all consumers alike:

- **Hard dependency** (`to-issues`, `to-prd`, `triage`, and now `code-review`)
  — cannot function correctly without the config. They publish to (or, for
  `code-review`'s Spec axis, read from) a *specific* tracker and apply
  *specific* label strings; without the mapping the output is wrong, not just
  fuzzy. These carry an explicit one-liner: *"…should have been provided to you
  — run `/setup-matt-pocock-skills` if not."* `code-review` joining this tier
  when it graduated out of `in-progress` shows the tier is drawn by what a
  skill *does* with the config, not by which bucket it ships in.
- **Soft dependency** (`diagnose`, `tdd`, `improve-codebase-architecture`,
  `zoom-out`) — only *sharpen* their output with the config (use the glossary
  for naming, respect ADRs in the area). They degrade gracefully: missing docs
  means less sharp output, not wrong output. These reference "the project's
  domain glossary" and "ADRs in the area you're touching" in vague prose only.

The reasoning is token economy and honesty: the loud setup pointer is reserved
for places where it is genuinely load-bearing, so it isn't cargo-culted into
skills that work fine without it.

## Running setup mid-project needs no special procedure

Asked how to bring the skills into a project that's already mid-development,
with no setup run yet, Matt's answer is that there's no separate on-ramp to
learn: "Just run `/setup-matt-pocock-skills` and you're good." The setup
skill's explore-first design (below) is what makes this safe to run at any
point rather than only at project start — it reads whatever the repo already
has and proposes from that, so arriving late costs nothing extra.

## Setup is prompt-driven, not scripted

The setup skill is itself an example of the explore → present → confirm → write
loop (see `explore-then-confirm-loop`): it inspects `git remote`, existing
agent-config files, and `.scratch/`, proposes a default posture from what it
finds (GitHub remote → propose GitHub), walks the user through the three
decisions one at a time, and edits the *existing* `CLAUDE.md`/`AGENTS.md` in
place rather than creating a competing file.

## Explore harder so the interview asks less

A later revision pushes the explore step to do more inferring, so the confirm
step asks less: it now also checks whether the `triage` skill is installed and
scans for monorepo signals (`pnpm-workspace.yaml`, a `workspaces` field, a
populated `packages/*`) *before* presenting anything. Two sections become
conditional on what exploration already settled — the triage-label question is
skipped outright when `triage` isn't installed (an uninstalled skill needs no
labels), and the multi-context domain-doc option is only offered when monorepo
signals are actually present, defaulting straight to single-context otherwise.
Every remaining section leads with a recommended answer the user can accept in
a word, rather than an open question. The principle: every fact exploration can
already establish is a question the interview shouldn't ask twice — a config
wizard's job is to shrink to exactly the decisions still open, not to walk a
fixed script regardless of what it already knows.

## The local-markdown tracker adopts the tracker-native shape

The local-markdown template for `to-tickets`' output changed from a single
`tickets.md` file to one file per ticket under `.scratch/<feature>/issues/`,
numbered from `01` and worked blockers-first — mirroring the per-issue,
native-blocking shape a real tracker already has (see the `wayfinder` local
template, which uses the same one-file-per-ticket layout for its map's child
tickets). Bringing the local fallback's file shape closer to the tracker-native
one keeps the two mediums structurally parallel, so a skill's logic for
"the next unblocked ticket" reads the same way regardless of backend.

## An indirection is only as safe as every consumer resolving it the same way

A later fix (#472) is a reminder of why the hard-dependency pointer above
matters: `wayfinder` had pinned the literal path `docs/agents/issue-tracker.md`
instead of resolving it through the `### Issue tracker` block this skill
writes into `CLAUDE.md`/`AGENTS.md` — so in a repo that keeps its agent docs
elsewhere, it silently fell back to the local-markdown tracker even when
`CLAUDE.md` clearly declared GitHub Issues. One skill hard-coding the path
breaks the indirection for everyone, silently and without an error — the fix
was making `wayfinder` resolve the doc via the same pointer every other
consumer already used, restoring one true resolution path across the suite.

## "Config is death": the setup skill's scope is deliberately narrow

Users repeatedly ask `setup-matt-pocock-skills` to become the home for more
than its three decisions — grilling cadence, question format, tone, per-user
preferences — and the standing answer is a flat refusal: "Config is death."
Anything beyond tracker, labels, and doc layout belongs in the repo's own
`CLAUDE.md` as plain instructions, which every skill already reads; growing the
setup skill's surface into a general preferences store is the thing being
refused, not an oversight to fix. The same narrowness shows up as an open
complaint the setup skill doesn't resolve on its own: `docs/agents/triage-labels.md`
only records the *mapping* between canonical role names and a tracker's real
label strings — it never runs `gh label create`, so a fresh GitHub repo still
needs the five state and two category labels created by hand once, or `triage`
fails outright trying to apply one that doesn't exist. A second, unrelated gap
sits in the file-selection rule: setup edits `CLAUDE.md` if it exists, else
`AGENTS.md` — checking which file *exists*, not which harness is actually
running — so a `CLAUDE.md` left over from an earlier Claude Code session can
collect the `## Agent skills` block somewhere a Codex session run afterward
never reads. Both gaps are worked around by hand today: create the tracker
labels once with `gh label create`, and either move the block to `AGENTS.md`
or make `CLAUDE.md` a one-line pointer at it.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-setup-matt-pocock-skills-7dbff8a3.md` — origin: https://www.aihero.dev/skills-setup-matt-pocock-skills
- `sources/mattpocock/skills-repo/docs-adr-0001-explicit-setup-pointer-only-for-hard-dependenc-071cb663.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/docs/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-SKILL.md-5dba7935.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/setup-matt-pocock-skills/SKILL.md (revision 2026-07-09, origin https://github.com/mattpocock/skills/blob/557a22040d64b8c03c725361637e6b10f2c64b73/skills/engineering/setup-matt-pocock-skills/SKILL.md; revision 2026-07-10, origin https://github.com/mattpocock/skills/blob/b93c987ac95a97bab83f4fd0263c5fb34a355ff1/skills/engineering/setup-matt-pocock-skills/SKILL.md — recommended-answer defaults and skipping settled/moot sections)
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-gi-d3eb2123.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-gi-586b767e.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-lo-606b1b18.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md (revision 2026-07-10, origin https://github.com/mattpocock/skills/blob/31dee0dfed958b42867d02168e4d300c452f86eb/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md — one-file-per-ticket local layout for `to-tickets`)
- `sources/mattpocock/skills-repo/docs-engineering-setup-matt-pocock-skills.md-ed003b6b.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/setup-matt-pocock-skills.md (revision 2026-07-10, origin https://github.com/mattpocock/skills/blob/29d7de66c30064a7a9df76ab428edf4c6bec6507/docs/engineering/setup-matt-pocock-skills.md)
- `sources/mattpocock/skills-repo/skills-engineering-to-issues-SKILL.md-04f1cc54.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/to-issues/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-code-review-SKILL.md-ffd0e041.md` — origin: https://github.com/mattpocock/skills/blob/a5c124ef9cfecc39636f426cc4ff956580d6ea10/skills/engineering/code-review/SKILL.md
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/9c306665c63db13e3cd9cf6df8871f7792051eab/CHANGELOG.md (revision 2026-07-09 — the `wayfinder` issue-tracker-path hardcoding fix, #472)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083115194268438833-ac7df7d2.md` — origin: https://x.com/mattpocockuk/status/2083115194268438833
