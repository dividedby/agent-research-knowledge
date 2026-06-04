# Practices — ronacher

How Armin Ronacher (creator of Flask/Jinja/Sentry; firsthand agentic-coding
practitioner) approaches working with coding agents day to day: his opinionated
end-to-end workflow advice, the way he shapes a codebase and its tooling to be
agent-legible (language choice, fast observable tools, parallel isolated runs),
and his hype-free read on what current agents can and can't be trusted to do.
One concept per file; this index lists them, one line each.

- [agent-as-collaborator-you-stay-accountable](./agent-as-collaborator-you-stay-accountable.md) — the AI is a curious intern you delegate to but never blame; you own every line.
- [pick-an-agent-legible-language](./pick-an-agent-legible-language.md) — language choice is an agentic decision; Go wins on weights, tooling, and low churn.
- [fast-observable-tools](./fast-observable-tools.md) — tools must be fast, user-friendly, chaos-monkey-proof, and log to a file the agent can read.
- [yolo-mode-delegate-and-wait](./yolo-mode-delegate-and-wait.md) — full permissions, hand off the whole job, watch and wait; the IDE shrinks.
- [code-over-inference-for-repeatable-work](./code-over-inference-for-repeatable-work.md) — for anything that recurs, have the agent write code you can review the approach of, not loop on inference.
- [cli-over-mcp](./cli-over-mcp.md) — `gh` beats the GitHub MCP; MCP relies on inference per step and can't compose.
- [own-your-tools-as-skills](./own-your-tools-as-skills.md) — have the agent write and maintain its own tools as skills so they stay under your control.
- [plan-via-a-file-on-disk](./plan-via-a-file-on-disk.md) — plan by iterating on a markdown file you control; plan mode is just a prompt plus UX.
- [shape-the-codebase-for-local-reasoning](./shape-the-codebase-for-local-reasoning.md) — simple code, plain SQL, local checks, greppability; refactor and parallelize at the right moment.
- [slop-loops-and-agent-psychosis](./slop-loops-and-agent-psychosis.md) — the dopamine loop produces slop and dependence the moment you turn off your brain.
- [you-are-the-bottleneck](./you-are-the-bottleneck.md) — review and accountability are the irreducible bottleneck; you were the bottleneck all along.
