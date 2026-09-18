# Reproduce borrowed content, don't depend on its source skill

When a skill's content is substantially another author's work, the fix is a
`CREDITS.md` attribution file, not a dependency edge to the skill it came
from — because skills in this collection are designed to install one at a
time (`npx skills add mattpocock/skills --skill=<name>`), and a real
dependency would force pulling in a whole second skill's directory just to
satisfy one section of the first.

The `pr` skill's Summary section is HumanLayer's `show-me` skill (Dex
Horthy), reproduced almost word for word and re-aimed at a diff instead of a
live conversation. `pr` doesn't declare `show-me` as a dependency — it isn't
even part of this repo — so the borrowed text is copied inline, and
`CREDITS.md` exists purely to carry the attribution a dependency relationship
would otherwise have carried: which section, whose original skill, and a link
to it. The same credit is duplicated into `SKILL.md`'s own frontmatter as a
structured `metadata.credits` block (skill/author/organisation/url), so the
provenance survives even if `CREDITS.md` itself is never opened.

The general move: borrowing content across skill boundaries doesn't have to
mean coupling to the source — copy the content in and attribute it
explicitly, and reserve real dependencies (see
`setup-seeded-config-and-dependency-tiers`) for cases where the consumer
actually needs the other skill's *behavior* at runtime, not just its text.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-pr-CREDITS.md-171b57e6.md` — origin: https://github.com/mattpocock/skills/blob/74ca5fe077456a0b3b2f5310cf9430999fd0b5fd/skills/in-progress/pr/CREDITS.md
- `sources/mattpocock/skills-repo/skills-in-progress-pr-SKILL.md-795517e8.md` — origin: https://github.com/mattpocock/skills/blob/74ca5fe077456a0b3b2f5310cf9430999fd0b5fd/skills/in-progress/pr/SKILL.md
