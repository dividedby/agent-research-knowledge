# Context Compression and Handoff Mechanics

Matt developed the `/handoff` skill to split concerns across independent agent sessions while preserving relevant context. This technique enables focused work sessions without losing critical information, addressing the context window smart zone limitations.

## The Smart Zone Problem

Context windows have smart zones (~120k tokens) and dumb zones. Early in the context window, agents perform much better because attention relationships aren't strained. As conversations develop, responses gradually get dumber due to diffuse attention across too many tokens.

This creates a practical limit: despite advertised massive context windows, only about 120k tokens are available for truly smart work.

## Handoff vs Compact

**`/compact`** summarizes large conversations to move from dumb zone back to smart zone, useful for long-running single-threaded work like debugging. Creates layers of previous conversations like sediment.

**`/handoff`** takes specific slices of context relevant to different work and creates independent sessions. Enables splitting concerns without losing focus on either task.

The handoff approach allows: extending current session would dilute context working on two things simultaneously, while handoff keeps each session pure and focused on one concern.

## Handoff Document Structure

The skill compresses current session context into markdown documents containing:

**Purpose of next session** — Clear description of what the new session will accomplish  
**Relevant context** — Only information needed for the specific handoff task  
**Suggested skills** — Recommended skills to invoke in the next session  
**Pointers to artifacts** — References to existing files rather than duplicated content  

Documents are saved to the OS temporary directory as disposable working documents, not permanent documentation.

## Common Usage Patterns

**Out-of-scope discovery** — During feature work, notice refactoring opportunity. Handoff the refactor to separate session, keep current work pure.

**Prototype handoff** — During grilling sessions, identify things that need prototyping. Hand off to prototype session, compress learnings back to parent session.

**Cross-tool workflow** — Pass handoff documents between different AI coding tools (Claude Code → Copilot CLI → Codex) for tool-specific advantages.

## Design Principles

**Tool portability** — Use markdown format instead of native agent features for cross-agent compatibility  
**Avoid duplication** — Reference existing artifacts rather than copying content to prevent bloat  
**Redact sensitive information** — Strip out API keys, passwords, or PII from handoff documents  
**Disposable documents** — Save to temporary directories, not permanent project documentation  
**Purpose-tailored content** — Include only context relevant to the next session's specific goals  

## DIY Sub-Agent Pattern

Handoff creates a DIY sub-agent pattern: use a full context window for exploration, compress learnings into a handoff document, and pass insights back to the parent session. This enables complex exploration without bloating the main session's context.

## `claude-handoff`: skip the "paste it into a new session" step

`/handoff` still leaves a manual step: it writes the markdown file, but a
*human* has to open a fresh session and reference it. The in-progress
`claude-handoff` skill automates that last step for Claude Code specifically —
it writes the same kind of handoff summary, then immediately launches the next
session itself: `claude --bg --name "<descriptive name>" "<handoff summary>"`.
The background job starts in the current working directory, returns
immediately, and is managed afterward with `claude agents` — so the handoff
document becomes the new session's *prompt* rather than a file waiting to be
read. Two disciplines carry over unchanged from `/handoff`: reference existing
artifacts (PRDs, plans, ADRs, issues, diffs) by path or URL instead of
duplicating their content, and redact anything sensitive (API keys, passwords,
PII) — doubly load-bearing here, since the summary is no longer just a
document a human skims before continuing, it's text a fresh agent executes
directly. A descriptive `--name` is mandatory, not cosmetic: it's the only
label distinguishing the job in the list, the session picker, and the terminal
title once several are running.

Two mechanics matter for what `--bg` does and doesn't give you for free.
First, it does **not** carry the calling session's context forward on its own
— asked directly, Matt confirms you still "pass a handoff prompt manually";
`--bg` starts a genuinely fresh session, and the handoff document is what
supplies continuity, not the flag. Second, that document isn't a fixed
template filled in by hand each time: "the agent does it" — the calling
session generates the handoff summary itself as part of running
`claude-handoff`, the same generate-then-launch shape as the rest of the skill.

## Scope boundary: fan-out orchestration is a harness task, not a skill task

Asked whether `claude-handoff` should itself detect which of several next
steps can run in parallel versus which must run in sequence — spawning and
assigning agents as needed, stopping only when it hits a human-in-the-loop
point — Matt draws a line: he already does exactly this by hand, calling
`claude --bg --name "<name>" "<prompt>"` in a loop, once per step, but
**"I think this is a harness task, not a skill task."** A slash-command skill
is scoped to producing one good handoff; deciding a multi-step plan's
dependency graph and driving several background sessions through it is
orchestration logic that belongs one layer down, in the harness, not bolted
onto a skill whose job is authoring a single prompt.

## Primary vs Secondary Source: the lossiness is structural

Underneath every handoff and compaction is a single trade-off Matt names with two
terms: a **primary source** is the thing itself — code, transcripts, raw data —
complete and authoritative but expensive to load into context; a **secondary
source** is an account of a primary source one step removed — summaries, docs,
compaction summaries — cheap to load but *lossy by construction*. This is why a
handoff artifact and an autocompact summary are never free wins: they buy context
headroom by spending fidelity. The practitioner consequence is to handoff with
**pointers to the primary source** (reference the file, don't paste it) so the
next session can re-load the authoritative original on demand, rather than
inheriting only the lossy secondary account — the same instinct behind "reference
existing artifacts rather than copying content."

Matt frames any context-engineering decision as managing this trade-off: primary
sources are expensive to load but give richer context; secondary sources are
cheap but information-lossy. The corollary that bites in practice is **doc rot**:
a secondary source captures its primary at one moment, so the more often the
primary changes the faster the secondary drifts out of true. Hence his rule —
**delete secondaries where the underlying primary changes often.** Spending tokens
to generate docs that go stale almost immediately is a *false economy*: you pay to
build a cache that lies. The escape hatch is to label intent: anything explicitly
marked a **historical record** drifts less, because it never claims to "represent
the truth right now" — it's an account of a past state, not a stale mirror of the
present one. (One subtlety: raw model reasoning is rarely a usable source on its
own — you cite the code or transcript it produced, the primary, not the reasoning.)

## Starting context as "coordinates" — why the first-loaded material matters most

Endorsing a framing another practitioner proposed, Matt names what a session's
initial context actually buys you: "'Where you are in the environment' is
good — means the agent doesn't need to re-explore the landscape." Treating the
first-loaded material as **coordinates** rather than just "some context"
sharpens why a handoff document, a primed plan-mode session, or a loaded
`CONTEXT.md` all pay off the same way — they place the agent at a known point
in the codebase's landscape instead of leaving it to reconstruct that point
through exploration it's already paid for once. It's the practical stakes
behind "it really matters what gets loaded into the beginning of the context
window," restated as a reason rather than only an assertion: good starting
coordinates are what a handoff, a primed plan, or a glossary read are all
buying, whichever mechanism supplies them.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-handoff-2afa3dc0.md` — origin: https://www.aihero.dev/skills/handoff
- `sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md` — origin: https://www.aihero.dev/ai-coding-dictionary (revision 2026-06-05)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062825992486269441-a87fb8b9.md` — origin: https://x.com/mattpocockuk/status/2062825992486269441
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062828424817737840-3c0696fe.md` — origin: https://x.com/mattpocockuk/status/2062828424817737840
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062830915466780739-12ea3c41.md` — origin: https://x.com/mattpocockuk/status/2062830915466780739
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062876525553197221-2eed6697.md` — origin: https://x.com/mattpocockuk/status/2062876525553197221
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062876787881718069-873859ad.md` — origin: https://x.com/mattpocockuk/status/2062876787881718069
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062947848203751824-8686f659.md` — origin: https://x.com/mattpocockuk/status/2062947848203751824
- `sources/mattpocock/skills-repo/skills-in-progress-claude-handoff-SKILL.md-f0e12f6d.md` — origin: https://github.com/mattpocock/skills/blob/efa058a349f5ce98b6115bf8b4e0d0ef9c310e0d/skills/in-progress/claude-handoff/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/228dd71020d95f7f6c813e96e2098f6d2c712a69/skills/in-progress/README.md (revision 2026-07-03, `claude-handoff` listed)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072792309150736800-386d1342.md` — origin: https://x.com/mattpocockuk/status/2072792309150736800
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072792311184949526-58f97b05.md` — origin: https://x.com/mattpocockuk/status/2072792311184949526
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072961646079729882-b157e148.md` — origin: https://x.com/mattpocockuk/status/2072961646079729882
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072974002235011469-b4c2fbc4.md` — origin: https://x.com/mattpocockuk/status/2072974002235011469
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072985928990138389-f6f53241.md` — origin: https://x.com/mattpocockuk/status/2072985928990138389
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080286071741460739-ce766514.md` — origin: https://x.com/mattpocockuk/status/2080286071741460739