# Images As High Bandwidth Context

A screenshot is the cheapest, densest way to give a multimodal agent context. Drag it into the terminal in two seconds and the model locates the exact place in the code by matching visible strings on screen to source. At least half of Steinberger's prompts contain a screenshot — it is a default input, not a special case.

The bandwidth is the point. Paste in a crash log, a broken UI, or a network-inspector panel and the model often "sees" the problem immediately. "Fix padding" plus a clipped image does work that paragraphs of careful prose cannot, because the image carries spatial and rendered detail that English would only approximate. Annotation — circling the offending element — works even better, but it is slower, so he usually skips it and lets the raw image plus a short instruction carry the load.

Images also close the loop in the other direction. Give the agent a screenshot tool and it can self-correct: it captures the running UI and checks "is this button enabled?" before reporting done, instead of asserting blind. That feedback keeps the loop honest and supports staying in it ([[stay-in-the-loop-active-steering]]).

Pair this with short, single-purpose prompts ([[just-talk-to-it-minimal-prompting]]): the image supplies the context so the words don't have to, which is exactly why minimal prompting works at all.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-the-future-of-vibe-coding-499411eb.md — https://steipete.me/posts/2025/the-future-of-vibe-coding/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-shipping-at-inference-speed-f7e15b10.md — https://steipete.me/posts/2025/shipping-at-inference-speed/
