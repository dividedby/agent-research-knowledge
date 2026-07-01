# Review as two independent axes, never merged

The in-progress `review` skill checks a diff against a fixed comparison point
along **two deliberately separate axes** — Standards (does the code follow
this repo's documented conventions?) and Spec (does the code faithfully
implement the originating issue/PRD?) — and refuses to merge or rerank their
findings into one list. The reason is structural: a change can pass one axis
and fail the other (code that's spec-perfect but breaks house style; code
that's clean but implements the wrong thing), and collapsing them into a
single ranked list would let one axis mask the other. Each axis runs as a
**parallel sub-agent** so their findings can't cross-pollute, then the skill
aggregates by presenting both reports side by side under their own headings —
the same fan-out-then-compare shape `codebase-design`'s DESIGN-IT-TWICE uses
for interface alternatives, applied to review instead of design.

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

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-review-SKILL.md-f60ae53b.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/review/SKILL.md (revision 2026-06-30)
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md
