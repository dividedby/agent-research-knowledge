# Practices — antirez

How Salvatore Sanfilippo (antirez, creator of Redis) works with coding agents —
developed firsthand on his blog as hype-free field notes on *steering* an agent.
The named methodology is *"automatic programming"*: disciplined, high-context
steering of the model as a deliberate counterpoint to vibe coding, written by a
working practitioner shipping real systems software (C, local inference) with
Claude Code/Opus. Material may also land in `artifacts/` (agent-tool-design
internals — e.g. his takes on the LLM agent EDIT tool), so let the concept
decide rather than pre-skewing. One concept per file; this index lists them, one
line each.

**Scope reminder:** the feed is a rolling ~100-post window reaching back to 2013,
so most captures are pre-2024 Redis/C/systems posts that are *out of scope* — see
`docs/subjects.md`. Synthesize only the coding-agent posts; ignore the rest as
inert, captured-but-unsynthesized noise.

- [automatic-programming](./automatic-programming.md) — the named method: AI-assisted production where the human owns the vision; code is automatic, vision is not.
- [large-context-and-braindump](./large-context-and-braindump.md) — steer by loading a big context plus a braindump of bad/good solutions and goals; "think what a human would need."
- [spec-first-development](./spec-first-development.md) — hand-write the design spec first; it's what you steer with and what makes line-by-line review possible.
- [verification-loop-and-the-human-edge](./verification-loop-and-the-human-edge.md) — only use the model where you can verify it; the human supplies the out-of-the-box creative leap.
- [agentic-qa-gate](./agentic-qa-gate.md) — a markdown QA-engineer agent that diffs against the last release and runs the manual/integration testing humans skip.
- [agents-build-organically-not-by-uncompressing](./agents-build-organically-not-by-uncompressing.md) — agents assemble new code incrementally; the "uncompressed copy" fear is false, and steering changes everything.
