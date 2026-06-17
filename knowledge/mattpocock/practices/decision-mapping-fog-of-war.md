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
