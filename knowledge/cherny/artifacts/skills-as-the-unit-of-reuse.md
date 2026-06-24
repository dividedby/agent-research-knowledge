# Skills: the unit of reusable agent knowledge

A skill, in Cherny's framing, is "a knowledge file that lives on your machine"
(markdown + YAML frontmatter) that Claude references automatically when relevant —
or on demand as a slash command. Skills are the **unit of reusable agent
knowledge**: write once, commit, reuse across every project. The site itself ships
as one (`/boris`), as does Thariq's skills guide (`/thariq-skills`).

The build guidance comes from Anthropic running *hundreds* of skills internally
(Thariq's catalog). Two load-bearing findings:

- **The best skills fit cleanly into one type.** After cataloging, their skills
  cluster into recurring categories, and a good skill belongs to exactly one. The
  observed types: **internal-API/library docs** (libs, CLIs, SDKs, gotchas),
  **product drivers** (drive the running product to verify), **data/query** (IDs,
  field names, query patterns — e.g. a BigQuery skill), **multi-tool workflows**
  (collapse a multi-step flow into one command — standup, weekly-recap),
  **scaffolding** (framework-correct boilerplate), **review/quality** (adversarial
  review, style, testing), **ship/deploy** (commit, push, deploy safely),
  **investigation** (symptom → investigation → report — oncall, log-correlation),
  and **safety-gated cleanup/maintenance**. A skill that spans several types is a
  sign to split it.
- **Progressive disclosure.** The authoring patterns center on surfacing detail
  only when needed (the guide explicitly covers "progressive disclosure patterns"),
  keeping the always-loaded surface small — the skill counterpart to the
  context-minimalism stance in [[context-hygiene]].

Distribution mirrors [[customization-checked-into-git]]: global install at
`~/.claude/skills/`, project install at `.claude/skills/`, or shipped via a
plugin marketplace; the `/boris` skill even self-updates on invocation. Built-in
skills are themselves examples of the form — `/simplify` (quality), `/batch`
(parallel migrations), `/go`/`/goal` (composite completion), `/deep-research`
(itself a workflow). The `/deep-research` and `/batch` cases show a skill can
*be* a [[dynamic-workflows]].

The principle: **package agent knowledge as small, single-purpose, committed,
auto-surfaced skills** rather than re-prompting it each time — the skill is to
knowledge what the slash command is to a workflow.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
