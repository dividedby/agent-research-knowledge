# Keep the agent in the smart zone

The single physical constraint behind most of Matt's habits is that an LLM's
quality decays as its context fills. Token relationships scale quadratically, so
every model has a **smart zone** (sharp, good decisions — roughly the first 40%
of context, which Matt personally feels ends around ~120k tokens) and a **dumb
zone** beyond it (diffuse attention, "lost in the middle", worse decisions). The
exact boundary is debated; that the boundary exists is not. The practical
corollary is counter-intuitive: a huge advertised context window (1M tokens) does
not mean 1M usable tokens — **better performance comes from using *fewer* tokens**,
not from filling the window. Context budgeting is therefore a first-class concern,
not an optimisation.

## Fresh context beats accumulated context (why Ralph loops, not the plugin)

This is the whole reason a bash Ralph loop works and Anthropic's in-session Ralph
plugin does not. The bash loop restarts the agent each iteration with an *empty*
context — the PRD and progress file go back in, the agent reconstructs what it
needs from git history, does one task, and exits. It never leaves the smart zone.
The plugin instead keeps every iteration inside one session via a stop hook, so
context climbs (~20% → ~35% → ~50% …) and by 3–4 iterations the agent is working
entirely in the dumb zone. The plugin *guarantees* the failure the loop was
designed to avoid. The same logic drives "take small steps": smaller tasks mean
less context accrued per unit of feedback, so quality stays high — "context rot"
is the name for the degradation when you don't.

## The dumb zone is inevitable — and staying out of it saves money

That a dumb zone exists isn't an empirical accident; Matt argues it "can't *not*
be true. It's some very simple scaling laws. If models didn't have a dumb zone,
you'd see 4m token context windows everywhere." The absence of usable
million-plus-token windows is the market revealing the constraint. So the smart
zone isn't a vendor-specific quirk to wait out — it's structural, and budgeting
against it is permanent.

The under-rated corollary is **cost**. Staying in the smart zone is "a great way to
save on tokens": in the dumb zone you're shipping 600K tokens on every request and
"that gets expensive FAST." Prompt caching softens it but doesn't remove it — "you
get charged for cache hits at a lower rate than normal input tokens," less per
token but it still adds up across a long session. So token discipline pays twice:
better decisions *and* a smaller bill. The same lens flags greedy tooling — Matt
finds the `/goal` command "incredibly dumb-zone hungry… it needs tuning to compact
earlier for it to be of any use." A feature that fills context fast is a quality
*and* cost regression until it learns to compact sooner.

## Move context deliberately: compact vs handoff

When a single thread must run long, `/compact` summarises the conversation to drop
you back toward the smart zone (layered summaries build up like sediment) — good
for long single-threaded debugging. But when you spot *out-of-scope* work
mid-session, compacting clobbers your progress and extending the session dilutes
it; the right move is **`/handoff`**, which lifts just the relevant slice of
context into a fresh focused session and leaves the current one pure. Handoff also
powers a DIY sub-agent pattern: spend a *full* context window exploring or
prototyping in a child session, compress the learnings into a handoff document,
and pass only those back to the parent — and because it's a portable markdown file
it works across tools (Claude Code → Codex, adversarial review, etc.). A worked
chain Matt endorses: a `/grill-with-docs` question that needs answering →
`/handoff` → `/prototype` → `/handoff` back to the original session.

The sharper rule for *when* to reach for handoff: **handoff only makes sense when
the work you're delegating to needs a human in the loop.** A background task that
runs to completion without HITL doesn't want a handoff at all — it wants to be
fired off and report back. Matt's worked example was a possible `/research`
skill: run a research agent in the background, have it save results to a `.md`
file, and have it resume its original activity (usually grilling) — *no*
handoff, because research doesn't need HITL. (That he says this verbatim every
time is itself his signal a skill is warranted — see the authoring heuristic in
`writing-great-skills-vocabulary`.) So the compact/handoff/fire-and-forget choice
keys on whether a human has to re-enter the loop.

That prediction has since shipped as the `research` skill, unchanged in shape:
a **background agent** does the reading so the calling session keeps working,
and it works only from **primary sources** — official docs, source code,
specs, first-party APIs — never a secondary write-up of them, saving one cited
Markdown file wherever the repo already keeps such notes. Confining it to
primary sources is the same anti-lossiness instinct as the primary/secondary
distinction elsewhere in this collection (see
`context-compression-and-handoff-mechanics`), applied to *evidence* rather
than to *session state*: a claim traced to the source that owns it survives
scrutiny; a claim traced to a summary of a summary doesn't. The file it
produces feeds the *thinking* skills (`grill-with-docs`, `to-prd`) rather than
sitting in the build chain itself — research is legwork you delegate, not
thinking you outsource.

## Set the auto-compact threshold deliberately

Smart-zone discipline isn't only manual `/compact` and `/handoff` — the harness
itself has a lever, and Matt tunes it. His `course-video-manager` project briefly
pinned `"autoCompactWindow": 180000` in `.claude/settings.json`: the token
threshold at which Claude Code automatically compacts the session. Setting it
explicitly (here, 180k tokens) is the same instinct as the status line — treat the
point at which context gets pulled back toward the smart zone as a configurable,
per-project decision rather than a vendor default to live with. It's the
deterministic-config counterpart to the manual budget habits: where the status
line tells *you* when to act, `autoCompactWindow` makes the harness act for you at
a chosen line. He later reverted the setting back to the vendor default — the
override was a live experiment, not a settled preference, which is itself a data
point: even someone who treats context budgeting as a first-class concern doesn't
assume a pinned number stays right forever, and reverts one deliberate default
back to another rather than leaving a stale override in place.

## Make the budget visible

Because the smart zone is invisible by default, Matt surfaces it: his Claude Code
status line shows the **percentage of context used this session**, which he calls
"a constant source of paranoia" — it tells him when to keep going, compact, or
hand off ("around 60% is probably where I want to stop"). The point generalises:
keep the load-bearing signal in front of you rather than spending an agent turn to
check it.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-why-the-anthropic-ralph-plugin-sucks-60344c9c.md` — origin: https://www.aihero.dev/why-the-anthropic-ralph-plugin-sucks
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-handoff-2afa3dc0.md` — origin: https://www.aihero.dev/skills-handoff
- `sources/mattpocock/aihero/https-www.aihero.dev-creating-the-perfect-claude-code-status-e04f7d09.md` — origin: https://www.aihero.dev/creating-the-perfect-claude-code-status-line
- `sources/mattpocock/aihero/https-www.aihero.dev-what-is-the-context-window-e993135d.md` — origin: https://www.aihero.dev/what-is-the-context-window
- `sources/mattpocock/aihero/https-www.aihero.dev-tips-for-ai-coding-with-ralph-wiggum-440a70a9.md` — origin: https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060389049681014871-2c145c3e.md` — origin: https://x.com/mattpocockuk/status/2060389049681014871
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060403350332448950-8300a75e.md` — origin: https://x.com/mattpocockuk/status/2060403350332448950
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060426881535512807-c7b0c21c.md` — origin: https://x.com/mattpocockuk/status/2060426881535512807
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060652913442062670-48fea6c3.md` — origin: https://x.com/mattpocockuk/status/2060652913442062670
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2070926582043062696-c75a0ca3.md` — origin: https://x.com/mattpocockuk/status/2070926582043062696
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2071153298950799868-33e370c2.md` — origin: https://x.com/mattpocockuk/status/2071153298950799868
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2071158794508284093-49902b89.md` — origin: https://x.com/mattpocockuk/status/2071158794508284093
- `sources/mattpocock/course-video-manager/.claude-settings.json-32bd95e6.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.claude/settings.json
- `sources/mattpocock/skills-repo/skills-engineering-research-SKILL.md-3753ea09.md` — origin: https://github.com/mattpocock/skills/blob/efa058a349f5ce98b6115bf8b4e0d0ef9c310e0d/skills/engineering/research/SKILL.md
- `sources/mattpocock/skills-repo/docs-engineering-research.md-ac883965.md` — origin: https://github.com/mattpocock/skills/blob/efa058a349f5ce98b6115bf8b4e0d0ef9c310e0d/docs/engineering/research.md
