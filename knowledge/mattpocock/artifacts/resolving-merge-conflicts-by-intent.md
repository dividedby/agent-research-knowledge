# Resolving merge conflicts by recovering intent

`resolving-merge-conflicts` is a small standalone skill (no dependencies on other
skills) for an in-progress git merge or rebase conflict. Its design point is that
a conflict is not a text-diff puzzle but an **intent** reconciliation: before
touching a hunk, the agent finds the **primary source** for each side — reading
the commit messages, PRs, and originating issues to understand *why* each change
was made — and only then resolves.

The resolution rules encode the same discipline:

- **Preserve both intents where possible.** Where they're genuinely incompatible,
  pick the side matching the *merge's stated goal* and note the trade-off.
- **Never invent new behaviour** while resolving — the skill is reconciling
  existing changes, not designing.
- **Always resolve; never `--abort`.** Backing out is not an option the skill
  offers.

It closes by discovering the project's automated checks and running them in
order (typically typecheck → tests → format), fixing anything the merge broke,
then finishing the merge/rebase — the same "let the deterministic feedback loop
confirm the work" instinct that runs through `tdd`, `diagnosing-bugs`, and
`implement` (see `feedback-loop-is-the-work`). The "find the primary source before
acting" move mirrors `diagnosing-bugs`' refusal to hypothesise before reproducing
and `domain-modeling`'s cross-referencing against the code: recover ground truth
first, act second.

## Don't zone parallel work off to dodge conflicts — merge back through the author instead

Asked whether parallel agent tasks should be kept off each other's files to
avoid conflicts altogether, the answer is mostly no: zoning files off between
parallel tasks costs more than it saves, because agents are good enough at
resolving merge conflicts that the trade-off isn't as harsh as it looks. The
one piece of discipline worth keeping regardless is sequencing — do large,
sweeping refactors *first*, before ten branches have forked off the
pre-refactor state, because a big rename landing late is the case that stays
genuinely expensive to reconcile. A field report on parallel git worktrees adds
one more caveat: when sibling sessions each build a ticket in their own tree,
the merge back is best done by the session that *wrote* the change, because it
already holds the intent this skill otherwise has to go and reconstruct from
commits, PRs and issues — batching everyone's conflicts onto one agent at the
end throws away exactly the context step one of this skill exists to recover.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-resolving-merge-conflicts-eaa48129.md` — origin: https://www.aihero.dev/skills-resolving-merge-conflicts
- `sources/mattpocock/skills-repo/skills-engineering-resolving-merge-conflicts-SKILL.md-f2c6b279.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/resolving-merge-conflicts/SKILL.md
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
