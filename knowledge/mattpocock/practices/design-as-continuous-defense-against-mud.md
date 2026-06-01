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
