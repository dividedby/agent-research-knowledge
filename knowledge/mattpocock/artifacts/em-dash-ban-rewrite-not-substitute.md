# Banning em-dashes as a prose rule, enforced by rewrite, not by find-and-replace

A repo-wide style rule bans the em-dash outright, across every kind of prose
the repo carries — `SKILL.md` files, docs, `README.md`, `CHANGELOG.md`, ADRs,
changesets, code comments. The rule matters less for the character itself than
for how it has to be removed: "where a sentence reaches for one, rewrite it
instead with a comma, colon, period, parentheses, or a conjunction, whichever
the sentence actually wants; never do a blind character substitution."

## Why a ban, not a style preference

The em-dash is one of the more reliable tells of AI-generated prose — a
default flourish models reach for that a `CLAUDE.md` line can suppress at the
prompt level (see `dead-prose-strips-ai-flair`'s "dead prose" instruction for
the softer version of the same instinct), but a repo accumulates prose across
many sessions and many contributors, so a standing structural rule closes the
gap a per-prompt instruction can't guarantee to hold every time.

## The failure mode a naive fix would introduce

A mechanical em-dash-to-comma or em-dash-to-colon substitution would "fix" the
character while leaving the sentence's grammar built around a pause the
replacement punctuation doesn't supply — the character changes, the sentence
doesn't stop reading like it was written for the one it lost. The rule heads
this off explicitly: rewrite for whichever mark the sentence's actual
grammatical relationship calls for (a comma for a parenthetical, a colon for
an explanation, a full stop for two independent clauses), rather than treating
every em-dash as interchangeable with one fixed replacement. This generalizes
past em-dashes specifically: any repo-wide find-and-replace over prose that
was written with a placeholder's specific shape in mind needs the same
per-instance judgement call, not a single global substitution rule.

## Sources

- `sources/mattpocock/skills-repo/AGENTS.md.md` — origin: https://github.com/mattpocock/skills/blob/3fa0c426c0fdd4c5cdee05c2bbf66e9cf4f1abc1/AGENTS.md (revision 2026-08-20 — the em-dash ban and the rewrite-not-substitute instruction)
- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/3fa0c426c0fdd4c5cdee05c2bbf66e9cf4f1abc1/CLAUDE.md (revision 2026-08-20, same rule)
