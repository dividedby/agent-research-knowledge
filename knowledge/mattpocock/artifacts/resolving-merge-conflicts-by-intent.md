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

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-resolving-merge-conflicts-SKILL.md-f2c6b279.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/resolving-merge-conflicts/SKILL.md
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
