# Agents For Domain Experts On Good Tasks

Agents are really only effective when wielded by a domain expert. The expert often can't judge the generated code line-by-line — but they *can* judge the outputs at each stage and verify correctness against what they know the answer should be. That judgment, not the typing, is the scarce ingredient.

Good agent tasks share concrete properties. They can be scoped so the agent needn't understand the whole system — a bounded surface where local blindness doesn't bite ([[agentic-search-recall-degrades-with-size]]). The loop can be closed, so the agent can evaluate its own work against something measurable ([[evaluation-functions-optimize-what-they-measure]]). And the output isn't mission-critical: an ad hoc tool, internal software, or a rubber duck for querying the compressed wisdom of the internet. An LLM's odds of building what you actually want also hinge on the simplicity of the target, so deliberately constrain the surface — complexity is where agents fail and drag you back in.

For a non-programmer, the unlock is structuring work as a pipeline of small scripts: files in, files out, each stage's output independently inspectable, the whole thing reproducible. You don't need to read the code if you can read every intermediate result and re-run from any point. The expert verifies at the seams ([[manual-testing-only-trustworthy-oracle]]) rather than auditing the implementation.

The bottleneck to spreading this is not tools — it's teaching. Every expert arrives with a different technical baseline, and meeting them there is the hard part. The capability is broadly available; the ability to *use* it well is what has to be taught, one person and one starting point at a time.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-12-22-year-in-review-2025-cbb5c6d1.md — https://mariozechner.at/posts/2025-12-22-year-in-review-2025
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-03-25-thoughts-on-slowing-t-e9b43800.md — https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down
