# Wayfinder (renamed from decision-mapping): planning that spans more sessions than one context holds

`wayfinder` — renamed from `decision-mapping` — targets the case the rest of the
planning chain can't: a loose idea whose open questions take **more than one
agent session** to resolve. Where `grill-with-docs → to-prd → to-issues` assumes
the plan can be settled in one unbroken smart-zone window, wayfinder is the
escape hatch for when it can't — it externalises the plan's state so
investigation can stretch across many sessions without losing the thread.

## Naming, live: a wayfinder takes you there, not there-and-back

Talked through in public before the rename landed, Matt tried `/scout` first and
rejected it on the word's own connotation: **"scouts go there and come back. A
wayfinder takes you there."** The old name (`decision-mapping`) described the
artifact; the candidates test whether the *word* matches the one-way trip the
skill actually makes — you don't send it out to report back, you use it to
navigate. Landing on `wayfinder` he immediately restates the skill's new place in
the stack: it **replaces `grill-with-docs`** in his own workflow, not by doing
grill-with-docs's job but by sitting **above** it as an **orchestrator** —
"you'll find wayfinder intuitive, I promise, it's just a more organized and
foolproof `grill-me`." Concretely, that orchestration means wayfinder is the one
that needs `/grilling`, `/prototype`, and `/research` as sub-skills (matching the
four ticket types above) and "operates on a level above, so it'll be responsible
for organizing multiple grilling sessions" — the frontier fan-out described above,
restated from the announcement itself rather than the SKILL.md.

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

## Name the destination before mapping the frontier

Charting now opens with a distinct first act: **naming the destination** — what
reaching the end of this map looks like (a spec to hand off, a decision to lock
before planning starts, a change made in place like a data-structure migration).
A short `/grilling` + `/domain-modeling` session settles it, because the
destination **fixes the scope** for every ticket the map will grow — you can't
tell fog from noise until you know what you're navigating toward. Only after
that does the second, deliberately **breadth-first** grilling pass run: fan out
across the whole space rather than going deep on any one thread, surfacing the
open decisions and the first steps takeable now. Two short passes, not one —
because a single pass that both names the destination and maps the frontier
conflates "what are we aiming at" with "what's the first move," and the first
question is cheaper to get wrong quietly if it's never asked on its own.

## Out of scope is a scope boundary, not fog

Once the destination fixes scope, the map's "not yet known" section (renamed
from Fog to **Not yet specified**) splits into two genuinely different things,
and conflating them was the bug the rename fixes. **Not yet specified** is
in-scope work too dim to ticket yet — it graduates into tickets as the frontier
advances. **Out of scope** is work that sits *past* the destination entirely —
it never graduates, because the frontier only ever advances *toward* the
destination, never past it. The test is scope, not sharpness: a vague-but-
in-scope idea is Not-yet-specified; a sharp, well-understood idea that simply
isn't what this effort is for is Out of scope. When a ticket already exists but
turns out to sit past the destination — mis-scoped while charting, or exposed
mid-resolution — it's **closed** (never resolved) with one line logged under
Out of scope: the gist and why, linking the closed ticket. That line stays out
of Decisions-so-far, which records the route actually *walked* — ruling
something out of scope is a boundary you draw, not a step you take. Because
out-of-scope work never graduates, it returns only if the destination itself is
redrawn — and then as a fresh effort, not a resumption of the old ticket.

## Fan out once the frontier is visible

From the frontier you **fan out** to multiple parallel grilling / prototyping /
research sessions, each pushing back one aspect of the fog as you go. Matt
road-tests this kicking off an AFK agent on "an extremely ambitious feature" and
reports never feeling "more confident that I'm aligned" — the payoff of
resolving the frontier before committing is alignment confidence on a large
autonomous build.

## Four ticket types route to the right tool, each tagged HITL or AFK

Each open question is one of four kinds, and the kind chooses how it gets
resolved. Every type now also carries an explicit **HITL** (human in the loop
— resolved only through a live exchange the agent never stands in for) or
**AFK** (agent-driven alone) tag:

- **Research** (AFK) — reading docs, third-party APIs, or knowledge bases;
  produces a markdown summary asset. Use when the answer lives outside the
  working directory.
- **Prototype** (HITL) — a cheap, rough, concrete artifact to react to (an
  outline, a stub, or runnable UI/logic code via `/prototype`); produces the
  prototype as an asset. The point isn't only code — raising the fidelity of
  the discussion with *any* concrete draft counts, which is why the type
  broadened from "UI/logic code" to "cheap concrete artifact" once the map
  started planning non-code work too. Use when "how should it look / behave"
  is the question.
- **Grilling** (HITL) — conversation with the agent via `/grilling` and
  `/domain-modeling`, one question at a time; the default. (The type was first
  named "Discuss" and renamed to "Grilling" — the resolution mechanism *is* a
  grilling session, so the type points straight at the skill that runs it.)
- **Task** (HITL or AFK) — literal manual work with nothing to decide,
  prototype, or research, but the discussion stays blocked until it's done:
  moving data, signing up for a third-party service, provisioning access. The
  agent drives it alone where it can (AFK); otherwise it hands the human a
  precise checklist (HITL). A Task resolves when the work is *done*, and its
  answer records what was done plus any resulting facts (a credential's
  location, a new URL, a row count) later tickets depend on — the same
  "record the fact, not the narrative" posture as an ADR.

The HITL tag guards against a specific failure: a Grilling or Prototype ticket
"resolved" by the agent quietly answering its own questions isn't resolved at
all — the whole point of a HITL ticket is the human's side of the exchange,
and the agent standing in for it silently reintroduces the misalignment the
skill exists to catch. Task is the one type that *does* rather than decides,
and earns its place on the map only because it unblocks a decision (provisioning
access, moving data so its shape can be seen) rather than delivering the
destination itself.

## Plan, don't do

Wayfinder defaults to **planning**, not doing: each ticket resolves a
decision, and the map is done once nothing is left to decide before someone
goes and executes. The pull to just do the work mid-session is treated as a
signal, not a shortcut to take — reaching for "let's just build it" usually
means you've hit the edge of the map and it's time to hand off, not to keep
resolving tickets. An individual effort can override this in its `## Notes`
block to carry execution into the map itself, but absent that override the
default output is decisions, not deliverables — the line that keeps
wayfinder's job distinct from `to-issues`'/`implement`'s further down the
chain.

## Tickets are tracker issues, blocked by the tracker's own dependency graph

A ticket's identity is now the tracker's own issue id, not a hand-picked slug,
and carries a `wayfinder:<type>` label naming its kind (below). Claiming moved
from a second label to the tracker's **native assignee**: a session claims a
ticket by assigning it to the driving dev, **before any work** — the same
write-before-work safety as before, but now the assignee field *is* the claim
(an open, unassigned ticket is unclaimed), so a second session reading the map
skips it without a bespoke label to maintain. Blocking now prefers each
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

## Field report: a hundred sessions feeding one map, and the map's shape in words

Days into using it to plan an entire course, Matt reports "closing in on 100
separate grilling/prototyping/research sessions" — a scale a single unbroken
context could never have held — "all contributing back to a central map that
grows as I learn more about the problem, shrinks as I find answers to the
questions," and names the result plainly: "the next evolution of `/grill-me`."
That grow/shrink pair is the fog-of-war and frontier-advance mechanics above,
restated as lived experience rather than design intent. He confirms one placement
detail directly, too: the map itself "sits in your issue tracker of choice" —
the tracker-native home described above, not a bespoke store — and that a
Prototype ticket resolves into exactly the kind of disposable artifact
`prototype-answer-is-the-artifact` describes: a course-editing session produced
"a modal I can open anywhere to edit the text of my courses with AI."

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-decision-mapping-SKILL.md-cdd9e8ec.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/in-progress/decision-mapping/SKILL.md (and revision 2026-06-24, origin https://github.com/mattpocock/skills/blob/846e8509f656adee303a5ea514a6830af4a962d6 — "Discuss" ticket type renamed "Grilling"; revision 2026-06-30, origin https://github.com/mattpocock/skills/blob/8258b0fa07254990b0d4d680ef28d353ef67788f — slug ids, `Status`, and the `Handoff` protocol; revision 2026-07-01, origin https://github.com/mattpocock/skills/blob/ac84e71c521d7636dc3db01ca36f0c167b6b39e2 — the `Task` ticket type, domain-agnostic framing, and the `## Notes` block)
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-06-17; revision 2026-07-02, origin https://github.com/mattpocock/skills/blob/00b0f60a9f2cea78216bc7165684bd5610495f9e — `decision-mapping` renamed `wayfinder`)
- `sources/mattpocock/skills-repo/skills-in-progress-wayfinder-SKILL.md-82165350.md` — origin: https://github.com/mattpocock/skills/blob/a5c124ef9cfecc39636f426cc4ff956580d6ea10/skills/in-progress/wayfinder/SKILL.md (the rename, and the map moving onto the issue tracker; revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/9ee274c8fecd74661dceee5ab4e314b8c58f9e47 — "refer by name" convention; revision 2026-07-04, origin https://github.com/mattpocock/skills/blob/8d45707bbe7c134eea25098b73085271a0c09370 — claiming moved from the `wayfinder:claimed` label to the tracker's native assignee; revision 2026-07-06, origin https://github.com/mattpocock/skills/blob/b70f59b0b2aa3a96dcc837adc3eacf238fedb556 — naming the destination as the first act of charting, the breadth-first frontier-mapping pass, and the map's `Not yet specified`/`Out of scope` split; revision 2026-07-07, origin https://github.com/mattpocock/skills/blob/2d3fffb7620883f23f0c0e9d47c87f7f9e173066 — the "Plan, don't do" framing and the HITL/AFK tag per ticket type)
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-gi-d3eb2123.md` — origin: https://github.com/mattpocock/skills/blob/81825ae44edc49c71a526b58a5225fde82f340fa/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md (revision 2026-07-02, the "Wayfinding operations" section added; revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/263a2d27d54d82e44d4587e6bbabd5833410c06b — the native issue-dependencies database-id detail; revision 2026-07-04, origin https://github.com/mattpocock/skills/blob/b9589cd45933b54e917e1f57a29278c751c1b297 — claiming moved from the `wayfinder:claimed` label to `--add-assignee @me`)
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-gi-586b767e.md` — origin: https://github.com/mattpocock/skills/blob/4dda53bfcb34d30f7d0a5024a07e0436fb9e5d79/skills/engineering/setup-matt-pocock-skills/issue-tracker-gitlab.md (revision 2026-07-02, the "Wayfinding operations" section added; revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/00ea3ba0cb738a2d723bfe28bf7a75419e1961d2 — the Premium/Ultimate-tier native-blocking caveat; revision 2026-07-04, origin https://github.com/mattpocock/skills/blob/e244acd60c9e370b1af0280a65be2b1ecc098f3e — claiming moved from the `wayfinder:claimed` label to `--assignee @me`)
- `sources/mattpocock/skills-repo/skills-engineering-setup-matt-pocock-skills-issue-tracker-lo-606b1b18.md` — origin: https://github.com/mattpocock/skills/blob/2f3267deb0afbb6f13294613a5f50e1b8df1156c/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md (revision 2026-07-02, the "Wayfinding operations" section added)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067965196618895564-c2d49f3d.md` — origin: https://x.com/mattpocockuk/status/2067965196618895564
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067602690725581067-eb6c35f9.md` — origin: https://x.com/mattpocockuk/status/2067602690725581067
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067682252742357292-b72bc2ce.md` — origin: https://x.com/mattpocockuk/status/2067682252742357292
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067682103030915278-5c57d5b4.md` — origin: https://x.com/mattpocockuk/status/2067682103030915278
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067710266230415567-f6fd1092.md` — origin: https://x.com/mattpocockuk/status/2067710266230415567
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067721635470147856-3d1433b6.md` — origin: https://x.com/mattpocockuk/status/2067721635470147856
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072388731969917328-d800daf2.md` — origin: https://x.com/mattpocockuk/status/2072388731969917328
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072391000706662641-b62e70a4.md` — origin: https://x.com/mattpocockuk/status/2072391000706662641
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072599827540578664-e1d5953f.md` — origin: https://x.com/mattpocockuk/status/2072599827540578664
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072601303927160997-f1b597a4.md` — origin: https://x.com/mattpocockuk/status/2072601303927160997
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072657344949887340-5a5aa0d0.md` — origin: https://x.com/mattpocockuk/status/2072657344949887340
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072657439535624674-895959d4.md` — origin: https://x.com/mattpocockuk/status/2072657439535624674
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072716979195326905-75e80d6b.md` — origin: https://x.com/mattpocockuk/status/2072716979195326905
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072743476765012080-b2165807.md` — origin: https://x.com/mattpocockuk/status/2072743476765012080
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072988266253406568-7bd4036c.md` — origin: https://x.com/mattpocockuk/status/2072988266253406568
