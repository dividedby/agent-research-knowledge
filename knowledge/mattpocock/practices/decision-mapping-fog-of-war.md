# Wayfinder (renamed from decision-mapping): planning that spans more sessions than one context holds

`wayfinder` — renamed from `decision-mapping` — targets the case the rest of the
planning chain can't: a loose idea whose open questions take **more than one
agent session** to resolve. Where `grill-with-docs → to-prd → to-issues` assumes
the plan can be settled in one unbroken smart-zone window, wayfinder is the
escape hatch for when it can't — it externalises the plan's state so
investigation can stretch across many sessions without losing the thread.

## The map moved onto the issue tracker, joining the engineering skills' shared spine

The map was originally a single git-tracked Markdown file; it is now a single
**issue** on whichever tracker `setup-matt-pocock-skills` already configured for
the repo (GitHub, GitLab, or local Markdown), labelled `wayfinder:map`, with
tickets as its **child issues**. This folds wayfinder into the same shared data
spine `to-prd`/`to-issues`/`triage` already read and write (see
`skills-compose-by-handoff`) instead of inventing a bespoke file format — the
map now lives wherever the team already tracks work. The map itself stays an
**index, not a store**: it holds Notes, a one-line gist-and-link per closed
ticket under Decisions-so-far, and the Fog — never a ticket's full detail, which
lives on the ticket issue itself. The hard constraint carries over unchanged:
the whole map is loaded as context **once per session**, so it must stay
compact, and each ticket is sized to roughly one 100K-token session. Where the
map, its children, blocking, and the frontier query physically live is
tracker-specific — a `docs/agents/issue-tracker.md` "Wayfinding operations"
section spells out the concrete calls per backend; absent that doc, wayfinder
defaults to the local-Markdown tracker.

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

## Tickets are tracker issues, blocked by the tracker's own dependency graph

A ticket's identity is now the tracker's own issue id, not a hand-picked slug.
Two label families carry state: `wayfinder:<type>` names the ticket kind
(below), and `wayfinder:claimed` is set by a session **before any work** —
the same write-before-work safety as before, so a second session reading the
map skips a claimed ticket rather than racing on it. Blocking now prefers each
tracker's **native** dependency link over a plain-text field, because a native
link renders the frontier *visually* in the tracker's own UI — the human sees
what's takeable without opening the map at all:

- **GitHub** — the native issue-dependencies API, added by posting the
  blocker's numeric **database id** (`gh api .../issues/<n> --jq .id`) — not
  its `#number` or its `node_id`, both easy to reach for by mistake and both
  wrong for this call.
- **GitLab** — the native `/blocked_by` quick action, but only on
  Premium/Ultimate tiers; the free tier falls back to a `Blocked by: #n, #n`
  line at the top of the ticket body.
- **Local Markdown** — no native tracker to defer to, so it stays the
  `Blocked by:` line, the original mechanism.

A ticket is **unblocked** once every blocker — native link or fallback line —
is closed; the **frontier** (open, unblocked, unclaimed children) is now a
tracker query per backend instead of a scan over one file.

## Refer by name, not by bare id

Because every map and ticket is now a tracker issue, each carries a **title**
— and the skill insists narration and the map's Decisions-so-far always cite
that title, never a bare `#42`. A wall of `#42, #43, #44` is illegible; names
read at a glance, with the id/URL riding *inside* the name as a link rather
than standing in for it. It's a small but transferable lesson on its own: once
an entity has both a durable identifier and a human label, prose should carry
the label and let the identifier travel underneath it, not the reverse.

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
you don't also resolve tickets. **Work through the map**: given a map (issue
URL or number) and an *optional* ticket (without one, the agent picks the
first frontier ticket in tracker order rather than the user choosing), claim
it, resolve it — invoking `/grilling` and `/domain-modeling` if in doubt, plus
anything the `## Notes` block names to consult — post the answer as a
resolution comment, close the ticket, and add or invalidate other tickets as
the resolution demands. Because tickets are resolved one at a time and the
user may run several in parallel, every session expects other agents to be
editing the tracker concurrently.

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
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-06-17; revision 2026-07-02, origin https://github.com/mattpocock/skills/blob/00b0f60a9f2cea78216bc7165684bd5610495f9e — `decision-mapping` renamed `wayfinder`)
- `sources/mattpocock/skills-repo/skills-in-progress-wayfinder-SKILL.md-82165350.md` — origin: https://github.com/mattpocock/skills/blob/a5c124ef9cfecc39636f426cc4ff956580d6ea10/skills/in-progress/wayfinder/SKILL.md (the rename, and the map moving onto the issue tracker; revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/9ee274c8fecd74661dceee5ab4e314b8c58f9e47 — "refer by name" convention)
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-gi-d3eb2123.md` — origin: https://github.com/mattpocock/skills/blob/81825ae44edc49c71a526b58a5225fde82f340fa/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md (revision 2026-07-02, the "Wayfinding operations" section added; revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/263a2d27d54d82e44d4587e6bbabd5833410c06b — the native issue-dependencies database-id detail)
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-gi-586b767e.md` — origin: https://github.com/mattpocock/skills/blob/4dda53bfcb34d30f7d0a5024a07e0436fb9e5d79/skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md (revision 2026-07-02, the "Wayfinding operations" section added; revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/00ea3ba0cb738a2d723bfe28bf7a75419e1961d2 — the Premium/Ultimate-tier native-blocking caveat)
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-lo-606b1b18.md` — origin: https://github.com/mattpocock/skills/blob/2f3267deb0afbb6f13294613a5f50e1b8df1156c/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md (revision 2026-07-02, the "Wayfinding operations" section added)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067965196618895564-c2d49f3d.md` — origin: https://x.com/mattpocockuk/status/2067965196618895564
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067602690725581067-eb6c35f9.md` — origin: https://x.com/mattpocockuk/status/2067602690725581067
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067682252742357292-b72bc2ce.md` — origin: https://x.com/mattpocockuk/status/2067682252742357292
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067682103030915278-5c57d5b4.md` — origin: https://x.com/mattpocockuk/status/2067682103030915278
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067710266230415567-f6fd1092.md` — origin: https://x.com/mattpocockuk/status/2067710266230415567
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067721635470147856-3d1433b6.md` — origin: https://x.com/mattpocockuk/status/2067721635470147856
