# Decision mapping: planning that spans more sessions than one context holds

`decision-mapping` targets the case the rest of the planning chain can't: a loose
idea whose open questions take **more than one agent session** to resolve. Where
`grill-with-docs → to-prd → to-issues` assumes the plan can be settled in one
unbroken smart-zone window, decision-mapping is the escape hatch for when it
can't — it externalises the plan's state into a file so investigation can stretch
across many sessions without losing the thread.

## The decision map is the durable, compact artifact

A single git-tracked Markdown file holds the whole plan as numbered **tickets**,
each a section keyed by its number with a `Blocked by:` edge list, a `Type:`, a
Question, and an Answer. The hard constraint: the **whole map is loaded as context
into every session**, so it must stay compact — assets produced while resolving a
ticket are *linked from* the map, never inlined. Each ticket is sized to roughly
one 100K-token session. This is the same "state lives in a file the next fresh
context reloads" pattern as `handoff` and the `teach` workspace, specialised for
multi-session planning.

## Fog of war: investigate only the frontier

The map is *deliberately incomplete beyond the frontier* — a **fog of war** the
agent pushes back one node at a time. You don't plan the whole tree up front; you
resolve the tickets at the frontier, which reveals the next ones. The map is
"done" not when fully filled in but when the fog has been pushed back far enough
that the path to the finish line is clear — at which point no more tickets are
needed. (The "fog of war" leading word is reused across the collection as the name
for deliberately-hidden lookahead.)

## "Frontier" and "fog of war" are the leading words

Matt promotes **frontier** and **fog of war** to named leading words for *all*
planning with an agent, not just the skill: *"Don't plan past the fog of war.
Let's resolve just the decisions at the frontier first."* The frontier is the
first visible edge of the unknown — the decisions you can resolve right now,
which once resolved reveal the next ones. Naming them gives a grilling session a
shared vocabulary for *how far ahead to plan*: you stop when the immediate
frontier is settled rather than trying to specify the whole tree, and the names
make the clear/handoff/compact decisions "totally obvious." The map is the
durable form of this, but the discipline works in a bare conversation too —
which is why the decision-map artifact itself is *deliberately incomplete beyond
the frontier* (above). There is no value in *visualising* the map (a mind-map
MCP buys nothing) — the frontier discipline is about what you resolve next, not
a picture.

## Bootstrap with a short grilling session, then fan out

The decision-map flow starts with a deliberately **short grilling session** —
just long enough to *discover the frontier*, the first visible part of the fog of
war, not to resolve it. From there you **fan out** to multiple parallel
grilling / prototyping / research sessions, each pushing back one aspect of the
fog as you go. Matt road-tests this kicking off an AFK agent on "an extremely
ambitious feature" and reports never feeling "more confident that I'm aligned" —
the payoff of resolving the frontier before committing is alignment confidence on
a large autonomous build.

## Three ticket types route to the right tool

Each open question is one of three kinds, and the kind chooses how it gets
resolved:

- **Research** — reading docs, third-party APIs, or knowledge bases; produces a
  markdown summary asset. Use when the answer lives outside the working directory.
- **Prototype** — runnable code to test a hypothesis or explore a design space;
  uses the `/prototype` skill, produces a prototype asset. Use when "how should it
  look / behave" is the question.
- **Discuss** — conversation with the agent via `/grilling` and `/domain-modeling`;
  the default.

## Bootstrap and resume; parallel-safe by construction

The skill has two invocations. **Bootstrap**: from a loose idea, run grilling +
domain-modeling to surface the decisions, write a mostly-fog map with the frontier
identified and trivial entries resolved inline, then *stop* — map-building is one
session's work, you don't also resolve tickets. **Resume**: given a map path and a
ticket number, load the whole map, resolve that one ticket, record the answer, add
newly-discovered tickets with correct `blocked_by` edges, and stop. Because
tickets are resolved one at a time and the user may run several in parallel, every
session expects other agents to have edited the map — and a resolution that
invalidates other nodes updates or deletes them. Crucially, the skill knows when
*not* to exist: if the initial grilling surfaces no fog (no multi-session
decisions), it offers to **skip the map entirely** and implement directly or go
straight to `/to-prd`.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-decision-mapping-SKILL.md-cdd9e8ec.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/in-progress/decision-mapping/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-06-17)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067965196618895564-c2d49f3d.md` — origin: https://x.com/mattpocockuk/status/2067965196618895564
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067602690725581067-eb6c35f9.md` — origin: https://x.com/mattpocockuk/status/2067602690725581067
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067682252742357292-b72bc2ce.md` — origin: https://x.com/mattpocockuk/status/2067682252742357292
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067682103030915278-5c57d5b4.md` — origin: https://x.com/mattpocockuk/status/2067682103030915278
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067710266230415567-f6fd1092.md` — origin: https://x.com/mattpocockuk/status/2067710266230415567
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067721635470147856-3d1433b6.md` — origin: https://x.com/mattpocockuk/status/2067721635470147856
