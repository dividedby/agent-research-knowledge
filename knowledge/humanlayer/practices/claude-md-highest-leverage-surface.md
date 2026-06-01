# CLAUDE.md is the highest-leverage surface — and the most abused

`CLAUDE.md` (and `AGENTS.md`) is the one file the harness injects into *every single
session*. That makes it the single highest-leverage point of the whole setup: it
shapes every phase of the workflow and every artifact produced. The leverage cuts
both ways — a bad line of code is one bad line, but a bad line in CLAUDE.md corrupts
research, plans, and code across every session that ever runs. So **craft it by hand,
line by line; never `/init` or auto-generate it.**

What it's *for* is onboarding: since the model knows nothing about your codebase at
the start of each session, CLAUDE.md supplies the **WHAT** (stack, structure, a map
of the repo — vital in monorepos), the **WHY** (purpose of the project and its
parts), and the **HOW** (how to build, test, typecheck, verify; e.g. "use `bun`").

The dominant failure is stuffing it. Three rules counteract that:

- **Less is more.** It spends instruction budget on every session (see
  *instruction-budget*), so include as few instructions as possible.
- **Universally applicable only.** Anything relevant to just *some* tasks (how to
  structure a new DB schema, deploy steps) is noise on every unrelated session.
  HumanLayer's own root file is **under 60 lines**; consensus ceiling is ~300.
- **Progressive disclosure over inclusion.** Don't put everything *in*; tell the
  agent *how to find* it. Keep task-specific guidance in separate, self-describing
  markdown files (`agent_docs/running_tests.md`, `…/service_architecture.md`) and
  have CLAUDE.md list them with one-line descriptions so the agent reads only the
  relevant one — optionally surfacing its picks for approval first. **Prefer pointers
  to copies**: reference `file:line` rather than pasting code snippets that rot.

There's also a *why-it-gets-ignored* insight you can act on. Claude Code wraps your
CLAUDE.md in a system reminder saying the content "may or may not be relevant… do not
respond unless highly relevant." The model therefore *discards* sections it judges
irrelevant — and the more non-universal cruft the file carries, the more readily it
discards even the good instructions. (Anthropic likely added the reminder precisely
because most CLAUDE.md files are bloated with non-applicable "hotfix" instructions;
telling the model to ignore the bad ones improved results.)

One tactic for the genuinely conditional content you can't fully externalize: wrap it
in **`<important if="…">` blocks** with a *narrow* condition
(`<important if="you are writing or modifying tests">`). The explicit trigger gives
the model a clear signal about *when* the rules apply instead of leaving relevance to
its own judgment, which improves adherence. Keep conditions specific —
`<important if="you are writing code">` matches everything and defeats the purpose —
and don't wrap the universal stuff (identity, structure, stack) at all.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-writing-a-good-claude-md-2fad0803.md`
  — origin: https://www.humanlayer.dev/blog/writing-a-good-claude-md
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-stop-claude-from-ignoring-your-8ba6ead7.md`
  — origin: https://www.humanlayer.dev/blog/stop-claude-from-ignoring-your-claude-md
