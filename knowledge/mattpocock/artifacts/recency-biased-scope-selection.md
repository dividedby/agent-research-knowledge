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

## The output is a survey to choose from, not a refactor to accept

`improve-codebase-architecture`'s scoping pass feeds a report, and the report
is deliberately inert: the whole run produces one self-contained HTML file in
temp and a conversation — no code changes, ever, during the scan itself. Each
candidate has to pass the **deletion test** (would removing this module
concentrate complexity behind a smaller interface, or just spread it across
callers?) before it earns a card, and each card carries a strength badge —
`Strong`, `Worth exploring`, `Speculative` — so a report where everything lands
`Speculative` is the skill's way of saying it found nothing, rather than
inventing findings to justify the run. The skill only starts a grilling session
*after* you pick one card; showing the survey and stopping is the intended
shape.

That intended shape is also the most-reported complaint about the skill in
practice: a weaker model skips straight to interviewing the user about the
first candidate it thought of, without ever presenting the ranked report — one
user who liked the tool as "a convenient way to get a thorough analysis of
improvements" called it "borderline unusable" once the grilling step started
firing unprompted, sometimes with dozens of questions about a single idea. The
workaround is to say so on invocation ("don't grill me, just show the report
first"); there's no shipped no-grill mode yet. A second, unrelated failure hits
the report's rendering rather than its content: the HTML report loads Tailwind
and Mermaid from a CDN, so a locked-down or offline environment — or a security
hook that adds SRI hashes computed by `curl` against bytes the CDN serves
differently to a browser — can silently produce unstyled, diagram-free output
that the agent has no way to notice, because it never renders the page itself.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-improve-codebase-architecture-23b24b6b.md` — origin: https://www.aihero.dev/skills-improve-codebase-architecture
- `sources/mattpocock/skills-repo/docs-engineering-improve-codebase-architecture.md-9de7ede1.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/engineering/improve-codebase-architecture.md (revision 2026-07-13, origin https://github.com/mattpocock/skills/blob/626593b256ee7424fe23d29d7420f391faf6bea4)
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md (revision 2026-07-13, origin https://github.com/mattpocock/skills/blob/dc900951502dc5cd3a0d96699fd2020fb79be9a2 — "Scope before you scan — YAGNI")
