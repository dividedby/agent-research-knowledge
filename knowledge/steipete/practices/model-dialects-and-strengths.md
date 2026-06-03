# Model Dialects And Strengths

Different models need different prompting dialects, and a single portable shared prompt is a fiction. Claude responds well to 🚨 SCREAMING ALL-CAPS threats that actively freak out GPT-5/codex — for those you "just use words like a human." A prompt tuned for one model is mistuned for another, so the same instruction file cannot serve both.

Match model to task, and trust practice over leaderboards: close benchmarks hide what actually matters in use. Codex was post-trained to silently read a lot of code before it writes — slower, but reliable on big refactors, where you don't end up having to "fix the fix." Eager models are excellent for small, well-scoped edits but skim on large tasks and wander off on "vision quests." Reserve an expensive deep-reasoning model for the gnarly bugs that justify the cost. The way to learn these dialects is to try both models on the same task and watch how each behaves.

Otherwise keep configuration simple. Rather than per-task fiddling with effort knobs, pick one high-effort setting and leave it — KISS over micro-optimization. And read each vendor's own prompting guide, then tune to the model you actually use day to day rather than to a generic average.

This is where [[just-talk-to-it-minimal-prompting]] gets its one real exception: prompting is minimal and intuition-driven, but the intuition is model-specific, and the dialect you ramble in changes with the model behind the terminal.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-shipping-at-inference-speed-f7e15b10.md — https://steipete.me/posts/2025/shipping-at-inference-speed/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-the-future-of-vibe-coding-499411eb.md — https://steipete.me/posts/2025/the-future-of-vibe-coding/
