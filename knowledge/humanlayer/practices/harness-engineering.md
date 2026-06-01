# Harness engineering: it's a config problem, not a model problem

When a coding agent ignores instructions, runs something dangerous, or gets stuck on
something simple, the instinct is to wait for a smarter model. HumanLayer's testing
across dozens of projects points the other way: **it's usually a configuration
problem.** Models will keep improving and will keep hitting unexpected failures
regardless — so the leverage is in getting the most out of *today's* model by
engineering the **harness**: the runtime environment and peripherals around the model.

Harness engineering is a subset of context engineering, framed as a loop: when the
agent makes a mistake, change the harness so it can never make that mistake again.
(The post even notes models can be *over*-fitted to their training harness — Opus
improved in relative ranking when moved to a different harness on Terminal Bench —
so configuring the harness is fair game, not a violation of how the model "wants" to
run.)

The configuration surfaces, in rough order of leverage:

- **CLAUDE.md / AGENTS.md** — deterministically injected every session; the highest-
  leverage and most-abused surface. Keep it concise and universally applicable.
  (See *claude-md-highest-leverage-surface*.)
- **MCP servers** — extend capability, but every tool description is injected into
  the prompt, costs instruction budget, and is a prompt-injection vector. Connect
  only trusted servers, only the tools actually needed. If a CLI already in training
  data (gh, docker, psql) covers it, prompt the agent to use the CLI — it composes
  with `grep`/`jq` and costs no budget.
- **Skills** — reusable knowledge delivered by progressive disclosure: only the
  relevant instructions/tools load when needed. Treat skill registries like untrusted
  npm — hundreds of malicious skills have circulated; review before installing.
- **Sub-agents** — context isolation (see *small-focused-agents*).
- **Hooks** — deterministic control flow at lifecycle events: notifications,
  auto-approve/deny, integrations, and verification that surfaces only errors (see
  *context-efficient-backpressure*).

The meta-lesson is about *how* to configure, and it mirrors good engineering taste:
**start simple and add configuration only when you hit a real failure.** Designing
the ideal harness up front, or installing dozens of skills and servers preemptively,
or running the full test suite at every turn — all backfire. Build, test, iterate,
and discard what doesn't help; optimize for iteration speed over first-attempt
success. "It's a skill issue" applies to your harness as much as to the model.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-skill-issue-harness-engineerin-313aa20b.md`
  — origin: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
