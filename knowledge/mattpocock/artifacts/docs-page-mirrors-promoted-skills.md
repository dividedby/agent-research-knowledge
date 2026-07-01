# A human-facing docs page, mechanically paired to every promoted skill

Skills in the two **promoted** buckets (`engineering/`, `productivity/`) each
get a second artifact beyond the `SKILL.md` itself: a human-facing docs page at
`docs/<bucket>/<skill-name>.md`, published at `aihero.dev/skills-<skill-name>`
regardless of which bucket the skill lives in — the docs-tree path is repo
organisation only, invisible to the reader. `misc/`, `personal/`,
`in-progress/`, and `deprecated/` skills get **no** docs page, mirroring the
same promotion gate that already governs `README.md`/`plugin.json` visibility
(`buckets-and-promotion-discipline`): a skill's graduation into the advertised
set now carries two obligations, not one, and both are enforced by the same
mechanical rule — bucket membership decides inclusion, not judgement calls per
skill.

## Why a second artifact, not just a longer SKILL.md

A `SKILL.md` is written to be *executed* — tight, imperative, front-loaded
with the trigger phrasing and steps an agent needs mid-run. A docs page is
written to be *read* — it orients a human deciding whether and when to reach
for the skill at all, in prose a `SKILL.md`'s progressive-disclosure structure
would never carry: a "What it does" framed by what the skill *refuses* to do,
a "When to reach for it" that names the neighbouring skills it's easily
confused with and why each isn't the fit, and a closing "Where it fits" that
places the skill on the map relative to `ask-matt`'s flows. Every docs page
ends by routing back to `ask-matt` — reinforcing that page's role as the
standing index over a set too large to hold in the reader's head
(`invocation-axis-user-vs-model`).

## The pairing is a maintenance obligation, not a one-time export

`CLAUDE.md` states the sync explicitly: when a promoted skill is added,
renamed, or has its *behaviour* changed, its docs page must be created or
re-synced in the same change — the docs tree is a live mirror of the
`SKILL.md`s, not a point-in-time snapshot generated once and left to drift.
This is the same anti-doc-rot posture as the primary/secondary-source
discipline in `context-compression-and-handoff-mechanics` (a secondary source
is only trustworthy if it's kept current with a fast-changing primary) —
applied here to a *published*, externally-linked artifact rather than a
disposable handoff document, which raises the cost of letting it drift.

## Sources

- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/CLAUDE.md (revision 2026-07-01)
- `sources/mattpocock/skills-repo/docs-engineering-ask-matt.md-cb27a380.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/ask-matt.md
- `sources/mattpocock/skills-repo/docs-engineering-tdd.md-54751a46.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/tdd.md
- `sources/mattpocock/skills-repo/docs-productivity-writing-great-skills.md-aa4b85bc.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/productivity/writing-great-skills.md
- `sources/mattpocock/skills-repo/skills-misc-README.md-40448e66.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/misc/README.md (revision 2026-07-01)
