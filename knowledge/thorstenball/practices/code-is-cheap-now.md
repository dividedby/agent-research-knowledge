# Code is cheap now — and that changes one constant in a fundamental equation

The reframe Ball preaches most insistently: we now have buttons that emit hundreds
or thousands of lines of working code in seconds, and **this is not "just another
code generator."** A single constant in a very fundamental equation has changed —
code is no longer hard-to-find, only-in-some-places, hard-to-extract. His oil
analogy: if someone learned to turn rainwater into oil, oil would still be oil and
some things wouldn't change (you still need refineries, contracts, safety), but the
*industry* — built around scarce, hard-to-extract oil — would be upended, and the
bottleneck would move through it, kicking over everything downstream. Software is
the same: most of what we built (GitHub's shape, open-source norms, the
ticket→PR→review→merge flow) rests on the assumption that **code is expensive**, and
most of that stops making sense when code is cheap. The need to do proper
engineering doesn't go away; almost everything else is up for grabs.

The flip side is a sharp line between practitioners who've "walked through the
one-way door" and those who haven't — and Ball's diagnosis of the latter is itself
practice advice, a checklist of what *using agents well* requires:

- **An agent is not ChatGPT copy-paste.** Pasting to and from a chat window is not
  equivalent to an agent that can run commands and *use feedback loops*. If you
  haven't given the agent the ability to run commands (via an `AGENTS.md` or
  similar), you haven't seen what it can do.
- **Use the frontier models, and spend on them.** Local models on your own hardware
  don't tell you the trajectory; judging the tech by them is judging the wrong end.
- **Prompt like you mean it.** "Fix it" is not a prompt; of course you'll be
  unimpressed by what it returns.
- **Stop judging the output by how *you'd* have written it.** Twenty years of "code
  must be Clean and Good and Formatted because humans read it" is worth re-examining
  when you can ask a model to explain any code to you on demand — and when the
  primary reader is increasingly an agent. Optimize the codebase for agents even at
  some cost to human developer experience (his own UUIDs-are-ugly aesthetic
  objection lost to "agents will read far more UUIDs than I ever will").
- **Take your hands off the wheel long enough to see where it goes.** Have the agent
  write tests, run them, modify the code, run them again — *without* you reading
  every line — and watch the loop carry further than you expected.

The recommended way to actually internalize this: throw problems of many sizes and
types at the models, in many environments, with *open eyes* — you won't get a fair
look if you don't push them hard in every direction.

A further corollary Ball draws out explicitly: cheap code creates a category of
**invisible software** — apps built entirely for yourself that never ship, because
the cost of generalizing a personal tool (packaging it, documenting it, supporting
it) now exceeds the cost of building it in the first place. He had Amp write him
"many hundreds of lines" of a personal tool he has no plan to publish — not because
it isn't useful, but because nobody will ever see that code unless he chooses to
show it. And released software isn't safe from the same math either: if a small
paid app took an hour or six to build, a hundred competitors can rebuild it in
thirty minutes, so cloneability — not scarcity — sets the price, and prices for
anything that easily replicable trend toward zero.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-72-67188f9a.md` — *Joy & Curiosity #72* intro: the disconnect between people who "get it" and those who don't; agent-vs-ChatGPT, frontier models, prompting, AGENTS.md, judging code by human standards, taking hands off the wheel (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-72)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-73-e7187f0c.md` — *Joy & Curiosity #73* intro: optimize for agents over humans even at the cost of developer experience (the UUIDs anecdote) (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-73)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-78-d865b504.md` — *Joy & Curiosity #78* intro: the rainwater-into-oil analogy; "all of it was built on the assumption that code is expensive" (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-78)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-75-32551187.md` — *Joy & Curiosity #75* intro: "invisible software" — personal Amp-built tools too costly to generalize to ever release; cloneability crashing prices for small paid apps (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-75)
