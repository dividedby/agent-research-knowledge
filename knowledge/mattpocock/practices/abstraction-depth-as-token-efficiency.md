# A framework's hidden complexity is a token-efficiency lever, not just a DX one

Matt's heuristic for judging a framework: "the more secrets a framework can
hide, the more token-efficient it is — to a point, obviously." A framework
that resolves a whole class of decisions internally means less of that
decision-making has to be spelled out in the conversation with the model —
fewer tokens spent re-explaining context the framework could have owned. This
reframes "good abstraction" from a purely human-ergonomics property into a
cost line item: the abstraction boundary you'd pick for a clean API is the
same boundary that keeps an agent's context cheap.

The load-bearing claim is that this isn't two separate concerns that happen to
point the same way: "models and humans have the same needs. Leaky
abstractions are bad for both." An abstraction that leaks its internals forces
both a human reading docs and an agent reading context to hold the
implementation in their head anyway, defeating the point of hiding it — so
the threshold for "this framework hides enough, and no more than it should"
is roughly the same whether the consumer is a person or a model, not a
separate bar to tune per audience.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2100520338412945914-9d849473.md` — origin: https://x.com/mattpocockuk/status/2100520338412945914
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2100522132992053385-962d7fec.md` — origin: https://x.com/mattpocockuk/status/2100522132992053385
