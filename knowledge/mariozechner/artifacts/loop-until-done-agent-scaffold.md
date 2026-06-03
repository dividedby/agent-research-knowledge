# Loop Until Done Agent Scaffold

The agent loop should be the simplest thing that works: process the user message, run any tool calls, feed the results back, and repeat — **until the model emits a turn with no tool calls, then stop**. There is no `max-steps` or similar knob, because Zechner never found a use for one; the loop just runs until the agent is done. Knobs you can't justify with a real use case are just surface area ([[minimal-harness-by-subtraction]]).

The loop emits **events for everything**, which is what enables reactive UIs to render progress as it happens. It also supports **message queuing** via a post-turn callback that injects queued user messages before the next assistant turn — so a human can pipe in a correction without racing the model.

A thin `Agent` class layers the genuinely useful concerns on top of this minimal loop: state management, simplified subscriptions, two queuing modes (one-at-a-time / all-at-once), attachment handling, and a transport abstraction for running directly or via a proxy. The discipline is to keep the *core loop* trivial and push every optional concern into this outer layer, so the part that must be correct stays small enough to reason about. Event emission also makes the loop observable by construction ([[observability-is-the-feature]]).

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
