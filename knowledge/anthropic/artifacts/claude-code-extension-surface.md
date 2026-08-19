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
  monorepos, on-demand child dirs) and supports `@path` imports. The project root
  actually holds two files with opposite sharing intent: `./CLAUDE.md` is checked
  into git for the team, while `./CLAUDE.local.md` holds personal,
  project-specific notes and belongs in `.gitignore` — separating "persistent
  context for every session" from "my own scratch notes" that shouldn't ship to
  teammates. `/init` analyzes
  the codebase to scaffold a first draft you then refine. Verify what actually
  loaded with `/context` rather than assuming it did — and since the whole file is
  paid for on every turn, route anything only *sometimes* relevant (domain
  knowledge, situational workflows) into a Skill instead, which loads on demand
  rather than bloating every conversation. Two symptoms diagnose a
  broken file: if the agent keeps violating a rule you already wrote, the file is
  too long and that rule is getting lost in the noise; if it asks a question
  `CLAUDE.md` already answers, the phrasing is ambiguous. Treat it like code —
  review it when things go wrong, prune it regularly, verify a change by observing
  whether behavior actually shifts — and check it into git so it compounds in
  value across the team. Emphasis markers (`IMPORTANT`, `YOU MUST`) measurably
  improve adherence to a given rule.
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
non-interactive `claude -p` for CI/hooks/pipelines, with a choice of output shape
for the consuming script: plain text, a single `json` object carrying a `result`
field (read it once the process exits), or `stream-json` — one JSON object per
line, starting with an init event, for a caller that wants to consume progress
as it happens rather than wait for the final object
— the run still creates a resumable session by default, so a scripted `-p` call
is not throwaway state; pass `--no-session-persistence` to opt out;
parallel sessions via git worktrees (isolated checkouts so edits don't collide),
the desktop app, web VMs, or coordinated agent teams; and **fan-out** across many
files for large migrations (have the agent write the file list to disk, e.g.
`files.txt`, rather than just enumerate it in the transcript — a loop script in
the next step needs a durable list to read, not conversation text — then
distribute the work across it: restrict tool access with `--allowedTools` since
there's no human backstop once it's running unattended, and keep `--verbose` for
developing the prompt but drop it once you're running at scale). Approval-per-action is safe by
default but has its own failure mode — after the tenth prompt you're no longer
reviewing, you're clicking through — so permission friction is reduced: auto mode
(a separate classifier model reviews each command and blocks only what looks
risky — scope escalation, unknown infrastructure, hostile-content-driven
actions — letting routine work proceed without a prompt) is now the **built-in
starting permission mode** for interactive terminal and VS Code sessions on
Pro/Max/Team plans; other plans still start in Manual mode (ask before every
file write, Bash command, MCP tool — now a named mode, not just unlabeled
default behavior). Two more levers cut interruptions further, in Manual mode and
layered on top of auto mode alike: allowlists for known-safe tools, and
OS-level sandboxing — each trading safety against convenience.
(Under `-p`, repeated classifier blocks no longer abort the run — auto mode
instead falls back to a different behavior past a threshold, so an unattended
`-p` invocation keeps going rather than dying mid-task on repeated blocks.)

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-code-best-practic-4d249e2a.md` — https://www.anthropic.com/engineering/claude-code-best-practices
- `sources/anthropic/best-practices/https-code.claude.com-docs-en-best-practices-fb8dc53b.md` — https://code.claude.com/docs/en/best-practices
