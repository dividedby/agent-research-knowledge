# Boundary objects must serve human legibility, not agent convenience

The artifacts that mediate between humans and agents — plans, prompts, skills,
AGENT.md files — are **boundary objects** in the sense Star and Griesemer coined
the term: things different parties (here, human and agent) each read through
their own lens, that only work if they're built to make sense on both sides.
Today's agent boundary objects fail this test: they're walls of Markdown
optimised for what the agent can produce and consume cheaply, and humans are
expected to adapt to that format rather than the reverse. The asymmetry is
severe — a human reads at roughly 240 words a minute, an agent writes at roughly
4,500, a 19x mismatch — so the human is structurally the bottleneck in an
exchange designed around the faster party's native format. Text is precise and
expressive but a narrow channel; humans have half a billion years of visual,
spatial, and social cognition to draw on and only five thousand years of
writing, so route decisions through the channel humans are actually built for —
visual, interactive, manipulable, and social (shared, debatable, multiplayer) —
instead of defaulting to more prose.

A second, complementary fix: don't ask the human to evaluate options they can't
picture — bring reality into the plan *before* presenting the decision. Rather
than a CLI asking "crisp, soft, or pronounced shadows?" as abstract text, wire
the decision to the live app so the human can manipulate the actual shadow and
see it change in place. For decisions too abstract to visualize directly
(architecture, retry-logic syntax), don't predict the outcome in prose — dispatch
subagents to fully implement each option on separate branches, then report back
comparative, measured evidence (call-site coverage, which changes are mechanical
vs. behaviour-altering, P95 latency) instead of a guess. Either way, the goal is
the same: replace "imagine the consequences of this text description" with
"look at, manipulate, or compare the actual outcome," because that's the kind of
decision a human can actually make well. The agent should absorb the extra labor
of building the boundary object richer — that trade is the point, since agent
labor is comparatively cheap and human decision-quality is the scarce resource.

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-planning-agents-1b47b34a.md` — origin: https://maggieappleton.com/planning-agents/
