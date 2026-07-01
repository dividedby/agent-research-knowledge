# A raw exec escape hatch on the warm sandbox, for verification gates between agent turns

Sandcastle's `Sandbox` handle (from `createSandbox()`, and `worktree.createSandbox()`)
exposes `sandbox.exec(command, options?)` — a direct passthrough to the underlying
provider's `exec()`, running a shell command in the same warm container an agent
turn just ran in. It returns the full `ExecResult`, including a non-zero `exitCode`
as data rather than throwing, so a caller can branch on pass/fail the same way it
would branch on any other result. `cwd` defaults to the sandbox's repo path, kept
consistent across providers, with an override available.

## Why this earns a harness primitive instead of staying provider-internal

The `Sandbox` handle already exposes `.resume()`/`.fork()` for continuing the
*agent's* session inside the same warm container ([[session-fork-for-fanout]]) —
but a verification gate (run the test suite, run the linter, run a custom check
script) is not an agent turn at all; it's a deterministic command
([[agent-feedback-loops-as-quality-gates]]) that needs the same warm environment
without paying for a model call. Before `exec`, getting that had meant reaching
past the `Sandbox` handle into the underlying provider — coupling caller code to
whichever provider was configured. Exposing `exec` on the handle itself keeps a
multi-phase loop (implement → verify → review) entirely on the same public
surface, provider-agnostic, without tearing down and re-creating the sandbox
between phases.

This is consistent with the harness's own stance on where the loop lives
([[thin-fail-fast-harness]]): Sandcastle doesn't build a "verification gate"
abstraction with its own config surface — it exposes the raw exec primitive and
leaves the caller to decide what "pass" means and what to do on failure (feed the
result back into a `.resume()` call, abort, retry). The warm-sandbox reuse payoff
is the same one `.resume()`/`.fork()` unlocked for agent turns: no repeated
container boot across phases of a single loop iteration.

## Sources

- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/CHANGELOG.md (0.12.0, changeset 0f577a4)
