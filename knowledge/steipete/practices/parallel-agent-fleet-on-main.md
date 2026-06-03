# Parallel Agent Fleet On Main

He runs 3–8 agents concurrently in a terminal grid, and — counterintuitively —
mostly in the *same folder on main*. He has repeatedly tried worktrees and
branches and reverted each time: they slow him down and cause more merge
conflicts than they prevent.

## Isolation by work selection, not filesystem

Separation comes from *picking non-overlapping areas* so changes don't
cross-pollinate, and from disciplined git ops — a tuned agent file ensures each
agent commits only the files it actually edited. That, plus
[[blast-radius-sizing]], replaces the safety filesystem isolation was supposed to
provide, without the merge tax. It pairs naturally with
[[work-on-main-no-ceremony]].

## Prompt-and-move-on

The loop is: kick one agent off, and while it churns for 5–15 minutes, prompt the
next on a different concern. The human is the bottleneck, so keeping every agent
saturated is what converts your attention into shipped code. Lightweight
message-queuing — a bare "continue," or several tasks queued ahead — keeps a long
run alive without stopping to craft a perfect prompt.

## The cost is cognitive

Holding 3–8 distinct models in your head at once demands deep, sustained focus;
this is the real ceiling, not the tooling. Spreading the fleet across machines
(laptop plus a remote Mac) buys more concurrency and keeps work running even when
you close the lid. Steering all of them still depends on
[[stay-in-the-loop-active-steering]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-shipping-at-inference-speed-f7e15b10.md — https://steipete.me/posts/2025/shipping-at-inference-speed/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-when-ai-meets-madness-peters-16-c80afbe0.md — https://steipete.me/posts/2025/when-ai-meets-madness-peters-16-hour-days/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-commanding-your-claude-code-arm-288d80f0.md — https://steipete.me/posts/2025/commanding-your-claude-code-army/
