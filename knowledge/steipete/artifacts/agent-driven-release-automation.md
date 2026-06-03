# Agent-Driven Release Automation

Encode the entire release and distribution pipeline as plain, debuggable shell scripts — chosen over opaque frameworks like Fastlane — so an agent can cut a release from a single English instruction ("make a new release 1.1 beta 1"). The scripts own the cryptic, error-prone steps that otherwise demand human babysitting: version bumping, packaging, signing and notarization, upload, and update-feed generation.

The reason plain scripts win is inspectability. Both the agent and you can read, run, and debug a shell script line by line; framework magic can't be opened up when it breaks mid-release, which is exactly when you need to. A pipeline the agent can *see* is a pipeline the agent can *drive* unattended — and one you can fix without reverse-engineering a black box.

For CLI and MCP tools the same idea becomes a sequential pre-release check script that stops at the first failure: clean git state, security audit, type-check and lint, tests, multi-arch binary validation, and a smoke test, in order. Fail-fast keeps a broken artifact from ever reaching users and gives the agent a precise, actionable stopping point rather than a pile of downstream errors. Rollout itself goes beta-tag-first, so a bad build is caught by a small audience before a general release.

This closes the release loop the way [[close-the-loop-with-purpose-built-tools]] closes the inner loop: the cryptic manual steps that used to require a human become a thing the agent invokes. It pairs with the version-discipline and health-check conventions in [[agent-tool-build-best-practices]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-vibe-meter-monitor-your-ai-cost-e7465ad6.md — https://steipete.me/posts/2025/vibe-meter-monitor-your-ai-costs/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-mcp-best-practices-500319cb.md — https://steipete.me/posts/2025/mcp-best-practices/
