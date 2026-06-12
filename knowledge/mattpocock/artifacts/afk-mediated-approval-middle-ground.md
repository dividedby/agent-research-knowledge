# AI-mediated per-tool approval: a middle ground between bypass and asking a human

An AFK agent that runs unattended on the host (`noSandbox()` + `run()`) has, until
now, only two postures toward tool permissions: **full bypass**
(`--dangerously-skip-permissions`), which is fast but unguarded, or **manual
approval**, which defeats the point of running away-from-keyboard. Sandcastle adds
a third: let *an AI* adjudicate each approval prompt, so the run stays autonomous
but every risky tool call is still judged rather than waved through.

## Two provider-specific routes to the same shape

The middle ground is exposed as a provider option, mapping onto whatever the
underlying CLI already offers:

- **Claude Code — `claudeCode({ permissionMode })`.** Sandcastle's default is to
  emit `--dangerously-skip-permissions`; setting `permissionMode` instead emits
  `--permission-mode <mode>`. The interesting value is `"auto"` — Claude evaluates
  each tool call and approves/denies without surfacing a human prompt and without
  blanket bypass. (The full Claude mode set is accepted: `default`, `acceptEdits`,
  `plan`, `auto`, `dontAsk`, `bypassPermissions`.)
- **Codex — `codex({ approvalsReviewer })`.** `"auto_review"` swaps
  `--dangerously-bypass-approvals-and-sandbox` for
  `-a on-request -s danger-full-access -c approvals_reviewer="auto_review"`, so
  Codex's own *reviewer agent* evaluates each approval prompt instead of the run
  bypassing approvals entirely.

## Why it's a per-provider knob, not a harness feature

Both routes are thin pass-throughs to the agent CLI's existing approval machinery —
Sandcastle's only job is to stop forcing the bypass flag and forward the milder one.
This is the thin-harness stance ([[thin-fail-fast-harness]]): the harness does not
build its own approval adjudicator; it exposes the provider's. The trade-off the
option encodes is autonomy vs. blast radius — `auto`/`auto_review` keeps an AFK run
hands-off while restoring a per-call check that the older all-or-nothing bypass
threw away. The default stays bypass (the AFK happy path is a sandboxed container
where the blast radius is already contained); the middle ground is opt-in for the
riskier host-run case.

## Sources

- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: github.com/mattpocock/sandcastle (CHANGELOG.md)
- `sources/mattpocock/sandcastle/README.md.md` — origin: github.com/mattpocock/sandcastle (README.md)
