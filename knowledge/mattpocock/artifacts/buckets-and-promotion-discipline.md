# Buckets and promotion discipline

The repo sorts skills into six bucket folders by *lifecycle and intent*, not by
topic: `engineering/` (daily code work), `productivity/` (daily non-code
workflow), `misc/` (kept but rarely used), `personal/` (tied to Matt's own
setup), `in-progress/` (drafts), and `deprecated/` (retired). The bucket a skill
lives in is a promotion state, and promotion carries a hard publication rule.

## The publication invariant

Only the three *public* buckets — `engineering/`, `productivity/`, `misc/` —
are advertised. Every skill in those buckets **must** appear in both the
top-level `README.md` and `.claude-plugin/plugin.json`, with the README link
pointing at the skill's `SKILL.md`. Every skill in `personal/`, `in-progress/`,
and `deprecated/` **must not** appear in either. There is no middle state: a
skill is either fully advertised or fully hidden, and which it is follows
mechanically from its folder.

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

- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/CLAUDE.md
- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/skills-repo/skills-engineering-README.md-1400dd55.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/README.md (revision 2026-07-09, origin https://github.com/mattpocock/skills/blob/f02469bf3e8c183fd269565808c7b613ec6011c5 — `wayfinder` added under User-invoked)
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-07-09, origin https://github.com/mattpocock/skills/blob/c150c7074b3523328da2c980d22c84b8c21a2308 — `wayfinder` dropped from the in-progress listing)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072680599802831258-4d6fbba7.md` — origin: https://x.com/mattpocockuk/status/2072680599802831258
