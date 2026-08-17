# domain-modeling: the active build-the-glossary discipline

`domain-modeling` is the model-invoked skill that *actively builds and sharpens* a
project's domain model — and its first design decision is to draw a hard line
between active and passive work. Merely **reading** `CONTEXT.md` for vocabulary is
a one-line prose pointer any skill can do; it is explicitly *not* this skill. The
skill fires only when you are **changing the model** — challenging terms,
inventing edge-case scenarios, recording decisions — not when you are consuming
it. (This is why `grill-with-docs`, which builds docs as it interviews, runs
`domain-modeling`, while a skill that only respects existing vocabulary just
references `CONTEXT.md` in passing.)

This is the synthesis-time complement to `shared-language-as-agent-fuel`
(why a glossary pays off) and `adrs-as-agent-memory` (what ADRs are for): this
doc captures the *skill mechanics* that produce them.

## The five in-session moves

The discipline is a set of interventions the agent makes mid-conversation, written
to capture decisions *the moment they crystallise* rather than batching:

- **Challenge against the glossary** — when a term conflicts with `CONTEXT.md`,
  call it out immediately ("your glossary defines 'cancellation' as X, but you
  seem to mean Y").
- **Sharpen fuzzy language** — propose a precise canonical term for an overloaded
  word ("'account' — do you mean Customer or User?").
- **Discuss concrete scenarios** — stress-test relationships with invented
  edge-case scenarios that force precision about boundaries.
- **Cross-reference with code** — when the user states how something works, check
  the code agrees and surface contradictions.
- **Update `CONTEXT.md` inline** — write the resolved term down right there, never
  later.

## CONTEXT.md is a glossary, nothing else

The skill is emphatic that `CONTEXT.md` is "totally devoid of implementation
details" — not a spec, scratch pad, or decision log. The `CONTEXT-FORMAT.md`
companion gives the shape: per-term `**Name**: one-or-two-sentence definition` with
an opinionated `_Avoid_:` list of rejected synonyms, define what a thing *is* not
what it *does*, and only include terms *specific to this project's context* (general
programming concepts like timeouts don't belong). Files are created **lazily** —
the root `CONTEXT.md` appears only when the first term is resolved. Multi-context
repos carry a `CONTEXT-MAP.md` at the root listing each context, where it lives,
and how the contexts relate (event flows, shared types); the skill infers
single-vs-multi from which files exist and asks if unclear.

## ADRs offered sparingly, behind a three-part gate

The `ADR-FORMAT.md` companion makes the ADR deliberately minimal — title plus 1–3
sentences of context/decision/why is a complete ADR; sections like Status,
Considered Options, Consequences are optional and added only when they earn their
place. The discipline is in *when* to offer one: all three must hold —
**hard to reverse**, **surprising without context**, and **the result of a real
trade-off**. Miss any one and you skip it (easy-to-reverse decisions get reversed;
unsurprising ones nobody questions; no-alternative ones record nothing). Worth-
recording cases are spelled out: architectural shape, cross-context integration
patterns, lock-in technology choices, boundary/scope no-s, deliberate deviations
from the obvious path, invisible constraints, and non-obvious rejected
alternatives. This is the exact bar this repo's own `CLAUDE.md` adopts for its
ADRs.

The gate is meant to bite hard in practice, not just in theory: "most sessions
produce a sharper glossary and few or no ADRs, and that's the intended shape."
A session that mints an ADR every time is a sign the gate isn't being applied —
the glossary is the expected steady output, the ADR the rare exception.

## When the glossary itself has drifted, re-run the discipline on it

The five moves above assume a live interview building the glossary forward.
Matt also names the fix for the opposite problem — a glossary that's already
been written but has since become confusing to its own owner. Told by a user
that they were "having a hard time even understand[ing] my own glossary now,"
his answer treats it as the same discipline applied retroactively rather than
a new tool: "go back through it and use the domain-modeling skill to make sure
it's aligned with what you want." A `CONTEXT.md` isn't a write-once artifact —
if it stops being legible, the fix is to re-run the same challenge-and-sharpen
moves against the existing file, not to abandon it or start a fresh one.

A model-invoked skill's trigger description isn't exempt from that same
maintain-don't-just-create posture. The skill's own description originally
gave editing only an indirect branch — "record an architectural decision,"
"pin down domain terminology," or the catch-all "another skill needs to
maintain the domain model" — leaving a session that only *edits* an existing
`CONTEXT.md` or ADR to be inferred rather than named. It was later revised to
name editing directly on each concrete artifact: "writing or editing a
CONTEXT.md," "recording or editing an ADR." A trigger branch left implicit is
a branch the model may not reliably fire on; naming maintenance explicitly,
not just creation, is what makes the description's coverage match what the
discipline above already does.

## Writing can silently fail inside someone else's orchestration layer

Empty output has two causes, and only one is benign. The mundane one: nothing
qualified — ADRs need all three gates, and a session with no new vocabulary
genuinely has nothing to write to `CONTEXT.md`. The filed-and-unfixed one: when
`grill-with-docs` runs *inside* another orchestration layer — a
spec-driven-development wrapper, a multi-agent framework, a rule that invokes
it as one step in someone else's pipeline — the file-writing half is reported
to silently not happen while the interview itself still runs to completion. An
agent (or a human skimming the transcript) has no signal that the write was
dropped; the only check is to look at the working directory afterward rather
than trust that a completed interview means `CONTEXT.md`/ADRs actually landed.

## The glossary and ADRs are not a full decision ledger

The most substantive open complaint about the discipline: everything that
crystallises in a grilling session but doesn't meet the glossary bar or the
three-part ADR gate goes into the conversation and nowhere else. There's no
ledger tying a resolved answer through to the spec, the ticket, and the test
that's supposed to enforce it downstream — and *precise* answers are the ones
that suffer most, because ordering guarantees, negative requirements, and
numeric defaults get softened into weaker prose the further downstream they
travel. The result can look complete (a plausible spec, plausible tickets)
while quietly missing the thing that was actually decided. The mitigation
available today isn't structural: keep the session alive and feed it straight
into `to-spec` rather than clearing it, and re-read the resulting spec against
your own answers instead of assuming synthesis captured them faithfully.

## Bootstrapping a repo with zero docs: pair it with improve-codebase-architecture

`grill-with-docs` is also the right tool for a codebase that has no ADRs, no
domain language, and no design principles at all — aimed at the repo itself
rather than at one change ("help me document my repo"). The community pattern
for this cold-start case is to pair it with `improve-codebase-architecture`:
one skill surfaces the seams and structure worth naming, the other captures
the resulting vocabulary and decisions. Expect to steer it more than a normal
session — it reads code and asks about what it finds, and the human is still
the one who decides which of the words already living in the codebase are the
canonical ones.

## The stateful artifacts assume one writer, and drift when that assumption breaks

`grill-with-docs`'s `CONTEXT.md`/ADR output is designed around a single person
curating it, and the assumption is load-bearing, not incidental. A two-developer
team running the workflow for four months in one repo reported state drift on
roughly 20% of sampled merged PRs, with ADR citations and README claims the
highest-drift surfaces — the deliberate, human-curated docs drifted *worse*
than agent-generated memory did over the same period. A one-off pruning sweep
of the stale docs didn't hold either; the same sweep was stale again within
days, because nothing separates one contributor's session from another's or
re-checks a claim once it's written. What actually worked was blunter:
deleting the shadow state outright and adding a deterministic citation-and-link
linter to CI, rather than trying to keep the prose itself continuously
accurate. A related, unfixed failure shows up even for a solo user: running the
skill repeatedly across unrelated changes in one repo tends to accumulate
mixed-topic docs, because nothing marks where one session's output ends and the
next one's begins.

There's also a live objection to the premise that grounds this drift risk: the
sharpest public pushback on the whole discipline is that a canonical term and
its plain-English expansion get the *same* result from the model — so the
vocabulary's real value is compressing communication between the humans who
share it, not improving the agent's performance. That reading doesn't make the
glossary worthless, but it relocates the payoff: keeping `CONTEXT.md` accurate
matters most for keeping a team of *people* aligned with what the agent is
doing, which is exactly the alignment a stale, drifted glossary quietly
undermines.

## A bloated glossary is a symptom, and the fix is the same skill run backwards

A `CONTEXT.md` that's grown to 500, 1,000, or 3,000 lines has absorbed
implementation detail and decisions that were never glossary material — size
is the symptom, not the disease. The fix is a direct instruction back through
the same skill rather than a manual prune: `/grill-with-docs make my
CONTEXT.md more concise and remove any implementation details from it`, run
against the bloated file, removes most of it. Splitting into a
`CONTEXT-MAP.md` and multiple per-context files is worth reaching for only
once a file is genuinely lean and still covers two domains a reader wouldn't
want to hold at once — splitting a bloated file just produces several bloated
files. There's no guardrail in the skill today that prevents the growth in the
first place; concision is a periodic maintenance pass, not a standing
property.

## Sharper terms don't help everywhere: the payoff is upstream, not near the code

DDD-style precision gets less useful the closer it gets to implementation — the
real payoff is upstream, in naming and concept alignment, not in aggregates
and layer ceremony. Synonym control matters most at *naming boundaries*:
module names, table names, status enums, issue titles, CLI commands. It
matters much less in ordinary prose, and on a one-day build the discipline is
worth skipping entirely. There's also an honest failure mode worth naming: an
unreviewed, agent-authored glossary is worse than none, because it becomes
confident-sounding lore that later sessions treat as established truth without
anyone having actually checked it.

## Not deprecated — absorbed and expanded

Asked whether the standalone `ubiquitous-language` skill had been dropped,
Matt corrects the framing: "Opposite - moved into `/domain-modelling`,
integrated more deeply with every part of the process." The skill didn't
disappear when it was folded in (see `shared-language-as-agent-fuel`); it
became a discipline other skills invoke rather than a thing you run on its
own — going from one narrow entry point to something woven through the whole
`grill-with-docs`/`wayfinder` chain is a promotion, not a removal.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-domain-modeling-SKILL.md-afe6b5a2.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/domain-modeling/SKILL.md (revision 2026-08-14, origin https://github.com/mattpocock/skills/blob/9e8760ab7d4cd49433dcda5dbec74f3c2ac8f9a4/skills/engineering/domain-modeling/SKILL.md — the trigger description revised to name editing an existing CONTEXT.md/ADR directly, not just creating one)
- `sources/mattpocock/skills-repo/skills-engineering-domain-modeling-CONTEXT-FORMAT.md-d4513441.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/domain-modeling/CONTEXT-FORMAT.md
- `sources/mattpocock/skills-repo/skills-engineering-domain-modeling-ADR-FORMAT.md-0fcfff53.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/engineering/domain-modeling/ADR-FORMAT.md
- `sources/mattpocock/skills-repo/docs-invocation.md-1ce78905.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/docs/invocation.md
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
- `sources/mattpocock/aihero/https-www.aihero.dev-grill-with-docs-d376dfd1.md` — origin: https://www.aihero.dev/grill-with-docs (revision 2026-07-02 — "most sessions produce a sharper glossary and few or no ADRs"; revision 2026-08-11 — the "assumes one writer" state-drift field report and the plain-English-expansion pushback)
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-grill-with-docs-ee25180c.md` — origin: https://www.aihero.dev/skills-grill-with-docs
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-domain-modeling-6c2be29b.md` — origin: https://www.aihero.dev/skills-domain-modeling
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2084255866543390766-29f40882.md` — origin: https://x.com/mattpocockuk/status/2084255866543390766
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085674908051275993-c3c44927.md` — origin: https://x.com/mattpocockuk/status/2085674908051275993
- `sources/mattpocock/skills-repo/docs-engineering-grill-with-docs.md-95a415e1.md` — origin: https://github.com/mattpocock/skills/blob/b848e846456fba9cc3f06a768cee78011042011f/docs/engineering/grill-with-docs.md (revision 2026-08-06 — the "Common questions" FAQ: the orchestration-layer silent-write-failure bug, the "no ledger tying answers to spec/ticket/test" complaint, and the pairing with `improve-codebase-architecture` for a repo with no docs at all)
