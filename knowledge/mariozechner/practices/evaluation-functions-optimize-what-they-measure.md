# Evaluation Functions Optimize What They Measure

Agent self-optimization and auto-research only work because you hand the agent an evaluation function — startup time, training loss, throughput — that it can measure itself against. The closed loop is what makes the agent useful: it can iterate, score its own attempts, and converge. But that function captures exactly *one* narrow metric, and the agent optimizes that metric and nothing else.

So the agent will happily ignore everything not in the eval. Code quality, complexity, maintainability — invisible. Even correctness, if your eval is foobar, gets sacrificed to whatever the number rewards. The optimizer is faithful, which is precisely the danger: it serves the metric you wrote, not the system you wanted.

The practical reading: agent-optimized output is a great source of *ideas* while being categorically not production-ready. It surfaces a faster approach, a leaner data path, an unobvious trick — genuine signal. But it is not a deliverable. Extract the good idea, then implement it properly, under judgment the eval function could never encode.

Treat the eval function's blind spots as the human's responsibility. The same measurable target that makes the agent useful is what bounds how far you can trust its output — usefulness and untrustworthiness come from the same source. This generalizes the closed-loop principle behind any good agent task: a measurable target is the enabling condition *and* the limit. Define the eval knowing the agent will pursue it literally, and own everything outside it yourself — quality, taste, and the call on whether the output is fit to ship.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-03-25-thoughts-on-slowing-t-e9b43800.md — https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down
