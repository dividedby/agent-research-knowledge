# Feed Agents Current Docs As Markdown

Agents produce wrong or outdated code when they can't see current docs — they hallucinate constraints or emit years-old API patterns lifted from stale training data. Don't ask the agent to reason from memory when you can hand it ground truth.

The fix is mechanical: convert authoritative docs into clean Markdown and drop them straight into context. This includes JavaScript-rendered pages the agent can't fetch on its own — pre-render and convert them. Markdown runs roughly 70% smaller than the equivalent HTML, so the conversion also conserves tokens for actual code. Always prefer current first-party docs over cached or example sources.

Make it reusable. Keep a library of pre-converted Markdown — an "agent-rules" repo of modern-idiom guides you reapply across projects. A single modern-Swift guide, dropped into context, drove a whole-codebase refactor toward current idioms; that artifact is reusable organizational memory (see [[agent-file-as-organizational-scar-tissue]]).

For whole-codebase comprehension, flatten the repo to Markdown — source plus docs, but skip tests and *especially* images, which bloat as base64 — and interrogate the result in a massive-context model: "what's notable, which edge cases did I miss?" When a job genuinely needs the whole codebase in view, work around per-file read limits explicitly by concatenating into one large Markdown file rather than trusting the agent to assemble the picture from scattered reads. Hand it the complete artifact; don't make it stitch.

The principle generalizes: agents are only as current and as complete as the context you engineer for them. Convert, cache, reapply.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-llm-codes-transform-developer-d-573d6d00.md — https://steipete.me/posts/2025/llm-codes-transform-developer-docs/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-vibe-meter-2-claude-code-usage--c1968274.md — https://steipete.me/posts/2025/vibe-meter-2-claude-code-usage-calculation/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-understanding-codebases-with-ai-1e970dd7.md — https://steipete.me/posts/2025/understanding-codebases-with-ai-gemini-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-migrating-700-tests-to-swift-te-ddcf01e3.md — https://steipete.me/posts/2025/migrating-700-tests-to-swift-testing/
