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

## Four ticket types route to the right tool

Each open question is one of four kinds, and the kind chooses how it gets
resolved:

- **Research** — reading docs, third-party APIs, or knowledge bases; produces a
  markdown summary asset. Use when the answer lives outside the working directory.
- **Prototype** — a cheap, rough, concrete artifact to react to (an outline, a
  stub, or runnable UI/logic code via `/prototype`); produces the prototype as an
  asset. The point isn't only code — raising the fidelity of the discussion with
  *any* concrete draft counts, which is why the type broadened from "UI/logic
  code" to "cheap concrete artifact" once the map started planning non-code
  work too. Use when "how should it look / behave" is the question.
- **Grilling** — conversation with the agent via `/grilling` and
  `/domain-modeling`, one question at a time; the default. (The type was first
  named "Discuss" and renamed to "Grilling" — the resolution mechanism *is* a
  grilling session, so the type points straight at the skill that runs it.)
- **Task** — literal manual work with nothing to decide, prototype, or research:
  moving data, signing up for a third-party service, provisioning access. The
  agent automates what it can; otherwise it hands the human a precise checklist.
  A Task resolves when the work is *done*, and its answer records what was done
  plus any resulting facts (a credential's location, a new URL, a row count)
  later tickets depend on — the same "record the fact, not the narrative" posture
  as an ADR.

## Tickets are slugs with status, not numbers

Each ticket's canonical id is a short dash-case slug (`relational-db`,
`auth-strategy`) rather than a sequence number — terse and stable enough to use
in prose and in every `Blocked by:` edge. Each also carries an explicit
`Status: open | in-progress | resolved`, and a ticket is **unblocked** only once
every entry in its own `Blocked by:` list is `resolved`. A session **claims**
its ticket by setting `Status: in-progress` and saving the map *before* doing
any work — the write-before-work ordering is what makes concurrent sessions
safe: a second session reading the map sees the claim and skips the ticket
rather than racing on it.

## Domain-agnostic: plans code, course content, or anything shaped the same

The map's own framing has generalised past engineering: it now explicitly
plans "course content, or anything else that fits the same shape," and an
optional `## Notes` block declares the map's **domain**, any skills every
session should `consult`, and freeform standing preferences the planning
surfaces. This is the fog-of-war discipline decoupled from its original
engineering use case — the shape (frontier, tickets, blocked-by edges) is
domain-neutral; only the ticket content and the consulted skills vary.

## Bootstrap and resume; parallel-safe by construction

The skill has two invocations, and **every session — either branch — ends with
a Handoff**, never resolving more than one ticket per session. **Create the
map**: from a loose idea, run grilling + domain-modeling to surface the
decisions, write a mostly-fog map with the frontier identified and trivial
entries resolved inline, then hand off — map-building is one session's work,
you don't also resolve tickets. **Work through the map**: given a map path and
an *optional* ticket slug (without one, the agent picks the next open,
unblocked ticket in document order rather than the user choosing), claim it,
resolve it — invoking `/grilling` and `/domain-modeling` if in doubt, plus
anything the `## Notes` block names to consult — record the answer, set
`Status: resolved`, and add or invalidate other nodes as the resolution
demands. Because tickets are resolved one at a time and the user may run
several in parallel, every session expects other agents to be editing the map
concurrently.

The **Handoff** step is itself a fixed protocol: clear the context and open
fresh sessions, closing with a copy-pasteable **Next steps** block. If open
tickets remain, it lists the currently-unblocked ones and offers two paths —
one bare command that lets the next session pick the ticket, and one pinned
command per unblocked ticket for running them in parallel windows. If none
remain, the fog is pushed back far enough that the finish line is clear — the
map is done, and the skill recommends implementing directly or handing off to
`/to-prd`. This is the same "skip the map when there's no fog" escape hatch as
before, now folded into the same Handoff step rather than a separate check:
the skill knows when *not* to exist.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-decision-mapping-SKILL.md-cdd9e8ec.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/in-progress/decision-mapping/SKILL.md (and revision 2026-06-24, origin https://github.com/mattpocock/skills/blob/846e8509f656adee303a5ea514a6830af4a962d6 — "Discuss" ticket type renamed "Grilling"; revision 2026-06-30, origin https://github.com/mattpocock/skills/blob/8258b0fa07254990b0d4d680ef28d353ef67788f — slug ids, `Status`, and the `Handoff` protocol; revision 2026-07-01, origin https://github.com/mattpocock/skills/blob/ac84e71c521d7636dc3db01ca36f0c167b6b39e2 — the `Task` ticket type, domain-agnostic framing, and the `## Notes` block)
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-06-17)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067965196618895564-c2d49f3d.md` — origin: https://x.com/mattpocockuk/status/2067965196618895564
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067602690725581067-eb6c35f9.md` — origin: https://x.com/mattpocockuk/status/2067602690725581067
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067682252742357292-b72bc2ce.md` — origin: https://x.com/mattpocockuk/status/2067682252742357292
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067682103030915278-5c57d5b4.md` — origin: https://x.com/mattpocockuk/status/2067682103030915278
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067710266230415567-f6fd1092.md` — origin: https://x.com/mattpocockuk/status/2067710266230415567
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067721635470147856-3d1433b6.md` — origin: https://x.com/mattpocockuk/status/2067721635470147856
