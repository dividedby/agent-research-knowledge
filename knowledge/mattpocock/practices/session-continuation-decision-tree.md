# At a phase boundary: continue, clear, handoff, subagent, or compact

When you reach the end of a chunk of work, the choice of what to do with the
session isn't binary (compact vs handoff, as `keep-the-agent-in-the-smart-zone`
frames it) — Matt names five live options and the decision between them: keep
going in the current session, `/clear`, `/handoff`, spin up a subagent, or
`/compact`. The crux he keeps landing on, restated simply: **if the context is
still relevant, compact it; if it isn't, clear it.** Handoff and subagent are
narrower escapes for cases plain compact/clear don't cover.

## "Phase" and "phase boundary" are the units this decision keys on

A **phase** is "a chunk of work in a session" — deliberately fuzzy, not a fixed
token count or a formal milestone. A **phase boundary** is the point where you
notice "ok, we're done with that" — even a grilling session counts as its own
phase. The boundary is what gives you room to choose: once you're at one, "you
have much more flexibility" than mid-phase, because the work in flight is
complete enough that compacting or clearing doesn't cost you unfinished
progress.

## Compacting mid-phase is the failure mode

The one move to avoid is compacting or clearing *before* a phase boundary:
"usually compacting mid-phase is really bad" — the summary is built from an
unfinished thought, and the next session inherits a half-formed picture rather
than a clean handoff point. When you're stuck mid-phase and the smart zone is
running out anyway, the alternative isn't to compact anyway — it's to
**continue** in the current (now dumb-zone) context, or to **split the
remaining work off to a subagent** instead of contaminating your compact
point. This is also why deciding *when* to compact is worth doing
deliberately rather than on a token trigger alone: reaffirming the ~150K
smart-zone number, Matt pairs it with "you could compact early and probably
should — though only when you've reached a phase boundary." Compacting early
is fine; compacting mid-phase isn't.

## `/clear` vs `/compact`: different mechanisms, not synonyms

The two are often conflated but do different things:

- **`/clear` starts a genuinely new session with no state retained** — "in
  Claude Code in the terminal, clearing a session is the same as creating a
  new session." Nothing carries forward automatically.
- **`/clear` doesn't destroy the old session** — you can still resume the
  previous session afterward through the session picker; clearing just stops
  using it as the active thread, it doesn't delete its history.
- **`/compact` seeds the new session with a summary** of the old one — this is
  the mechanical difference that makes it the right choice when the context
  is still relevant: you get continuity without keeping the actual accumulated
  tokens (see `context-compression-and-handoff-mechanics` for the primary/
  secondary-source trade-off this involves).

## Exceptions and adjacent decisions

- **Teeny changes don't need ceremony.** For a change too small to bother
  compacting for, just continue in the current session even in the dumb zone —
  the discipline is proportional to the task, not a rule to apply uniformly.
- **`/handoff` is for specific, narrow needs, not the default fork.** Reach
  for it only if you're swapping to a new harness, swapping directory, or
  need to act mid-phase — unless you need one of handoff's specific features
  (like the portability of a plain markdown file across tools), plain
  `/compact` covers the rest.
- **Whether to spawn a subagent is its own decision tree**, separate from
  (and answered inversely to) the compact/clear/handoff choice — a question
  Matt flags as worth keeping distinct rather than folding into the same
  tree, since asking "should I compact?" and "should I spawn a subagent?" at
  the same point in a session tend to have opposite answers.
- **Naming the decision changed the behavior.** After drawing the whole tree
  out explicitly, Matt reports compacting manually "a LOT more" than before —
  organizing the reasoning surfaced compaction opportunities that were easy to
  miss when the choice wasn't made explicit.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079879414297330146-94b9c271.md` — origin: https://x.com/mattpocockuk/status/2079879414297330146
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079882858655535402-da913fb1.md` — origin: https://x.com/mattpocockuk/status/2079882858655535402
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079887646403280928-35192e3e.md` — origin: https://x.com/mattpocockuk/status/2079887646403280928
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079892366786277377-9912df37.md` — origin: https://x.com/mattpocockuk/status/2079892366786277377
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079892900175864207-758665d8.md` — origin: https://x.com/mattpocockuk/status/2079892900175864207
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079893804039942502-f6e174a8.md` — origin: https://x.com/mattpocockuk/status/2079893804039942502
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079900046875631713-9721e05c.md` — origin: https://x.com/mattpocockuk/status/2079900046875631713
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079900522853626241-fcfc8976.md` — origin: https://x.com/mattpocockuk/status/2079900522853626241
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079901836845154532-3cf7439c.md` — origin: https://x.com/mattpocockuk/status/2079901836845154532
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079902001354158183-2f15d836.md` — origin: https://x.com/mattpocockuk/status/2079902001354158183
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079919043780214917-4fcd7f2a.md` — origin: https://x.com/mattpocockuk/status/2079919043780214917
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080191683279360079-346ffcca.md` — origin: https://x.com/mattpocockuk/status/2080191683279360079
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080274002967204310-64aada10.md` — origin: https://x.com/mattpocockuk/status/2080274002967204310
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080274176359768263-455a24e2.md` — origin: https://x.com/mattpocockuk/status/2080274176359768263
