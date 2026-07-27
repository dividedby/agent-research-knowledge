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

The fix he wants for `/goal` names the missing feature precisely: let him pass in
a batch of tasks, have the agent `/compact` *between* tasks, and keep going until
each one is done — "that would fix all my issues with `/goal` - too much time
spent in the dumb zone." The gap isn't the model, it's that the command currently
runs one long undifferentiated session instead of chunking itself into
compact-sized units of work. A related shape he's open to for the same reason:
a top-level `/goal` that orchestrates several `/goal`'ed subagents rather than
doing the work directly — "this might end up being fine" — because nesting the
work into subagent sessions means fewer total compactions bleed into the parent's
context, the same fresh-context-per-unit logic that makes the Ralph bash loop work
above.

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

## The line moved to 150K, it's vibes not measurement, and phases can still blow it

Matt has since revised the number he gives out loud: rather than the ~120k he
floated earlier, his rule of thumb is "you might be better off sticking to only
the first 150K tokens" even against a 1M-token window — a 1M context is "a nice
gimmick" precisely because more available headroom isn't more usable headroom.
Pressed on why the number moved from 100k to 150k, and whether there's a metric
behind it, he's blunt: "No, just personal vibes." The graph he uses to illustrate
smart-zone decay is "illustrative, not based on real data" — the shape (quality
holds, then degrades) is the claim; the exact curve isn't. That the boundary is
vibes-calibrated rather than measured doesn't weaken the underlying constraint
(see "The dumb zone is inevitable" above) — it just means the specific number is
a working heuristic to revise on feel, not a benchmarked threshold to defend.

The 150k line is also not a hard per-session ceiling: "some phases spiral out of
control and end up needing 300K tokens." The target is to compact **after a
milestone**, not mid-phase — "autocompacting can be disastrous when it happens
mid-phase," so the trigger is finishing a coherent unit of work, wherever that
lands token-wise, not a fixed number hit blindly.

## The dumb zone isn't always wrong to use

Working in the dumb zone costs more than the smart zone even beyond the quality
hit — "cached input tokens still cost money," so re-exploring a codebase from a
dumb-zone state burns real spend on top of worse decisions; the fix, when you
need to keep exploring, is to compact first rather than push forward staler.
But Matt doesn't treat the dumb zone as universally off-limits: for tail-end,
low-difficulty work he's "not scared of the dumb zone, it's fine sometimes" —
consistent with the smart/dumb split being about *matching* effort to task
difficulty (see `evaluating-models-past-tier-labels`), not avoiding the dumb zone
categorically. The discipline is knowing which kind of work you're doing when you
let context run past the line, not refusing to ever cross it.

## Make the budget visible

Because the smart zone is invisible by default, Matt surfaces it: his Claude Code
status line shows the **percentage of context used this session**, which he calls
"a constant source of paranoia" — it tells him when to keep going, compact, or
hand off ("around 60% is probably where I want to stop"). The point generalises:
keep the load-bearing signal in front of you rather than spending an agent turn to
check it.

The status line only gets him a *visual* readout, though, and he agrees the next
gap is a *programmatic* one: "the missing piece is an easy way to get the current
token usage programmatically so we can build on top of it and decide for
ourselves when it's time to compact/handoff" — turning "check the percentage,
then decide" into logic that can act on the number directly, rather than a human
reading a UI and deciding by feel every time. Or, more tersely: "a bowl is most
useful when it is empty" — same for your context window.

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
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079150593524772864-a1f183e8.md` — origin: https://x.com/mattpocockuk/status/2079150593524772864
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079151499393876479-209f0f4a.md` — origin: https://x.com/mattpocockuk/status/2079151499393876479
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079152236035281316-a926dd98.md` — origin: https://x.com/mattpocockuk/status/2079152236035281316
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079161882154348637-3465d019.md` — origin: https://x.com/mattpocockuk/status/2079161882154348637
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079167754830012452-368a6c39.md` — origin: https://x.com/mattpocockuk/status/2079167754830012452
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079175586971304297-c653c35e.md` — origin: https://x.com/mattpocockuk/status/2079175586971304297
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079317125638783180-f0e3ded2.md` — origin: https://x.com/mattpocockuk/status/2079317125638783180
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080675075397685300-2202f7f0.md` — origin: https://x.com/mattpocockuk/status/2080675075397685300
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080678327086465028-b2bc1dc9.md` — origin: https://x.com/mattpocockuk/status/2080678327086465028
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080913962137215470-0d85cb36.md` — origin: https://x.com/mattpocockuk/status/2080913962137215470
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081105631591698694-01d43731.md` — origin: https://x.com/mattpocockuk/status/2081105631591698694
