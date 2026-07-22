# Instrument the wire, not the harness

The harness (Claude Code, or any CLI wrapper) is not the thing you're actually
answering to — the model provider's raw request/response wire format is. Matt's
practical move when a harness disappoints him: **"Proxy Claude Code so you see
what gets sent to the model,"** then take whatever's worth keeping from that
captured traffic and feed it into a different harness (his example: Pi). The
harness stops being an opaque black box you're stuck evaluating on vibes and
becomes one implementation choice among several reading and writing the same
wire protocol — so "is this harness good?" turns into an answerable, inspectable
question instead of a brand-loyalty one. ("IMO Claude Harness is not that great,
you can do a great job with pi.")

## Why this is worth building deliberately, not just using once to debug

The same request logger shows up as a first-class teaching tool in Matt's
upcoming course, and he names three payoffs that go beyond one-off debugging:

- **Demystifies the mechanics.** Reading the raw stuff sent to Anthropic/OpenAI
  "makes all the mechanics completely clear: sessions, context window,
  model/harness boundary" — concepts that stay abstract when you only see the
  harness's rendered chat UI become concrete once you see the literal payload.
- **Instills context paranoia.** Once every token riding along on every request
  is visible, "it's easy to see waste" — the same discipline behind
  `token-economics-as-a-cost-lever`'s logging-proxy technique, but aimed at
  building the habit rather than just finding one expensive line item.
- **Empowers building your own harness.** Seeing the wire format strips the
  vendor's magic away — "all the magic disappears" — which is what makes
  swapping to (or building) a different harness a live option instead of a
  leap of faith. He calls the logger itself "really simple to build," which is
  the point: the harness's value-add is thinner than it looks once you can see
  underneath it.

The instinct generalises past this one course tool: any layer that intermediates
between you and a model is worth being able to bypass and inspect directly,
because the wire format — not the wrapper's opinions about it — is the actual
interface you and the model share.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079153661322686630-f4ff308f.md` — origin: https://x.com/mattpocockuk/status/2079153661322686630
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079193858190041399-12dfe71a.md` — origin: https://x.com/mattpocockuk/status/2079193858190041399
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079501025434550624-79510ade.md` — origin: https://x.com/mattpocockuk/status/2079501025434550624
