# Subagents are good now: they can manage, not just work

Matt's stance on subagents flipped when their capability did. Subagents "were
nerfed before"; now you can treat them like regular agents — which means a subagent
can itself spawn subagents. Watching a subagent spawn its own subagent he calls
"unbelievably satisfying," and the point is precise: the unlock is that a subagent
can now become a good *manager*, not merely a good *worker*. Earlier, the nerf
meant delegating to a subagent gave you a capable doer that couldn't coordinate;
the lifted constraint is what makes nested delegation viable as a real
orchestration shape rather than a curiosity.

He does not read this as licence for unbounded depth. Pressed on how many layers
before the tree becomes an undebuggable mess, he doesn't dispute the failure mode
— he asks for a concrete example of where it actually went wrong, signalling the
risk is real but should be judged on evidence rather than assumed. The takeaway is
a capability update, not a depth recommendation: nested subagents are now a tool
worth reaching for, with the manager-vs-worker framing as the test for when an
extra layer earns its keep.

## The dictionary still states the default as one level deep

Matt's own AI Coding Dictionary defines Subagent plainly: "an agent spawned by
another agent via a tool call. Runs in its own session, reports a single tool
result. Cannot spawn further subagents." That's a live tension with the
capability update above, not a contradiction to resolve away — the dictionary
names the *default* harness behavior (most harnesses stop nesting at one level,
which is why watching one recurse further reads as remarkable), while the
Twitter thread is Matt reporting a specific, capable harness clearing that
default. Read the two together: assume one level of subagent nesting unless
you've verified your harness supports more, and treat deeper nesting as an
opt-in capability to confirm, not a baseline to build on.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065372560578003013-2736f0c6.md` — origin: https://x.com/mattpocockuk/status/2065372560578003013
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065374016328675609-b01859b6.md` — origin: https://x.com/mattpocockuk/status/2065374016328675609
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065376397862818212-a4512f4b.md` — origin: https://x.com/mattpocockuk/status/2065376397862818212
- `sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md` — origin: https://www.aihero.dev/ai-coding-dictionary
