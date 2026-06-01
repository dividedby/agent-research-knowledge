# Skill anatomy and progressive disclosure

A Matt Pocock skill is a directory, not a file. The directory holds one required
`SKILL.md` and an optional cluster of bundled resources that the `SKILL.md`
*links to but does not inline*. This layering is the load-bearing design choice:
it controls what an agent pays tokens for and when.

## The three tiers

1. **The frontmatter `description`** — the only thing the agent sees before
   loading anything. It is surfaced in the system prompt alongside every other
   installed skill, so it is pure routing metadata: first sentence says *what
   the skill does*, second says *"Use when [specific triggers]"* (keywords,
   contexts, file types). Third person, ≤1024 chars. The description is 
   **the only thing your agent sees when deciding which skill to load** — it
   must give the agent just enough info to know what capability this provides
   and when/why to trigger it. A vague description ("Helps with documents")
   strands a good skill because the agent can't distinguish it from its
   neighbours.
2. **`SKILL.md` body** — the working instructions, kept short (the
   `write-a-skill` checklist targets ~100 lines, with 500 as the hard "must
   split" threshold). Loaded only once the description has matched.
3. **Bundled resources** — `*.md` reference docs, format templates, and
   `scripts/`. Loaded only when the body explicitly links to them
   (`See [tests.md](tests.md)`). The `improve-codebase-architecture` skill keeps
   its full architecture vocabulary in `LANGUAGE.md` and its HTML scaffold in
   `HTML-REPORT.md`; `tdd` pushes mocking, refactoring, and deep-module guidance
   into sibling files. The body stays scannable; depth is one link away.

## When to split, when to script

The split rules are explicit. Spawn a reference file when the body would exceed
its budget, when content covers distinct domains, or when a feature is rarely
needed. Add a `scripts/` utility when an operation is **deterministic** (the
`git-guardrails` block script, the `diagnose` HITL-loop template) — scripts save
tokens and are more reliable than code the agent regenerates each run. The rule
of thumb: prose for judgement, scripts for determinism, reference files for
depth the common path doesn't need.

References stay "one level deep" — the body links to a reference; the reference
does not chain to a third. This keeps the agent's loading decisions legible.

## Sources

- `sources/mattpocock/skills-repo/skills-productivity-write-a-skill-SKILL.md-57ae21a8.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/productivity/write-a-skill/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-tdd-SKILL.md-29d824ee.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/tdd/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-improve-codebase-architecture-SKILL.md-bb41f177.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/improve-codebase-architecture/SKILL.md
