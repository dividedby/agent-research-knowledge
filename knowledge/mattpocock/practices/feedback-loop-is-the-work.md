# The feedback loop is the work

The third failure mode Matt targets is "the code doesn't work", and his answer is
that an agent without a fast pass/fail signal is flying blind. Across `diagnose`
and `tdd` the same conviction recurs: constructing the feedback loop *is* the
skill; everything downstream just consumes its signal.

## Build the loop before hypothesising

`diagnose` makes Phase 1 — building a feedback loop — the heart of the whole
discipline and refuses to proceed to hypothesising without one. It offers a
ranked menu of loop constructions (failing test → curl script → CLI snapshot
diff → headless browser → replay a captured trace → throwaway harness → fuzz
loop → bisection harness → differential loop → HITL bash script as last resort),
ordered roughly from cheapest/most-deterministic to most-manual. Then it tells
you to **treat the loop as a product**: make it faster, sharper, more
deterministic. "A 30-second flaky loop is barely better than no loop; a 2-second
deterministic loop is a debugging superpower." For non-deterministic bugs the
goal isn't a clean repro but a *higher reproduction rate* — loop 100×,
parallelise, inject sleeps until the flake rate is debuggable.

When no loop can be built, the skill stops and says so explicitly rather than
hypothesising into the void — it asks for environment access, a captured
artifact, or permission to instrument.

## HITL bash script as the last resort feedback loop

When automated loops fail but human interaction is required, `diagnose` provides
a **human-in-the-loop (HITL) bash script template** that structures even manual
reproduction into a disciplined loop. The template (`hitl-loop.template.sh`)
defines two primitives: `step "<instruction>"` (shows instruction, waits for
Enter) and `capture VAR "<question>"` (reads human response into variable), then
outputs all captured values as `KEY=VALUE` pairs for the agent to parse.

This bridges the gap between "no automated feedback possible" and "staring at
the problem randomly" — the human still does the clicking/testing, but the
*sequence* is scripted, the *questions* are designed, and the *results* are
structured for the agent to reason about systematically. Even when automation
hits a wall, the loop discipline persists.

## Red-green, one vertical slice at a time

`tdd` applies the same "signal first" stance to building, and its sharpest
opinion is an anti-pattern warning: **do not write all tests then all
implementation** ("horizontal slicing"). Tests written in bulk test *imagined*
behaviour — they verify the *shape* of things, pass when behaviour breaks, and
commit you to a structure before you understand it. The correct unit is a
**vertical slice / tracer bullet**: one test → one implementation → repeat, each
cycle informed by what the last one taught you. Tests must exercise behaviour
through public interfaces so they survive refactors; a test that breaks on an
internal rename was testing implementation. "Never refactor while RED."

The tracer-bullet principle propagates beyond testing: `to-issues` breaks plans
into thin vertical slices that each cut through every layer end-to-end, for the
same reason — a slice you can actually verify beats a layer you can't.

## Tracer bullets are the antidote to slop

Matt's articles sharpen *why* the vertical slice matters with agents
specifically. LLMs are sycophantic: they want to please by producing a whole
finished feature in one leap — all the endpoints, models, middleware, auth —
and only *then* discover the database connection string was wrong. The Pragmatic
Programmer calls this "outrunning your headlights", and the result is slop: huge
chunks of code that need reworking and a crushing review burden. A **tracer
bullet** is the opposite — a tiny slice built end-to-end (e.g. one backend
endpoint wired to a *single* UI location), tested immediately, then expanded in a
fresh context window. The agent's default is to build big layers in isolation, so
you have to be explicit in the prompt to force it small. The discipline isn't new
(it's decades old) but "the principles apply *harder* to AI than they ever did to
humans": context-window limits make it non-negotiable, and **the rate you can get
feedback is your speed limit — never outrun your headlights.**

## Minimize test seams for agent effectiveness

Agents perform significantly better with fewer **test seams** — boundaries where
tests exercise different parts of the system. Single-seam testing (testing from
the outside by invoking the library or running the language) produces stronger
results than multi-seam approaches that test individual functions or mock
modules. More seams create test-implementation coupling and reduce confidence
that the whole system works together. While some apps resist single-seam testing
(requiring extensive service mocking), the principle holds: fewer seams mean
better agent outcomes.

## A feedback loop is a stack you build into the repo

For everyday building (not just debugging), the loop is concrete infrastructure
the agent triggers on every change: TypeScript/`tsc` ("essentially free feedback
… catches errors the AI would never find without testing in a browser"), unit
tests (Vitest), linting/formatting (ESLint + Prettier via lint-staged), and a
Husky **pre-commit hook that blocks the commit unless every check passes** — so
the agent literally cannot declare victory while the suite is red. Matt frames
friction (pre-commit hooks, CI, strong types) as *desirable*: the more immediate
the signal, the better the agent's next decision. The same humility that makes
great programmers distrust their own code, libraries, and colleagues applies to
agents — except "AI agents don't get frustrated by repetition", so they just
retry against the failing check until it's green. Letting the running dev server
be reachable (or a headless browser / Playwright MCP) extends the loop to the
frontend.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-diagnose-SKILL.md-82a24dd7.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/diagnose/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-diagnose-scripts-hitl-loop.template.sh-7d00841a.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/diagnose/scripts/hitl-loop.template.sh
- `sources/mattpocock/skills-repo/skills-engineering-tdd-SKILL.md-29d824ee.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/tdd/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-to-issues-SKILL.md-04f1cc54.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/to-issues/SKILL.md
- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/aihero/https-www.aihero.dev-tracer-bullets-0575e91a.md` — origin: https://www.aihero.dev/tracer-bullets
- `sources/mattpocock/aihero/https-www.aihero.dev-essential-ai-coding-feedback-loops-for--3a500e40.md` — origin: https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects
- `sources/mattpocock/aihero/https-www.aihero.dev-ways-ai-coding-has-rewired-my-brain-dc20954e.md` — origin: https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain
- `sources/mattpocock/aihero/https-www.aihero.dev-skill-test-driven-development-claude-co-70281ace.md` — origin: https://www.aihero.dev/skill-test-driven-development-claude-code
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2059955079067713960-179ae319.md` — origin: https://x.com/mattpocockuk/status/2059955079067713960
