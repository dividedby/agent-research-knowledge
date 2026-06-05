# Agent Skills: composable expertise via progressive disclosure

A **Skill** is a folder containing a `SKILL.md` (plus optional bundled files and
scripts) that packages domain expertise an agent can discover and load
dynamically — "like an onboarding guide for a new hire." It turns a
general-purpose agent into a specialized one without building a bespoke agent per
use case, and it's portable across Claude.ai, Claude Code, the Agent SDK, and the
Developer Platform.

The design principle that makes it scale is **progressive disclosure** — the same
"references, not data" idea applied to instructions, in discrete levels:
1. **Metadata** — the `name` and `description` from the YAML frontmatter are
   pre-loaded into the system prompt at startup. Just enough for the agent to know
   *when* the skill applies, at negligible context cost.
2. **The `SKILL.md` body** — read into context only if the agent judges the skill
   relevant to the current task.
3. **Bundled files** — `reference.md`, `forms.md`, etc., referenced by name from
   `SKILL.md` and navigated only as needed. The PDF skill keeps form-filling
   instructions in a separate `forms.md` so the core stays lean, trusting the
   agent to read it only when filling a form.

Because an agent with a filesystem and code execution never needs the whole skill
in context at once, **the context that can be bundled into a skill is effectively
unbounded**. Skills can also bundle **code as deterministic tools**: the PDF skill
ships a Python script that extracts form fields, which the agent runs without
loading either the script or the PDF into context — cheaper and more reliable than
doing the operation by token generation, and repeatable because code is
deterministic. Code can serve double duty as executable tool *and* as reference
documentation; the skill should make clear which.

Authoring guidance follows from the levels: invest in a sharp `name`/`description`
(it's the trigger signal); split an unwieldy `SKILL.md` into referenced files, and
keep mutually-exclusive paths separate to save tokens. Skills are powerful enough
to be a security surface — install only from trusted sources and audit untrusted
ones (bundled code, dependencies, instructions to reach external networks) before
use. The longer arc is agents that **create, edit, and evaluate their own
skills** — codifying their working patterns into reusable capabilities (the same
"save working code as a Skill" loop that code-execution-with-MCP describes).

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-equipping-agents-for-the-77ae700c.md` — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-code-execution-with-mcp-4dd2373a.md` — https://www.anthropic.com/engineering/code-execution-with-mcp
