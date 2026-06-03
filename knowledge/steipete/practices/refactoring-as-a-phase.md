# Refactoring As A Phase

Treat fast feature-building and codebase cleanup as alternating PHASES, not a per-commit obligation. Trying to keep every commit pristine fights the grain of how agents work; batching the cleanup into its own mode is both more productive and more fun.

Steinberger spends roughly 20% of his time on agent-run refactoring, batched into dedicated "refactor days." These need less focus than feature work, which makes them ideal for when you're tired — low-stakes, tool-guided, easy to supervise. The tooling does the finding: jscpd for duplication, knip for dead code, eslint plugins, splitting overgrown files, consolidating API routes, rewriting slow tests, modernizing stale patterns. The agent executes against what the tools surface, so the work is mechanical rather than inventive.

The rationale is a property of agents themselves: they "make a mess but are equally great at cleaning up." Speed of feature iteration and tidiness of the result are in tension, but the same capability that produces sprawl also clears it — provided you schedule the clearing. If you don't deliberately set aside the pay-down mode, technical debt compounds silently, because the iterate-fast mode never volunteers to slow down and clean.

Separating the two modes is the whole point. Iterate-fast mode optimizes for getting the shape right; pay-down mode optimizes for the codebase staying tractable for the next round. Mixing them dilutes both. This is the maintenance counterpart to [[engineer-the-codebase-for-agents]]: one keeps the codebase legible going forward, the other periodically restores legibility after a burst of speed.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
