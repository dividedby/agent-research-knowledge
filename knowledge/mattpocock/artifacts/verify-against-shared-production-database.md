# Verifying against a live, shared database needs structural isolation, not restricted access

When there is no seed data and no staging copy — every row an agent's browser
session sees is real work — the safety mechanism for automated verification
can't be "be careful." `course-video-manager`'s `verify-cvm` skill drives the
real app against the production database and gets its safety from two
structural guarantees instead: a run can never collide with a concurrent user
of the same resource, and any change it does make is provably visible
afterward. Neither guarantee depends on the agent behaving well — both hold
even if it doesn't.

## Disjoint address space, refused rather than hoped for

The author's own dev server and every verification run share one database but
never one port: the CVM owns a fixed band (5170–5199, with individual ports
pinned to specific processes — the author's own dev server sits at 5173),
verification runs take a separate band (5200–5299) and `launch` **asks for
exactly one port and refuses a server that comes up anywhere else** — a taken
port is a startup failure to retry, never a silent drift onto the next one.
A `doctor` check run before driving fails outright if a run's port ever lands
in the author's band: "you may be driving Matt's own CVM." The isolation is
checked mechanically on every launch, not documented as a rule to remember.

## A before/after counter diff, not the agent's own account

The proof of non-interference is a **Write Ledger**: before driving, record
Postgres's own `pg_stat_user_tables` insert/update/delete counters (a cheap
catalog read, never a table scan); after driving, diff them. A clean diff is
the proof nothing changed — not the agent's summary of what it clicked. Because
the counters are database-wide, the author's own live instance and every
sibling verification run write to the same tables, so a moved counter is a
**lead, not a verdict** — a separate `forensics` verb names the actual rows by
querying `created_at`/`updated_at` inside the drive's own timestamp window.
The protocol is to report a non-clean Ledger up front regardless of how
confident the agent is that it wasn't the cause: a false alarm costs one
glance, and silence about a possible write costs trust in every future run.

## When a write is unavoidable, make it self-labeling and reversible

Some verifications genuinely need a write (a form submit, a status toggle).
The rules that make that safe: **create, never edit**, something that already
exists; **title it to sort last and read as scaffolding** to any human who
finds it (`ZZ-VERIFY-<timestamp>`); **write down what was created before
creating the next thing**, so a crash mid-run still leaves a trail; and
**archive through the same UI path a real user would take** rather than a
direct delete — most nouns soft-delete, so the row survives and the report
says "archived," not "removed."

Two pages are excluded from this protocol entirely rather than trusted to it,
because their writes leave the database and can't be undone through it: one
submits a release and ships files to an external system, the other spends
real API tokens rewriting real content. A side effect this system's own
restore path can't reach doesn't get a careful-write allowance — it gets a
blanket "observe only."

## The general shape

A verification agent driving a real, mutable, shared resource — not a sandbox
copy — needs two independent guarantees, and both have to be structural: it
must be unable to collide with whoever else is using the same resource right
now (a disjoint, mechanically-enforced address space), and any change it does
make must be provable after the fact from the resource's own change-tracking
(a before/after diff), not merely a promise the agent kept from acting. Access
control alone gives neither guarantee — it can restrict *what* the agent is
allowed to touch, but not *prove* what it actually did.

A smaller instance of the same "make it addressable, don't trust live-only
output" instinct shows up in the same repo's dev server: `pnpm dev`/`pnpm
start` tee their output to `.data/logs/dev-<timestamp>-<pid>.log`, with a
`dev-latest.log` symlink to the most recent run, kept for a day — so a crash
or a runtime error is something an agent (or the author) can read back after
the fact, not something only visible in a terminal that's already scrolled
past.

## Sources

- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-SKILL.md-b0ae1453.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/SKILL.md
- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-scripts-verify.sh-5eae10bd.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/scripts/verify.sh
- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-features-README.md-1095ff28.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/features/README.md
- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-features-course-view.md-6b9ad7bf.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/features/course-view.md
- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-features-deliverables.md-1287c236.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/features/deliverables.md
- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-features-pitches.md-e195a840.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/features/pitches.md
- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-features-publish.md-486f3a16.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/features/publish.md
- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-features-video-editor.md-742ae28e.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/features/video-editor.md
- `sources/mattpocock/course-video-manager/.claude-skills-verify-cvm-features-videos-and-shorts.md-5be91211.md` — origin: https://github.com/mattpocock/course-video-manager/blob/032ca77664694b8dd95eb1241966ca34b459d3df/.claude/skills/verify-cvm/features/videos-and-shorts.md
- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md (revision 2026-09-26, "Verifying a change in the real app" pointer, and "What the running server printed": `.data/logs/dev-<timestamp>-<pid>.log` with a `dev-latest.log` symlink, kept a day)
