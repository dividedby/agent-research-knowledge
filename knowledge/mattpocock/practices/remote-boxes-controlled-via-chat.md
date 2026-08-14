# Move agent execution off the laptop; buy the box, don't build it

With his AI Coding course shipped, Matt names his next infrastructure project in
one line: "the next week is all about personal infra — getting all my agent
interactions off my PC and into remote boxes, controllable via Discord." The
target isn't a specific skill or prompt but the execution environment itself —
where the agent runs, not what it's told to do — moving from a laptop-bound
session to a persistent remote host reachable from chat.

## Buy the sandbox provider, don't build one

Asked what provider he's using, his answer is a single word — "Daytona" — and
when a correspondent describes something adjacent as "an interesting facade
for ECS tasks," he draws the line explicitly: **"I'm buying, not building
atm."** This is a narrower stance than his usual bespoke-integration instinct
(see `personal-software-optimized-integration`): the *workflow* on top stays
custom, but the sandbox-provisioning layer underneath is exactly the kind of
undifferentiated infrastructure he'd rather pay a provider for than build
himself. He applies the same reasoning to the chat-control layer: aware of
Hermes, an existing Discord-agent tool a correspondent is already running,
he calls it "a bit bloated" rather than adopting it outright — evaluating
someone else's off-the-shelf option on its merits before deciding whether to
buy that piece too or build the thinner version himself.

## The outcome: custom-built, not Hermes

The Hermes evaluation named above resolved to build, not buy. Summing up the
finished remote-agent setup, Matt writes "My IDE is Discord" — the chat
surface has fully replaced a normal editor as where he drives agent work, not
merely a notification layer on top of one. Asked directly whether that setup
runs on Hermes, the existing Discord-agent tool he'd called "a bit bloated,"
his answer is flat: "No, custom" — he built the thinner version himself
rather than adopting the off-the-shelf option.

## Named trade-offs he's accepting up front, unresolved

Two constraints a correspondent raised against running agents from a
persistent remote box, Matt accepts rather than solving preemptively:
outbound web requests from a server IP get blocked more than requests from a
home connection, and iOS development needs a simulator that can't run on a
UNIX box (the correspondent's reason for going back to a Mac running 24/7).
Matt's answer to both is to defer, not design around them: "If the IP thing
becomes an issue I'll figure it out. I don't do iOS dev." The second
constraint doesn't apply to his own workflow; the first he's choosing to
learn from actually hitting rather than architecting against speculatively —
consistent with treating infra decisions the same way he treats model/effort
choices elsewhere: evaluate empirically once the cost is real, not by
reasoning from a hypothetical worst case.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086104430412181587-3053369f.md` — origin: https://x.com/mattpocockuk/status/2086104430412181587
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086106175402025468-c59afab6.md` — origin: https://x.com/mattpocockuk/status/2086106175402025468
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086106829814194412-bab8be6a.md` — origin: https://x.com/mattpocockuk/status/2086106829814194412
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086107289669226977-477c172d.md` — origin: https://x.com/mattpocockuk/status/2086107289669226977
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086112433165250852-21226b49.md` — origin: https://x.com/mattpocockuk/status/2086112433165250852
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087555290174566491-b495025d.md` — origin: https://x.com/mattpocockuk/status/2087555290174566491
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087556320073289829-4ad641e7.md` — origin: https://x.com/mattpocockuk/status/2087556320073289829
