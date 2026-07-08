# Align before building: the grilling session

The most common agent failure mode Matt targets is misalignment — the agent
builds something other than what you meant, because "no-one knows exactly what
they want" until pushed. The fix is a **grilling session**: before any code, the
agent interviews the human relentlessly, one question at a time, walking down
each branch of the decision tree and resolving dependencies between decisions
before moving on. For every question the agent offers its *recommended* answer,
so the human is reacting to a concrete proposal rather than generating from
scratch.

`grill-me` is the bare form of this. Two rules give it its character:

- **One question at a time, wait for the answer.** No question dumps. The next
  question depends on the last answer, so batching them produces a shallow
  interview.
- **Prefer the codebase over the human — but only for facts.** "If a question
  can be answered by exploring the codebase, explore the codebase instead."
  The human's attention is the scarce resource; spend it only on what the code
  can't tell you. The rule later sharpens from "question" to an explicit
  fact/decision split: *"If a fact can be found by exploring the codebase,
  look it up rather than asking me. The decisions, though, are mine — put
  each one to me and wait for my answer."* Exploring the codebase to spare the
  human's attention is license to skip *verifiable* facts only — never license
  to infer a decision from what the code already happens to do and treat that
  as the human's answer.

This is positioned as the thing to run *every time you make a change*, not an
occasional ceremony — it is Matt's most-used pair of skills. A third line was
later added to the bare skill — *"For each question, provide your recommended
answer"* — so the human reacts to a concrete proposal and can often just say
"yes", which sharply speeds the interview. The skill is domain-agnostic: drop the
"explore the codebase" line and it runs grilling sessions for non-code decisions
(someone used it to write a eulogy).

## Only grill the grillable

Not every question can be answered in a chat. Matt splits them by **fidelity**:
*low-fidelity* questions need no picture to answer ("what URL should this live
on?") and are grillable; *high-fidelity* questions can only be answered by seeing
the thing ("how should this UI feel?", "one big form or several pages?"). Trying
to grill a high-fidelity question is a top failure mode — the move is to hand off
to a prototype session, build enough to answer it, then hand back:
**grill → prototype → grill again**. Matt names this move on its own —
**prototyping**: having the agent build a quick, rough version precisely *when
conversation is too low-fidelity* and you need a real artifact to react to. It's
the general escape from a stalled design concept, not a grilling-only step: when
talk can't resolve a decision, stop talking and make something to talk about.
Grilling is also a *conversation, not an
interview*: stay active and steer, or the agent explodes the scope with hundreds
of low-fidelity questions; but don't over-grill low-fidelity detail when you
should be writing code.

## Under-specification is the disease; a shared concept, not a PRD, is the cure

Asked about an AFK agent that ran for two hours making wrong assumptions and
needing constant steering, Matt diagnoses it as the **classic symptom of
under-specification** — *"no-one knows exactly what they want"* (the Pragmatic
Programmer line). The fix is *not* a heavyweight detailed PRD; that's "overkill."
The fix is to **reach a shared design concept first** — "not necessarily an asset,
but a shared *understanding*" — via the adversarial conversation of having the
agent grill you before it builds. A plain conversation discussing the finer
details ahead of building is enough; the deliverable is alignment, not a
document. **The human, not the agent, decides when enough detail has been given**
— the onus is on the person driving, and how long that takes scales with the size
of the task. This is grilling's reason for existing, restated as a cure for the
specific failure mode of long autonomous runs drifting off intent.

## Scope grilling to stay in the smart zone

A grilling session accumulates tokens fast, and past the model's "dumb zone"
(~120k) its answers degrade — so an over-large scope is self-defeating. The fix
is to have the agent break a big scope into smaller grillable chunks up front and
grill each separately. Use a **smart (high-parameter) model** for grilling
specifically: grilling leans on the model's *parametric* knowledge (its innate
sense of what you haven't considered) rather than the *contextual* knowledge that
dominates implementation, and a small model simply won't surface good
suggestions. Because each session is one slow human-paced thread, you can run two
or three **in parallel** like Slack threads to multiply throughput. (Smart/dumb
zone: see `keep-the-agent-in-the-smart-zone`.)

## grill-me vs grill-with-docs

`grill-me` lives in *productivity* for general use without a codebase;
`grill-with-docs` is the *engineering* successor for when you have code, folding
the grilling session together with live glossary capture (see
`shared-language-as-agent-fuel`). The rule is simple: codebase →
`grill-with-docs`; no codebase → `grill-me`.

The sharpest statement of *why* the docs-capturing variant beats the bare
interview: a plain interview "sharpens your thinking and then evaporates when
the session ends"; `grill-with-docs` instead captures each term the moment it
resolves into `CONTEXT.md` and records the hard, one-way decisions as ADRs, so
**the alignment survives the conversation instead of living only in your
head.** That framing also supplies the choice between three related skills, not
just two: want the interview with no lasting artifact → `grilling`; the plan is
already clear and you just need to pin down or record terminology → the active
discipline in `domain-modeling` (see `domain-modeling-active-discipline`); want
both the interview and the docs, starting from scratch → `grill-with-docs`.

Matt has since demoted `grill-me` further down his own stack. He now recommends
starting codebase-aware planning with **`domain-model`** — the skill that checks a
plan against the codebase's language, `CONTEXT.md`, and ADRs (the `grill-with-docs`
lineage) — as the default front of the planning chain: `domain-model → to-prd →
to-issues → tdd`. `grill-me` is kept as the *lighter* tool: a relentless interview
about a plan for when you don't yet need the full domain-model workflow — before a
PRD, before implementing a feature, before committing to a data model or API shape,
or whenever you want the agent to push back instead of agree.

## Grilling is a reusable primitive — now literally extracted into one

Grilling is not a one-off skill; it's a sub-routine other skills drop into.
`triage` runs a grilling session to flesh out an underspecified issue;
`improve-codebase-architecture` grills the user through the design of a chosen
refactor. Establishing "interview to alignment" as a named, reusable move is
what lets the heavier workflows assume the human and agent actually agree before
work starts.

This principle was eventually made structural. The relentless-interview logic —
previously duplicated verbatim in `grill-me` and `grill-with-docs` — was extracted
into a single **model-invoked** `grilling` skill (the one-paragraph "interview me
relentlessly… one question at a time… explore the codebase instead" loop). The two
former skills collapsed to thin **user-invoked** wrappers: `grill-me` is now just
"Run a `/grilling` session", and `grill-with-docs` is "Run a `/grilling` session,
using the `/domain-modeling` skill" — so the only difference between them is that
the codebase variant also fires the active glossary-building discipline (see
`domain-modeling-active-discipline`). This is the invocation-axis refactor applied
to grilling: the orchestrators a human types stay thin; the reusable competence
lives in a model-invoked primitive that other skills (and the model) can reach
(see `invocation-axis-user-vs-model`).

## Don't enact until the shared understanding is confirmed

A later revision adds one explicit gate to the primitive itself: *"Do not enact
the plan until I confirm we have reached a shared understanding."* Without it,
an interview that trails off (the human stops answering, or the agent judges the
tree "resolved enough") could slide straight into building on an alignment that
was never actually confirmed — silently reintroducing the exact misalignment
failure mode the whole grilling technique exists to prevent. Naming the gate
explicitly turns "we're aligned" from an inference the agent makes on its own
into a fact only the human gets to assert.

## Sources

- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/skills-productivity-grill-me-SKILL.md-5d73b98f.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/grill-me/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/skills-engineering-grill-with-docs-SKILL.md-1015ebf3.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/grill-with-docs/SKILL.md (revision 2026-06-17)
- `sources/mattpocock/skills-repo/skills-productivity-grilling-SKILL.md-84a3ca23.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/productivity/grilling/SKILL.md (revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/8fb15cf60fd1db0ed9b23abb9b87956ab2d63ffc — the "do not enact until confirmed" gate; revision 2026-07-07, origin https://github.com/mattpocock/skills/blob/8b33f408156c94ffaafac979e4be1f6f96b3d6a3 — the fact/decision split on the "prefer the codebase" rule)
- `sources/mattpocock/skills-repo/docs-productivity-grilling.md-f585c446.md` — origin: https://github.com/mattpocock/skills/blob/5a4191541c97ec759a4c21ef9d9875e8d3f42507/docs/productivity/grilling.md (revision 2026-07-03, origin https://github.com/mattpocock/skills/blob/34435929c02d4238a5390a4aab533ece2842535b — the same gate, on the docs page)
- `sources/mattpocock/aihero/https-www.aihero.dev-things-people-get-wrong-with-grill-me-a-2cf46126.md` — origin: https://www.aihero.dev/things-people-get-wrong-with-grill-me-and-grill-with-docs
- `sources/mattpocock/aihero/https-www.aihero.dev-my-grill-me-skill-has-gone-viral-2f0f061b.md` — origin: https://www.aihero.dev/my-grill-me-skill-has-gone-viral
- `sources/mattpocock/aihero/https-www.aihero.dev-grill-with-docs-d376dfd1.md` — origin: https://www.aihero.dev/grill-with-docs (revision 2026-07-02 — the "paper trail" framing and the three-way routing between `grilling`/`domain-modeling`/`grill-with-docs`)
- `sources/mattpocock/aihero/https-www.aihero.dev-5-agent-skills-i-use-every-day-056774d5.md` — origin: https://www.aihero.dev/5-agent-skills-i-use-every-day
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-grill-me-8337a3c4.md` — origin: https://www.aihero.dev/skills-grill-me
- `sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md` — origin: https://www.aihero.dev/ai-coding-dictionary (revision 2026-06-05, "Prototyping")
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067524579455578372-692b7037.md` — origin: https://x.com/mattpocockuk/status/2067524579455578372
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067536646459855215-ebf9adea.md` — origin: https://x.com/mattpocockuk/status/2067536646459855215
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067592457957650920-5ed8b7b0.md` — origin: https://x.com/mattpocockuk/status/2067592457957650920
