# Contributor Trust Bottleneck

When an open-source project becomes popular, the influx of agent-generated PRs —
"everyone just slinging their clanker without a lot of thought" — forces a
deliberate bottleneck on merging. Rather than accepting the firehose, Zechner
concentrates reviews into dedicated OSS time, throttling intake to a pace a human
can actually reason about.

The gate loosens only as specific individuals earn trust as contributors, not as a
blanket policy. Trust is the scarce resource governing what agent-authored
contributions get in: a known contributor's PR clears faster because the human has
been vetted, not because the diff looks plausible. Plausible is exactly what agent
output is best at producing, which is why surface review doesn't scale — you have
to gate on the person behind the contribution. Design your review cadence around
throttling slop until human trust is established.

This is the maintainer-side mirror of [[stay-in-the-loop-not-agent-armies]]: the
human reviewer is the rate-limiter that keeps agent output from compounding into
mess. On the authoring side you stay in the loop so your own agents don't run away
from you; on the receiving side you become the loop for everyone else's. In both
cases the constraint is the same — a human's bandwidth to understand and trust is
the real bottleneck, and pretending otherwise just defers the mess to whoever
maintains the project next.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-04-08-ive-sold-out-8c1d96ed.md — https://mariozechner.at/posts/2026-04-08-ive-sold-out
