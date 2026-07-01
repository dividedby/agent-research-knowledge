# A generator agent should check the backlog before adding to it

An agent that *proposes new work* — rather than executing work handed to it —
needs its own brake, because nothing else in a label-driven pipeline stops it
from outrunning the humans who triage its output. `course-video-manager`'s
`architecture-review.yml` runs on a weekday cron and used to go straight from
"scan the codebase" to "open a PRD issue." A later revision inserts a
`check-backlog` job ahead of it: count open issues labeled
`source:architecture-review` (capped at a 10-item query — the workflow only
needs to know *whether* the backlog is at or above the threshold, not the exact
count past it) and skip the whole run, via a job-level `if:`, when 10 or more
are already open.

## Why this differs from the reactive pipeline's guards

The refusal guards in [[label-driven-agent-ci-pipeline]] (defer to the PRD
workflow, refuse a sub-issue, refuse a duplicate PR) all fire *reactively* —
they inspect the one issue or PR in front of them and decide whether *this*
request is well-formed. The backlog check is different: it's a **generator**
gating itself against the aggregate state of everything it has produced so
far, not the shape of the current input. A cron-triggered proposer has no
external caller to reject; if it doesn't measure its own output pile, the only
limit is how fast a human can triage, and a daily cadence with no cap
silently produces more PRDs than anyone reads. Wiring the cap as a separate
`check-backlog` job (rather than a step inside the review job) means the count
runs cheap and read-only, and the outcome is legible in the job graph — a
skipped run shows up as "backlog full," not as a review job that silently did
nothing.

## The general shape

Any autonomous agent whose job is to *create* backlog items — issues, PRDs,
review comments, follow-up tasks — benefits from the same two-part check: (1)
query the current count of its own output still awaiting action, gated by
label or another provenance marker so it counts only its own kind of item, and
(2) refuse to add more once a threshold is crossed, on the theory that a
growing unread backlog is worse than a missed day's proposal. The threshold is
a return-on-attention judgment, not a hard constraint — the point transfers
regardless of the number chosen.

## Sources

- `sources/mattpocock/course-video-manager/.github-workflows-architecture-review.yml-9f64ad36.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.github/workflows/architecture-review.yml (revision 2026-06-30)
