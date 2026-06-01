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
- **Prefer the codebase over the human.** "If a question can be answered by
  exploring the codebase, explore the codebase instead." The human's attention
  is the scarce resource; spend it only on what the code can't tell you.

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
**grill → prototype → grill again**. Grilling is also a *conversation, not an
interview*: stay active and steer, or the agent explodes the scope with hundreds
of low-fidelity questions; but don't over-grill low-fidelity detail when you
should be writing code.

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

Matt has since demoted `grill-me` further down his own stack. He now recommends
starting codebase-aware planning with **`domain-model`** — the skill that checks a
plan against the codebase's language, `CONTEXT.md`, and ADRs (the `grill-with-docs`
lineage) — as the default front of the planning chain: `domain-model → to-prd →
to-issues → tdd`. `grill-me` is kept as the *lighter* tool: a relentless interview
about a plan for when you don't yet need the full domain-model workflow — before a
PRD, before implementing a feature, before committing to a data model or API shape,
or whenever you want the agent to push back instead of agree.

## Grilling is a reusable primitive

Grilling is not a one-off skill; it's a sub-routine other skills drop into.
`triage` runs a grilling session to flesh out an underspecified issue;
`improve-codebase-architecture` grills the user through the design of a chosen
refactor. Establishing "interview to alignment" as a named, reusable move is
what lets the heavier workflows assume the human and agent actually agree before
work starts.

## Sources

- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/skills-repo/skills-productivity-grill-me-SKILL.md-5d73b98f.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/grill-me/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-grill-with-docs-SKILL.md-1015ebf3.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/grill-with-docs/SKILL.md
- `sources/mattpocock/aihero/https-www.aihero.dev-things-people-get-wrong-with-grill-me-a-2cf46126.md` — origin: https://www.aihero.dev/things-people-get-wrong-with-grill-me-and-grill-with-docs
- `sources/mattpocock/aihero/https-www.aihero.dev-my-grill-me-skill-has-gone-viral-2f0f061b.md` — origin: https://www.aihero.dev/my-grill-me-skill-has-gone-viral
- `sources/mattpocock/aihero/https-www.aihero.dev-grill-with-docs-d376dfd1.md` — origin: https://www.aihero.dev/grill-with-docs
- `sources/mattpocock/aihero/https-www.aihero.dev-5-agent-skills-i-use-every-day-056774d5.md` — origin: https://www.aihero.dev/5-agent-skills-i-use-every-day
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-grill-me-8337a3c4.md` — origin: https://www.aihero.dev/skills-grill-me
