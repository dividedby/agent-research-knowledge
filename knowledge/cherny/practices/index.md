# Practices — cherny

Boris Cherny is the author of TypeScript in Practice and Claude Code's lead
engineer at Anthropic. The fan-curated `howborisusesclaudecode.com` aggregates
~107 tips from his X threads (Jan–Jun 2026), each linking the original post —
making this the highest-density firsthand account of Claude Code workflows from
the engineer who built the harness. Material skews here (practices — prompting
habits, workflow sequencing, agent/LLM principles, the "why" behind his
process); `artifacts/` may also receive harness-internals material where Cherny
documents the build side. One concept per file; this index lists them, one line
each.

- [parallel-agents-are-the-productivity-unlock](./parallel-agents-are-the-productivity-unlock.md) — going from one agent to many (checkouts → worktrees → agent view) is the single biggest gain.
- [verification-is-the-number-one-tip](./verification-is-the-number-one-tip.md) — give Claude a way to check its own output and it iterates until great; his explicit #1 tip.
- [plan-first-then-context-minimalism](./plan-first-then-context-minimalism.md) — the plan-then-1-shot habit, and why a stronger model made him drop it for context minimalism.
- [delegate-dont-pair-program](./delegate-dont-pair-program.md) — treat the model as an engineer you delegate to with a full upfront brief, not a pair you guide line by line.
- [compounding-memory](./compounding-memory.md) — make every correction pay forward by having the agent write its own CLAUDE.md rules.
- [context-hygiene](./context-hygiene.md) — rewind over correcting, /clear vs /compact, and defending the window against context rot.
- [autonomous-unattended-operation](./autonomous-unattended-operation.md) — composing auto mode, focus, /goal, /loop, recaps, and notifications into hands-off runs.
- [give-the-agent-your-whole-toolbox](./give-the-agent-your-whole-toolbox.md) — wire Claude to every tool you use (DB CLIs, Slack, browser, voice, mobile) via CLI/MCP/API.
- [claude-code-for-learning](./claude-code-for-learning.md) — treat "explain this" as a first-class output: explanatory mode, HTML slides, ASCII diagrams, a spaced-repetition skill.
- [automation-as-leverage](./automation-as-leverage.md) — a correction fixes one run, infrastructure fixes every run; "a rejected PR is a failure of automation."
- [finding-your-unknowns](./finding-your-unknowns.md) — the skill of agentic coding is surfacing what Claude doesn't know before it has to guess; a toolkit for before, during, and after implementation.
