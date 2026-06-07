# Verify against your mental model, don't read every line

There's a spectrum from "never look at the code" to "review every line the agent
writes," and Ball plants himself deliberately in the middle: **you don't have to
know every line — but you do have to test.** His working method: before the agent
starts, he knows (a) what he wants the resulting code to do and (b) how he'll test
that it does exactly that. Once the agent declares done, he "tests" in every sense
of the word — unit tests, manual browser checks, running a command, inspecting the
database, a curl — across the happy path, the sad path, the edge cases, with
existing data, no data, real data, fake data, and with an eye to what's different
in production. Sometimes he asks the agent itself how to manually verify what it
just did and to walk him through it.

The load-bearing move: **once he's tested something and compared its behavior to
his mental model of how it's supposed to work, the code itself becomes less
important.** He still spot-checks for insanity (less and less of a problem with
newer models) and runs a fixed mental checklist — where/how is data stored, does
this box us in for future changes, security, does it touch functionality I hadn't
considered. But beyond that: does he know every line? "Not if I don't have to."

Verification effort scales with **blast radius**, not uniformly: code at the heart
of a system warrants more than peripheral code. And the strength of the loop
depends on the strength of your test — the harder it is for the agent to "do the
job badly," the more you can trust the output, which is why the verification
discipline and the design of executable checks (tests, oracles, types,
conventions) reinforce each other.

A caveat Ball flags as the loop tightens: as models one-shot bigger features
correctly, you may need *less* feedback, not just faster feedback — "why put
training wheels on someone who never wobbles?" The verification stays, but its
shape keeps changing.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-71-9d01a5bf.md` — *Joy & Curiosity #71* intro: "do you have to know every line?"; testing in every sense; code becomes less important once tested against the mental model; blast radius (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-71)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-87-9c595687.md` — *Joy & Curiosity #87*: feedback loops are changing; "why put training wheels on someone who never wobbles?" (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-87)
