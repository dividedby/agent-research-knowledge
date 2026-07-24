# Writing great skills: predictability and its levers

`writing-great-skills` (which replaced `write-a-skill`) is a reference skill whose
whole domain model is "what makes a skill great." Its root claim is sharp: **a
skill exists to wrangle determinism out of a stochastic system**, and the virtue
every other lever serves is **predictability** — the agent taking the same
*process* every run, not producing the same *output* (a brainstorming skill should
predictably *diverge*). Cost and maintainability are symptoms of predictability,
not rivals to it. The skill ships its full definitions in a sibling `GLOSSARY.md`,
itself a worked example of progressive disclosure — whose terms are grouped by
four axes so the taxonomy is explicit: **Invocation** (how a skill is reached),
**Information Hierarchy** (how its content is arranged), **Steering** (how runtime
behaviour is shaped), and **Pruning** (how it is kept lean), with each failure
mode parked beside the lever that cures it.

This is the matured, theory-backed successor to the looser
`skill-anatomy-and-progressive-disclosure` notes — it names the levers precisely
and gives each an *avoid* list. Matt's own daily usage backs the claim: `/writing-great-skills`
is, in his words, "quickly becoming my most often-invoked skill" — evidence that a
skill about skill quality earns its keep by being reached for constantly, not
written once and left.

## The two loads, and granularity as spending them

The central trade-off is two distinct costs a skill can impose:

- **Context load** — what a *model-invoked* skill costs the agent: its
  `description` sits in the window every turn, spending tokens and attention.
- **Cognitive load** — what a *user-invoked* skill costs the *human*: they are the
  index who must remember it exists. Not a cost to minimise — it is "the price of
  human agency."

**Renaming a model-invoked skill pays this same cost, which is why Matt rejects
symlinking old and new names side by side.** Asked why not keep the old skill
name as a symlink to ease the transition, his answer is the context-load
argument applied to migration: "symlinking a model-invoked skill would mean
costing every user a non-zero amount of tokens every request" — a duplicate
registration means a duplicate always-loaded `description`, charged on every
turn to every user, indefinitely. **Better to just move it** — pay the one-time
churn of a hard rename over the standing, compounding cost of a permanent
duplicate. (An expiring redirect note is the milder alternative he didn't
reject outright, but the default move is the clean break.)

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
- **Negation** — steering by *prohibition* backfires: "don't think of an
  elephant" names the elephant and makes it *more* available, not less; "never
  write verbose comments" drags verbosity into the frame it's meant to forbid.
  The weakly-worded ban half-reads as an instruction to do the forbidden thing,
  because the strongly-activated concept it names overruns the negation
  modifying it. The cure is to prompt the **positive** — describe the target
  behaviour ("write one-line comments") so the banned one is never spoken at
  all. A prohibition earns its place only as a hard guardrail on behaviour you
  genuinely can't phrase positively, and even then pair it with the positive
  target so attention lands on what to do, not just what to avoid.
- **Negative Space** — the adjacent, opposite-direction blind spot: steering
  done by what a skill *leaves out*, not what it says. Every decision a skill's
  author declines to make on the page — a branch left unaddressed, a case never
  mentioned — isn't neutral; it's silently delegated to the agent's priors,
  which fill the gap with whatever's most probable rather than what the author
  actually wanted. Negation is a misfire in something written; Negative Space is
  the failure of never having written anything there at all. The cure is to
  read a draft specifically for its silences and decide each omission on
  purpose — either fill it with an explicit instruction, or leave it open as a
  deliberate, named **branch** the agent is meant to choose on its own. Carried
  as a full failure mode alongside Negation, not folded into it, because the
  two need different diagnostics: one is caught by reading what's on the page,
  the other only by asking what isn't.

Pruning is the discipline against these: keep each meaning in a **single source of
truth**, check every line for **relevance** (does it still bear on the task?), then
hunt no-ops *sentence by sentence* and delete whole sentences rather than trim
words — "be aggressive."

## The no-op is context-relative, and the deletion test is how you find it

Matt's sharpest public framing of the no-op: agent-authored skills are *littered*
with them — "Be thorough", "Make the commit message very detailed", "Make the
implementation easy to read" — because **agents already do these by default**.
Such a line pays load (tokens, attention) to say nothing the model wasn't already
going to do, and it makes the skill harder to evaluate and maintain. The test is
operational and blunt: **delete the line and re-run; if the output doesn't
meaningfully change, it was a no-op.** This is also his answer to *how he keeps
skills so short* — "just remove the no-ops, kill duplication, and take out
anything irrelevant; you'll be surprised how little is left, and how effective it
is" — and it has its own pass: `/writing-great-skills "Do a no-op pass on this
skill"`.

Crucially the no-op is **not** a canonical list of forbidden phrases. The same
phrase can change behaviour in one skill and be inert in another — a "be rigorous"
line is dead weight in a 100-line review skill that already *describes* a rigorous
process, but live in a skill that doesn't. So the judgement is per-skill: *can you
delete this line, in this context, with no meaningful change?* (He concedes the
purist objection — every token participates in attention, so nothing is a *literal*
no-op — but holds the practical claim: the phrase's marginal effect here is
negligible, settle disputes by running it rather than debating the theory.)

The flip side of pruning no-ops is **authoring by hand**. Matt's experience is that
*the more of a skill he has handwritten, the better it is* — "paying attention to
each word as you write it is unreasonably effective" — which is the same discipline
the deletion test enforces after the fact, applied up front: every word earns its
place. (He amplified @ankrgyl's "hand-writing prompts is dead; prompt engineering
is not" while disagreeing with the headline — the endorsement is of prompt
engineering's survival, not of abandoning the handwritten word.)

## The skill's own domain may widen past skills specifically

Matt has floated broadening `writing-great-skills` beyond skill authoring to
cover **any writing aimed at an agent** — docs, `AGENTS.md`, and skills alike,
under a candidate name like `/writing-for-agents`. The reasoning behind the
widen: the levers this doc collects (predictability, the two loads, the
information hierarchy, no-ops, negation) aren't actually skill-specific — they
apply to any text a human writes for an agent to read, and a `SKILL.md` is
just one instance of that genre. The rename is still undecided ("no idea what
to name it" at time of writing), but the scoping question itself is the
transferable point: a skill's charter can outgrow its original artifact type
once its underlying levers turn out to be genre-general rather than
format-specific.

## Sources

- `sources/mattpocock/skills-repo/skills-productivity-writing-great-skills-SKILL.md-b96ebc68.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/productivity/writing-great-skills/SKILL.md (revision 2026-07-07, origin https://github.com/mattpocock/skills/blob/ce24f42a242b70cbdda304f3422545a3e452285a — the Negation failure mode)
- `sources/mattpocock/skills-repo/skills-productivity-writing-great-skills-GLOSSARY.md-1e43a906.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/skills/productivity/writing-great-skills/GLOSSARY.md (revision 2026-07-07, origin https://github.com/mattpocock/skills/blob/82ecc586f26c5a31062113faa3cef08e6e394116 — the same Negation term added to the Steering axis)
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/2454c95dc305c158b21a0cdafeb728879dd0359a/CHANGELOG.md (revision 2026-07-09, PR #463, origin https://github.com/mattpocock/skills/blob/af6d6922c3e2b5288eef155346cbe319e4ed3bd0 — the Negative Space failure mode)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069784839474032896-7bd866f0.md` — origin: https://x.com/mattpocockuk/status/2069784839474032896
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069785124950945825-07710416.md` — origin: https://x.com/mattpocockuk/status/2069785124950945825
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069812144183324793-5fce97b8.md` — origin: https://x.com/mattpocockuk/status/2069812144183324793
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069866145931276592-782394b3.md` — origin: https://x.com/mattpocockuk/status/2069866145931276592
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069837651335614614-a73e48c8.md` — origin: https://x.com/mattpocockuk/status/2069837651335614614
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2070127727575748736-bbd2c0f1.md` — origin: https://x.com/mattpocockuk/status/2070127727575748736
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069836906674688083-576ccce4.md` — origin: https://x.com/mattpocockuk/status/2069836906674688083
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069463356700770816-a53b09ac.md` — origin: https://x.com/mattpocockuk/status/2069463356700770816
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2071935238666617154-12915eea.md` — origin: https://x.com/mattpocockuk/status/2071935238666617154
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072774233453638136-c9e523de.md` — origin: https://x.com/mattpocockuk/status/2072774233453638136
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080279667479585173-5e5fa538.md` — origin: https://x.com/mattpocockuk/status/2080279667479585173
