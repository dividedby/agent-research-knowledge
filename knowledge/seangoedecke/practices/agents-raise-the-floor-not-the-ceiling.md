# Coding agents compress team output by raising the floor, not the ceiling

Software engineering ability is heavy-tailed: the strongest engineers produce
outsized useful output, while the weakest are often actively net-negative,
creating problems colleagues have to spend time cleaning up. Coding agents change
this specifically at the bottom of the distribution — not by making weak
engineers good, but by making their worst-case output survivable.

**What agents reliably catch is a bounded, mechanical class of error.** Try to
deliberately introduce obvious mistakes while working with a coding agent — a
cache key that isn't user-specific, an infinite loop that might never terminate,
a leaked open file — and the agent pushes back hard. That class of error used to
define a net-negative engineer's pull requests: something that could never
possibly work, or would cause immediate, obvious problems. With an agent in the
loop, the worst realistic output shifts to "wrong in some ways, baffling in
others, but functional at the line-by-line level" — a real improvement in the
floor.

**What agents still miss is the systemic, contextual class.** Subtle errors that
require understanding other parts of the codebase go through, because that's
exactly the kind of error an agent's local, mechanical checking doesn't reach.
The floor rises because agents are reliable on local correctness; the ceiling
doesn't move, because good judgment about a system as a whole is still a human
skill agents don't substitute for.

**The organizational consequence:** a colleague who is effectively "relaying
your Slack messages into a coding agent and pasting back the response" is a real
category now, worth treating as functionally equivalent to reviewing that
agent's output directly — awkward and slower than working with a strong engineer
directly, but strictly better than working with the same weak engineer's
unassisted output, because more compute thrown at a problem beats less, however
badly mediated. The one adjustment this forces: since a human reads what you
write even when an agent is doing the work, curt or hostile prompting habits
have to be dropped.

**The self-check that keeps this from overgeneralizing:** strong engineers don't
show this pattern. Even lazy or sloppy strong engineers retain enough baseline
taste to catch an agent's obvious errors before they ship. "Becoming a thin
wrapper around a coding agent" is a phenomenon specific to engineers for whom
that wrapper is already an improvement on their unassisted output — not a
general trend to expect across a team.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-ai-makes-weak-engineers-less-harmful-48921ced.md` — origin: https://seangoedecke.com/ai-makes-weak-engineers-less-harmful/
