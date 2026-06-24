# Hooks: deterministic lifecycle integration

Hooks are Cherny's primitive for making *deterministic* logic run at points in
the agent's lifecycle — the escape hatch for the things you cannot leave to a
probabilistic model. The design intent is explicit: "deterministically hook into
Claude's lifecycle." Where a skill or prompt is advisory, a hook *always* fires.

How the team uses them, by lifecycle event:

- **`PostToolUse`** — auto-format Claude's code after every edit. Claude generates
  well-formatted code ~90% of the time; the hook catches the edge cases that would
  otherwise fail CI. (A clean illustration of the division of labour: the model
  does the work, a deterministic hook enforces the invariant.)
- **`Stop`** — gate when Claude is allowed to *finish*: trigger a notification
  (Slack/system) so you know an unattended run is done, or run your test
  suite / hit a CI endpoint and refuse completion until it passes (the deterministic
  spine under `/goal`-style completion).
- **`UserPromptSubmit`** — e.g. auto-rename a session from the first prompt.
- **`PostCompact`** — fires *after* context compaction, letting you re-inject
  instructions or run commands so important context survives a compact.
- **Permission routing** — route permission requests to a model (Opus) via a hook
  that scans for attacks and auto-approves the safe ones (a precursor to built-in
  auto mode; see [[layered-permission-system]]).

Operational details worth keeping: settings live-reload (and so do
keybindings — every key binding is customizable in `~/.claude/keybindings.json`);
Claude can *write the hook config for you* — "ask Claude to add a hook to get
started." Non-Git VCS users (Mercurial, Perforce, SVN) can define worktree hooks
to get isolation benefits without Git.

The principle: **use hooks for the invariants you refuse to leave to the model —
formatting, completion gates, notifications, post-compact survival.** They are the
deterministic counterweight to everything else in the harness being a judgment
call. Committed in `settings.json` like the rest (see
[[customization-checked-into-git]]).

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
