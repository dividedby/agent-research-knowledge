# Review as two independent axes, never merged

The `code-review` skill (shipped out of `in-progress` and renamed from
`review`) checks a diff against a fixed comparison point along **two
deliberately separate axes** — Standards (does the code follow this repo's
documented conventions?) and Spec (does the code faithfully implement the
originating issue/PRD?) — and refuses to merge or rerank their findings into
one list. The reason is structural: a change can pass one axis and fail the
other (code that's spec-perfect but breaks house style; code that's clean but
implements the wrong thing), and collapsing them into a single ranked list
would let one axis mask the other. Each axis runs as a **parallel sub-agent**
so their findings can't cross-pollute, then the skill aggregates by
presenting both reports side by side under their own headings — the same
fan-out-then-compare shape `codebase-design`'s DESIGN-IT-TWICE uses for
interface alternatives, applied to review instead of design.

Graduating out of `in-progress` gave it a fixed home in the main build chain,
now `grill-with-docs → to-prd → to-issues → implement → code-review`:
`implement` drives `tdd` internally for the red-green loop, then closes out
by running this skill as its own final gate before committing. Refactoring
itself moved with it — `tdd`'s red-green loop explicitly excludes refactoring
now, deferring it to this review stage instead (see
`feedback-loop-is-the-work`). Matt confirms this chain directly when asked
whether a skill can act as post-generation critique: "Yeah, my `/implement`
skill calls `/code-review`" — the review isn't something a user has to
remember to invoke separately, it's wired into the end of implementation
itself.

## Spec discovery is a fallback chain, and the tracker dependency is now hard

The **Spec** axis doesn't ask the user where the spec lives; it looks in a
fixed order — an issue reference in the commit messages, a path the user
passed as an argument, a PRD/spec file under `docs/`/`specs/`/`.scratch/`
matching the branch or feature name — and only asks the user if all three come
up empty, at which point (if there truly is no spec) it skips the axis and
says so rather than inventing requirements. Because that lookup leans on the
project's issue tracker, `code-review` now carries the same explicit
hard-dependency pointer as `to-issues`/`to-prd`/`triage` — *"The issue tracker
should have been provided to you — run `/setup-matt-pocock-skills` if
`docs/agents/issue-tracker.md` is missing"* — joining that tier (see
`setup-seeded-config-and-dependency-tiers`). The **Standards** axis needs no
such setup: its Fowler baseline (below) works in a repo with zero configured
conventions.

## Preconditions are checked before spawning, not inside the sub-agents

The fixed point (a SHA, branch, tag, or `main`) is confirmed to resolve and
the diff confirmed non-empty *before* the two sub-agents are spawned — a bad
ref or empty diff fails at the top level, not silently inside two parallel
sub-agents where it would be harder to diagnose. This is the same "fail fast,
at the seam, before delegating" instinct that shows up elsewhere in the
collection wherever an orchestrator hands work to sub-agents it can't easily
watch mid-run.

## A fixed Fowler smell baseline backstops undocumented repos

The Standards axis doesn't rely solely on what a repo happens to document. It
carries a **baseline set of twelve classic code smells** (Fowler,
*Refactoring* ch. 3 — Mysterious Name, Duplicated Code, Feature Envy, Data
Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent
Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest)
that applies even when the repo's own standards docs say nothing. Two rules
keep the baseline from overriding local judgement: **the repo always wins** —
where a documented standard endorses something the baseline would flag, the
smell is suppressed — and **the baseline is always a judgement call**, labelled
("possible Feature Envy") rather than asserted as a hard violation, unlike a
documented-standard breach which can be reported as hard. Each smell is
written as a *what it is → how to fix* pair so a sub-agent can pattern-match
it against a hunk and immediately propose the remedy, not just name the smell.

The lesson generalises past this one skill: a review or lint pass that only
checks what a repo happens to have written down is only as good as that
repo's documentation discipline. A fixed, portable baseline plus an
explicit "documented standard overrides baseline" rule gives useful signal on
day one of a project with zero conventions written down, while never
fighting a repo that's made a deliberate, documented, different choice.

## Why a generic review skill is hard — and why a bare prompt isn't enough

Matt names the structural limit of any *shared, generic* review skill directly:
"writing a generic 'review' skill is really, really hard — mostly because it
really needs a custom set of curated standards for that project. And once
you've done that, you might as well just run your own review agent." The
Fowler baseline above is exactly the fallback for the gap this creates — it's
what a generic skill can offer *before* a project has curated its own
standards — but the real value, in his own account, comes from the
project-specific Standards axis, not the portable one: "my `/code-review`
does a bit of generic review (mostly through Fowlerite 'Refactoring'
heuristics) but mostly it delegates to your own coding standards + spec
compliance." A generic skill's ceiling is deliberately low; the curated,
project-specific layer is where the useful signal lives.

That's also why he pushes back on review-by-prompt as a substitute for this
structure: told "decent CLAUDE.md + 'review last commits' is all you need,"
he disagrees — "it's actually not that simple." A one-line ad-hoc prompt has
neither of the two things that make `/code-review` work: a separated Spec
axis checked against the originating issue/PRD, and a Standards axis anchored
to a portable smell baseline *plus* curated project conventions. Skipping
straight to a prompt collapses both axes back into vibes.

## CODING_STANDARDS.md accretes by observation, and review is where it gets budget to enforce it

The curated-standards half of the Standards axis has a stated feed mechanism:
"Notice the agent is doing something bad. Write it in `CODING_STANDARDS.md`
(root of the repo). `/code-review` picks it up and enforces it at review time."
Matt calls this the underplayed customizability of the skill and backs it with
scale — "I have hundreds of lines in my `CODING_STANDARDS.md` files." Every
constraint starts as an observed failure, not a speculative rule written in
advance; the file is a running log of corrections, and `code-review`'s
Standards axis is what turns each new line into an enforced check on every
future diff instead of a one-off fix.

Asked why this correction doesn't just go straight into `AGENTS.md` so the
agent avoids the mistake by default, Matt's answer is a budget argument, not a
preference: "implementation is already hugely overloaded, and code review is
usually underloaded" — confirmed again when pressed on whether a long
`CODING_STANDARDS.md` risks bloating a session's context: "you have more
budget during review because it isn't so overloaded by the burden of
implementation/exploration." This is `keep-the-agent-in-the-smart-zone`'s
budgeting logic applied to *where* a standard lives, not just how much context
a session uses: implementation is already spending attention on exploration
and code generation, so a growing rulebook competes hardest with the phase
that can least afford it; review is comparatively idle, so the same rulebook
costs less there per unit of enforcement. It's also why `CODING_STANDARDS.md`
is kept as a file separate from `AGENTS.md`/`CLAUDE.md` rather than folded in —
a standards file "can afford a bit more bloat" precisely because it's only
loaded at the review checkpoint, not on every session regardless of phase (see
`claude-md-is-an-instruction-budget`'s CODING_STANDARDS.md carve-out).

## A harness-level name collision, an unguarded delegation loop, and no convergence guarantee

Three practitioner-reported problems sit outside the skill's own design and are
unfixed. First, the skill's name collides with Claude Code's own built-in
`/code-review`, which hunts bugs in a diff rather than checking spec compliance
and repo standards — installing this skill means one of the two wins, silently,
depending on install method (plugin-marketplace installs alias everything under
a `mattpocock-skills:` prefix and make the built-in hard to reach unqualified;
a plain skills install lets the local file shadow the built-in outright). The
shadowing is arguably a harness bug — a skill author should be free to name a
skill anything — but the practical fix today is forking the skill under a new
name and dropping `code-review` from the managed set, since editing the
frontmatter or renaming the directory gets undone by the next `npx skills
update`. Second, neither sub-agent prompt forbids delegation, so a Standards or
Spec sub-agent can rediscover `/code-review` and fan out again; one report
reached 50-plus agents from a single invocation. The field fix people apply on
forks is one line in both sub-agent briefs — "do not invoke `/code-review` or
spawn additional agents, perform this review directly" — but nothing in the
shipped skill guards against it, so an unattended run needs the agent count
watched. Third, the skill gives **no convergence guarantee**: fixes create new
surface, and the Standards axis's judgement-call half isn't deterministic
between runs, so a second pass on already-fixed code routinely finds new
things. The intended posture is to treat one pass as a list of leads, act on
the cited ones, and stop — running it in a loop expecting a clean pass is
chasing a signal the skill was never built to converge to.

A separate, structural argument favors running the skill in a **fresh session**
from the one that wrote the code, even though `implement` calls it inline at
the end of a build: "same context reviewing itself isn't review, it's
confirmation bias with a slash command." The session that just wrote the diff
holds every assumption that shaped it — exactly the context an independent
reviewer wouldn't have — so invoking `/code-review` yourself from a clean
session, against a fixed point, is the more honest version of the same check.
The skill also only ever diffs `<fixed-point>...HEAD` (three-dot, from the
merge-base), which excludes staged and uncommitted working-tree changes — if
`implement` hasn't made an interim commit, there is nothing yet for the review
to see, which reads as the skill silently reviewing nothing rather than
failing loud.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-code-review-4631b0e8.md` — origin: https://www.aihero.dev/skills-code-review
- `sources/mattpocock/skills-repo/skills-in-progress-review-SKILL.md-f60ae53b.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/review/SKILL.md (revision 2026-06-30)
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md
- `sources/mattpocock/skills-repo/skills-engineering-code-review-SKILL.md-ffd0e041.md` — origin: https://github.com/mattpocock/skills/blob/a5c124ef9cfecc39636f426cc4ff956580d6ea10/skills/engineering/code-review/SKILL.md (the skill promoted to `engineering/` and renamed `code-review`)
- `sources/mattpocock/skills-repo/docs-engineering-code-review.md-ff6105b1.md` — origin: https://github.com/mattpocock/skills/blob/a5c124ef9cfecc39636f426cc4ff956580d6ea10/docs/engineering/code-review.md
- `sources/mattpocock/skills-repo/docs-engineering-tdd.md-54751a46.md` — origin: https://github.com/mattpocock/skills/blob/94e6208c841d34df742015be950c3a4ccff3297b/docs/engineering/tdd.md (revision 2026-07-02, the main chain gains the `→ code-review` tail)
- `sources/mattpocock/skills-repo/skills-engineering-README.md-1400dd55.md` — origin: https://github.com/mattpocock/skills/blob/4d49c0fc99c3a732f7acb87a0fa00a32440a603d/skills/engineering/README.md (revision 2026-07-02, `code-review` listed under Model-invoked)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080760177494577332-0afcef76.md` — origin: https://x.com/mattpocockuk/status/2080760177494577332
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080760324945301917-ebf81aaf.md` — origin: https://x.com/mattpocockuk/status/2080760324945301917
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080905425449308448-6725b6a4.md` — origin: https://x.com/mattpocockuk/status/2080905425449308448
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082885965798920502-f603b3e0.md` — origin: https://x.com/mattpocockuk/status/2082885965798920502
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088256132234055978-f3b53053.md` — origin: https://x.com/mattpocockuk/status/2088256132234055978
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088256432265167185-30575da8.md` — origin: https://x.com/mattpocockuk/status/2088256432265167185
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088272552967705071-69ec5b18.md` — origin: https://x.com/mattpocockuk/status/2088272552967705071
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088347274610880648-73d24dae.md` — origin: https://x.com/mattpocockuk/status/2088347274610880648
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088742184245731443-67a7980c.md` — origin: https://x.com/mattpocockuk/status/2088742184245731443
