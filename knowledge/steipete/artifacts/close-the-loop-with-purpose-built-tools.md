# Close The Loop With Purpose-Built Tools

Any manual step that forces you to babysit the agent's inner loop is a candidate to become a tool the agent calls itself. The goal is "closing the loop": if an agent can answer its own question or recover from its own failure, you never have to intervene.

The archetype is an "oracle" CLI that wraps escalation to a stronger model — file upload plus prompt plus session — so a stuck agent consults the smarter model automatically instead of you copy-pasting transcripts. The same instinct produces a screenshot-and-vision tool so a stuck agent can *observe* a broken build or UI and keep fixing; a way to run dev servers detached so they don't block the loop; and auto-clicking "Continue" so unattended runs don't stall on a prompt.

Building infrastructure *for* the agents — admin pages, small CLIs, curl-able endpoints, env-loading snippets — is a uniquely AI-era investment. The agent makes building these helpers cheap, and each helper compounds the agent's own throughput, so the return is high and self-reinforcing. Accept the recursive "tools to build tools" rabbit hole as part of the work rather than a distraction from it.

Each helper should be a small CLI the agent invokes directly — see [[cli-over-mcp]] — and built to the standards in [[agent-tool-build-best-practices]]. The vision and detached-server cases are concrete instances; the watcher in [[invisible-build-watcher]] closes the rebuild loop the same way.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-shipping-at-inference-speed-f7e15b10.md — https://steipete.me/posts/2025/shipping-at-inference-speed/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-the-future-of-vibe-coding-499411eb.md — https://steipete.me/posts/2025/the-future-of-vibe-coding/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
