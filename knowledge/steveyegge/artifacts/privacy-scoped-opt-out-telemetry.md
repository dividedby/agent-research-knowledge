# Privacy-Scoped, Opt-Out Telemetry

A CLI meant to be invoked unattended by agents cannot rely on an interactive
consent prompt, so its telemetry design has to earn trust structurally: collect
the minimum signal that's useful, and make opting out layered and discoverable
rather than a single buried flag. Beads' usage metrics do both.

## What's collected — and what deliberately isn't

Each event is a `cli_command` record carrying only the command name; each batch
adds the bd version and OS platform, keyed by a machine-derived, HMAC-protected
anonymous ID. No email, repo path, remote URL, issue content, or other
user-supplied string is collected. Scoping the event to "which command ran" —
not its arguments or output — gives maintainers real adoption/usage signal
without the payload ever being able to leak what a user or agent was actually
working on.

## Layered opt-out, not one off-switch

Metrics are on by default, but three independent ways to turn them off compose
without conflicting:

- `bd metrics off` (or `on` / `example`) — the persistent, discoverable toggle;
  takes effect on the next command, no restart needed.
- `BD_DISABLE_METRICS=1` — a one-off, shell-scoped override for a single
  invocation or session, without touching the saved preference.
- `DO_NOT_TRACK=1` — the cross-tool [DO_NOT_TRACK](https://donottrack.sh/)
  convention, honored as **disable-only**: a falsey or empty value
  (`DO_NOT_TRACK=0`, `false`, or unset) falls through to the saved `bd metrics`
  preference rather than forcing metrics back on. Respecting the standard's
  intent — an explicit opt-out is honored — without letting its absence
  override a user's explicit opt-*in*.

`BD_DISABLE_METRICS` is the bidirectional override and wins when both env vars
are set, so a script that needs metrics off in one specific run has an
unambiguous lever even in an environment where `DO_NOT_TRACK` is already
managed by something else.

## Why this shape

An agent embedded in someone else's repo runs commands the human never
individually approved; if telemetry defaults were invasive (full arguments,
repo identity) or hard to disable (no env var, no honoring of the ecosystem
standard), every agent invocation would be silently exporting information the
human never agreed to share. Minimizing the payload and stacking cheap,
composable opt-outs — a persistent command, a one-shot env var, and the
industry convention — moves the design from "technically has an opt-out" to
"an agent operator can trust the default."

## Sources

- `sources/steveyegge/beads/AGENT_INSTRUCTIONS.md.md` (`## Telemetry` section — payload scope, `bd metrics`, `BD_DISABLE_METRICS`, 2026-06-23 revision; `DO_NOT_TRACK` disable-only honoring + precedence, 2026-07-22 revision) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/AGENT_INSTRUCTIONS.md
