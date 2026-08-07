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
