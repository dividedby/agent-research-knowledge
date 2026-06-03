# Match Spec Rigor To Uncertainty

Match spec-rigor to uncertainty rather than always speccing hard. The cost of writing a detailed spec is only worth paying when a wrong direction is expensive; otherwise it's overhead that slows discovery.

For UI and exploratory work, deliberately UNDER-specify the first prompt, watch the browser update live, and "morph the chaos into the shape that feels right." Never reset — just iterate. The model often builds interactions you hadn't imagined, and the live feedback loop turns spec-writing into exploration. You discover what you want by reacting to what you see, which no amount of up-front writing could have surfaced. This is [[just-talk-to-it-minimal-prompting]] applied where iteration is cheap.

Reserve heavyweight spec-driven development — the [[adversarial-and-cross-model-spec-refinement]] machinery of master contexts, naive critics, and cross-model review — only for genuinely tricky, high-uncertainty, high-blast-radius features where a wrong turn costs real time and effort to unwind.

Steinberger explicitly abandoned the earlier "design a big spec, let it run for hours" default as the *old* way of thinking for exploratory work. He doesn't treat it as wrong everywhere — he treats it as miscalibrated. The discipline is calibration, not dogma: iterate visually when iteration is cheap, spec hard only when the cost of being wrong is high. Knowing which regime you're in is the actual skill; reaching for the wrong one wastes time at both ends.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-understanding-codebases-with-ai-1e970dd7.md — https://steipete.me/posts/2025/understanding-codebases-with-ai-gemini-workflow/
