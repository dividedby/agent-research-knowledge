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

## Skip it and pay later: the aphorisms and a live example

Matt compresses the whole argument for grilling into repeatable one-liners:
**"Get grilled before you build"** and **"Talk shop before you slop"** are the
imperative form of the discipline above — interview first, write code second,
never the reverse. The cost asymmetry is why: **"If you only align after you've
built something then it's much more expensive to alter. It's like sending back a
dish once a waiter has already brought it out."** Whatever questions a grilling
session would have surfaced don't disappear if you skip it — **"those questions
can either be answered before building or after… they are faster and cheaper to
answer before."**

He's caught himself skipping it, too: firing off `/prototype` straight on a new
feature (a teleprompter view for his video editor) without grilling first, he
calls the result "shite" and names the fix in the same breath — "Should have run
`/grill-with-docs` first." The failure mode the whole discipline exists to
prevent isn't hypothetical or reserved for other people's workflows — its own
author reaches for the shortcut occasionally too, and pays the
under-specification tax when he does.

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
should be writing code. Recording the failure at a concrete scale: filming a
`/grill-me` course lesson, the skill fired **46 questions** at him in one
session — his own reaction, "Dude, chill, you're scaring the noobs," is the
runaway-interview failure mode caught live, not just described in the abstract.
Pressed later on whether 46 questions was something to brag about, Matt
qualifies the scale: they landed "over four rounds," which softens the number
once you read it against the round-batching model (see "Update: grill-me and
grill-with-docs adopt rounds too (v1.2)" below) — 46 questions sounds like a
runaway interview one-at-a-time, but is a more modest ~11-per-round average
under batching.

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

## grill-me vs batch-grill-me: one question or the whole frontier at once

`batch-grill-me` keeps grilling's design-tree/interview shape but breaks its
first rule on purpose: instead of one question at a time, it asks the whole
**frontier** in a single round — every decision whose prerequisites are already
settled — numbering each question with a recommended answer, then waits for the
user's answers before recomputing the frontier for the next round. A question
whose answer still depends on another open question stays out of the current
round; it only enters once its prerequisite resolves and pushes the frontier
outward. This borrows the frontier vocabulary wayfinder coined for planning
across sessions (see `decision-mapping-fog-of-war`) and applies it *within* a
single live interview: batching is safe precisely because "frontier" already
means "the questions answerable right now without guessing," so a round never
dumps a question the user isn't yet equipped to answer. The trade this makes
explicit: `grill-me`'s one-at-a-time pacing protects interview depth (each
question can build on the last answer); `batch-grill-me`'s round pacing trades
that depth for throughput — useful when the tree is wide (many independent
branches) rather than deep. It restates the fact/decision split as a non-blocking
rule: a frontier question needing a fact is dispatched to a sub-agent rather
than asked, and only the questions *downstream* of that lookup wait — the rest
of the round's questions still go to the user immediately. As with grilling, the
session isn't over until the user confirms a shared understanding; an empty
frontier ends the interview, but it still doesn't authorize acting on it alone.

A field report quantifies the throughput trade: a plan that would have taken
13 questions across 13 one-at-a-time rounds resolved in 3 rounds under
`batch-grill-me`'s frontier batching — each round dumping every question
whose prerequisites were already settled. The fact/decision split holds under
batching too: a frontier question needing a lookup is scheduled as a
background research sub-agent rather than asked, so the round doesn't stall
waiting on it.

## Update: grill-me and grill-with-docs adopt rounds too (v1.2)

The rounds model didn't stay confined to `batch-grill-me`. In v1.2, the
front-door skills themselves drop grilling's original "one question at a
time" rule in favor of the same round-based batching: "faster, less token
spend, but still keeps dependencies between questions clear." Matt confirmed
the timing directly when asked: "Yep, batching is coming to all grillings in
1.2." Dependency
tracking survives the switch — asked directly whether a previously-answered
question still shapes the next one, Matt confirms it does. Nor does the
interaction mechanism change: `AskUserQuestion` still presents each round: the
round model is a batching change to the interview's shape, not a new UI. This
narrows the distinction the "grill-me vs batch-grill-me" section above draws —
depth-preferring one-at-a-time pacing was, for a time, `grill-me`'s
differentiator from the round-batching in-progress variant; as of v1.2 that
differentiator is gone from the front door itself. Fielding a user's own
recommendation for round-based batching, Matt confirms it's already landed:
"In 1.2, grilling asks questions in rounds — agree with your rec here."

## When not to automate the decision to prototype

Fidelity misjudgment cuts the other way too: asked about a workflow where
prototype tickets get auto-spawned as subtickets and sometimes over-trigger,
Matt's answer draws a line around *who* decides to prototype, not just *when*
prototyping is the right move. Recognizing you're at the wrong fidelity for a
discussion is itself a hard call, and prototypes are expensive to build but
critical when actually needed — so taking that decision out of the user's
hands is "probably not the right call." He floats making it a human-checked
step rather than something the map decides unilaterally. The fidelity split
this doc already draws (grillable vs. needs-a-prototype) is a judgment call;
this sharpens it further — whether to *trigger* a prototype automatically is
itself a decision worth keeping in the human's hands, not just the underlying
fidelity question.

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
(see `invocation-axis-user-vs-model`). Matt states the composition just as
tersely when asked directly: "Yeah, `/grill-with-docs` just runs
`/domain-modeling` + `/grilling`."

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
- `sources/mattpocock/skills-repo/skills-in-progress-batch-grill-me-SKILL.md-51100ca0.md` — origin: https://github.com/mattpocock/skills/blob/9603c1cc8118d08bc1b3bf34cf714f62178dea3b/skills/in-progress/batch-grill-me/SKILL.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2077715572788224003-a371807c.md` — origin: https://x.com/mattpocockuk/status/2077715572788224003
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2077720474344174039-798b5e1c.md` — origin: https://x.com/mattpocockuk/status/2077720474344174039
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2078077849785815465-ef541a6b.md` — origin: https://x.com/mattpocockuk/status/2078077849785815465
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2078080679070339222-b2fe8d2d.md` — origin: https://x.com/mattpocockuk/status/2078080679070339222
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079534578285371544-7a3fa317.md` — origin: https://x.com/mattpocockuk/status/2079534578285371544
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2078812658141180341-28ab1112.md` — origin: https://x.com/mattpocockuk/status/2078812658141180341
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2078052653993447522-9db27eb3.md` — origin: https://x.com/mattpocockuk/status/2078052653993447522
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079845268707516835-ae522041.md` — origin: https://x.com/mattpocockuk/status/2079845268707516835
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081473558698492060-fd2be5af.md` — origin: https://x.com/mattpocockuk/status/2081473558698492060
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081474728913510855-5733c6f9.md` — origin: https://x.com/mattpocockuk/status/2081474728913510855
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081475376383979929-41fd71d7.md` — origin: https://x.com/mattpocockuk/status/2081475376383979929
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081475524128383293-5caf67ca.md` — origin: https://x.com/mattpocockuk/status/2081475524128383293
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081482446566998172-40e60dfb.md` — origin: https://x.com/mattpocockuk/status/2081482446566998172
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081739847912378406-e06245b2.md` — origin: https://x.com/mattpocockuk/status/2081739847912378406
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083247554985169028-f1445fd6.md` — origin: https://x.com/mattpocockuk/status/2083247554985169028
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083195552703943148-3657e44d.md` — origin: https://x.com/mattpocockuk/status/2083195552703943148
