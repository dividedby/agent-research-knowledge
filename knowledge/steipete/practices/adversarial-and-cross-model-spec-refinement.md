# Adversarial And Cross-Model Spec Refinement

A solid spec is still the bedrock — AI just makes producing one fast and dialectical. Voice-dump raw ideas into one model to get a structured first-draft spec, then harden it with critics rather than trusting the first pass.

Two complementary moves drive the refinement. First, keep a *master* context that holds the full evolution of the spec, and run a SEPARATE, fresh context whose only job is to attack it: "take this apart — give me 20 points that are underspecified, weird, or inconsistent." Feed those critiques back into the master, never the reverse — the master usually already holds the answers, so the critic must stay naive to keep finding real gaps. Second, route the spec to a DIFFERENT, stronger model (e.g. GPT-5-Pro) for review before any code is written. A second architecture brings genuinely different ideas, and reviewing a plan is far cheaper than reviewing the implementation.

Iterate three to five rounds until the critiques turn niche. Watch for context amnesia: output-limit truncation silently drops earlier requirements, so generate in logical blocks and manually concatenate them into a master doc with a requirements checklist you can re-verify.

Only then hand "build spec.md" to a coding agent. Tokens spent on planning up front buy code that needs far less correction downstream — a different posture from [[just-talk-to-it-minimal-prompting]], and reserved for high-uncertainty work per [[match-spec-rigor-to-uncertainty]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-understanding-codebases-with-ai-1e970dd7.md — https://steipete.me/posts/2025/understanding-codebases-with-ai-gemini-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-the-future-of-vibe-coding-499411eb.md — https://steipete.me/posts/2025/the-future-of-vibe-coding/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
