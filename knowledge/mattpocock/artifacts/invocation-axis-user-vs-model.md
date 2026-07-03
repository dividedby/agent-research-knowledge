# The invocation axis: user-invoked orchestrators vs model-invoked discipline

The collection was reorganised around a single axis — **who can reach a skill** —
and the whole skill set now sorts cleanly into two roles. What was earlier framed
as a *future* "Commands vs Skills" split (see `skills-compose-by-handoff`) is now
the realised architecture, renamed and made load-bearing.

- **User-invoked** (`disable-model-invocation: true`) — reachable *only* when the
  human types its name. Its `description` is stripped of trigger phrasing and
  becomes a one-line human-facing summary; it costs zero context load. These are
  the **orchestrators**: the top-level entry points a person reaches for
  deliberately (`grill-me`, `grill-with-docs`, `to-prd`, `to-issues`, `triage`,
  `improve-codebase-architecture`, `prototype`, `handoff`, `teach`, `ask-matt`,
  `wayfinder` — renamed from `decision-mapping`).
- **Model-invoked** (the default — omit the flag) — reachable by the model *or*
  the human, so the agent can auto-fire it and other skills can reach it. Its
  `description` keeps rich "Use when…" trigger phrasing and pays a permanent
  context load. These hold the **reusable discipline** the orchestrators compose
  (`grilling`, `domain-modeling`, `codebase-design`, `diagnosing-bugs`, `tdd`).

## The one-way invocation rule

Because a user-invoked skill has no `description`, *nothing but the human can
reach it* — so a user-invoked skill may invoke model-invoked skills, but **never
another user-invoked one**. This single constraint is what forces the role split:
shared logic that several orchestrators need must live in a model-invoked skill
(or a plain external reference file), not in another orchestrator. The dependency
graph is therefore always orchestrator → primitive, never orchestrator →
orchestrator.

## The refactor it drove

Formalising the axis triggered a fleet-wide rewrite. The relentless-interview
logic, previously duplicated in `grill-me` and `grill-with-docs`, was extracted
into one model-invoked `grilling` primitive; both former skills collapsed to a
single line that runs it (`grill-with-docs` additionally runs `domain-modeling`).
The deep-module vocabulary that lived inside `improve-codebase-architecture`'s
`LANGUAGE.md` moved out to a standalone model-invoked `codebase-design` skill so
`tdd` and others can reach it; `tdd` dropped its bundled `deep-modules.md` /
`interface-design.md` in favour of pointing at `/codebase-design`. The pattern:
**a primitive earns model-invocation precisely when more than one orchestrator
must reach it.**

## `ask-matt`: a router over the orchestrators

Because user-invoked skills are invisible to the agent, the human is the index
that must remember they exist — and as they multiply, that cognitive load needs
its own cure. `ask-matt` is a **router skill**: a user-invoked skill whose only
job is to name the other user-invoked skills and when to reach for each. It can
only *hint*, never fire them (it has no way to reach a sibling user-invoked
skill). It encodes a **main flow** (`grill-with-docs → [prototype detour via
handoff] → to-prd → to-issues → implement → code-review`), **on-ramps** that merge
onto it (`triage` for incoming issues, `diagnosing-bugs` for something broken),
and standalone tools — turning the loose pile of slash-commands into a navigable
map with explicit context-hygiene rules (keep the planning chain in one unbroken
smart-zone window; start each `/implement` fresh). It has since grown past
naming only the user-invoked set: it also points at the model-invoked
primitives worth reaching for *by name* (`/tdd`, `/diagnosing-bugs`,
`/prototype`, `/code-review`, and the two vocabulary references
`/domain-modeling`/`/codebase-design`) — still only a pointer, since it still
can't fire them itself. And the map is now a maintained artifact in its own
right: `CLAUDE.md` obliges a re-read and update of `ask-matt`'s `SKILL.md`
whenever a user-reachable skill is added, renamed, removed, or changes how it
fits the flows — the same doc-rot discipline as the paired docs pages (see
`docs-page-mirrors-promoted-skills`), because a router that names a skill that
no longer exists, or omits one that now does, actively misleads instead of
merely going stale.

## "Context load" is the cost being managed; continuous verbs name the model-invoked set

Matt's own term for the permanent per-turn tax a model-invoked `description`
charges is **context load** — every model-invoked skill's trigger phrasing sits
in the window whether or not it fires, so the axis is fundamentally a context-load
budget. The v1 release was largely a *de-loading* pass: "loads of them changed
from model-invoked to user-invoked, and I shortened the descriptions" — and he
frames the improvement honestly, "behind every improved perf metric is an implicit
admission of previous guilt." A naming convention falls out of the axis:
**continuous verbs (`-ing`) are the standard for skills the model invokes
itself** (`grilling`, `domain-modeling`), distinguishing the model-reachable
primitives from the user-typed orchestrators by their description grammar alone.

The split is a deliberate choice about *where the cognitive load lives*. Matt
prefers the load on the **user**, not the model: a skill the model is trusted to
auto-fire "runs counter to how my skills actually work." He rejects two common
attempts to dodge the axis. (1) Keeping a skill model-invocable but giving it a
"don't invoke unless explicitly asked" description "costs nothing" only on paper —
Matt finds "the token waste of that approach very annoying," because the
description still loads every turn. (2) Hiding rarely-used skills *outside*
`/skills` and pointing at them manually is rejected the other way: that's "higher
cognitive load for the user, makes no sense." The user-invoked mechanism
(zero-context-load, typed by name) is the principled middle — neither paying
context load for a skill the model shouldn't fire, nor offloading filing onto the
human.

## How the buckets express it

The convention is enforced structurally: `CLAUDE.md` mandates that every
`SKILL.md` is one or the other, and that bucket `README.md`s and the top-level
`README.md` group their entries under **User-invoked** and **Model-invoked**
headings. The full definitions, the description conventions, and the one-way rule
live in a dedicated `docs/invocation.md`. Two skills were dropped in the same
release as redundant (`caveman`, `zoom-out`), and `write-a-skill` was replaced by
`writing-great-skills` — the axis is also a pruning lens.

## Sources

- `sources/mattpocock/skills-repo/docs-invocation.md-1ce78905.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/docs/invocation.md
- `sources/mattpocock/skills-repo/skills-engineering-ask-matt-SKILL.md-f5c205a8.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/ask-matt/SKILL.md
- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/CLAUDE.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/skills-engineering-README.md-1400dd55.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/README.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
- `sources/mattpocock/skills-repo/skills-productivity-grill-me-SKILL.md-5d73b98f.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/grill-me/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/skills-engineering-grill-with-docs-SKILL.md-1015ebf3.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/grill-with-docs/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067321326801437113-2af8141d.md` — origin: https://x.com/mattpocockuk/status/2067321326801437113
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067330241266061777-1f8ff90f.md` — origin: https://x.com/mattpocockuk/status/2067330241266061777
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067272387905671362-3c1d62fe.md` — origin: https://x.com/mattpocockuk/status/2067272387905671362
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067264261408063757-4da8b3a1.md` — origin: https://x.com/mattpocockuk/status/2067264261408063757
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067536507653468380-59ce88dc.md` — origin: https://x.com/mattpocockuk/status/2067536507653468380
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067556399945589239-1ceb3ba7.md` — origin: https://x.com/mattpocockuk/status/2067556399945589239
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067966169860931606-a1f7c79f.md` — origin: https://x.com/mattpocockuk/status/2067966169860931606
- `sources/mattpocock/skills-repo/skills-engineering-ask-matt-SKILL.md-f5c205a8.md` — origin: https://github.com/mattpocock/skills/blob/8e9705356ea758e0bf375ccfa5efdd78a5a4fbff/skills/engineering/ask-matt/SKILL.md (revision 2026-07-02 — the "Vocabulary underneath" section and the `code-review` chain step; revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/ebee08eb332d93484b9afda9acaa84eb1e024640 — `/research` added to Standalone)
- `sources/mattpocock/skills-repo/docs-engineering-ask-matt.md-cb27a380.md` — origin: https://github.com/mattpocock/skills/blob/1f39f6f24749f410d98d3c39cc3402e9446f9f9b/docs/engineering/ask-matt.md (revision 2026-07-02 — the same "Vocabulary underneath" pointer, on the docs page)
- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/754bff7aeec587bf80d31075fa64717aa915b241/CLAUDE.md (revision 2026-07-02 — `ask-matt`'s resync obligation)
