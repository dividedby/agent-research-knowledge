# Work On Main No Ceremony

For a solo operator moving fast, team process is pure overhead. Commit straight
to main with small, surgical, atomic commits — and skip the apparatus built for
coordinating humans: PRs, issue trackers, manual checkpointing, worktrees. Git
history plus backups already form the safety net, so the discipline lives in
*commit granularity*, not branch ceremony.

## Granularity over gating

The thing worth being strict about is the size and atomicity of each commit (see
[[blast-radius-sizing]]) — that's what makes a revert cheap. Per-action manual
approvals, by contrast, are worse than useless: they degrade into "Windows Vista
prompts" you click through mindlessly, providing the feeling of control without
the substance. Better to move fast and review diffs after the fact.

## The mountain metaphor

Building software is like walking up a mountain — you circle, double back, and
take wrong turns, but the codebase itself evolves linearly upward. Process
ceremony tries to make every step formally correct; the reality is that
backtracking is the normal texture of the work, and a clean linear history on
main captures the ascent just fine.

## Explicit caveat

This is scoped advice, not a universal law. It holds for solo and tiny-team work
where you *are* the review process; it will not fly on a real team where PRs and
trackers coordinate people who can't see each other's terminals. Within that
scope it pairs directly with the [[parallel-agent-fleet-on-main]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-shipping-at-inference-speed-f7e15b10.md — https://steipete.me/posts/2025/shipping-at-inference-speed/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-when-ai-meets-madness-peters-16-c80afbe0.md — https://steipete.me/posts/2025/when-ai-meets-madness-peters-16-hour-days/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-live-coding-session-building-ar-6d007535.md — https://steipete.me/posts/2025/live-coding-session-building-arena/
