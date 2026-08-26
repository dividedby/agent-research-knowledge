# The codebase is the memory system; a bolted-on one is a red flag

Asked whether he runs any kind of agent memory system, Matt's answer refuses
the premise that one is missing: **"My codebase is my memory system."** Pressed
further on how that covers process, lessons, and rules — not just code — the
answer stays inside the same discipline this collection already documents:
**"A thin layer of docs, in the codebase."** The instinct is consistent with
everything else in the collection: don't stand up a parallel memory
apparatus when the artifacts you already maintain — the code itself,
`CODING_STANDARDS.md`, ADRs, the domain glossary (see `adrs-as-agent-memory`,
`shared-language-as-agent-fuel`) — already are the durable record. A
"memory system" as a distinct piece of infrastructure is solving a problem
that a disciplined, thin-docs-in-the-repo habit already solves, at the cost of
one more thing to keep in sync.

## Cross-project sharing is an extraction problem, not a new system

Pushed on the gap this creates — a convention learned on one project is
"locked in the project," so carrying it to another means manually re-teaching
it, whereas a dedicated memory tool would apply it everywhere automatically —
Matt's answer stays inside the codebase-as-memory frame rather than reaching
for new infrastructure: **"extract it to a shared steering repo, or move
things into a monorepo. There's no reason for an extra system here."** The
same "where does this live" question `shared-language-as-agent-fuel` answers
for glossaries that span multiple repos (centralise only when the language is
genuinely 100% shared) applies to conventions generally: the fix for
"I want this everywhere" is restructuring where the docs live, not adding a
system whose job is remembering things the repo structure could hold instead.

## Skepticism about self-improvement, and the deliberate design he's willing to risk

This preference for durable docs over a memory system is not naivety about
what compound engineering promises — Matt has specifically avoided building
its signature feature. Asked why his skill set has nothing like it, he states
the reluctance and the reason together: **"One thing missing from my skill
set is what compound engineering has - the promise that your process improves
over time. I have been extremely reluctant to add this since I think models
are REALLY bad at improving their own behavior."** Left unattended, a model
asked to record what it learned after every session degrades into
clutter — a separate user reports exactly this failure mode, and Matt's own
one-word reply, "Definitely," to the fix that user proposes (self-improvement
"has to be paired with very strict instructions on what can and cannot go
into `agents.md`, `context.md`, and so on") confirms the risk is real, not
hypothetical.

Despite the skepticism, he's warming to a bounded version: **"a skill that you
run at the end of a session to: update your `CODING_STANDARDS.md`, rework &
cull existing skills/steering instructions, powered by `/writing-for-agents`
... would actually be pretty great."** Names floated in the same breath —
`/improve-me`, `/be-better`, and eventually `/retro` ("Yep, that's the one.
Love it") — are less important than the shape: a **deliberately invoked**
checkpoint (not an automatic per-PR loop) that writes to the same curated,
human-reviewed files this collection already treats as durable (see
`review-skill-two-axis-with-smell-baseline`'s `CODING_STANDARDS.md`-accretion
discipline), rather than a freeform memory the model updates on its own
judgement. He names the tension explicitly when a correspondent points out the
obvious risk of clutter: **"Yeah this is exactly what I'm nervous about. But I
DO need a mechanism for adding stuff to `CODING_STANDARDS.md`, which can
afford a bit more bloat IMO."** The resolution isn't "models can self-improve
after all" — it's that a curated file with review-time enforcement (not a
freeform memory blob) can absorb some bloat safely because a human still reads
what lands in it, the same guard that makes `CODING_STANDARDS.md` safe
elsewhere in this collection.

## Multi-session retro over single-session over-indexing

The same session-end idea gets a scaling fix from the field rather than from
Matt himself: a user reports orchestrating Explore agents to analyze many
session transcripts from the same project at once, specifically "to find
common patterns and not over-index on a single example from a single context
window." Matt endorses the move directly: "Great call. A multi session retro
makes sense." This closes the loop on his own skepticism above — a *single*
session judging its own behavior is exactly the unreliable self-improvement he
distrusts, but a retro that pattern-matches across many past sessions is
closer to an independent review pass than to a model grading its own
homework, the same "same context reviewing itself isn't review" caution
`review-skill-two-axis-with-smell-baseline` already applies to code review.

## From floated name to a stubbed skill

The idea materialized: `retro` now exists as a real file in the `in-progress`
beta bucket, carrying the caveat `STUB: design notes only, not functional
yet.` Its `disable-model-invocation: true` frontmatter keeps it a
deliberately-invoked checkpoint rather than something the model fires on its
own — the same "not an automatic per-PR loop" shape floated above, now
encoded as a harness-level switch instead of just an intention. Its concrete
category checklist for what a retro is allowed to write into (see
`retro-skill-symptom-to-intervention-checklist`) is the bounded taxonomy that
answers the clutter worry named above: a fixed set of intervention types, not
an open-ended "write down what you learned."

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088733788335489218-b6633825.md` — origin: https://x.com/mattpocockuk/status/2088733788335489218
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088741042744901842-3262c172.md` — origin: https://x.com/mattpocockuk/status/2088741042744901842
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088741306021425166-d1f1a1cf.md` — origin: https://x.com/mattpocockuk/status/2088741306021425166
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088742574454390795-52b55044.md` — origin: https://x.com/mattpocockuk/status/2088742574454390795
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088742184245731443-67a7980c.md` — origin: https://x.com/mattpocockuk/status/2088742184245731443
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088761527910220013-4ed43741.md` — origin: https://x.com/mattpocockuk/status/2088761527910220013
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088890920213098686-5f721aaf.md` — origin: https://x.com/mattpocockuk/status/2088890920213098686
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088913666141765977-20edb29f.md` — origin: https://x.com/mattpocockuk/status/2088913666141765977
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088988804635935104-22e042a4.md` — origin: https://x.com/mattpocockuk/status/2088988804635935104
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088997639735951629-7ee07601.md` — origin: https://x.com/mattpocockuk/status/2088997639735951629
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-08-25, origin https://github.com/mattpocock/skills/blob/c4745476a77d0b34af2933a01cf13f9bcd22fc30/skills/in-progress/README.md — `retro` listed as a STUB)
- `sources/mattpocock/skills-repo/skills-in-progress-retro-SKILL.md-95ca61b1.md` — origin: https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/in-progress/retro/SKILL.md
