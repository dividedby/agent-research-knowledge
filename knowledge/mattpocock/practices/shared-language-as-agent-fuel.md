# A shared language is agent fuel, captured live

A project's `CONTEXT.md` is a glossary and *nothing else* — devoid of
implementation detail, not a spec, not a scratchpad. Matt rates building this
shared language with the agent as possibly the single most powerful technique in
the repo. The payoff is concrete: the agent stops using twenty words where one
will do ("the materialization cascade" instead of a paragraph), variables and
files get named consistently from the same vocabulary, the codebase becomes
easier for the agent to navigate, and the agent spends fewer tokens thinking
because it has a more concise language to think in.

## Capture terms the moment they resolve, not in a batch

The discipline that makes this work is *liveness*. In `grill-with-docs`, the
moment a term is pinned down during the interview, `CONTEXT.md` is updated right
there — don't batch. Files are created lazily: no `CONTEXT.md` until the first
term resolves, no `docs/adr/` until the first decision needs one. The agent also
*polices* the language as it goes: if the user says a term that conflicts with
the glossary, it calls it out immediately; if the user is vague ("account" —
Customer or User?), it proposes a precise canonical term; if the code
contradicts a stated rule, it surfaces the contradiction.

This same live-capture discipline is reused, not reinvented:
`improve-codebase-architecture` adds a term to `CONTEXT.md` the moment it names a
deepened module after a concept the glossary doesn't yet have, citing
`grill-with-docs`'s `CONTEXT-FORMAT.md` as the shared standard.

## Where the glossary lives: by language overlap, not by repo

When the same vocabulary spans multiple repos, the placement rule is overlap-
driven. "If you have multiple repos that 100% share the same domain language,
store the glossary outside the repo and have `/grill-with-docs` fetch it. If they
don't share 100% of the language, keep them in the repos." A glossary is only worth
centralising when it's genuinely identical across consumers; the moment two repos
diverge on even part of the language, a shared external glossary starts lying to
one of them, and per-repo `CONTEXT.md` files (with a context map above them) are
the safer shape.

## Where the glossary came from: ubiquitous language

The practice traces to **ubiquitous language** from domain-driven design — one
vocabulary shared by the codebase, the developers, and the domain experts. Matt
arrived at it by noticing the limits of plain `grill-me`: alignment on the code
kept dissolving because he had to re-explain the domain every session, and good
terms coined in a session were never written down. "What's the thinnest layer of
documentation I could use to give the AI a head start?" The answer became
`CONTEXT.md`, and the standalone `ubiquitous-language` skill was folded into
`grill-with-docs` so capture happens *inside* the alignment interview, supporting
multiple bounded contexts (one `CONTEXT.md` per context, a context map above
them) rather than one glossary per repo.

The same conviction scales past a single project. Matt also publishes a canonical
**dictionary of AI coding** (`mattpocock/dictionary-of-ai-coding`) — terse,
one-line definitions for the field's vocabulary (model, harness, context window,
smart zone, progressive disclosure, handoff/spec/ticket, AFK/HITL, grilling). It's
the field-level instance of the same move: pin precise, shared terms so humans *and*
agents reason in the same concise language. The whole KB downstream leans on exactly
these terms, which is why a fixed gloss is worth maintaining.

## Vocabulary precision through continuous refinement

The dictionary itself demonstrates the practice in motion — tracked revisions show continuous refinement of definitions and growth from 62 to 64+ terms across multiple versions. The word count evolution (1,932 → 1,955 words across revisions) captures the disciplined expansion: new concepts earn inclusion only when they represent genuinely distinct ideas rather than synonym proliferation.

Each revision tightens definitions rather than expanding them — "smart zone" becomes more precise, "handoff" mechanisms get clearer distinctions. This demonstrates that vocabulary maintenance isn't just about adding terms but about continuously sharpening the existing language to eliminate ambiguity and improve precision.

A later revision shows the sharpening move from a different angle: the 62 entries are now grouped into seven thematic sections — The Model; Sessions, Context Windows & Turns; Tools & Environment; Failure Modes; Handoffs; Memory and Steering; Patterns of Work — and many definitions are stated *relationally*, by their counterpart. Parametric knowledge is defined against contextual knowledge, stateless against stateful, input tokens against output tokens, and "attention relationship / budget / degradation" form a deliberate family. Precision comes not just from a tight one-liner per term but from contrast: a term is pinned by what it is *not* and by the neighbour it trades off against, which is exactly the discriminating signal an agent needs to keep two adjacent concepts from collapsing into one.

The refinement isn't monotonically toward brevity, though. A 2026-07-17 revision (69 entries) reverses the tightening trend: most definitions roughly double in length, trading the one-liner for causal explanation and a concrete anchor — Model now names "Claude Opus 4.x" and "GPT-5.x" as examples, Harness contrasts "Claude Code" against "Claude.ai" running the same underlying model. The discipline was never really "stay short" — it's "say only what earns its place"; when a one-liner proved too thin to actually discriminate a term from its neighbours or explain why it matters, the fix was more words, not fewer.

A three-revision window immediately after (2026-07-18 through 2026-07-20, still 69 entries) reverses the reversal: almost every definition contracts back toward a terse one-liner, shedding the causal padding the 07-17 pass had just added. But the swing back isn't a round-trip to the *old* one-liners — a handful of terms land at a sharper resting point than either prior version had. Hallucination stops gesturing at "two flavors with different causes and fixes" and names them — factuality (invented facts) versus faithfulness (drift from loaded context). Subagent adds a hard constraint, "cannot spawn further subagents," and Handoff acquires the mirror-image trait, "with no return path" — the pair now discriminate on exactly the axis that matters (does the child report back automatically, or not). Attention relationship gets its scaling law spelled out numerically: a context of N tokens has roughly N² of these. So brevity keeps winning as the resting state, but each length cycle discards different weight than it added — precision compounds even while word count oscillates.

## The glossary drives the questions

In a real session the documented terms aren't passive — they generate the
interview. Adding a "pitch" concept to a course tool, the agent immediately flags
a *terminology collision* with the existing `CONTEXT.md` definition of
"Standalone Video", and resolves it by minting sub-terms (Pitched vs Unattached
Standalone Video) precisely because the distinction "will affect every variable
name and file name the AI generates." That is the whole payoff loop: the glossary
forces the question, the answer sharpens the glossary, and the sharpened glossary
makes the *next* generation of code and questions tighter. The benefit is
two-sided — replies get concise ("standalone videos are changing, we need to
change the pitches and how they display" instead of a paragraph), and because the
model thinks *to itself* in chain-of-thought, a precise shared vocabulary makes
its internal reasoning cheaper too. The same reason DDD works for humans is why
it works for agents.

The committed form of that course-tool glossary makes the policing mechanical: each
term in `course-video-manager`'s `CONTEXT.md` ships with an explicit `_Avoid_` line
listing the rejected synonyms — **Course** _Avoid_ Repo/Project, **Section**
_Avoid_ Module/Unit, **Pitch** _Avoid_ Idea/Concept/Draft. The anti-synonyms aren't
decoration; they're what lets the agent (and a reviewer) catch drift the moment a
generated name reaches for a banned word, the same enforcement posture as the
structural vocabulary in [[enforced-architecture-vocabulary]].

## Endorsement signal: the shared-vocabulary move travels

The practice resonates outside Matt's own repos. He amplifies a practitioner
(@delba_oliveira) describing a Claude Code + Remotion pipeline for animated
diagrams whose load-bearing insight is exactly this one: "It really helps to have
a shared vocabulary with your agent" — having taught the agent that "rise in fast
on enter" means a specific fade-up offset, duration, and bezier curve, plain
English now compiles to the team's input language. Her recommended reading for
building that common language explicitly names Matt's `/grill-with-docs`. This is a
foreign author's account that Matt endorsed, not his own assertion — but it
corroborates that the canonical-vocabulary technique generalizes well past code
into design-system and animation work.

## ADRs only for genuine, hard-to-reverse trade-offs

The glossary's companion is the ADR, and Matt is deliberately stingy with them.
An ADR is offered only when **all three** hold: the decision is hard to reverse,
surprising without context, and the result of a real trade-off with genuine
alternatives. Miss any one and skip it. The framing is forward-looking: record
it so a *future explorer* (or a future architecture review) doesn't re-litigate
the decision — not as a log of everything that happened.

## Sources

- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md
- `sources/mattpocock/skills-repo/CONTEXT.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/CONTEXT.md
- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md
- `sources/mattpocock/skills-repo/skills-engineering-grill-with-docs-SKILL.md-1015ebf3.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/grill-with-docs/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060426073083412751-d41431eb.md` — origin: https://x.com/mattpocockuk/status/2060426073083412751
- `sources/mattpocock/aihero/https-www.aihero.dev-grill-with-docs-d376dfd1.md` — origin: https://www.aihero.dev/grill-with-docs
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-changelog-ubiquitous-language-gr-ec926d6c.md` — origin: https://www.aihero.dev/skills-changelog-ubiquitous-language-grill-with-docs
- `sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md` — origin: https://www.aihero.dev/ai-coding-dictionary
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2065470273160097977-1e6995c1.md` — origin: https://x.com/mattpocockuk/status/2065470273160097977
