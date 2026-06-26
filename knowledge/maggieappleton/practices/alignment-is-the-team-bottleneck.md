# Alignment is the team bottleneck

Single-player agent tooling optimises the wrong thing. The "one developer, two
dozen agents" dream assumes software is made by one person — but software is a
team sport, and **there is limited value in scaling up an individual**. More
individual output doesn't solve problems that require everyone to communicate and
coordinate; it makes them worse ("nine women make a baby in one month" logic).

When implementation is fast, cheap, and rising in quality, the hard question is
no longer *how* to build it but *should* we build it. Agreeing on what to build
becomes the new bottleneck. Alignment was always a bottleneck on teams, but
agents raise the *cost of being unaligned*: the window between logging an issue
and an agent opening a PR collapsed to minutes, so the conversations, draft PRs,
and Slack checkpoints that used to spread alignment across a slow implementation
phase no longer have time to happen. Worse, most agent "plan mode" is local and
unshared — you don't even check the plan with your team before shipping it off.
The poor pull request is left carrying all the alignment weight at the very end,
when it's too late, which is not what PRs were ever designed to do.

The failure modes are concrete: **wasted work** (features nobody asked for;
critical feedback arriving after you've built the wrong thing) and **coordination
debt** (merge conflicts from multiple agents touching the same files, two
engineers assigning agents to the same feature, giant stacks of context-free PRs
to review).

Two structural claims follow. First, **PRs and issues are the wrong primitives**
for the speed, shape, and volume of agentic work — a heretical-sounding but
widely-held view even inside GitHub. Second, **most alignment context isn't in
the codebase — it's in people's heads**: business and financial constraints,
political dynamics of who decides, product vision, user-research insight,
organisational history. Agents can't discover this on their own, so tools must
get humans to share it early and naturally, without piling on process. The remedy
is to make alignment continuous and *shared* — planning, context-gathering,
decision-making, and development under one roof — so teams align *before* agents
start working, not after. (For the prototype that operationalises this, see
artifacts/collaborative-multiplayer-agent-workspace.)

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-zero-alignment-2cbd2b48.md` — origin: https://maggieappleton.com/zero-alignment/
