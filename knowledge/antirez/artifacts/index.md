# Artifacts — antirez

How antirez (Salvatore Sanfilippo) designs the *internals* agents lean on, when
his blog documents them firsthand. The additive vantage here is a C /
local-inference angle on agent tooling — e.g. his notes on the EDIT tool of LLM
agents and token-constrained tool design, which overlap the mariozechner/ronacher
tool-design cluster. No skew is forced (harness-builder posture): material lands
here as readily as in `practices/` — let the concept decide. One concept per
file; this index lists them, one line each.

**Scope reminder:** most feed captures are out-of-scope Redis/C/systems posts
(see `docs/subjects.md`); synthesize only the coding-agent material.

- [agent-instruction-files](./agent-instruction-files.md) — the markdown driver file that runs an unattended agent: a rules block + a self-maintained WIP log re-read after every context compaction.
