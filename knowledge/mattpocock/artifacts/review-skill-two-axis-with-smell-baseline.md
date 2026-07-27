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
`feedback-loop-is-the-work`).

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

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-review-SKILL.md-f60ae53b.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/review/SKILL.md (revision 2026-06-30)
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md
- `sources/mattpocock/skills-repo/skills-engineering-code-review-SKILL.md-ffd0e041.md` — origin: https://github.com/mattpocock/skills/blob/a5c124ef9cfecc39636f426cc4ff956580d6ea10/skills/engineering/code-review/SKILL.md (the skill promoted to `engineering/` and renamed `code-review`)
- `sources/mattpocock/skills-repo/docs-engineering-code-review.md-ff6105b1.md` — origin: https://github.com/mattpocock/skills/blob/a5c124ef9cfecc39636f426cc4ff956580d6ea10/docs/engineering/code-review.md
- `sources/mattpocock/skills-repo/docs-engineering-tdd.md-54751a46.md` — origin: https://github.com/mattpocock/skills/blob/94e6208c841d34df742015be950c3a4ccff3297b/docs/engineering/tdd.md (revision 2026-07-02, the main chain gains the `→ code-review` tail)
- `sources/mattpocock/skills-repo/skills-engineering-README.md-1400dd55.md` — origin: https://github.com/mattpocock/skills/blob/4d49c0fc99c3a732f7acb87a0fa00a32440a603d/skills/engineering/README.md (revision 2026-07-02, `code-review` listed under Model-invoked)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080760177494577332-0afcef76.md` — origin: https://x.com/mattpocockuk/status/2080760177494577332
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080760324945301917-ebf81aaf.md` — origin: https://x.com/mattpocockuk/status/2080760324945301917
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080905425449308448-6725b6a4.md` — origin: https://x.com/mattpocockuk/status/2080905425449308448
