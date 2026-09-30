# A review surface for structured AI output opens collapsed, not expanded

When a human is judging AI-produced content by its coarse shape before drilling into detail, the review page should load with every subsection folded shut — the outline first, the detail only on request — rather than opening on the fully expanded view and asking the reviewer to fold away what they've already judged.

## The reversal in course-video-manager's Animatic

The **Animatic** page lets an author watch a Video's storyboard before a shoot, grouped into **Clip Mockup Chapters** (collapsible dividers, each foldable behind its title). An earlier revision left every Chapter's fold state "born empty" on load — i.e. open by default, with folding something the author had to do by hand each visit. The later revision inverts this: every Chapter now starts folded on every load, and a Chapter created while the page is open also arrives folded, so "the page opens on the dividers alone and the author opens what he is judging." Fold state itself is unchanged in every other respect — still ephemeral, per-tab, never persisted or shared.

## Why the default matters more than the mechanism

The fold control existed in both versions; only its starting state changed. That's the whole lesson: a collapse *feature* doesn't protect a reviewer's attention on its own — its *default* does. Opening expanded puts every already-settled Chapter in front of the author's eyes before they've decided anything is worth a second look, so the first several seconds on the page are spent re-collapsing what's already fine rather than judging what isn't. Opening collapsed makes the reviewer's attention opt-in: the outline (titles + rolled-up run time) is the first read, and expanding any one Chapter is a deliberate signal that it's the thing being judged right now.

## The general shape

For any page whose job is letting a human judge AI-authored structure at a glance before deciding what to inspect closely, default every foldable unit to its collapsed state on load. The reviewer should never spend their first pass un-collapsing what a well-behaved default would have collapsed for them.

## Sources

- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-09-30, **Clip Mockup Chapter** entry: fold state changes from "born empty" on load to "EVERY CHAPTER STARTS FOLDED on every load... so the page opens on the dividers alone and the author opens what he is judging")
