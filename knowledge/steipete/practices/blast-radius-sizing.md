# Blast Radius Sizing

Size every task by its *blast radius* — how many files it touches and roughly
how long it will take — before you hand it off. Blast radius is the core
estimation primitive that makes solo multi-agent work tractable: it tells you
how to scope, how to commit, and how many agents you can safely run at once.

## Keep changes small so resets stay cheap

The discipline is to keep each change small enough that commits stay atomic and a
revert is painless. One large change (a "Fat Man") alongside a handful of small
ones is fine — but multiple large changes landing at once make isolated commits
impossible and recovery a nightmare. Small blast radius is what makes
[[reroll-and-revert-over-repair]] a viable everyday move rather than a costly
rollback.

## Blast radius governs parallelism

The safe number of concurrent agents scales inversely with how much each one can
break. High-impact feature work — large blast radius — gets 1–2 agents and close
attention. Low-blast-radius work like cleanup, test-writing, and UI tweaks can
run ~4 agents at once because no single one can do much damage. This is the
arithmetic behind the [[parallel-agent-fleet-on-main]].

## It is also your steering yardstick

Once you've estimated a task's blast radius, you have a prediction to measure
against. When an agent runs noticeably longer than the radius implied, that
mismatch is the cue to interrupt and check in — the trigger condition for
[[stay-in-the-loop-active-steering]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
