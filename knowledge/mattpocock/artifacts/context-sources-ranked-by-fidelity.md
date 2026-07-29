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

**Beats** (the pre-recording plan — "what I'm going to do or say") sit at the
bottom: sketched intent, not authored prose. **Script** (a screenplay-style
flowing document read off the teleprompter) is one rung up — the plan
actually written out, verbatim for framing beats and bracketed cues for
improvised ones. The **Transcript** — clip text harvested from the recording
itself — is the top rung and *supersedes both once filmed*: it is the only
source that records what was actually said, so it is the sole basis for
anything the article claims the speaker said.

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
