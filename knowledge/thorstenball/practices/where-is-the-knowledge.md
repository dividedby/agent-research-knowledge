# Where is the knowledge?

Ball's diagnostic for *why* an agent sometimes nails a task and sometimes flails:
**it depends on where the knowledge required to do the task well is encoded.**
There are three places it can live — your prompt, the codebase, or the model's
training data — and things go fine when all the knowledge the task needs is in at
least one of them. Things go badly when there's a **gap**: you wrongly assumed the
agent would know something that is in *none* of the three.

The examples make it concrete. A button's hover state doesn't fire on hover: easy,
because everything needed is present — the problem is in the prompt, the code
explains what the button is, and "what a hover state is" is in the training data.
Now flip it: a bug you can't even *describe* (you don't know how to explain the bug
or the desired state) — not good. Or: you ask for a feature assuming the agent will
add it "over here and over there," but the codebase actually allows fifteen other
ways and the training data doesn't say those fifteen are bad — not good.

The practical move is to **ask "where is the knowledge?" before and during a task,
then put the missing piece where the agent can reach it.** Sometimes the codebase
already carries it through types, tests, or conventions; sometimes the training
data does (there's only one blessed way to add a Rails / Next.js / SvelteKit
endpoint). But if it's in neither, *you* have to put it in the prompt. This is the
same insight that underlies his paint-by-numbers practice — supplying the missing
"statements" — viewed as a routing question rather than a hand-coding one.

The "put it in the prompt" branch has an upstream precondition: **you can only put
knowledge in the prompt if you possess it yourself.** Watching his 9-year-old edit
video in iMovie, directed only by "cut out the part where you see my hand," Ball
realized she'd never be able to ask an agent for a J-cut or a jump cut — she's seen
those effects on screen a hundred times but doesn't know the words for them. No
increase in agent capability closes that gap; only the person's own vocabulary can.
The same ceiling applies to software: sometimes you can't describe a bug or a
feature crisply not because the codebase or training data lacks the answer, but
because you haven't yet learned the domain's vocabulary yourself — which makes
"where is the knowledge?" a question to ask of yourself first, before the agent.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-80-065f0c03.md` — *Joy & Curiosity #80* intro: "Do you know how it should work? Does the agent? Or does the codebase?"; the prompt/codebase/training-data theory and the knowledge gap (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-80)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-91-055a0420.md` — *Joy & Curiosity #91* intro: the iMovie anecdote — his daughter can't ask an agent for a J-cut or jump cut because she doesn't know the vocabulary, though she's seen the effect; "that, of course, made me think about software engineering" (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-91)
