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

## PRD sub-issues are linked natively, and creation logs its own progress

`to-issues-prd.ts` is what actually produces the sub-issues the refusal guard
above detects. A `runWithRetry` pass drafts an ordered list of slices (title,
what-to-build, acceptance criteria) from the PRD; the *script*, not the agent,
then turns each slice into a real GitHub sub-issue: `gh issue create`, followed
by `gh api -X POST repos/{repo}/issues/{prdNumber}/sub_issues` to link it to the
parent through GitHub's native sub-issue relationship — not just a "Parent PRD:
#N" text reference in the body, which `agent-implement.yml`'s "has sub-issues"
check couldn't detect. The creation loop logs which sub-issues it already made
before re-throwing on a failed create, so a partial batch failure surfaces as
"created so far: #12, #13" rather than silently vanishing — the same
never-leave-a-crash-unexplained instinct as the failure-reason comments below.

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

## The review phase now installs and defers to the shared skill

A later revision of `agent-review.yml` adds one step before the review runs:
`npx --yes skills@latest add mattpocock/skills -g -s review -a claude-code -y --copy`,
installing the `review` skill (see [[review-skill-two-axis-with-smell-baseline]])
globally into `~/.claude/skills` — outside the git work tree, so the review
agent's own commit step can never sweep the skill files into the PR. It's a
**global**, not project, install: every run pulls the current version of the
skill, and installing it globally rather than pinning a copy into the repo means
the CI pipeline always exercises the skill's latest revision, not a stale
snapshot frozen at whatever commit last vendored it.

The matching change lands in `.sandcastle/review/prompt.md`: the review process
step that used to be an inline six-point checklist (read the diff, verify
against spec, stress-test edge cases, ...) is replaced with a single instruction
to invoke the now-installed `review` skill and treat **its findings as the
single source of truth** — "act only on what it reports, not on a separate
ad-hoc pass of your own." The prompt still owns everything the skill doesn't:
fixing the fixed point to `main` and the diff to `git diff main...HEAD` so the
skill "does not run its own discovery and does not prompt or pause," passing the
already-fetched linked issue as the spec, and translating the skill's report
into concrete actions (fix correctness findings with a breaking test, apply
quality findings, surface spec findings for a human rather than silently adding
scope). The shape this reveals: when a shared, versioned skill exists, the
consuming CI prompt shrinks to *plumbing the skill its inputs* and *acting on
its output* — the review logic itself is deleted from the prompt and delegated
to the skill it now installs at run time.

A further revision renames the installed skill and every reference to it, in
lockstep, from `review` to `code-review` — matching the skill's own graduation
out of `in-progress` under that name (see
[[review-skill-two-axis-with-smell-baseline]]). Both the CI install step
(`-s code-review`) and the prompt's skill-invocation instructions update
together, in the same commit shape as the earlier install-and-defer change.
The mechanic this confirms: because the CI pipeline installs the shared skill
by name at run time rather than vendoring a copy, a rename upstream is a
one-line follow-up in the *consumer* — the coupling is a name, not a pinned
snapshot, so keeping the two in sync is a search-and-replace, not a re-audit of
frozen skill content.

## The upfront diff shrinks to a stat once the agent can pull the rest on demand

A later pair of revisions makes the same edit independently to two sibling
prompts: `.sandcastle/review/prompt.md` and `.sandcastle/implement-pr/prompt.md`
both replace their injected `<diff-to-main>` block — previously the full
`git diff main..HEAD` patch — with `git diff main..HEAD --stat`, a file-and-
line-count summary instead of the patch body. The review prompt states the
reasoning inline: "The full patch is deliberately omitted here because it can
be very long. Go deeper on the files that matter — run
`git diff main..HEAD -- <path>` on the changed files above to read the actual
changes before reviewing." Both prompts already had a reason the full patch
wasn't load-bearing up front: review delegates the actual diff analysis to the
installed `code-review` skill, which does its own `main...HEAD` discovery (see
above); implement-pr's work is driven by the PR-comments payload, not the raw
diff. So the injected block was mostly for situational orientation, not the
substance of either agent's task — trimming it to a stat, with an explicit
per-file drill-down path, is [[keep-the-agent-in-the-smart-zone]]'s smart-zone
budgeting applied to *prompt template design*: don't pay upfront-context cost
for content the agent can fetch precisely, and only for the files that turn
out to matter.

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
- `sources/mattpocock/course-video-manager/.github-workflows-agent-review.yml-ddaff44e.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.github/workflows/agent-review.yml (revision 2026-06-30)
- `sources/mattpocock/course-video-manager/.github-workflows-agent-review.yml-ddaff44e.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.github/workflows/agent-review.yml (revision 2026-07-02)
- `sources/mattpocock/course-video-manager/.sandcastle-review-prompt.md-c5851432.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/review/prompt.md (revision 2026-06-30)
- `sources/mattpocock/course-video-manager/.sandcastle-review-prompt.md-c5851432.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/review/prompt.md (revision 2026-07-02)
- `sources/mattpocock/course-video-manager/.sandcastle-review-prompt.md-c5851432.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/review/prompt.md (revision 2026-07-07)
- `sources/mattpocock/course-video-manager/.sandcastle-implement-pr-prompt.md-7ec7a8d7.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/implement-pr/prompt.md (revision 2026-07-08)
- `sources/mattpocock/course-video-manager/.sandcastle-to-issues-prd-to-issues-prd.ts-d8d5feb8.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/to-issues-prd/to-issues-prd.ts (revision 2026-07-25)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067721938894500036-65f0fb11.md` — origin: https://x.com/mattpocockuk/status/2067721938894500036
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067919429216645366-e4027437.md` — origin: https://x.com/mattpocockuk/status/2067919429216645366
