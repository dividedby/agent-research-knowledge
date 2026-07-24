# Split the plan: a spec for the destination, tickets for the journey

For big chunks of work, Matt recommends splitting a single plan document into
two: a **spec** (where you're going) and **tickets** (the steps on the journey
there). The split exists to make a specific failure cheap: plans change
mid-implementation, and a monolithic plan doc conflates "what we're building"
with "what's left to do," so a change of direction forces you to untangle both
at once. Keeping them separate means you can pivot the destination without
re-deriving the whole journey.

## The procedure when the plan changes

If you discover mid-implementation that the destination itself needs to
change: edit the spec, delete every ticket that hasn't been completed yet, and
create new tickets from the revised spec. Completed tickets stay as a record;
only the unwalked path gets thrown away and re-derived — because the spec, not
any individual ticket, retains the destination.

## Ticket-sizing and the point of clearing between them

Each ticket is scoped to **one coding session**. That sizing is what makes
clearing context between tickets safe and cheap: because the spec (not your
head, not the previous ticket's session) is what retains the destination, you
can `/clear` between tickets without losing the plan — or `/compact` instead
if you'd rather not double-pay for re-exploring the codebase from scratch.
**Clearing context between each ticket is the main, load-bearing benefit of
`/to-tickets`** — routing tickets through something that skips this (e.g. a
`/goal` command that keeps rolling context forward) throws away exactly the
property that makes the split worth doing.

The skills for this are `/to-spec` and `/to-tickets`, both in Matt's public
skills repo. The normal sequencing is to run `/to-tickets` immediately after
`/to-spec`, in the same session — you don't need a fresh session to make the
jump from destination to steps. The one exception is when the tracker is
GitHub issues specifically: there, clearing or starting a new thread before
`/to-tickets` is worth doing, likely because writing tickets as GitHub issues
benefits from a clean context rather than one still carrying the spec-writing
conversation.

## Why this pairs naturally with AFK agents

The `/to-spec` / `/to-tickets` split "plugs into an AFK agent beautifully":
because each ticket is a self-contained, one-session unit of work anchored to
a durable spec, an AFK agent can pick up a ticket cold, complete it, and stop
— the same shape `durable-briefs-for-afk-agents` describes for issue-tracker
briefs, arrived at here from the planning side rather than the brief-writing
side.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079926515257520400-ce5571da.md` — origin: https://x.com/mattpocockuk/status/2079926515257520400
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079926855788855524-9cb40b6e.md` — origin: https://x.com/mattpocockuk/status/2079926855788855524
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079926961313345825-47140eae.md` — origin: https://x.com/mattpocockuk/status/2079926961313345825
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079952609419407431-e86145f7.md` — origin: https://x.com/mattpocockuk/status/2079952609419407431
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079999765350171119-255baf64.md` — origin: https://x.com/mattpocockuk/status/2079999765350171119
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080000544102375889-1d1b71fa.md` — origin: https://x.com/mattpocockuk/status/2080000544102375889
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080001909486682311-76073172.md` — origin: https://x.com/mattpocockuk/status/2080001909486682311
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080183646254752194-41f4e9ad.md` — origin: https://x.com/mattpocockuk/status/2080183646254752194
