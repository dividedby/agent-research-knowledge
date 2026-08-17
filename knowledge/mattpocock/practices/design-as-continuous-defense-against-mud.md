# Design as continuous defence against the ball of mud

Matt's fourth failure mode is the one agents make *worse*: because they
accelerate coding, they accelerate software entropy, so codebases turn into
balls of mud faster than ever. His counter is that software-design fundamentals
matter *more* in the AI age, not less — and that caring about design has to be
built into the everyday workflow rather than saved for a cleanup sprint.

## Depth is the design target everywhere

The same idea — **deep modules** (a lot of behaviour behind a small,
rarely-changing interface) versus shallow pass-throughs — shows up at every
stage, not just in refactoring:

- `to-prd` makes the agent sketch the modules to build *before* writing the PRD
  and "actively look for opportunities to extract deep modules that can be
  tested in isolation".
- `tdd` lists "identify opportunities for deep modules" and "design interfaces
  for testability" as planning-phase checkboxes, and "deepen modules" as a
  refactor move.
- `improve-codebase-architecture` is dedicated to finding **deepening
  opportunities** and is meant to be run "once every few days" as routine
  maintenance, not emergency surgery.

Testability and AI-navigability are treated as the same goal: a deep module's
interface is its test surface, and the same small interface that makes it easy
to test makes it easy for an agent to reason about.

## Prevent the class, don't just catch the instance

A sharper cut on the same thesis: **"Less 'let me write tests to catch the
next time that error happens' — more 'let me make that class of error
impossible with a better design.'"** A test only catches the specific bug you
already found; redesigning the interface so the bug's *shape* can't recur
closes off the whole category at once. His own before/after makes the
distinction concrete: bad is commenting the fix in prose ("I forgot to
include a file in the `sendTheseFilesToDocker` array"); good is removing the
place a human (or agent) could forget in the first place — "let's bundle
these files before we send them, that way any included file will be
automatically sent." Asked how to get agents to write good code the first
time, rather than needing this kind of fix applied after the fact, Matt's
answer is to move the habit upstream: "by baking this thinking into the
planning process" — the same "make errors structurally impossible" instinct
applied before code exists, not only after a bug surfaces.

## Firsthand account, and a caution about pointing at the skill by name

A field report matches the "routine maintenance" framing above: after
"vibing out" an app without ever looking at its internals, and getting scared
once things started going wrong, running `improve-codebase-architecture` felt
like "a lovely, warm bath of a skill" — the intended rescue path once
accumulated entropy becomes visible. But Matt adds a caution about how the
skill gets reached: if you explicitly hand the agent this skill's path as an
option, "it'll choose it way more often than it should" — the skill doesn't
reliably self-judge when nothing actually needs improving, so naming the path
too readily biases the agent toward reaching for it even when the codebase
doesn't warrant a pass.

Matt confirms his own trigger matches the field report rather than a fixed
cadence: asked whether this is what he opens on an older codebase or something
he runs regularly to keep a newer one tight, his answer is a feeling, not a
schedule — "I use it basically whenever I start feeling terrified about the
internals of my app." The "once every few days" framing above is the routine
default; in practice the actual signal that fires it is the same loss-of-
confidence moment the field report describes.

## Do it right or do it twice

Pressed on the "go fast vs. go straight" trade-off — the observation that more
developers are choosing speed (more code, faster) over the fundamentals because
it feels better in the moment — Matt names the tax up front: "this is the same
conversation we've been having for years. Do it right or do it twice." Skipping
the design discipline doesn't remove the cost, it defers it: get it wrong the
first time and you spend more time cleaning up than the shortcut saved. He ties
the aphorism directly to agent output quality, not just human effort: "if your
codebase is easier to make changes in, you'll get better results from agents" —
the same claim as "the codebase out-votes the prompt" below, restated as the
reason cutting corners is self-defeating specifically *because* an agent is
doing the next round of work in whatever state you left the codebase in.

## The codebase out-votes the prompt

Matt's blunt claim: your codebase — far more than your prompt or `CLAUDE.md` — is
the biggest influence on an agent's output. "If you have a garbage codebase, the
AI will produce garbage within that codebase." Two forces explain it. First,
**AI has no taste for software architecture**: it sees a flat web of shallow,
mutually-importing modules with no groupings, and your mental map of the system
isn't visible to it. Second, **the repo wins** any conflict with your
instructions — you can write "never use `any`" but if `any` is strewn through the
code, the agent follows the thousands of lines of evidence over the few lines of
rule. Agents *amplify what they see*, so entropy compounds: a human commits once
or twice a day, an agent can pile dozens of low-quality commits in hours. The
defence is to keep the codebase clean *before* turning an agent loose and to make
quality bars explicit (prototype vs production vs public-API repos behave
differently, and the agent can't tell which it's in unless told).

## Grey-box modules: own the interface, delegate the inside

The deep-module idea gets an operational name in Matt's writing: the **grey-box
module**. You carefully design and test a module's interface, then hand its
*implementation* to the agent — you *can* look inside to apply taste or tune
performance, but as long as the tests at the boundary pass you don't have to.
This is what makes large AFK delegation safe: you hold seven or eight chunks in
your head instead of hundreds of interrelated files, the agent manages what's
inside each, and cognitive load drops. Give each module its own folder with a
clear public interface so the file system advertises the structure — "progressive
disclosure of complexity", the interface on top, implementation a level down.
(TypeScript makes these boundaries hard to enforce, which is why Matt reaches for
Effect's services as ready-made deep modules.)

## Make the agent zoom out

A second, lighter design habit: before touching unfamiliar code, get the agent
to go *up* a level of abstraction and map the relevant modules and callers in
the project's own vocabulary (`zoom-out`). Understanding a change in the context
of the whole system is positioned as a precondition for not making the mud
worse.

## Fix architecture after the bug, with information

`diagnose` closes the loop back to design: after a fix lands, it asks "what
would have prevented this bug?" and, if the answer is architectural (no good
test seam, tangled callers, hidden coupling), hands off to
`improve-codebase-architecture` *with specifics*. Crucially the recommendation
comes **after** the fix — when you know the most — not as upfront speculation.

## Endorsement: you can't tell an agent to be clean, you have to measure it

Matt amplified a point from Robert "Uncle Bob" Martin (`@unclebobmartin`) that
restates his own thesis from the outside, in response to Martin noting that
skyrocketing agent adoption seemed to be undercutting sales of his own *Clean
Code*-adjacent writing: **"You can't tell an agent to be clean. You have to
measure the cleanliness that they produce and have them correct failures of
cleanliness… Without such constraints agents are more than happy to build big
balls of mud that they can't maintain."** This is Martin's framing, credited to
him — Matt's own addition is a one-line aside about book sales for *A
Philosophy of Software Design* — but it converges exactly with "the codebase
out-votes the prompt" above: a prose instruction to be clean doesn't survive
contact with an agent that has no taste for architecture; what has to exist
instead is a measurable gate the agent is held to.

## Sources

- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/skills-repo/skills-engineering-to-prd-SKILL.md-c9420806.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/to-prd/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-tdd-SKILL.md-29d824ee.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/tdd/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-zoom-out-SKILL.md-4adec2ab.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/zoom-out/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-diagnose-SKILL.md-82a24dd7.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/diagnose/SKILL.md
- `sources/mattpocock/aihero/https-www.aihero.dev-how-to-make-codebases-ai-agents-love-1ba6d0b5.md` — origin: https://www.aihero.dev/how-to-make-codebases-ai-agents-love
- `sources/mattpocock/aihero/https-www.aihero.dev-ways-ai-coding-has-rewired-my-brain-dc20954e.md` — origin: https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain
- `sources/mattpocock/aihero/https-www.aihero.dev-tips-for-ai-coding-with-ralph-wiggum-440a70a9.md` — origin: https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082528210319745433-082a8d65.md` — origin: https://x.com/mattpocockuk/status/2082528210319745433 (repost/quote-tweet: point credited to Robert "Uncle Bob" Martin/@unclebobmartin, amplified by Matt)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086830429416333758-6512adaa.md` — origin: https://x.com/mattpocockuk/status/2086830429416333758
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086836045354541074-7f7ed73c.md` — origin: https://x.com/mattpocockuk/status/2086836045354541074
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086924475153449317-957eecb9.md` — origin: https://x.com/mattpocockuk/status/2086924475153449317
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086838432102228008-9622d53f.md` — origin: https://x.com/mattpocockuk/status/2086838432102228008
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086839443084701816-39a08c9d.md` — origin: https://x.com/mattpocockuk/status/2086839443084701816
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086879498679484471-c84ba2ba.md` — origin: https://x.com/mattpocockuk/status/2086879498679484471
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088172162641170923-dee95946.md` — origin: https://x.com/mattpocockuk/status/2088172162641170923
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088885540288442462-b2b15b80.md` — origin: https://x.com/mattpocockuk/status/2088885540288442462
