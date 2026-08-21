# AI ate tactical programming; your skill is the ceiling on its output

Matt frames the AI-era division of labour with John Ousterhout's vocabulary from
*A Philosophy of Software Design*: **tactical programming** is the day-to-day
writing of code; **strategic programming** is long-term code design, architecture,
and planning. His claim is sharp and repeated — AI has *eaten* tactical
programming, but it is bad at strategic. The work that used to take an engineer
from junior to senior (planning, QA, codebase design, figuring out *what* to
build) is no longer optional seniority polish; in this era it is table stakes,
because the tactical layer it used to sit on top of is now commoditised. He's
compressed the same split into a reusable aphorism, batted back at someone
else's "Engineering is for the machines, design is human": "Tactics for the
bots. Strategy for the people."

## The skill ceiling: your level multiplies, it doesn't get bypassed

The load-bearing principle is that **your skill level acts as a ceiling for the
agent** — so every skill you gain multiplies your output, and there has never been
a better time to "git gud." Asked whether coding is still worth learning, Matt's
answer is unequivocally yes: the people who think the model lets them skip skill
acquisition are overvaluing the one skill AI replaced (writing the code) and
undervaluing the ones that always mattered (figuring out what to build,
architecture, planning).

He pushes back hard on the "I shipped things beyond my technical ability, so skill
doesn't matter" argument: the act of building those projects *was* skill
acquisition — abilities that were shaky in the first project and developed across
later ones. That someone improved while shipping is evidence *for* the ceiling
claim, not against it. (A correspondent's refinement is worth recording: skill may
be better read as the *floor/foundation* — what you can demand, judge, integrate,
and ship — than a hard ceiling on what the agent can produce; Matt's frame holds
that the human's strategic judgement is still the binding constraint on quality.)

## Don't wait for the model to fix your problems

The corollary is a stance against passivity. "Instead of waiting for a new model
to fix your problems, why not just fix your problems." Matt's analogy: he once
told himself he wouldn't get a driving licence because self-driving cars would
get good — and was wrong to wait. Don't defer your own skill development against a
hoped-for future model; the leverage is available now, gated only by what you can
do. This is the motivating worldview behind his `/teach` skill — its whole pitch
is closing the junior-to-senior strategic-skills gap that AI has *not* eaten.

## Get good at the thing, not just at coding

The ceiling claim generalizes past software specifically: "If you want to get
good at using AI, GET GOOD AT THE THING YOU'RE USING IT FOR." The skill that
bounds output quality is domain skill in whatever you're building, not
narrowly "programming ability" — the same logic that makes a strategic
engineer's judgement the constraint applies to any subject matter an agent is
pointed at. Matt names an explicit, achievable bar rather than mastery:
"learn enough to be dangerous" — "good enough to be dangerous" is offered
directly to someone worried they're only "mediocre at 50 different things,"
reframing breadth-without-depth as still clearing the bar that matters,
because the bar isn't expertise, it's enough working knowledge to judge and
steer the agent's output.

That bar has a behavioral corollary: don't dumb down your input to the level
you imagine a novice would use. Asked whether he should simplify his prompts
to something a less-experienced person could write, Matt's answer is
"Definitely not, treat it as a subject matter expert" — the fix for feeling
under-qualified isn't writing vaguer prompts, it's building the domain
knowledge that lets you talk to the model as one expert to another. His
`/teach` skill (see `stateful-teaching-workspace`) is the concrete mechanism
he points people at when asked how to build that "get good at the thing"
knowledge deliberately rather than by accident.

## "We are all engineering managers now" — and that role still reads the code

Matt names the tactical/strategic split with a job-title analogy: "we are all
engineering managers now. Strategists, not tacticians." Pressed on what that
concretely obligates you to do — a correspondent's gloss was "you should be
able to understand the code that is written, you should be inspecting critical
sections, AIs are wrong at times, it's a tool" — Matt affirms it and turns the
claim back on the objector: "what do you think an engineering manager does?"
An EM doesn't write every line, but they still read the code their reports
ship and are accountable for it; the analogy is doing real work here, not just
decoration — it's naming the *specific* obligation (inspect, understand,
catch what's wrong) that "strategist, not tactician" leaves implicit.

That's also why Matt "strongly disagrees" with the more sweeping claim that
"the specification is permanent, the implementation is disposable... dev is so
cheap now, because it is disposable." His own practice does treat *some* code
as disposable — prototypes are explicitly throwaway (see
[[small-adaptable-not-process-owning]]) — but that's a narrow, deliberate
exception scoped to code built solely to answer one design question, not a
general claim that shipped implementation no longer needs to be understood or
maintained. Read together with the engineering-manager framing, the objection
is the same one: if the human's job is to inspect and understand what ships,
implementation can't be fully disposable — someone still has to be able to
read it.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065500685362237868-fec632ae.md` — origin: https://x.com/mattpocockuk/status/2065500685362237868
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065499079283470810-a7d8c8d1.md` — origin: https://x.com/mattpocockuk/status/2065499079283470810
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065517703733875079-e5a9ad9e.md` — origin: https://x.com/mattpocockuk/status/2065517703733875079
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065524412082970996-0ba4848d.md` — origin: https://x.com/mattpocockuk/status/2065524412082970996
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065529469989789852-470c49d9.md` — origin: https://x.com/mattpocockuk/status/2065529469989789852
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065548496753565885-38363aae.md` — origin: https://x.com/mattpocockuk/status/2065548496753565885
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065063650797277665-999504f4.md` — origin: https://x.com/mattpocockuk/status/2065063650797277665
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065501043685802385-2493e51e.md` — origin: https://x.com/mattpocockuk/status/2065501043685802385
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2064663221718425660-cdf72b78.md` — origin: https://x.com/mattpocockuk/status/2064663221718425660
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080995054043193661-7b3eaca4.md` — origin: https://x.com/mattpocockuk/status/2080995054043193661
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081103551141499289-e670b4d8.md` — origin: https://x.com/mattpocockuk/status/2081103551141499289
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081103647702724772-78154770.md` — origin: https://x.com/mattpocockuk/status/2081103647702724772
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083853702696231097-a8b1e896.md` — origin: https://x.com/mattpocockuk/status/2083853702696231097
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083855409958302147-281b2be3.md` — origin: https://x.com/mattpocockuk/status/2083855409958302147
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083883100702949626-236c94ad.md` — origin: https://x.com/mattpocockuk/status/2083883100702949626
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083933709971988567-8b631fa9.md` — origin: https://x.com/mattpocockuk/status/2083933709971988567
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083934253440549174-0a655ccf.md` — origin: https://x.com/mattpocockuk/status/2083934253440549174
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090419774161383714-4cc14a02.md` — origin: https://x.com/mattpocockuk/status/2090419774161383714
