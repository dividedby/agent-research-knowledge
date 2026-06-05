# Permission system design: rules over file restrictions

How Amp gates tool calls. The design premise is the inverse of "lock the agent
down": agents work best with feedback and easy-undo tools (git makes a wrong edit
free), so the default should be permissive, with rules layered on only where the
*action* is genuinely irreversible — a deploy, a prod-DB write, a `git push`,
`terraform apply`. The system serves two valid operator types: those who want to
get out of the way, and those tired of approving every call.

The model: before *any* tool call, Amp checks permission rules **in sequence**
until one matches; that rule's action wins. Actions are `allow`, `ask`,
`reject`, and `delegate`. Rules live under the `amp.permissions` setting, edited
via CLI or VS Code, and match on tool name plus tool-specific arguments
(`--path`, `--cmd`, MCP params like `--projectKey`). A `test` subcommand shows
which rule matches a hypothetical call, and `tools list` / `tools show` reveal
tool names and their parameters so you can write precise rules.

Patterns the system supports:

- **Allowlist-by-default with narrow asks** — `ask Bash --cmd '*rm*rf*'` then
  `allow '*'`: wave everything through except dangerous-looking deletes.
- **Order matters; specific-before-general or broad-then-carve-out** — prepend a
  rule to ask on reads of dotfiles; or `allow Bash --cmd "*terraform*"` then a
  later `reject` of `*apply*`/`*destroy*`/`*force-unlock*`.
- **Cmd-string matching is substring/glob over the whole pipeline** — `*git*push*`
  matches `git push`, `... && git push`, `git --work-tree=. push`. You're
  matching text that *looks like* the command, not parsing it.
- **MCP-param scoping** — allow `createJiraIssue` only when `--projectKey
  EXPERIMENT`, ask otherwise.
- **`delegate` to an external helper** — hand the decision to a program on
  `$PATH` that receives tool params as JSON on stdin and answers by exit code
  (`0` allow, `1` ask, `2` reject, with stderr forwarded to the model). Enables
  stateful logic (reject `git push` only when there are unstaged changes) or
  forwarding to a central policy engine like Open Policy Agent for org-wide rules.

What Amp deliberately does **not** do, and why (the design boundary):

- **No file-ignore lists.** Hiding files from the model is *actively harmful*: it
  encourages creative workarounds (reading via Bash), wasting tokens, and any
  Bash-circumventable restriction is only a false sense of security. Amp instead
  redacts known secrets and offers the permission system for real control.
- **The agent doesn't touch VCS on its own.** Maximum freedom to edit/run, with
  VCS as the always-present background safety net — so it won't stage/commit
  unprompted (you can still tell it to).
- **Not a defense against prompt-injection** driving the Bash tool to run
  malicious code — explicitly out of the threat model for now.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-permissions-b6eba13f.md` — origin: https://ampcode.com/notes/permissions
- `sources/amp/chronicle/https-ampcode.com-notes-fif-dc1eb004.md` — origin: https://ampcode.com/notes/fif
