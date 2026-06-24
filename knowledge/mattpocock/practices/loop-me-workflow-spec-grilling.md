# loop-me: grill your life into delegatable workflow specs

`loop-me` aims the grilling discipline at a different target than the engineering
chain. Where `grill-me`/`grill-with-docs` interrogate *one change* to alignment,
`loop-me` interrogates *the user's recurring life* to find work worth handing to
an agent at all. Its only output is **workflow specs** — it never implements; it
decides what is worth specifying and pins down each one until an implementer could
build it without a question.

## The loop lens: a life is loops worth delegating

The framing primitive is the **loop** — any recurring pattern in the user's life
(their career, their week, their morning, one repeated activity). Picturing a life
as loops-within-loops exposes how *predictable* its activities actually are, and
predictability is exactly what makes a thing delegatable. The lens is also
generative: the skill is told to **propose loops the user hasn't noticed**, not
just catalogue the ones they name. A **workflow** is the spec of one loop made
real; you *run* a workflow *on* a loop, so the loop is the running instantiation
and `workflows/*.md` is the source of truth.

## Mandate nothing structural — the vocabulary is reached for, not imposed

The skill carries a small shared vocabulary, but the hard rule is that it is
**reached for only when a workflow calls for it, never a checklist**: a workflow
needs no AI, no checkpoint, and no schedule unless the grilling proves it does.
This is the same anti-over-engineering posture as the rest of Matt's collection —
discipline supplied, structure not forced (see `small-adaptable-not-process-owning`).
The vocabulary:

- **Trigger** — what fires each run: an **event** (a new email, a new issue) or a
  **schedule** (every morning). Event-triggering is usually more efficient than
  polling on a clock.
- **Checkpoint** — a human-in-the-loop verify/decide point. Some workflows have
  none and run autonomously; some use no AI at all.
- **Push right** — defer the checkpoint as far as it will go: do the maximal work
  *before* involving the human, so they are asked once, late, with everything
  prepared.
- **Brief** — what a checkpoint presents: a decision-ready summary (what was
  produced, why, plus a link down to the asset), **never the raw output**. The
  user reads a brief, not a draft; speed of review is the imperative. (This is the
  same brief discipline AFK engineering work uses — see `durable-briefs-for-afk-agents`.)

"Push right" + "brief" together are the delegation economics restated: maximise
unattended work, minimise the human's attention per run, and spend that attention
on a summary rather than a draft.

## Done = an implementer needs zero questions; the directory is the state

Definition of done is borrowed straight from the grilling lineage: a spec is done
only when an implementer agent could build it **without asking a single question**
— grill until then, nothing is done while a question remains. The session is
**stateful across multiple sittings**, using the current directory as the
workspace: `workflows/*.md` holds one spec per workflow, and `NOTES.md` holds raw
notes on the user's world — the tools they use, the channels they process, and
*their own terminology* for both. When `NOTES.md` is thin the skill interviews the
user about their world before specifying anything, and sharpens fuzzy terms into
canonical ones as they surface (the same live-glossary move as
`shared-language-as-agent-fuel`, applied to the user's life rather than a
codebase). Specs are created, edited, and deleted as the grilling resolves things.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-loop-me-SKILL.md-cb8cc094.md` — origin: https://github.com/mattpocock/skills/blob/74f0450b9cbfc562a9d0f16f73f23745931f048d/skills/in-progress/loop-me/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-06-24)
