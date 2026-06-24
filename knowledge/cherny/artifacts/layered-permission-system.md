# The layered permission system

How the harness author thinks about *safety as a system*, not a single switch.
Cherny describes Claude Code's permissioning as "a sophisticated permission system
with a combo of **prompt-injection detection, static analysis, sandboxing, and
human oversight**" — defense in depth, with the explicit goal of *reducing
prompts while staying safe* rather than choosing between the two.

The layers, and the design tension they resolve:

- **The two bad extremes.** Approving every file write and bash command (friction,
  and humans rubber-stamp) versus `--dangerously-skip-permissions` (no oversight at
  all). The system exists to give you a middle that is *both* safer and lower-
  friction.
- **Pre-approval lists.** Out of the box a small set of safe commands is approved;
  extend allow/block lists with `/permissions` (e.g. `"Bash(bun run *)"`,
  `"Edit(/docs/**)"`) and check them into the team's `settings.json`. This is the
  static, declarative layer.
- **The sandbox runtime.** An open-source, on-machine sandbox (`/sandbox`) with
  **file and network isolation** — opt in to improve safety *and* reduce prompts at
  once. (Worktrees give a complementary code-level isolation; see
  [[parallel-agents-are-the-productivity-unlock]].)
- **Auto mode — the classifier layer.** Instead of asking you, route each action
  to a safety classifier that decides on your behalf (built-in injection detection
  + static analysis). Cherny's argument is the load-bearing one: auto mode is
  *arguably safer than reading every prompt yourself*, because a human approving a
  stream of prompts stops actually checking, while the classifier doesn't fatigue.
  This is the productized form of the earlier "route permission requests to Opus via
  a hook" pattern (see [[hooks-deterministic-lifecycle-integration]]).
- **Scope.** Permissions configure per-codebase, per-subfolder, per-user, or via
  enterprise-wide policy.

The principle: **safety is layered and declarative, and the human-in-the-loop is
the *weakest* layer for routine decisions** — a rubber-stamp adds friction without
real review. The right design pushes routine safety to deterministic/classifier
layers and reserves human attention for what those can't judge. This is what makes
[[autonomous-unattended-operation]] defensible rather than reckless.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
