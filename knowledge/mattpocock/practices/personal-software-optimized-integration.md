# Personal Software with Optimized Integration

Matt advocates for building bespoke applications that deeply integrate with personal workflows rather than using generic AI tools. His course video manager exemplifies this approach — software adapted exactly to how he works, handling grunt work while preserving human thinking.

## The Generic Tool Problem

Generic AI tools make impressive demos but fall flat in daily use because they don't know who you are, what you're working on, or how you work. They require constant context-setting and can't leverage existing file structures, content formats, or project-specific workflows.

Matt's course manager demonstrates the alternative: it knows his file structure, understands his content formats, plugs into his existing repositories, and handles his entire video-to-content workflow in one integrated application.

## AI for Grunt Work, Not Thinking

The core principle: delegate repetitive work to AI while keeping all thinking for yourself. Matt's tool handles transcription, text generation, and content repurposing — pure grunt work that doesn't require judgment.

**The moment you start delegating your thinking to an LLM, you're screwed.** But building systems that integrate AI into workflows you already have becomes powerful.

Matt reviews all AI outputs closely, especially anything users will see. The AI accelerates his work without replacing his judgment or taking over his decision-making.

## Bespoke Integration Advantages

**Workflow optimization** — The software knows exactly how Matt works and optimizes for his specific needs rather than trying to be general-purpose.

**Context retention** — Unlike generic tools that start fresh each session, personal software maintains context about ongoing projects and preferences.

**Deep integration** — Connects directly with existing repositories, file structures, and output formats without manual setup each time.

**Task-specific optimization** — Built for specific workflows (record video → generate accompanying text → publish) rather than broad categories.

## Worked example: the teleprompter

Filming a course with a teleprompter for the first time, Matt reports it's "far
less exhausting and makes the quality higher" than filming from nothing — even
though he's still "90% improvising" around the pre-written text rather than
reading it verbatim. The bespoke-integration payoff shows up in how the text
gets there: his custom video editor keeps teleprompter state **synced to the
editor itself** ("Absolute dreamland, personal software paying off again"), and
the script it displays is AI-drafted from beats **he hand-organizes first** —
"doesn't need to be perfect since I'm improvising around it," so the AI's job
is a rough scaffold, not a finished script the way "AI for grunt work, not
thinking" describes above. The hardware side stays proportionate to the
payoff: an Elgato teleprompter, about £200 — a small, one-time cost against a
workflow that now runs through software built to know exactly how he films.

## Field example: a private wiki syncing every input channel, planned by a daily standup agent

Another bespoke build follows the same shape as the teleprompter, aimed at
Matt's own admin rather than course production: syncing every "input" work
channel he has into a single private wiki, powered by a custom CLI rather than
a generic tool. The next step he named for it — having an agent run a daily
morning standup against that wiki to plan the whole week — is a direct
application of the loop lens from `loop-me-workflow-spec-grilling`: a recurring
pattern (his week) turned into a scheduled, agent-driven checkpoint, fed by a
month's accumulated wiki data rather than a cold start each time. Pressed on
whether a daily process makes sense for planning something as coarse as a
week, he holds the cadence anyway: **"Yah, things change but it's nice to have
a plan and see ahead"** — the plan is expected to drift, but replanning daily
is worth it for the visibility, not despite the drift.

Asked what's behind the wiki, Matt calls it **"Karpathy-inspired"** and locates
the hard part precisely: **"it's not hard, it's more about the quality of the
input"** — the wiki's value is bounded by how good the material syncing into it
is, not by the mechanism that syncs it. He also reports not reaching for
embeddings or a document-processing step (**"agentic research, haven't felt
the need for qmd yet"**) — plain agentic search over the wiki's markdown has
been sufficient so far, without a retrieval-index layer on top. That both
extends and sits in tension with the stateless-harness preference in
`where-ai-coding-assets-live`: the coding harness itself stays stateless by
choice, but a separate, deliberately-built personal wiki is where Matt *does*
want durable, accumulating state — because it's system he controls end to end,
not a harness-vendor memory feature he can't inspect.

## Applying the wiki to knowledge work: parallel sections, dictation, and a night-shift linter

Matt reports extending the same Karpathy-inspired-wiki approach from admin to
knowledge work specifically — course and talk planning — and names four parts
that, together, let him "speak the thing I want into existence" while the
model does the integration:

1. Give each **deliverable** (a course, a talk — more than a day's labour) its
   own wiki.
2. Split the deliverable into **sections** that can be worked on in
   independent agent threads during the day, so more than one thread means
   parallelizing work across different sessions, all reading from and writing
   to the same wiki as shared state. Concretely, sections live in "different
   folders in the same repo" — accessible to every thread, but each thread is
   discouraged from writing outside its own workspace folder.
3. His own input arrives as **braindumps** — large chunks of dictated text the
   model integrates into the wiki — and he reacts to the model's own HTML
   reports of the current state by dictating again, closing a speak-in,
   read-back loop rather than typing.
4. A **linting skill**, run during a "night shift," uses "a ton of subagents"
   generously to check the whole deliverable for every possible weakness. Its
   checks are qualitative review, not deterministic pass/fail assertions: "not
   'run the tests', more like 'check that the content is in the correct
   order,' 'check that the language is not too confusing' — more like
   automated review than automated checks." He confirms the loop already
   extends past planning into execution — "the agents execute commands in my
   CMS, have been doing this for a while" — so the wiki isn't just a planning
   scratchpad, it drives real publishing actions too.

Matt frames this explicitly as a work in progress rather than a finished
methodology, but one he already likes: the combination of parallel
day-shift threads plus a broad night-shift review pass is a distinct
division of labour from the single-thread `/retro` or `code-review` loops
elsewhere in the collection — many cheap, generous review subagents hunting
open-endedly for weaknesses, rather than one focused pass against a fixed
checklist.

## The Future Bet

Matt sees the future in bespoke applications rather than generic tools everyone uses the same way. Personal software that deeply understands your specific needs and projects rather than trying to serve all use cases adequately.

This approach leverages AI for what it's best at (grunt work, text processing, format conversion) while preserving human strengths (judgment, taste, strategic thinking).

## Implementation Philosophy

Build systems that:
- Leverage AI for repetitive tasks
- Keep human thinking central to the process
- Integrate deeply with existing workflows
- Optimize for personal productivity patterns
- Maintain quality gates on AI output

The goal is moving faster through automation, not replacing human judgment with AI decision-making.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-personal-software-is-insane-in-the-age--3d6a74ea.md` — origin: https://www.aihero.dev/personal-software-is-insane-in-the-age-of-ai-u2hx2
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081766847477666147-dd85e64b.md` — origin: https://x.com/mattpocockuk/status/2081766847477666147
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081768373721985302-20c61ea0.md` — origin: https://x.com/mattpocockuk/status/2081768373721985302
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081771165060571302-3b0710b7.md` — origin: https://x.com/mattpocockuk/status/2081771165060571302
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081773309599822321-ab9cb3b6.md` — origin: https://x.com/mattpocockuk/status/2081773309599822321
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082545875922882718-06dc1a88.md` — origin: https://x.com/mattpocockuk/status/2082545875922882718
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082547448413630502-bf728589.md` — origin: https://x.com/mattpocockuk/status/2082547448413630502
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082748002226032666-dd713d5b.md` — origin: https://x.com/mattpocockuk/status/2082748002226032666
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082814640623378587-9d4c97d5.md` — origin: https://x.com/mattpocockuk/status/2082814640623378587
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2097638166232457451-d39b3368.md` — origin: https://x.com/mattpocockuk/status/2097638166232457451
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2097639875449094230-1e8a2f3f.md` — origin: https://x.com/mattpocockuk/status/2097639875449094230
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2097640030609002873-2ab4a1d9.md` — origin: https://x.com/mattpocockuk/status/2097640030609002873