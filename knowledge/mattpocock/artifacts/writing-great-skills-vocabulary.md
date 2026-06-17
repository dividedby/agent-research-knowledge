# Writing great skills: predictability and its levers

`writing-great-skills` (which replaced `write-a-skill`) is a reference skill whose
whole domain model is "what makes a skill great." Its root claim is sharp: **a
skill exists to wrangle determinism out of a stochastic system**, and the virtue
every other lever serves is **predictability** — the agent taking the same
*process* every run, not producing the same *output* (a brainstorming skill should
predictably *diverge*). Cost and maintainability are symptoms of predictability,
not rivals to it. The skill ships its full definitions in a sibling `GLOSSARY.md`,
itself a worked example of progressive disclosure.

This is the matured, theory-backed successor to the looser
`skill-anatomy-and-progressive-disclosure` notes — it names the levers precisely
and gives each an *avoid* list.

## The two loads, and granularity as spending them

The central trade-off is two distinct costs a skill can impose:

- **Context load** — what a *model-invoked* skill costs the agent: its
  `description` sits in the window every turn, spending tokens and attention.
- **Cognitive load** — what a *user-invoked* skill costs the *human*: they are the
  index who must remember it exists. Not a cost to minimise — it is "the price of
  human agency."

**Granularity** (how finely you divide skills) spends one load per cut. Two
sanctioned cuts: **by invocation** (split off a model-invoked skill only when it
has a distinct triggering *leading word* or another skill must reach it — you pay
context load for the new always-loaded description) and **by sequence** (split a
run of steps when the *post-completion steps* still in view tempt the agent to
rush the current one). A **router skill** cures piled-up cognitive load when
user-invoked skills multiply (this is exactly what `ask-matt` is).

## The information hierarchy and co-location

Content sorts onto a three-rung ladder by how immediately the agent needs it:
**in-skill steps** (ordered actions, the primary tier) → **in-skill reference**
(definitions/rules, often a legitimately flat peer-set) → **external reference**
(disclosed behind a *context pointer*, loaded only when the pointer fires).
**Progressive disclosure** is the move *down* the ladder to keep the top legible;
**branching** licenses it — inline what every branch needs, disclose what only some
reach. A **context pointer**'s *wording*, not its target, decides when and how
reliably the agent reaches the material — so a must-have behind a weak pointer is a
variance bug fixed by sharpening the wording, not by inlining. **Co-location** is
the orthogonal move: once material is on a rung, keep a concept's definition,
rules, and caveats under one heading so reading one part brings its neighbours.

## Completion criteria carry two independent properties

Every step ends on a **completion criterion**, and it has two separable axes:
**clarity** (can the agent tell done from not-done?) resists *premature completion*
and needs steps to bite; **demand** (how much it requires — "every modified model
accounted for" vs "produce a change list") sets **legwork**, the digging the agent
does within a step, and binds flat reference too ("every rule applied"). The
strongest criteria are both checkable and exhaustive.

## Leading words: recruit pretraining priors

A **leading word** is a compact concept already in the model's pretraining
(`lesson`, `fog of war`, `tracer bullets`, `tight`, `red`) that the agent thinks
with while running the skill. Repeated as a *token* (never restated as a
sentence), it accumulates a distributed definition and anchors a whole region of
behaviour in the fewest tokens. It serves predictability twice — anchoring
*execution* in the body and *invocation* in the description (word the description
with the leading words you actually type when you want the skill). Coining your own
works only if you define it; a made-up word recruits no priors, so reach for an
existing one first. Examples of collapsing restatement into a leading word: "fast,
deterministic, low-overhead" → *tight*; "a loop you believe in" → *red*.

## The named failure modes — a diagnostic kit

The skill's most reusable contribution is a vocabulary of skill pathologies, each
with a test:

- **Premature completion** — ending a step early as attention slips to *being
  done*; a between-steps failure. Defend in order: sharpen the criterion first
  (cheap, local); only hide post-completion steps by splitting if the bound is
  irreducibly fuzzy *and* you observe the rush — and hiding works only across a
  real context boundary (a user-invoked hand-off or subagent), not an inline call.
- **Duplication** — the same meaning in two places; costs maintenance and tokens
  and inflates a meaning's ladder rank. The accidental inverse of a leading word.
- **Sediment** — stale layers that accrete because adding feels safe and removing
  risky; the default fate of any skill without a pruning discipline.
- **Sprawl** — a skill simply too long even when every line is live and unique;
  cured by the hierarchy (disclose, split by branch/sequence).
- **No-op** — a line the model already obeys by default, so you pay load to say
  nothing. The test — *does it change behaviour vs the default?* — is model-
  relative (settle disputes by running the skill, not debating), and is also how
  you grade whether a leading word is earning its repetitions (a leading word too
  weak to beat the default is a no-op; the fix is a stronger word).

Pruning is the discipline against these: keep each meaning in a **single source of
truth**, check every line for **relevance** (does it still bear on the task?), then
hunt no-ops *sentence by sentence* and delete whole sentences rather than trim
words — "be aggressive."

## Sources

- `sources/mattpocock/skills-repo/skills-productivity-writing-great-skills-SKILL.md-b96ebc68.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/productivity/writing-great-skills/SKILL.md
- `sources/mattpocock/skills-repo/skills-productivity-writing-great-skills-GLOSSARY.md-1e43a906.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/productivity/writing-great-skills/GLOSSARY.md
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md
