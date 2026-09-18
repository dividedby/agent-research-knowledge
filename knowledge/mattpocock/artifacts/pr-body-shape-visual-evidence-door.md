# A PR body separates three jobs: the smallest visual, tiered evidence, a door call

The `pr` skill (in-progress, model-invoked) treats a pull-request body as three
distinct questions rather than one narrative paragraph of "what I did": what
changed (Summary), does it actually work (Evidence), and how dangerous is
merging it (Merge Danger). Splitting them keeps a reviewer from having to
extract risk and proof from prose that's really just restating the diff.

**Summary** picks the *smallest* view that makes the key point clear, not
always the raw diff — pseudocode for logic/algorithm changes, a call tree for
control-flow changes, a component tree for UI structure, a shallow file tree
for a refactor's file-responsibility shift, or a Mermaid sequence diagram for
cross-component interaction. `diff` itself is reserved for the case where the
point *is* what changed and the surrounding shape already exists in the
reader's head — matching diff shape to topic (a component-tree diff, a
file-tree diff, a call-tree diff) rather than one generic unified diff. The
rule of thumb is coverage, not completeness: use one visual, or a few, never
all of them, and place each one next to the short text it supports.
Pseudocode earns its specific slot for a reason beyond legibility: a
high-level view of the change has been, in Matt's words, "an incredible way to
understand the *why* of the code change" — the goal is causal understanding,
not just a shorter diff. The implementation shortcut he lands on for
generating Summary and Evidence is to have the diff itself summarized, rather
than hand-writing each section.

**Evidence** is ranked by tier, not left to whatever's convenient to paste:
screenshots are S-tier when the change is visual and the environment supports
capturing one; execution-based evidence — the exact test that now fails then
passes, console output — is A-tier otherwise. Either way it's a before/after
pair, not a single "it works" assertion.

**Merge Danger** reframes risk as a reversibility question borrowed from
options theory: is this a one-way door (hard to walk back) or a two-way door
(cheap to revert), and what's the blast radius if it goes wrong (consumer
breakage, layout shift, mobile responsiveness, etc.)? Naming the door
explicitly gives a reviewer a risk budget to calibrate scrutiny against,
instead of leaving them to infer reversibility from the diff's size. The call
has a direct payoff for *when* review happens, not just how it's labeled: for
a two-way door, Matt takes it as fine to merge first and read the review
after — the same reversibility argument that licenses auto-fixing
`/code-review` findings before inspection
(`auto-fix-review-after-revert-safety-net`), applied one layer up to the PR
itself.

## Origin: replacing garbage default PR bodies

The skill's premise, stated bluntly: "every model/harness I've seen creates
garbage PR bodies" — the default is a narrative paragraph restating the diff,
exactly the failure mode the three-question split above replaces. Two
borrowed constraints shape it rather than starting from a blank page: Evidence
reuses HumanLayer's `/show-me` (Dex Horthy) almost directly — "`/show-me` has
been phenomenal for me, a big difference; really just trying to make a small
tweak on top of that" — and the whole body is written in the repo's own
domain language, reusing the vocabulary a `/grill-with-docs` pass already
established rather than generic engineering prose.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-pr-SKILL.md-795517e8.md` — origin: https://github.com/mattpocock/skills/blob/74ca5fe077456a0b3b2f5310cf9430999fd0b5fd/skills/in-progress/pr/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-09-18, origin https://github.com/mattpocock/skills/blob/700989c0b6e64d1133449793d86bcb3a35a031f9/skills/in-progress/README.md — `pr` listed)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2100521948786667822-1c6587b1.md` — origin: https://x.com/mattpocockuk/status/2100521948786667822
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2100539180560363692-49546026.md` — origin: https://x.com/mattpocockuk/status/2100539180560363692
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2100526189899083985-ec979a98.md` — origin: https://x.com/mattpocockuk/status/2100526189899083985
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2100547293275394206-a1879b96.md` — origin: https://x.com/mattpocockuk/status/2100547293275394206
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2100574289393004839-0789c15c.md` — origin: https://x.com/mattpocockuk/status/2100574289393004839
