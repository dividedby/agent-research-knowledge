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

## Sources

- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/9c306665c63db13e3cd9cf6df8871f7792051eab/CHANGELOG.md (revision 2026-07-09, PR #409, origin https://github.com/mattpocock/skills/blob/0d74d01cbc64ca27778a49b38599f70c534e76a0 — the `research` skill added)
- `sources/mattpocock/skills-repo/skills-engineering-README.md-1400dd55.md` — origin: https://github.com/mattpocock/skills/blob/f02469bf3e8c183fd269565808c7b613ec6011c5/skills/engineering/README.md (revision 2026-07-09 — `research` listed under Model-invoked)
- `sources/mattpocock/skills-repo/skills-engineering-ask-matt-SKILL.md-f5c205a8.md` — origin: https://github.com/mattpocock/skills/blob/7d8d0ee43f671178d8cb2519c82fc68cf03335b3/skills/engineering/ask-matt/SKILL.md (revision 2026-07-09 — `research` under Standalone, routed back into `/grill-with-docs`)
