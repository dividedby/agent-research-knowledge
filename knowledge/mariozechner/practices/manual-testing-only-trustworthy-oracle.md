# Manual Testing Only Trustworthy Oracle

Once an agent-built codebase has decayed, its agent-written tests are no more trustworthy than the code they cover. Unit tests, snapshot tests, and e2e suites authored by the same agent encode the same local misunderstandings — they assert that the broken behavior is the intended behavior. A green suite under these conditions proves only internal consistency, not correctness.

So the only reliable measure of "does this actually work" is a human manually testing the product: clicking through it, exercising the real paths, comparing against what it's supposed to do rather than what the agent assumed it should do. Don't treat a passing agent-authored test suite as proof of correctness; keep manual verification as the final quality gate that no amount of automated green can substitute for.

This follows directly from [[agents-are-merchants-of-complexity]]: tests inherit the same blind spots as the code that generated them, because the agent's model of the problem is shared across both. It also reinforces why you must [[stay-in-the-loop-not-agent-armies|stay in the loop]] — the further you remove yourself, the longer the rotten tests stay green while the product quietly stops working, and the later you discover it. Manual testing is the oracle that doesn't lie because it sits outside the agent's mental model entirely.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-03-25-thoughts-on-slowing-t-e9b43800.md — https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down
