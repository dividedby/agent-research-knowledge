# `research`: delegate reading legwork to a background agent

`research` is a small, model-invoked skill whose only job is reading: it
investigates a question against **primary sources** — official docs, source
code, specs, first-party APIs, never a blog post's paraphrase of them — and
leaves a single cited Markdown file wherever the repo keeps such notes. It runs
as a **background agent**, so the point isn't just delegation, it's
*concurrency*: you keep working in the foreground while it reads, and come
back to a document rather than a wall of chat you'd have had to sit through
turn by turn.

## The artifact is the interface, and it feeds — never replaces — the thinking

A `research` run's only output is the cited file. That's deliberate: the
skill's job is to gather and cite, not to decide anything on the strength of
what it found. The file is explicitly something you take *into* the main
planning flow at `/grill-with-docs` (or `/to-spec`) to argue over, not a
verdict to act on directly — the same "answer feeds the next step, the
artifact itself is disposable-ish" shape `/prototype` uses for a runnable
answer instead of a written one (see `prototype-answer-is-the-artifact`). Both
skills exist because talking in the abstract can't settle some questions —
one needs a concrete thing to react to, the other needs ground truth from
outside the room — and both hand back an artifact rather than trying to close
the loop themselves.

## The delegation is unguarded, and "high-trust" has no gate

The background agent `research` spawns holds the same `Agent` tool and the
same instructions as the skill that launched it, and nothing restricts what
kind of agent it may become — so it can, and reportedly does, spin up a
*further* background research agent of its own, duplicating the run. One
reporter measured a single research task costing roughly 450k tokens across
three overlapping runs, with the duplicate finishing entirely out of view half
an hour later; the same nesting reproduces outside Claude Code, in Codex.
There's no shipped fix — the field patch is an instruction telling an agent
that is already a subagent to do the work itself rather than delegating
further, which is instruction-level, not structural. The opposite failure
exists too: a global instruction forbidding an agent from re-delegating work
makes the background agent politely decline the research task, and the skill
quietly does nothing.

A second, unresolved objection targets the skill's core premise rather than
its implementation. `research` names the *kinds* of source that qualify as
primary — official docs, source code, specs, first-party APIs — but ships no
allowlist, no domain gate, and no verification pass; the model alone decides
what counts. The sharpest framing of the objection, from when the skill was
first proposed: "five research subagents pointed at junk just gives you five
confident wrong answers faster." The mitigation that actually exists is the
citation on every claim — following two or three of them and checking they
land on the primary thing itself, not a summary of it, is the only check the
skill doesn't do for you. Relatedly, nothing auto-loads a past research file
into a later session; the artifact only earns its keep if something —
a human, a spec, a ticket — deliberately points at it afterward. A write-once
file nobody re-reads is, in the words of an early critic, "just a fancy
search."

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-research-a3bcef26.md` — origin: https://www.aihero.dev/skills-research
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/9c306665c63db13e3cd9cf6df8871f7792051eab/CHANGELOG.md (revision 2026-07-09, PR #409, origin https://github.com/mattpocock/skills/blob/0d74d01cbc64ca27778a49b38599f70c534e76a0 — the `research` skill added)
- `sources/mattpocock/skills-repo/skills-engineering-README.md-1400dd55.md` — origin: https://github.com/mattpocock/skills/blob/f02469bf3e8c183fd269565808c7b613ec6011c5/skills/engineering/README.md (revision 2026-07-09 — `research` listed under Model-invoked)
- `sources/mattpocock/skills-repo/skills-engineering-ask-matt-SKILL.md-f5c205a8.md` — origin: https://github.com/mattpocock/skills/blob/7d8d0ee43f671178d8cb2519c82fc68cf03335b3/skills/engineering/ask-matt/SKILL.md (revision 2026-07-09 — `research` under Standalone, routed back into `/grill-with-docs`)
