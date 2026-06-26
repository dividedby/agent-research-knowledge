# Design is the new bottleneck

When agents write all the code, implementation stops being the constraint and
**design, planning, and taste become the limiting factor**. A stack of agents
churns through implementation plans faster than a human can produce good ones —
so you have to do a *lot* of design and planning just to keep the engine fed.

The work that remains is the work agents cannot do for you: imagining what to
build, architecting it, deciding what it should feel and look like, choosing the
right metaphor, sequencing the highest-priority features, and judging whether
what got built is any good. These require human context, taste, preferences, and
vision — the parts that don't compress into a prompt.

This reframes the danger of fast agents. Because prompting is so cheap, it's easy
to "get ahead of yourself," stumbling into stacks of generated functions that
should never have been prompted into existence because they don't render your
actual intentions. The footgun of hands-off agentic development is that you can
move so fast you never stop to think — burning a billion tokens in exchange for a
pile of architectural debt you didn't design. Gas Town is held up as the
cautionary case: not just vibe-coded but *vibe-designed*, a stream of
consciousness converted directly into code, complicated "not because [the author]
wanted it to be" but because components kept getting bolted on until it barely
worked.

The corollary is where leverage now lives. As software production gets cheap, the
pressure shifts to the other parts of the pipeline — thoughtful design, critical
thinking, user research, planning, deciding what to build and whether it was
built well. The most valuable tools in this world won't be the ones that generate
the most code fastest; they'll be the ones that help you think more clearly, plan
more carefully, and hold the quality bar while everything accelerates. And the
practical implication for an individual practitioner: the *capabilities overhang*
is enormous — even if model progress stalls, we are far behind in using what
already exists, so pick any slice and you'll find low-hanging fruit.

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-gastown-31a465e3.md` — origin: https://maggieappleton.com/gastown/
- `sources/maggieappleton/blog/https-maggieappleton.com-zero-alignment-2cbd2b48.md` — origin: https://maggieappleton.com/zero-alignment/
- `sources/maggieappleton/blog/https-maggieappleton.com-now-2026-01-a588650f.md` — origin: https://maggieappleton.com/now-2026-01/
