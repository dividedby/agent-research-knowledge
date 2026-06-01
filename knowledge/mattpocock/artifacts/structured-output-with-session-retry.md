# Structured output: separate the work from the report, retry only the report

Sandcastle's seam between a generative agent and the deterministic pipeline around
it is a **single `<output>` JSON block**, emitted as the last thing in the agent's
response and schema-validated by the runner. The review phase's `extraction.md`
shows the discipline: copy the field names exactly, omit nothing required, and
"do **not** add fields that aren't listed (no `verdict`, no `file`, no
`lineRange`) — the JSON is machine-parsed; extra or renamed fields cause a
validation failure." Downstream the workflow even validates semantic anchors
(an inline comment's `path`+`line` must exist in the diff) and silently drops
hallucinated ones.

## Producing and reporting are different acts

The prompt that does the work and the prompt that emits structured output are kept
apart. `implement/prompt.md` is pure task instruction (read `CONTEXT.md` and ADRs,
red-green-refactor, conventional commits, "do not close the issue yourself") with
no mention of output shape. `review/extraction.md` is pure emission instruction:
"You have finished the review. **Do not make any further code changes** — only
report what you already did." Separating them keeps each prompt single-purpose and
lets the report be regenerated without touching the work.

That separation is encoded as two runner wrappers, chosen by whether the work has
side effects:

- **`runWithExtraction`** — for side-effecting work (an agent that edited files):
  a *produce* pass does the work, then a separate *extract* pass emits the output.
- **`runWithRetry`** — for side-effect-free work where "the structured output IS
  the work" (drafting a PR title/description, slicing a PRD): one combined prompt,
  because splitting "buys nothing — the drafting and the emission are the same act."

## Failed extraction resumes the session — it never redoes the work

The key move: when validation throws `StructuredOutputError`, the wrapper does not
re-run from scratch. It **resumes the same agent session** (via
`error.sessionId`) and sends only a feedback message — `buildRetryFeedback` shows
the agent *exactly what it emitted last time* and the precise schema/JSON reason it
failed, then says "Fix the problem and re-emit a single corrected `<output>`
block. **Do not change any code — only the output.**" Because the session still
holds everything the agent did, the retry only re-emits; nothing is recomputed.
Default `maxAttempts` is 3 (one call + two resumed retries); the final error
propagates if all fail.

Two details make the feedback load-bearing: it special-cases "no `<output>` block
at all" versus "block present but invalid," and the feedback text always contains
the literal opening tag so it satisfies the runner's "resolved prompt must contain
the tag" constraint when sent as a standalone retry prompt. The captured rationale:
showing what was emitted and why it failed is "the highest-leverage signal for
getting valid output next time."

This is the seam both Sandcastle topologies rely on — the
[[label-driven-agent-ci-pipeline]] feeds the `<output>` JSON straight into
`gh api` review calls, and the [[sandcastle-plan-execute-merge-loop]] parses the
planner's `<plan>` tag the same way.

## The seam is designed into the framework, not bolted on

The Sandcastle framework itself defines this contract, and its ADRs spell out the
reasoning the consumer-side wrappers inherit. **Structured output is orthogonal to
the completion signal** (ADR 0010): `run({ output: Output.object({ tag, schema }) })`
scans stdout for the tag, *last match wins* (so an agent's self-correction is
benign), unwraps an optional ```` ```json ```` fence, and **throws**
`StructuredOutputError` on a missing tag / invalid JSON / schema failure — no
tolerant parsing ("Hides genuine model failures… Loud is better"), no auto-cleanup,
caller decides recovery. The caller owns the prompt-side instruction; `run()`
refuses at entry if the resolved prompt lacks the tag.

Crucially, an amendment to ADR 0010 added the failed iteration's `sessionId` to the
error *specifically* to make "resume the session and re-emit" possible — "Resuming
the session **is** recovery… rather than redo the work," replacing the fragile
workaround of scavenging the newest session file by mtime. And the framework draws
the line there: "**Retry/feedback orchestration stays out of Sandcastle: the error
exposes what's needed for recovery, and the loop lives in the consumer**" — which is
exactly why the `run-with-retry`/`run-with-extraction` wrappers above live in the
*workflows*, not the library. Resumability rests on two more decisions: `.resume()`
is exactly one iteration (ADR 0011 — each iteration is its own session, so
multi-step is the caller chaining calls) and providers own their session storage
end-to-end (ADR 0012 — `supportsResume` is derived from whether a provider supplies
it). See [[thin-fail-fast-harness]] for the stance behind keeping the loop out of
the harness.

## Sources

- `sources/mattpocock/course-video-manager/.sandcastle-run-with-retry.ts-fa4260dc.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/run-with-retry.ts
- `sources/mattpocock/course-video-manager/.sandcastle-retry-feedback.ts-da71923d.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/retry-feedback.ts
- `sources/mattpocock/course-video-manager/.sandcastle-review-extraction.md-416b5aff.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/review/extraction.md
- `sources/mattpocock/course-video-manager/.sandcastle-implement-prompt.md-2fa692ad.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/implement/prompt.md
- `sources/mattpocock/sandcastle/docs-adr-0010-structured-output.md-df5103e4.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0010-structured-output.md
- `sources/mattpocock/sandcastle/docs-adr-0011-resume-is-one-iteration.md-217c0b1d.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0011-resume-is-one-iteration.md
- `sources/mattpocock/sandcastle/docs-adr-0012-agent-provider-owned-session-storage.md-8ca410f0.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0012-agent-provider-owned-session-storage.md
- `sources/mattpocock/sandcastle/.sandcastle-agent-workflows-shared-run-with-retry.ts-6076580a.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.sandcastle/agent-workflows/shared/run-with-retry.ts
- `sources/mattpocock/sandcastle/.sandcastle-agent-workflows-shared-run-with-extraction.ts-9695224e.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.sandcastle/agent-workflows/shared/run-with-extraction.ts
- `sources/mattpocock/sandcastle/.sandcastle-agent-workflows-shared-retry-feedback.ts-06891b84.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.sandcastle/agent-workflows/shared/retry-feedback.ts
