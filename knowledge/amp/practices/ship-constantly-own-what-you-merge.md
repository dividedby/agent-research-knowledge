# Ship constantly, own what you merge

Amp's internal operating principles for a team building an agent in a fast-moving
field. The throughline: optimize for **speed**, because everything is changing
constantly and slowness means falling behind — but pair speed with hard
**ownership** so velocity doesn't degrade into mess.

The principles:

- **Constant shipping over big releases.** No task longer than a week; ship to
  production every week (worst case two). "Hours and days over weeks and months."
  Prototypes over RFCs and discussions.
- **You merge it, you own it.** No code review for core committers — but owning
  means you make it work, keep fixing it, and are responsible for it. The flip
  side is the real constraint: *don't merge what you can't own.* One person per
  project; get help, but you alone are accountable.
- **Speed is a design constraint, not just a pace.** Keep surface area small
  (fewer features that do more; when in doubt, no feature), and from the start
  ask "how will we debug this?" and "how easy is it to remove?".
- **Build for where the puck is going,** not where it is.
- **Dogfooding is a superpower.** Ship, use, iterate. Everyone talks to customers
  (be in the Discord), and everyone promotes their work — the product is how you
  sell it, not only marketing's job.
- **Bugs first.** Fixing bugs takes priority over everything else.
- **Peer accountability.** Promise what you'll do this week publicly; deliver, or
  publicly break the promise next week. People choose what to work on — better
  they ship what they want than not ship what you want.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-how-we-build-05ca09e2.md` — origin: https://ampcode.com/notes/how-we-build
