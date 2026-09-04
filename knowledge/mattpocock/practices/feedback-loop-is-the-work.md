# The feedback loop is the work

The third failure mode Matt targets is "the code doesn't work", and his answer is
that an agent without a fast pass/fail signal is flying blind. Across
`diagnosing-bugs` (formerly `diagnose`) and `tdd` the same conviction recurs:
constructing the feedback loop *is* the skill; everything downstream just consumes
its signal.

## Build the loop before hypothesising

`diagnosing-bugs` makes Phase 1 — building a feedback loop — the heart of the whole
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

The completion bar for Phase 1 is precise and self-policing: name **one command**
you have **already run at least once** (paste the invocation and output) that is
*red-capable* (drives the actual bug path and asserts the user's exact symptom —
not "runs without erroring"), *deterministic*, *fast*, and *agent-runnable*. "If
you catch yourself reading code to build a theory before this command exists, stop
— jumping straight to a hypothesis is the exact failure this skill prevents."

## The phases past the loop are mechanical — but each guards a specific failure

Once the loop exists the rest of `diagnosing-bugs` is a six-phase discipline where
every phase exists to head off a named mistake: **reproduce + minimise** (shrink
to the smallest scenario that still goes red, cutting one element at a time, so
the hypothesis space and the eventual regression test are both minimal);
**hypothesise** (generate 3–5 *ranked, falsifiable* hypotheses before testing any
— single-hypothesis generation anchors on the first plausible idea — and show the
list to the user, who often re-ranks it instantly); **instrument** (one variable
at a time, prefer a debugger/REPL over logs, tag every debug log with a unique
prefix like `[DEBUG-a4f2]` so cleanup is one grep, and *measure first* for perf
regressions where logs mislead); **fix + regression test** (write the test before
the fix — *but only if a correct seam exists*: a too-shallow seam gives false
confidence, and "if no correct seam exists, that itself is the finding" to hand to
architecture work); and **cleanup** (remove tagged instrumentation,
state the correct hypothesis in the commit message so the next debugger learns).
A later revision drops the phase's own "post-mortem" framing along with the
explicit final instruction to recommend an architectural change to
`/improve-codebase-architecture` once the fix is in — the checklist items
(repro gone, regression test present, instrumentation removed, hypothesis
recorded) are unchanged, but the skill no longer names the hand-off to
architecture work as its own closing step.

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

## Redact before you show the agent anything

The feedback loop `diagnosing-bugs` builds runs on commands, outputs, and
captured artifacts — and all three routinely carry secrets (auth headers,
tokens, credentials). A later revision makes **redaction the first move**,
ahead of Phase 1: write `<REDACTED>` in a secret's place, build loops against
env vars so the credential stays in the environment rather than in anything
shown to the agent, and when a captured artifact carries auth headers, quote
only the lines that carry the diagnostic signal rather than pasting it whole.
The Phase 1 completion criterion changed to match — "paste the invocation and
its output" now reads "show it redacted" — and the same rule extends to the
last-resort HITL escape hatch: when no loop can be built, the artifact the
skill asks the user for is a *redacted* capture, not a raw one. This is the
same "loop as a product" discipline turned toward safety rather than speed: a
tight feedback loop that leaks a credential into the agent's context isn't a
loop worth tightening, it's a loop worth fixing first.

## Red-green, one vertical slice at a time

`tdd` applies the same "signal first" stance to building, and its sharpest
opinion is an anti-pattern warning: **do not write all tests then all
implementation** ("horizontal slicing"). Tests written in bulk test *imagined*
behaviour — they verify the *shape* of things, pass when behaviour breaks, and
commit you to a structure before you understand it. The correct unit is a
**vertical slice / tracer bullet**: one test → one implementation → repeat, each
cycle informed by what the last one taught you. Tests must exercise behaviour
through public interfaces so they survive refactors; a test that breaks on an
internal rename was testing implementation. "Never refactor while RED." `tdd`'s
planning step no longer bundles its own deep-module notes — it now points at the
shared `/codebase-design` skill for interface-design and testability guidance
(see `codebase-design-deep-module-vocabulary`), a consequence of the
invocation-axis refactor that extracted reusable discipline into model-invoked
primitives.

The tracer-bullet principle propagates beyond testing: `to-issues` breaks plans
into thin vertical slices that each cut through every layer end-to-end, for the
same reason — a slice you can actually verify beats a layer you can't.

## Tautological tests: a second, sharper failure mode than implementation-coupling

`tdd` later names a failure mode distinct from testing implementation details:
a **tautological** test, where the assertion recomputes the expected value the
same way the code does — `expect(add(a, b)).toBe(a + b)`, a snapshot derived
by hand the same way the code derives it, a constant asserted equal to itself.
Such a test passes by construction and can never disagree with the code: break
the implementation wrong and the assertion breaks wrong right alongside it,
so it gives zero real confidence despite being green. The fix is the same
discipline good tests already need — the expected value must come from an
**independent source of truth** (a known-good literal, a worked example, the
spec), never a figure computed the way the code computes it. Implementation-
coupling and tautology are both ways a green suite lies, but by different
mechanisms: one breaks on a harmless refactor, the other never breaks at all.

## Seams are pre-agreed, and refactoring left the loop entirely

`tdd` also formalised the vocabulary for *where* a test lives: a **seam** is
the public boundary under test, and the rule is that **no test is written at
an unconfirmed seam** — the seams under test are written down and confirmed
with the user before the first test, not discovered test-by-test. This is the
same instinct as "you can't test everything": agreeing the seams up front is
what keeps testing effort on the critical paths instead of drifting to every
edge case as it's noticed mid-loop. Refactoring was also removed from the
red-green loop itself — it's now explicitly deferred to the **review** stage
(`code-review`, run at the end of `implement`) rather than folded into the
last step of every TDD cycle, so the loop stays exactly two states, red and
green, and cleanup happens once, downstream, against the whole diff rather
than piecemeal after each slice.

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

## RGR: the named answer to unnecessary agent "fixes"

Asked how to stop an agent from "fixing" things that never actually failed —
without forcing a failing test every single time — Matt's answer is a
three-letter compression of the whole discipline above: **"Yeah I use RGR"**
(red-green-refactor). The abbreviation names the same forcing function `tdd`
already encodes structurally (write the failing test, watch it fail for the
right reason, then make it pass) as the practical answer to a specific
symptom: an agent that "fixes" untested, unbroken code is an agent that
skipped red. He confirms this discipline lives in the `/tdd` skill itself, not
a system-prompt instruction — steering here is a reusable, model-invoked
procedure the agent runs, not a standing rule repeated in every prompt.

## Minimize test seams for agent effectiveness

Agents perform significantly better with fewer **test seams** — boundaries where
tests exercise different parts of the system. Single-seam testing (testing from
the outside by invoking the library or running the language) produces stronger
results than multi-seam approaches that test individual functions or mock
modules. More seams create test-implementation coupling and reduce confidence
that the whole system works together. While some apps resist single-seam testing
(requiring extensive service mocking), the principle holds: fewer seams mean
better agent outcomes.

## A renderer's real output is the wrong seam — test the contract instead

`course-video-manager`'s coding standards apply the single-seam principle to
a concrete, expensive case: **never write an automated test against a
Remotion renderer package's actual render output**, for any renderer package
that exists today or is added later. The reasoning is cost and signal, not
squeamishness — a real render boots Chromium, takes minutes, downloads a
browser on a cold machine, and asserts on pixels that a deliberate branding
change is *supposed* to move, so the test fails for the one reason that isn't
a bug. The fix isn't "don't test the renderer," it's picking a cheaper, more
stable seam one layer in: test the renderer's **props schema** (pure
validation, no Chromium — the contract every caller writes against) and the
**orchestration around the render** (the props a service builds, and the
arguments it spawns the renderer with, with the renderer faked at the process
boundary like any other external process). The actual visual "look" is left
to a human checking Remotion Studio, not a test. It's the same move
`diagnosing-bugs`' loop-construction menu applies generally: when the
literal, most-direct seam is slow, flaky, or expensive, move the seam to the
nearest boundary that's still deterministic and fast, rather than either
skipping the test or eating the Chromium cost anyway.

## Agreeing the seam is a planning-stage step, enforced downstream

Deciding *where* the seams are isn't left to whichever skill happens to write a
test — it's built into every stage of the planning chain, each with a different
job against the same agreed seam: `/to-spec` is where the seam gets agreed in
the first place; `/tdd` is told to only write tests at the seam already agreed,
not to invent new ones mid-implementation; `/code-review` checks after the fact
that only the agreed-upon seam was actually used; and `/improve-codebase-architecture`
is the escape hatch when the *codebase itself* makes good seams hard to reach —
it refactors specifically to make test seams better. The chain matters because
the failure it targets is specific: pushed by a user asking for a testing
policy to stop GPT writing "junk unit tests," Matt notes that a model left to
its own devices defaults to multi-seam testing — many small unit tests, mocks
included — where "mere humans" would default to fewer, higher-level tests
covering multiple behaviors. Agreeing the seam upstream and enforcing it at two
more points downstream is what makes the single-seam preference stick against
that default, rather than relying on a prompted preference the model quietly
drifts away from.

## Don't trust a review with no findings, and don't try to nail it in one pass

The RGR discipline above targets an agent "fixing" code that never broke;
a companion habit targets the human's *expectations* going into the review
step. Asked how to get AFK runs that don't surface multiple `/code-review`
findings, Matt rejects the goal itself: "I consider code review part of the
run. I.e. I don't consider findings during code review to be a bad thing." He
states the inverse just as plainly — "I don't trust reviews with no findings.
I never expect the code to be better than 80% after first coding pass" — a
clean review is a warning sign about the *review*, not evidence the
implementation pass was unusually good. Pushed on whether it's worth trying
harder to get everything right on the first run, his answer is that the
attempt backfires: "what's the point of trying? You'll just overload the first
run and lower quality" — piling more correctness pressure onto the
implementation pass degrades it rather than improving it, because it's
competing for the same context and attention the pass already needs.

The reasoning he gives for keeping the two passes separate is architectural,
not just habitual: "different circuits fire for impl vs verify. No need to
overload them." This is red-green-refactor's rationale one level up — RGR
already keeps writing code and verifying it as distinct steps within a slice;
this same split scales to the whole AFK run, where implementation is one pass
and `/code-review` (with its own separated Standards/Spec axes — see
`review-skill-two-axis-with-smell-baseline`) is the second, deliberately
different pass that's expected to find the ~20% the first pass didn't get to.

## Named boundaries: not a performance sweep, not the same pass as triage, and a redaction gap the fix didn't fully close

Three more limits `diagnosing-bugs`' docs page names explicitly, once it had
enough real usage to report them. It refuses to be a proactive performance
auditor: pointed at a whole codebase and asked "where are the bottlenecks",
the answer is no — the skill diagnoses one failure you can already name, its
performance branch establishes a baseline and bisects *from* a reported
symptom, and a proposal for the proactive sweep version was raised and closed.
It also doesn't dedupe against `triage`: triage's own verification step is
already "a shallow, bounded instance of diagnosing-bugs Phase 1–2," but
neither skill's file references the other, so running triage first gives you
most of Phase 1's raw material without the skill ever crediting or reusing it
— expect to redo the work properly here regardless. And the redaction fix
above (Phase 1's own completion criterion) doesn't reach everywhere a secret
can travel: the skill also asks the agent to request and paste *artifacts* —
HAR files, log dumps, core dumps — and none of those are sanitised by
instruction, so credentials and personal data can still ride along into a
chat, an issue, or a PR through that second door even after the first one was
closed. Treat redaction of anything beyond the Phase 1 command's own output as
your job, not the skill's, until that gap is addressed.

## Two open gates: over-firing on easy questions, and no checkpoint before the fix

`diagnosing-bugs` is heavy by design — six gated phases before a fix lands —
which makes it the wrong tool when it fires on something that didn't need it.
This is the most-reported problem with the skill: on models with a lower
activation threshold than the one it was calibrated against, a plain
description of a problem triggers the full discipline anyway, building a
reproduction scenario of limited value before answering a question the user
just wanted answered directly. The accepted fix — graduate to the heavy
version only once a lighter answer proves insufficient — hasn't shipped; the
practical workaround is saying "just answer this, don't diagnose" or disabling
model invocation for the skill. A second, structural gap sits later in the
loop: only Phase 3 (the ranked hypothesis list) has a human checkpoint. Nothing
gates the step *between* instrumentation and the fix, so the agent can start
writing the fix before the user has agreed the root cause is right — a request
for that gate is open and unaddressed.

`tdd`'s pre-agreed-seam rule decides *where* a test goes once you're inside the
red-green loop, but nothing in the skill decides *whether* a change deserves
the loop at all. Config, wiring, glue code, type annotations, and straight CRUD
delegation are a real, named, unfixed gap: run `tdd` on a change with no
independent source of truth to assert against, and the result is a test that
restates the implementation — the tautological anti-pattern above, arrived at
by picking the wrong change to test-drive rather than the wrong assertion.
Until that judgement is built in, it's the caller's call, or a line in
`CLAUDE.md`.

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

## Scope the local loop to what changed; know when red is the sandbox, not the code

`course-video-manager`'s testing convention narrows the loop from the whole repo
to just what's touched, because "the rate you can get feedback is your speed
limit" only holds if the loop stays fast as the suite grows. While iterating,
run only the specific test file(s) that cover the change, directly (`pnpm
--filter <package> test -- path/to/thing.test.ts`) — never a package's full
suite by hand. The full, unfiltered suite is CI's job, run on every PR, so
targeting locally never leaves a change actually unverified; it moves the
exhaustive pass to the check that runs regardless, freeing the interactive loop
to stay proportional to the diff instead of growing with the whole repo.

A named, environment-specific failure mode travels with the convention: known
PGlite flakiness under a sandboxed agent workspace's CPU load. A red result
from a loop running inside a resource-constrained sandbox can be the sandbox
contending for CPU, not a real regression — the same "diagnose the environment
before concluding the code (or the model) is wrong" instinct as
[[diagnose-environment-before-blaming-the-model]], applied specifically to test
infrastructure: before treating a local red as a bug, check whether the
environment running the loop is the actual cause.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-diagnosing-bugs-15a5eaa7.md` — origin: https://www.aihero.dev/skills-diagnosing-bugs
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-tdd-48650cc0.md` — origin: https://www.aihero.dev/skills-tdd
- `sources/mattpocock/skills-repo/skills-engineering-diagnose-SKILL.md-82a24dd7.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/diagnose/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-diagnosing-bugs-SKILL.md-175875ba.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/diagnosing-bugs/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-diagnose-scripts-hitl-loop.template.sh-7d00841a.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/diagnose/scripts/hitl-loop.template.sh
- `sources/mattpocock/skills-repo/skills-engineering-diagnosing-bugs-scripts-hitl-loop.templat-b79f1c8e.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh (revision 2026-08-07, origin https://github.com/mattpocock/skills/blob/efce423018fc6468a3239621f1c1bcaacc723801 — noting `capture` echoes its value to the terminal)
- `sources/mattpocock/skills-repo/skills-engineering-diagnosing-bugs-SKILL.md-175875ba.md` — origin: https://github.com/mattpocock/skills/blob/efce423018fc6468a3239621f1c1bcaacc723801/skills/engineering/diagnosing-bugs/SKILL.md (revision 2026-08-07 — the Redact section and the redacted Phase 1 completion criterion; revision 2026-08-16, origin https://github.com/mattpocock/skills/blob/8bf2b38ed1b90eca40024849f33206ecd095f2c3 — Phase 6 renamed "Cleanup" and the closing "recommend an architectural change" hand-off dropped)
- `sources/mattpocock/skills-repo/docs-engineering-diagnosing-bugs.md-c0888f15.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/diagnosing-bugs.md (revision 2026-08-06, origin https://github.com/mattpocock/skills/blob/c7726a74444dc1ab490fab108b5893cb06ed6dee — the "Common questions" section: the out-of-scope performance sweep, the unacknowledged overlap with `triage`, and the artifact-redaction gap)
- `sources/mattpocock/skills-repo/skills-engineering-tdd-SKILL.md-29d824ee.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/tdd/SKILL.md (revision 2026-06-17; revision 2026-06-30, origin https://github.com/mattpocock/skills/blob/dc338028858adc73f624ebdb5cda1dd9f61c5c17 — tautological tests; revision 2026-07-02, origin https://github.com/mattpocock/skills/blob/5eea6114412fce36e27f3cbf19a9bf1e25b76fb4 — pre-agreed seams and refactoring moved out of the loop; revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/ffef7e3e24c271fc7f7ac6fc43a2556e6c9269d9 — the reference to `code-review` by its new name)
- `sources/mattpocock/skills-repo/docs-engineering-tdd.md-54751a46.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/tdd.md
- `sources/mattpocock/skills-repo/skills-engineering-to-issues-SKILL.md-04f1cc54.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/to-issues/SKILL.md
- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/aihero/https-www.aihero.dev-tracer-bullets-0575e91a.md` — origin: https://www.aihero.dev/tracer-bullets
- `sources/mattpocock/aihero/https-www.aihero.dev-essential-ai-coding-feedback-loops-for--3a500e40.md` — origin: https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects
- `sources/mattpocock/aihero/https-www.aihero.dev-ways-ai-coding-has-rewired-my-brain-dc20954e.md` — origin: https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain
- `sources/mattpocock/aihero/https-www.aihero.dev-skill-test-driven-development-claude-co-70281ace.md` — origin: https://www.aihero.dev/skill-test-driven-development-claude-code
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2059955079067713960-179ae319.md` — origin: https://x.com/mattpocockuk/status/2059955079067713960
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082087683757629538-73357efb.md` — origin: https://x.com/mattpocockuk/status/2082087683757629538
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082092243360293212-4ec6cd9c.md` — origin: https://x.com/mattpocockuk/status/2082092243360293212
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082470683712360592-a931f9fa.md` — origin: https://x.com/mattpocockuk/status/2082470683712360592
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086089056711036949-a7b4b448.md` — origin: https://x.com/mattpocockuk/status/2086089056711036949
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086093679677034920-85117314.md` — origin: https://x.com/mattpocockuk/status/2086093679677034920
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086110209961828833-589d231b.md` — origin: https://x.com/mattpocockuk/status/2086110209961828833
- `sources/mattpocock/course-video-manager/.sandcastle-CODING_STANDARDS.md-7b893b74.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/CODING_STANDARDS.md (revision 2026-08-24, "Remotion renderer packages": never test actual render output, test the props schema and the render-orchestration boundary instead, leave the visual "look" to a human in Remotion Studio)
- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md (revision 2026-09-04, new "Testing" section: two-tier discipline — targeted test file(s) while iterating via `pnpm --filter <package> test`, full unfiltered suite runs in CI on every PR, and known PGlite flakiness under a sandboxed agent workspace's CPU load, per `docs/agents/testing.md`)
