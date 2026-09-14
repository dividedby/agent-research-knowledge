# Test agent-friendliness by spawning agents who don't know what you're testing

To find out whether a codebase (and its `AGENTS.md`) is actually discoverable
to an agent, don't ask an agent whether it's agent-friendly — spawn fresh,
unbriefed agents at a nearby task and watch whether they stumble onto the
thing you built for them, without being told it exists. A self-report from an
agent that already knows the answer isn't a test; a blind agent's spontaneous
behavior is.

Ball's own prompt (Joy & Curiosity #99): spawn three agents into three
separate orbs and give them ordinary-sounding work — "add new database
queries or something" — deliberately chosen so they'd ideally end up needing
the database-performance-testing tool he'd just built, but withhold that the
tool exists or that `AGENTS.md` changed. The orchestrating agent then closes
the loop itself: it checks the sub-agents' transcripts to see whether they
actually found and used the tool, reports back honestly when some of them
didn't, and proposes revising `AGENTS.md` and re-running with fresh agents
until they do.

Why this matters: it reframes "agent-friendliness" as a property of the
codebase and its documentation that has to be deliberately engineered and
verified, not something that emerges by giving a single agent free rein.
Responding to Armin Ronacher's skepticism about software factories that let
the model manage its own context and record findings in a free-form
`agent-notes` folder, Ball stakes out the opposite position explicitly: "I
think agent-friendliness is a real property of a codebase you have to build
towards and I don't think just letting the model decide it all is the best
way to go about it." The blind multi-agent test is how that building-towards
gets actually verified — the same iterate-until-verified discipline this
corpus already documents for correctness, aimed instead at documentation and
discoverability — and withholding the information from the sub-agents is
what makes it a real test rather than a staged demo.

It's a familiar loop shape running one level up: the artifact under test is
`AGENTS.md`/tool discoverability, the "test" is other agents' unprompted
behavior, and the loop (test → observe a miss → patch the doc → retest) runs
automatically because the orchestrating agent both spawns and audits its own
subordinates.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-99-9fa8651f.md` — Joy & Curiosity #99: the "spawn three agents in three orbs, don't tell them about the tool or the AGENTS.md change" prompt, checking sub-agent transcripts and revising AGENTS.md; his reply to Armin Ronacher's "Astra for Coding" arguing agent-friendliness must be deliberately built, not left to the model (origin: https://registerspill.thorstenball.com/p/joy-and-curiosity-99)
