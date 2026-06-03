# Stay In The Loop Active Steering

The highest-leverage skill in agentic coding is not prompt-crafting — it's
*active steering*. Watch the agent work live, and the moment it runs longer than
your [[blast-radius-sizing]] estimate predicted, hit escape, ask "what's the
status," and either redirect or abort. Drift is the enemy, and you can only
correct drift you can see.

## Interruption is a tool, not a setback

Stopping an agent mid-task is cheap: file changes are atomic and modern models
resume well from a clean checkpoint. So interruption costs almost nothing and
saves you from letting a confused run dig a deeper hole. The yardstick is your
own estimate — when wall-clock time overshoots predicted blast radius, that's
your signal to step in rather than hope it recovers on its own.

## Visibility is the whole point

This is precisely why he rejects background, web-based, and async agents for
primary work. Anything that hides the live terminal — wrappers, framework
subagents, detached background runs — trades away the very control that produces
good output. The unedited stream of what the agent is doing IS the interface;
obscuring it is a downgrade dressed as convenience.

## Remove friction so steering stays fluid

Pre-authorizing the agent (skip-permissions mode), backed by frequent commits
and snapshots, strips out approval prompts so your attention stays on the work,
not on clicking dialogs. The safety net is git, not the prompt gate. Fluid
steering beats granular gating.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-shipping-at-inference-speed-f7e15b10.md — https://steipete.me/posts/2025/shipping-at-inference-speed/
