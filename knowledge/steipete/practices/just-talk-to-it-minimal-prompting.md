# Just Talk To It Minimal Prompting

With a capable model working on a codebase it reads thoroughly, elaborate prompting is a harness charade. Prompts shrink to one or two sentences — often plus a screenshot — because the model reads enough surrounding files to just "get you." The work that prompt-engineering frameworks pretend to do, the model now does itself by looking.

Counterintuitively, rambling beats structure. Explaining the same thing redundantly from several angles gives the model more surface to latch onto than a tidy, templated prompt. The "10 amazing prompting tricks" genre is bullshit; there is no portable trick. The real skill is intuition built by sheer volume of practice — a felt sense of the minimum context a task needs and an early warning when a model starts drifting. That is why Steinberger distrusts spec-driven development, RAG, plugins, and subagents: each is ceremony substituting for the intuition you should be building instead.

The corollary is maintenance by deletion. As models improve, strip the scaffolding — he removed his Tailwind-4 guidance once models had internalized it. Lightweight phrases do the work formal modes used to: "let's discuss" or "give me options" elicits plan-mode behavior without invoking a plan mode.

This pairs with dictation ([[voice-as-primary-input]]) and high-bandwidth images ([[images-as-high-bandwidth-context]]) — both lower the cost of getting half-formed intent into the loop — and it is the human-side mirror of [[less-is-more-tooling]]: thin the prompt for the same reason you thin the tools.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-one-more-prompt-b53d4449.md — https://steipete.me/posts/just-one-more-prompt/
