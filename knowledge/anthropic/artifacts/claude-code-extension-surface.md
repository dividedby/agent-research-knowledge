# Configuring and extending the Claude Code harness

Claude Code ships a layered set of extension points; choosing the right one for a
given need is most of the configuration craft. Each trades off advisory-vs-
deterministic, in-context-vs-out, and manual-vs-automatic.

- **`CLAUDE.md`** — a file read at the start of every conversation, giving
  persistent context the agent can't infer from code: bash commands it can't
  guess, code-style rules that differ from defaults, test runners, repo etiquette,
  project-specific architecture, environment quirks, non-obvious gotchas. It is
  *advisory*, and subject to context-as-finite-resource: keep it short, and apply
  the test "would removing this cause mistakes?" — a bloated `CLAUDE.md` causes the
  agent to ignore the rules that matter. Exclude anything the agent can figure out
  from the code, standard conventions, frequently-changing info, and detailed API
  docs (link instead). It composes across scopes (home, project root, parents for
  monorepos, on-demand child dirs) and supports `@path` imports. `/init` analyzes
  the codebase to scaffold a first draft you then refine.
- **Hooks** — scripts run automatically at workflow points. Unlike `CLAUDE.md`
  instructions, hooks are **deterministic**: they guarantee the action happens
  (run eslint after every edit; block writes to a protected folder). Convert a
  rule the agent keeps violating into a hook. A Stop hook can gate turn completion
  on a check passing.
- **Skills** — folders with a `SKILL.md` under `.claude/skills/`, applied
  automatically when relevant or invoked with `/name`; use
  `disable-model-invocation: true` for side-effecting workflows you want to trigger
  manually. (See the Agent Skills concept.)
- **Subagents** — run in their own context window with their own allowed tools;
  the primary tool for investigation, since reading many files in a subagent keeps
  that load out of the main context and returns only a summary.
- **MCP servers, CLI tools, plugins** — MCP connects external systems
  (issue trackers, databases, Figma, monitoring). But **CLI tools are the most
  context-efficient** way to reach a service — install `gh` rather than relying on
  the raw GitHub API; the agent can even learn an unfamiliar CLI from its
  `--help`. Plugins bundle skills/hooks/subagents/MCP into one installable unit.

The harness also scales **horizontally** beyond one human/one conversation:
non-interactive `claude -p` for CI/hooks/pipelines (with parseable JSON output);
parallel sessions via git worktrees (isolated checkouts so edits don't collide),
the desktop app, web VMs, or coordinated agent teams; and **fan-out** across many
files for large migrations (have the agent generate the file list, then distribute
the work). Permission friction is reduced three ways — allowlists for known-safe
tools, OS-level sandboxing, or auto mode (a classifier vets commands) — each
trading safety against convenience. (Auto mode self-limits under `-p`: with no
human to fall back to, it aborts if the classifier repeatedly blocks actions.)

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-code-best-practic-4d249e2a.md` — https://www.anthropic.com/engineering/claude-code-best-practices
- `sources/anthropic/best-practices/https-code.claude.com-docs-en-best-practices-fb8dc53b.md` — https://code.claude.com/docs/en/best-practices
