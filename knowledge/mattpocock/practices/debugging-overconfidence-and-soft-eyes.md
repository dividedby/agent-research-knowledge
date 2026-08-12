# Debugging overconfidence: agents narrate false certainty, so push back with "soft eyes"

Agents debugging a hard problem exhibit a classic "bad developer" trait: they
get hopeful, and their language escalates well before the evidence justifies
it — "we're getting closer," "this is the decisive piece of information,"
building to "we've eliminated all possible hypotheses" or "this is the
definitive fix." The confidence of the narrative outruns the confidence the
evidence actually supports, and unless someone interrupts it, the agent
commits to a wrong conclusion (declaring an "upstream bug," treating a
hypothesis as ruled out when it isn't) instead of continuing to look.

## The fix is one line: "don't jump to conclusions yet"

Matt's countermeasure is procedural, not a rewrite of the investigation:
"Pull back. Don't jump to conclusions. Soft eyes." In a live example, an
agent's debugging session ran out of hypotheses and declared the bug an
"upstream" issue outside its control — a classic exit ramp for overconfident
narrative debugging. Told simply "don't jump to conclusions yet," it kept
looking and solved the bug two turns later. The intervention supplies no new
information; it just refuses to let the agent's own narrative substitute for
evidence that hasn't actually been exhausted.

## The gap this leaves in `/diagnosing-bugs`

Matt names the skill that should own this discipline — `/diagnosing-bugs` —
and flags that it doesn't yet encode the "soft eyes" push-back: "it doesn't
yet have this 'soft eyes' approach. Need to add that." A structured debugging
skill can still miss a purely conversational failure mode like narrative
overconfidence if nothing in it explicitly interrupts the agent's own
escalating certainty.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086770919423258707-68e18662.md` — origin: https://x.com/mattpocockuk/status/2086770919423258707
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086772810521714851-8565f985.md` — origin: https://x.com/mattpocockuk/status/2086772810521714851
