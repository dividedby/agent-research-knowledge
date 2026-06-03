# Tests In The Warm Context

Always ask the model to write tests right after a feature or fix, in the SAME context, as an explicit separate step. For anything beyond a pure UI tweak this is non-negotiable.

The value isn't the tests themselves — AI-generated tests are mediocre. The value is that generating them while the implementation is still loaded in context reliably surfaces bugs in the just-written code, and the agent holding all that context is best placed to fix them right then. Context is finite, so spending it on test-writing while the relevant code is still warm beats a fresh-context pass that must re-derive everything from scratch.

Keep "build" and "test" as separate prompts. Bundling them into one makes the agent skimp on both — it races to a single "done" and shortchanges each half. Two prompts force two real efforts.

This is tests-AFTER-the-shape-exists, not TDD. Agents are good at back-filling tests once the structure has settled, and in doing so they catch edge cases — timezones, expired cookies, offline states — that a human wouldn't bother to write by hand. That breadth is a genuine payoff even when the test quality is unremarkable.

Add CI early so coverage isn't trapped on your machine. A green local run proves nothing about the next contributor or the next context. This pairs naturally with [[just-talk-to-it-minimal-prompting]] and [[stay-in-the-loop-active-steering]]: the warm-context test pass is one more checkpoint where you stay close to what the agent just produced.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-poltergeist-ghost-keeps-builds--36395e11.md — https://steipete.me/posts/2025/poltergeist-ghost-keeps-builds-fresh/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-live-coding-session-building-ar-6d007535.md — https://steipete.me/posts/2025/live-coding-session-building-arena/
