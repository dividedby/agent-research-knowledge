# A thin harness: own only what you control, fail fast, loop in the consumer

Sandcastle's ADRs and `.out-of-scope/` notes converge on one design stance for an
agent harness: **stay thin.** The framework does the irreducible orchestration
(sandbox, worktree, run the agent, extract output) and deliberately refuses
responsibility for anything it doesn't control or the user can do themselves. The
recurring phrase is "control is inverted towards the user."

## Don't wrap an interface you don't own

- **No provider-error retry.** Sandcastle shells out to provider CLIs (Claude Code,
  etc.) and won't parse their error shapes to detect retryable conditions: "taking
  responsibility for an interface we don't control and that could change at any
  time." Blind retry on any non-zero exit "would mask real errors… and waste
  time/money." It fails fast so the user gets actionable feedback (upgrade, wait,
  switch provider).
- **User owns the scaffold.** `init` writes a working `Dockerfile` into the project
  and then it's the user's — no Dockerfile-composition abstraction layer, which
  "would add complexity for something already achievable by editing the Dockerfile
  directly" and couples init too tightly to one of several sandbox providers.
- **Inline prompts pass through literally** (ADR 0008): if you built the string in
  JS you own its interpolation; only `promptFile` templates go through the
  `{{KEY}}` pipeline. The rule follows the *source* of the prompt rather than a
  flag, so forwarded content (issue bodies, transcripts) that happens to contain
  `{{…}}` never trips the substitution scanner.

## Fail fast, never degrade — especially AFK

ADR 0020 makes the asymmetry explicit: idempotent infrastructure races (a
`git worktree add` hitting an overlayfs 126/137) are safe to retry, but prompt
expansion "produces content the agent acts on," so its failures fail fast — no
retry, no graceful `<expansion-failed>` degradation. The reasoning is an
AFK-cost argument: silently feeding the agent a prompt built under a degraded
environment "runs the agent against a wrong prompt, burning an iteration and
possibly committing garbage — more expensive to recover from… than a clean abort."
Loud beats lossy. (The same instinct rejects tolerant JSON parsing for structured
output in ADR 0010: "Hides genuine model failures behind a forgiving parser… Loud
is better.")

The same instinct shapes `sandcastle init`: every interactive prompt is paired with
a CLI flag so the whole setup can run non-interactively (CI, scripts). When stdin is
not a TTY and a required flag is missing, init **fails fast naming the missing
flag** rather than wedging on a prompt library or proceeding with a silent default —
a wrong setup is worse than a clean stop that tells you exactly which flag to pass.

## Expose recovery, but keep the loop in the consumer

The thin-harness line is sharpest where it would be tempting to add cleverness:
retry/feedback orchestration. `run()` *throws* `StructuredOutputError` carrying
everything needed to recover — `commits`, `branch`, preserved worktree, and
(post-amendment) the failed iteration's `sessionId` — and stops there. "Retry/
feedback orchestration stays out of Sandcastle: the error exposes what's needed
for recovery, and the loop lives in the consumer." Likewise `.resume()` is
*exactly one iteration* (ADR 0011) — multi-step continuation is the caller chaining
`.resume()` calls, making each session boundary explicit, rather than the harness
hiding a loop. This is the seam the consumer-side retry pattern is built on
([[structured-output-with-session-retry]]).

The payoff of the discipline is that adding a provider or a workflow is *purely
additive* (ADR 0012: providers own their own session storage end-to-end, so a new
agent is "implement `sessionStorage`, emit `session_id`… no central code changes").
A harness that owns less has less to change. The payoff is visible in the breadth
the abstraction now carries: a single `AgentProvider` interface fronts claudeCode,
codex, pi, opencode, copilot, and cursor, each normalizing its own CLI-flag shape,
stream-parse format, and session quirks behind the same contract — adding the next
one is still purely additive. Most of these boundaries are recorded
as refusals in [[out-of-scope-as-design-discipline]]; the philosophy here is the
*why* underneath them.

## Sources

- `sources/mattpocock/sandcastle/.out-of-scope-provider-error-retry.md-19d09e74.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.out-of-scope/provider-error-retry.md
- `sources/mattpocock/sandcastle/.out-of-scope-custom-base-image-abstraction.md-27495145.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.out-of-scope/custom-base-image-abstraction.md
- `sources/mattpocock/sandcastle/docs-adr-0008-inline-prompts-skip-processing.md-5f56cccd.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0008-inline-prompts-skip-processing.md
- `sources/mattpocock/sandcastle/docs-adr-0020-prompt-expansion-fails-fast.md-20cdf35e.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0020-prompt-expansion-fails-fast.md
- `sources/mattpocock/sandcastle/docs-adr-0010-structured-output.md-df5103e4.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0010-structured-output.md
- `sources/mattpocock/sandcastle/docs-adr-0011-resume-is-one-iteration.md-217c0b1d.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0011-resume-is-one-iteration.md
- `sources/mattpocock/sandcastle/docs-adr-0012-agent-provider-owned-session-storage.md-8ca410f0.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0012-agent-provider-owned-session-storage.md
- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: github.com/mattpocock/sandcastle (CHANGELOG.md)
- `sources/mattpocock/sandcastle/README.md.md` — origin: github.com/mattpocock/sandcastle (README.md)
- `sources/mattpocock/sandcastle/src-AgentProvider.ts-c6a6e278.md` — origin: github.com/mattpocock/sandcastle (src/AgentProvider.ts)
