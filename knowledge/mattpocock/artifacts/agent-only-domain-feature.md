# A feature can ship agent-authored only, with no human UI at all

Once a write path already carries every constraint a UI would otherwise
enforce client-side, building the UI stops being mandatory infrastructure —
the CLI alone can be the finished authoring surface, not a stopgap ahead of
one. `course-video-manager`'s Overlay and Definition Card feature (an
on-screen definition card composited onto exported video) is implemented as
pure domain data, authored exclusively through `cvm overlay
add|list|get|update|delete`: "there is no editor UI." That's a deliberate
contrast with the same glossary section's own **Overlay Template** and
**Transition**, each explicitly flagged "(not yet implemented)" — Overlay and
Definition Card carry no such flag. Agent-only authorship is the shipped
state, not a placeholder waiting on a UI that hasn't been built yet.

A later addition to the same glossary shows the pattern isn't a one-off: the
**Learning Goal** (a Section's pre-Beat planning artifact) is "read-mostly in
the UI — the Section card shows a closed-by-default collapsible of its
Learning Goals; the `cvm learning-goal` CLI (create/update/move/delete) is the
editing surface." The UI keeps a passive display here rather than dropping to
nothing, but the split is the same one: the human-facing surface shows state,
the CLI is where the state is authored, and a second instance of the same
design choice — made independently, for a different entity — is what turns
this from an isolated decision into a repeatable one.

## The CLI absorbs every guard a UI's affordances would otherwise give

With no human eyeballing a draft before it's saved, the write path itself has
to catch every mistake a UI's client-side affordances would normally prevent.
`cvm overlay add|update` refuses an overlapping window against another
Overlay, refuses content that doesn't match the Overlay's declared Kind,
refuses a shortening `--duration` update that would strand a Bullet's reveal
time past the panel's new end — each one a constraint a drag handle or a
disabled button would enforce visually in a UI, reimplemented instead as a
server-side refusal because nothing else stands between the agent and a
malformed write.

## Field semantics follow how an agent actually derives its inputs

The schema shape isn't just UI-agnostic, it's agent-shaped: a Bullet's
`revealAt` is stored as seconds *after the Overlay's own start* — "which is
the whole reason it is authored per bullet: an agent working from a
transcript derives it as `wordStartTime - overlayAt`, and the bullet appears
exactly as the words are spoken." An absolute timestamp would be the more
natural unit for a human dragging a marker on a timeline; an offset from the
Overlay's start is the natural unit for an agent computing a value from its
one source of truth (a transcript) by subtraction. Once a UI is out of the
picture, the field can be shaped for the arithmetic that actually produces
it.

## When a cascade can't regenerate the data, clamp it visibly instead of dropping it silently

The same feature's **Retiming Cascade** — what happens to positioned data when
a Clip is recut — draws the general lesson out explicitly. Data that shifts
out of the Clip's new bounds splits into two treatments by whether it can be
regenerated: a **Transcript Word** is read-side data, reproducible by
re-transcribing, so one that falls outside the new range is simply dropped.
An **Overlay** carries hand-authored content (a Definition Card's words, a
Bullet Panel's bullets) that no re-run reproduces, so its anchor is clamped
back inside the range instead — never deleted, its content never rewritten.
The reasoning is stated directly: "a clamped Overlay is visibly in the wrong
place, which is a problem an agent can see and fix; a deleted one is just
gone." The general shape: when a cascading update would otherwise destroy
data nothing can regenerate, prefer a visibly-wrong state that whoever owns
the fix — human or agent — can act on, over a clean deletion that erases the
fact that anything needed fixing at all.

## Sources

- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-08-24, "Overlays and transitions": `Overlay`/`Definition Card` implemented as domain data authored only via `cvm overlay add|list|get|update|delete`, no editor UI; the **Bullet** entry's `revealAt` derivation from a transcript; the **Retiming Cascade** entry's clamp-vs-drop split)
- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-09-04, new **Learning Goal** entry: read-mostly in the UI, `cvm learning-goal` CLI is the editing surface)
