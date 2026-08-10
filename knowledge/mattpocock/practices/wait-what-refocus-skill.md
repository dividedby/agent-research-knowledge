# Passive instructions don't change tone; an active refocus skill does

A steering instruction sitting passively in a system prompt or `CLAUDE.md`
rarely changes how verbose or jargon-heavy a model's output reads — "a passive
instruction never does that much to alter output tone." Matt's fix wasn't a
more forcefully worded instruction; it was to stop trying to steer tone
ambiently and instead ship an **actively invoked** skill, `/wait-what`,
reached for in the moment output is confusing rather than hoped to hold across
a whole session by default.

## What it does: refocus into domain language, simplified

`/wait-what` takes confusing model output and restates it in the user's own
domain language, simplified using ASD-STE100 (the aerospace industry's
Simplified Technical English standard) — a concrete, borrowed
vocabulary-discipline rather than a vague "be clearer" instruction. It exists
for "when you have no clue what the agent is saying."

## Confirmed: neither CLAUDE.md nor an output style reproduces it

Matt later tested the passive-instruction claim above directly rather than just
asserting it. He pasted `/wait-what`'s content into both `CLAUDE.md` and a
custom output style and reports the same result either way: "this didn't work.
Not as CLAUDE.md, nor as an output style. Still spamming `/wait-what` on Opus
5." Pressed on what "didn't work" means precisely, he clarifies it made *no
difference to the default output* — not a partial improvement, no change at
all. A correspondent pushed back that output styles work "like a charm" for
them; Matt's answer was to stand by the original result rather than concede
the counterexample — though pressed on whether it categorically doesn't work,
he adds a caveat rather than a flat claim: "Not for me, but I am but a small
sample size," treating his own result as one data point, not a universal
verdict. The one-shot version still earns its keep despite the
friction of invoking it every time — "`/wait-what` is effective at a one-shot
response, which is mostly all you need, but it is very frustrating" to have to
call it out explicitly instead of it just holding by default.

He also declined the obvious automation fix — wiring `/wait-what` to fire via a
hook after every response — despite otherwise favoring deterministic hooks over
prose rules elsewhere in his workflow: "I consider that way too aggressive, I
would find that really annoying." The active-invocation requirement isn't a gap
he wants automated away; a refocus tool that fires on demand, when output is
actually confusing, is the design, not a stopgap for a hook that hasn't been
built yet.

## An underrated use: pointed at the codebase, not just the chat

The skill generalizes past its original purpose. Matt names three prompts
that turn it into a code-archaeology tool rather than a chat-clarifier:
"`/wait-what` is this module doing," "`/wait-what` happened since I last
looked in this file," "`/wait-what` is that bit of syntax." A user's
testimonial confirms the payoff is real, not theoretical: running it on a
legacy auth file "saved me digging through git blame to find why some random
wrapper existed" — the same refocus-into-plain-language move that clarifies a
confusing agent reply works just as well pointed at confusing code the agent
didn't even write.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2084941367659168064-78315c94.md` — origin: https://x.com/mattpocockuk/status/2084941367659168064
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2084985277102031137-a06755bf.md` — origin: https://x.com/mattpocockuk/status/2084985277102031137
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085283315896979793-8eca86c8.md` — origin: https://x.com/mattpocockuk/status/2085283315896979793
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085287196420886988-6bb72ec2.md` — origin: https://x.com/mattpocockuk/status/2085287196420886988
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085681281795232026-fd37c36a.md` — origin: https://x.com/mattpocockuk/status/2085681281795232026
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085684200221323432-590b17ba.md` — origin: https://x.com/mattpocockuk/status/2085684200221323432
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085712712185597975-334ea952.md` — origin: https://x.com/mattpocockuk/status/2085712712185597975
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085716654525161573-822edf43.md` — origin: https://x.com/mattpocockuk/status/2085716654525161573
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085721799724007737-4e32d2f1.md` — origin: https://x.com/mattpocockuk/status/2085721799724007737
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085734075713700297-dac76242.md` — origin: https://x.com/mattpocockuk/status/2085734075713700297
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085738402612146329-4fa560b1.md` — origin: https://x.com/mattpocockuk/status/2085738402612146329
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085746196467929466-dc44abc9.md` — origin: https://x.com/mattpocockuk/status/2085746196467929466
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085772378584351013-f82641ac.md` — origin: https://x.com/mattpocockuk/status/2085772378584351013
