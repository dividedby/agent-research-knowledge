# Agents erode team coordination silently — the tower doesn't fall, it just keeps rising

Ronacher's Tower of Babel reading: the biblical story isn't really about pride,
it's about coordination. The builders' power came from a shared language — a
common understanding of what things mean, where boundaries are, which
invariants matter, who owns what. Take that away and construction *stops
immediately*. That's the reassuring part of the myth: loss of shared
understanding is self-announcing.

His claim about AI-assisted engineering is that it breaks this reassurance. A
software project's "shared language" was never English or the programming
language — it's the common mental model of the system: concepts, boundaries,
invariants, ownership, the reasons the system has the shape it does. That
model was rarely written down; it was maintained by *friction*. Before agents,
changing someone else's storage layer meant reading their code, asking them
questions, coordinating with a dependent team. Much of that friction was pure
waste, but not all of it — some of it was the mechanism by which your
understanding became theirs, and by which you both discovered whether you
still agreed on how the system worked.

Agents remove that friction. One person asks an agent to add OAuth, another
asks one to add caching, a third asks one to rebuild the database and "make
the UI pink" — each change reasonable in isolation, code compiling, tests
passing, explanations generated on demand — and nobody has to talk to anybody
else, or acquire the part of the shared model the change would previously have
forced on them. Ronacher's line: agents don't feel pain, only humans do, so
agents now let people act in parts of a system where they'd previously have
needed other humans — and where those humans would have synchronized.

The dangerous asymmetry with the biblical Babel: there, losing the common
language stopped construction. In agent-assisted engineering, **construction
keeps going after shared understanding has already collapsed** — every
developer has a tireless local translator that can explain and alter any
corner of the tower on demand, so the architectural language that would let
the humans reason about the system *together* can disappear while the tower
keeps visibly, successfully rising. There's no failure signal to notice, which
is what makes it a genuine risk rather than mere metaphor-mongering: teams find
out only when someone needs the whole picture and discovers nobody has it.

This is the team-scale complement to [[you-are-the-bottleneck]] (which is
about *individual* accountability holding even as writing speed explodes) and
sits alongside [[the-harness-level-loop]]'s warning that hands-off loops make
single codebases less comprehensible over time — here the same mechanism plays
out across people instead of across iterations: coordination, not
comprehension, is the thing quietly lost.

## Sources
- `sources/ronacher/blog/https-lucumr.pocoo.org-2026-7-13-the-tower-keeps-rising-faeb5936.md` — origin: https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/
