# Buckets and promotion discipline

The repo sorts skills into bucket folders by *lifecycle and intent*, not by
topic: `engineering/` (daily code work), `productivity/` (daily non-code
workflow), `misc/` (kept but rarely used), `in-progress/`, and `deprecated/`
(retired). The bucket a skill lives in is a promotion state, and promotion
carries a hard publication rule.

A sixth bucket, `personal/` (tied to Matt's own setup), was later removed
outright rather than left empty: its two skills were deleted with it — one
hardcoded a path to his own Obsidian vault, the other was tied to his own
machine — because neither was ever meant for another user, unlike a demoted
skill that still has a home in `misc/` or `deprecated/`. `in-progress/` was
redefined in the same pass, from "drafts not yet ready to ship" to a **beta
channel**: skills there are public on purpose, installable one at a time
through `skills.sh`, and wanted for feedback — not held back, just not yet in
the plugin's promoted set. The distinction matters for what "in-progress"
promises a user: not "unfinished and hidden," but "finished enough to try,
not yet finished enough to bundle."

## The publication invariant

Only the **promoted** buckets are advertised. This started as the three
buckets `engineering/`, `productivity/`, `misc/`; a later revision narrowed it
to just `engineering/` and `productivity/`, demoting `misc/` out of the
advertised set to join `personal/`, `in-progress/`, and `deprecated/` as
unpromoted. Every skill in a promoted bucket **must** appear in both the
top-level `README.md` and `.claude-plugin/plugin.json`'s `skills` array, with
the README link pointing at the skill's `SKILL.md`. Every skill in an
unpromoted bucket **must not** appear in either. There is no middle state: a
skill is either fully advertised or fully hidden, and which it is follows
mechanically from its folder — the boundary moved, but the mechanism (folder
decides visibility) didn't.

This makes "ship it" and "shelve it" the same operation as "move the folder",
and keeps the installable surface (`npx skills add mattpocock/skills`) honest —
what's listed is exactly what's promoted. `npx skills update` closes the loop
on the consumer side: an already-installed set re-syncs against whatever the
promoted list currently is, so a bucket move on Matt's end reaches a consumer
without a fresh `add`.

## A concrete graduation: the folder move is the whole release note

`wayfinder` (see `decision-mapping-fog-of-war`) shipped in v1.1.0 by moving out
of `in-progress/` into `engineering/`: it appears in the top-level and
Engineering `README.md`s under User-invoked, gains a `.claude-plugin/plugin.json`
entry and a docs page, and is dropped from the `in-progress/README.md` listing
in the same release. No other mechanism marks the promotion — the same skill,
the same `SKILL.md` content, becomes advertised purely by which folder holds
it, exactly as the publication invariant above predicts.

## README as a redundant index

Each public bucket *also* carries its own `README.md` listing its skills with
one-line descriptions, duplicating the top-level README's per-bucket section.
The redundancy is deliberate: the bucket README is the local map for someone
browsing that folder; the root README is the global catalogue. Both link skill
names to their `SKILL.md`, so the same "name → SKILL.md" convention holds at
every level.

## Sources

- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/CLAUDE.md (revision 2026-07-01, origin https://github.com/mattpocock/skills/blob/44868f473c65fe0172090224551c8b40bf5b16de/CLAUDE.md — `misc/` demoted out of the promoted set, leaving only `engineering/`+`productivity/`)
- `sources/mattpocock/skills-repo/AGENTS.md.md` — origin: https://github.com/mattpocock/skills/blob/66898f60e8c744e269f8ce06c2b2b99ce7660d5f/AGENTS.md
- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/skills-repo/skills-engineering-README.md-1400dd55.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/README.md (revision 2026-07-09, origin https://github.com/mattpocock/skills/blob/f02469bf3e8c183fd269565808c7b613ec6011c5 — `wayfinder` added under User-invoked)
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-07-09, origin https://github.com/mattpocock/skills/blob/c150c7074b3523328da2c980d22c84b8c21a2308 — `wayfinder` dropped from the in-progress listing)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072680599802831258-4d6fbba7.md` — origin: https://x.com/mattpocockuk/status/2072680599802831258
- `sources/mattpocock/skills-repo/AGENTS.md.md` — origin: https://github.com/mattpocock/skills/blob/29de6f3f3088823b95ca741eeaff8c79116722ad/AGENTS.md (revision 2026-08-06 — `personal/` removed, `in-progress/` redefined as a beta channel)
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/c66bdeeee002d81e3f8b21403c07f9a0d7bea6da/CHANGELOG.md (revision 2026-08-06, PR #752 — `edit-article` and `obsidian-vault` deleted along with the `personal/` bucket)
