# Labels are the state machine: agent phases as GitHub Actions

In `course-video-manager`, the AFK pipeline runs as a family of
`.github/workflows/agent-*.yml` workflows (implement, implement-pr, implement-prd,
review, update-branch, promote-queued, architecture-review). The control surface is
**GitHub labels**: an issue gets `agent:implement`, a PR gets `agent:review`, and
the corresponding workflow fires on the `labeled` event. The label set
(`agent:implement` / `agent:review` / `agent:in-progress` / `agent:blocked`) is a
visible state machine the agent and the human share — work advances by relabelling.

## Each workflow is the same envelope

`agent-implement.yml` and `agent-review.yml` share a shape that any phase reuses:

1. **Transition in.** Remove the trigger label and `agent:blocked`, add
   `agent:in-progress` — so the board always shows what's mid-flight.
2. **Do the phase** by running the matching `.sandcastle/*.ts` script.
3. **Advance on success.** The implement phase ends by *adding the next label* —
   `agent:review` on the new PR — which fires the review workflow. Phases chain by
   label, not by one monolithic job.
4. **Block on failure.** Add `agent:blocked`, comment the failure reason (read from
   a `failure_reason.txt` the script writes) and a "re-add the label to retry" line.
5. **Always** remove `agent:in-progress` (`if: always()`), so a crash never strands
   the board in a lie.

## Refuse before you act

The highest-signal part is the pre-flight guards that make the pipeline safe to
leave unattended. `agent-implement.yml` inspects issue shape before doing anything
and **refuses** when the request is malformed, each refusal commenting *why* and
clearing the label:

- The issue is a **PRD** (has sub-issues) → silently defer to
  `agent-implement-prd.yml`.
- The issue is itself a **sub-issue** → refuse; "add `agent:implement` to the parent
  PRD instead," mark `agent:blocked`.
- An **open PR already targets this issue** (searched by `Closes/Fixes/Resolves
  #N`) → refuse; "close it first, then re-add the label."

Acting only when preconditions hold — and explaining the refusal in-thread — is
what lets a label-trigger be fire-and-forget.

## The CI-specific sharp edges

Two non-obvious mechanics make label-chaining actually work on GitHub:

- **Chaining needs a PAT, not `GITHUB_TOKEN`.** Label adds made with the default
  `GITHUB_TOKEN` do **not** trigger downstream workflows; the implement job adds
  `agent:review` with `AGENT_PAT` (falling back to `GITHUB_TOKEN` with a logged
  warning that a human will then have to re-label).
- **`pull_request_target`, not `pull_request`, for review.** The standard trigger
  needs a generated merge commit GitHub fails to produce on a conflicting/out-of-date
  PR; `pull_request_target` runs in the base context and fires reliably.
- **Push safety matches the phase.** Implement force-pushes (the branch name is
  deterministic from the issue number, so any remote ref is an orphan); review
  uses `--force-with-lease` against the SHA it checked out and **aborts cleanly**
  if the branch advanced mid-run, writing a "branch advanced" reason and blocking
  rather than clobbering.

This is the event-driven, one-issue-per-trigger topology. The same repo also runs a
batch orchestration loop — see [[sandcastle-plan-execute-merge-loop]] — and both
hand the agent's results to deterministic steps via
[[structured-output-with-session-retry]].

## The shipped stack: GitHub Actions + Sandcastle + Claude Code

Matt's current "favourite stack" is exactly this topology productised:
**GitHub Actions + Sandcastle + Claude Code**, with the one-line promise *"Label
an issue, get an implementation."* The same label-as-trigger surface scales up
from a single issue to **multi-step PRDs** running live. Where this repo's
`course-video-manager` shows the pattern hand-rolled, the Sandcastle harness is
the reusable form — and it carries built-in support for the autonomous-loop case
too: a Ralph loop is configured by setting `maxIterations` rather than scripting a
bash cap (see `sandcastle-plan-execute-merge-loop`, `autonomous-loops-ralph`).

## Sources

- `sources/mattpocock/course-video-manager/.github-workflows-agent-implement.yml-f2a00aec.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.github/workflows/agent-implement.yml
- `sources/mattpocock/course-video-manager/.github-workflows-agent-review.yml-ddaff44e.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.github/workflows/agent-review.yml
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067721938894500036-65f0fb11.md` — origin: https://x.com/mattpocockuk/status/2067721938894500036
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067919429216645366-e4027437.md` — origin: https://x.com/mattpocockuk/status/2067919429216645366
