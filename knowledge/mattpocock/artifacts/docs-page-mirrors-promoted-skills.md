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

## A fourth recurring section: the self-check

Beyond "What it does", "When to reach for it", and "Where it fits", most docs
pages carry a fourth structural section, "It's working if" — a short bulleted
self-check for telling whether the skill behaved as designed *this run*, not
merely whether it ran. `tdd`'s reads "it writes one test, gets it passing, and
only then writes the next"; `grill-with-docs`'s reads "it asks one question at
a time and waits" and "ADRs stay rare." Each bullet names an observable
*symptom* of the skill working, never an internal step — so a human (or a
supervising agent) can catch the skill quietly drifting off its own discipline
before trusting whatever it produced, the same failure the docs page's other
sections exist to head off before the skill is even invoked.

## The template settled on four fixed sections, not three-plus-a-recurring-one

`CLAUDE.md` later names the shape explicitly rather than leaving it to be
inferred from example: a finished docs page carries exactly four sections —
**What it does**, **When to reach for it**, **Common questions**, and **It's
working if** — with a dedicated `.agents/writing-docs.md` holding the
template, the section order, and where to mine the questions from. **Common
questions** is the section this later pass adds: an FAQ answering the
objections and edge cases a reader actually raises against the skill —
`prototype`'s docs page, for instance, fields "isn't the prototype supposed to
be deleted?" and "isn't this the fastest possible way to burn tokens?" head
on, each with a real answer rather than a restatement of "What it does." Naming
the section (and where its content comes from) turns what used to read as an
optional flourish into a required, checkable part of every promoted skill's
sync obligation.

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

## The same obligation extends to `ask-matt`'s own map

`CLAUDE.md` widens this discipline to a second artifact that isn't a docs
page at all: `ask-matt`, the router over every user-reachable skill (see
`invocation-axis-user-vs-model`). "The same trigger that re-syncs a docs page
applies to it" — whenever a user-reachable skill is added, renamed, removed,
or changes how it fits the flows, `ask-matt`'s `SKILL.md` must be re-read and
updated so its map stays accurate. The framing is pointed: *"a new skill it
never mentions, or a stale one it still routes to, is a router that lies."*
The lesson generalises past docs pages specifically — any artifact whose whole
value is being an accurate *index* over a faster-changing set carries this
same obligation, and it decays the same way a docs page does if a change to
the underlying set isn't mirrored into it in the same commit.

## Sources

- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/CLAUDE.md (revision 2026-07-01)
- `sources/mattpocock/skills-repo/docs-engineering-ask-matt.md-cb27a380.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/ask-matt.md
- `sources/mattpocock/skills-repo/docs-engineering-tdd.md-54751a46.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/tdd.md
- `sources/mattpocock/skills-repo/docs-productivity-writing-great-skills.md-aa4b85bc.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/productivity/writing-great-skills.md
- `sources/mattpocock/skills-repo/skills-misc-README.md-40448e66.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/misc/README.md (revision 2026-07-01)
- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/754bff7aeec587bf80d31075fa64717aa915b241/CLAUDE.md (revision 2026-07-02 — `ask-matt`'s resync obligation)
- `sources/mattpocock/aihero/https-www.aihero.dev-grill-with-docs-d376dfd1.md` — origin: https://www.aihero.dev/grill-with-docs (revision 2026-07-02 — the "It's working if" self-check section)
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-tdd-48650cc0.md` — origin: https://www.aihero.dev/skills-tdd (revision 2026-07-02 — the same "It's working if" section)
- `sources/mattpocock/skills-repo/AGENTS.md.md` — origin: https://github.com/mattpocock/skills/blob/29de6f3f3088823b95ca741eeaff8c79116722ad/AGENTS.md (revision 2026-08-06 — the four-section template naming "Common questions")
- `sources/mattpocock/skills-repo/docs-engineering-prototype.md-ccedcc07.md` — origin: https://github.com/mattpocock/skills/blob/72f8eb0ff1b18ad2306a4b9c114a727bf113f7fe/docs/engineering/prototype.md (revision 2026-08-06 — a worked "Common questions" section)
