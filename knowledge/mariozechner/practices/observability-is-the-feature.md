# Observability Is The Feature

Zechner's throughline across his harness design is that you should be able to inspect every aspect of the agent's work and intervene mid-stream — observability IS the feature, not a nice-to-have bolted on top. It's the lens through which he rejects opaque mechanisms: hidden context injection, framework-managed sub-agents, plan-mode sub-agents, and black-box background processes all fail the same test because you can't see or steer what they do.

Concretely, the preference shows up as choices that keep the work in plain view. File-based plans you can co-edit rather than a hidden planning step. tmux sessions you can attach to and co-debug rather than a detached process. A code-review sub-agent whose full output you can save and reopen rather than a summarized verdict. A browser agent whose every DOM read leaves a traceable trail rather than a screenshot-and-guess loop.

The reasoning is grounded in current model reality: models still miss context and produce work that needs rework. Given that, the worst thing you can do is optimize for autonomy you can't audit — you trade the ability to catch a failure early for the illusion of hands-off speed. Keeping the agent steerable and watchable means you intercept mistakes while they're cheap.

This is also his critique of "mature" mainstream harnesses: they erode observability by injecting context behind your back and silently changing system prompts and tools each release, so you can no longer reason about why the agent did what it did. The principle pairs tightly with [[minimal-harness-by-subtraction]] (fewer hidden parts to watch) and explains why he stays [[stay-in-the-loop-not-agent-armies|in the loop]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-10-05-jailjs-f2aeaf25.md — https://mariozechner.at/posts/2025-10-05-jailjs
