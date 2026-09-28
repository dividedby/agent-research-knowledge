# Rank context sources by fidelity, not just by inclusion

When a generative feature draws on several sources of context for one task,
curating *which* sources it sees isn't enough — sources differ in how much
they can be trusted to ground a claim, and that difference has to be stated
explicitly or the agent will treat them as interchangeable. Course Video
Manager's Article Writer reads four sources for a Video — **Beats**,
**Script**, **Transcript**, and text **Video Files** — and its glossary entry
ranks them on a **fidelity ladder** rather than listing them as one
undifferentiated pool.

## The ladder: intent → plan → what actually happened

A later revision names the ladder explicitly and adds a rung below Beats: a
**Beat** (what a moment of the video does for the *viewer* — the job, not the
words) is authored first, then a **Clip Mockup** (one still image and its
spoken line — the picture and the words, decided before the camera is on) is
built from it, then the **Script** is written out from the Clip Mockup lines,
and the **Transcript** is what was actually said on camera. Stated once, in
the glossary itself: "each rung is authored from the one below it," and the
Transcript "supersedes all of them once the Video is filmed" — it is the only
source that records what was actually said, so it is the sole basis for
anything the article claims the speaker said. The generative direction runs
opposite the fidelity order: each rung is *written from* the one beneath it,
but *outranked by* it once a more-faithful rung exists.

## Supporting material never joins the ladder

Text **Video Files** (attached code samples, notes, session logs) are excluded
from the ladder entirely rather than slotted below Beats. They are evidence
and texture — "what was on screen" — that the writer draws on for detail and
specifics, but never a source the article can cite as a claim in its own
right. A code sample that was never narrated on camera can illustrate a point
the Transcript already makes; it cannot itself establish that the point was
made.

## Why the ranking has to be explicit

Without a stated hierarchy, a writer assembling several context sources into
one output has no way to know that a plan, a rehearsed script, and a recording
of what actually happened carry different truth-values — a detail from an
unfilmed Script beat would look exactly as authoritative as something the
speaker actually said on camera. Naming the ladder in the domain glossary —
not just curating which files get attached (see
[[attachable-files-as-opt-in-agent-context]]) — is what lets the Article
Writer, and a human reviewer, tell "this is what happened" from "this is what
was planned or nearby."

## Sources

- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-07-29 — the **Video File** entry's writer-context clause now names **Script** alongside Transcript/Beats and cross-references the fidelity ladder, ranking Transcript as the sole source of claims and Video Files as evidence-only)
- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-09-27 — the **Script** entry states "THE FIDELITY LADDER" explicitly: Beat → Clip Mockup → Script → Transcript, each rung authored from the one below it)
