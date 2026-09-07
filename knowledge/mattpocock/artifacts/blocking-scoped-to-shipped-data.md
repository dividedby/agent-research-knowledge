# A validation only blocks release if what it flags actually ships

A derived warning earns the right to block a release by one fact alone: whether the entity it's warning about is part of what gets published. How wrong the state looks, or how badly it nags an author, is irrelevant — a warning on data that never ships can never be a release blocker, no matter how loudly it fires in the authoring UI.

## Same shape, opposite blocking rights

course-video-manager computes two structurally identical kinds of derived warning — live from current state, never stored, each with a stable `kind` name — and wires them to opposite outcomes. **Video Warning** covers **Videos**, which are exactly what a **Publish** ships: even the two kinds Autofill now owns (missing chapters, missing description) are removed from the authoring surfaces once Autofill exists to fix them silently, yet they stay fully wired into **Publish Readiness** and can still refuse a release. **Beat Warning** / **Learning Goal Warning** cover **Beats** and **Learning Goals** — in-app planning artifacts that **Publish** always skips, never rendering them into shipped output — and are "deliberately excluded from Publish Readiness," full stop, regardless of how many Beats fail to serve a Learning Goal. The glossary names the exclusion directly in the term's own `_Avoid_` line: "Publish blocker (this never blocks a Publish)."

## Why the split is by shipped-ness, not by severity

The naive rule is "a warning is a blocker until it's fixed, then it's fine" — treating every derived defect as equally eligible to stop a release. course-video-manager's split shows the real criterion is upstream of severity: ask whether the flagged entity reaches the artifact at all. A Video that's missing chapters will ship broken if ignored, so its warning has to be able to say no. A Beat that serves no Learning Goal is real, useful authoring feedback — it just can never be a *reason a course fails to publish*, because a Beat was never going to be in the published course in the first place. Wiring it into the release gate anyway would let purely internal planning hygiene stall shipping, coupling two things — "is this plan well-organized" and "is this artifact correct" — that have no causal link.

## The transferable rule

Before adding a new derived check to a release/CI/publish gate, ask "does the thing this check is about end up in what we ship?" If yes, it can block. If no — a draft note, an internal annotation, a planning artifact your own format already excludes from the output — give it a warning surface, never a gate. The check computing "is this state valid" and the decision "should this block release" are two different questions, and this pattern answers the second one with a fixed, one-line rule instead of re-deciding it per warning kind.

## Sources

- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-09-07, new **Beat Warning** / **Learning Goal Warning** entry: "deliberately excluded from Publish Readiness"; the **Video Warning** entry's Autofill-owned kinds staying "fully blocking inside Publish Readiness" despite no longer being shown on authoring surfaces)
