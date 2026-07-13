# Scope the scan by commit recency, not just by size

Before an open-ended codebase scan runs at all, decide *where to look* the same
way you'd decide *what to build*: YAGNI applied to attention, not code. Rather
than surveying the whole repo evenly, `improve-codebase-architecture` first
walks recent commit history (`git log --oneline`) to find the files and areas
that keep coming up, then lets those hot spots pull the exploration's attention
first — widening the net only if the recent changes are too scattered to show a
hot spot. A user-named direction (a module, a subsystem, a pain point) always
overrides the inference and skips it entirely.

## Why recency is the right proxy

The payoff for deepening a module is realised the *next* time someone touches
it — so weighting toward code that's still actively changing targets the scan
at where the architectural debt is actually costing something right now, not
at code that's stable and rarely revisited. An even, whole-repo survey spends
the same attention on a frozen corner of the codebase as on the file five
people edited this week, which is attention spent where it can't pay off.

## Transferable beyond this one skill

The technique generalises to any agent task that has to choose *where* to
focus before it can start: code review, architecture review, a "what should I
clean up today" pass. The commit log is a free, always-available recency
signal that requires no extra tooling — `git log --oneline` — and it's a
cheap, honest proxy for "where does more work still land," which is a better
question to scope against than "where is the code ugliest."

## Sources

- `sources/mattpocock/skills-repo/docs-engineering-improve-codebase-architecture.md-9de7ede1.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/improve-codebase-architecture.md (revision 2026-07-13, origin https://github.com/mattpocock/skills/blob/626593b256ee7424fe23d29d7420f391faf6bea4)
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md (revision 2026-07-13, origin https://github.com/mattpocock/skills/blob/dc900951502dc5cd3a0d96699fd2020fb79be9a2 — "Scope before you scan — YAGNI")
