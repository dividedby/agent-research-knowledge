# Practices — amp

How the engineers who ship **Amp** (Sourcegraph's commercial, team-built coding
agent) teach *working with* an agent, distilled from the Chronicle's
practitioner notes against real production usage: specifying rather than asking,
engineering verification into the prompt ("trust isn't a feeling, it's a passing
test suite"), designing work to be feedback-loopable, and avoiding the speed trap
when output outpaces review. One concept per file; this index lists them, one
line each.

Scope: synthesize the Chronicle's practitioner-guide notes only; the `/news/*`
product-changelog/marketing stream is out of scope.

- [short-threads-one-task-each](./short-threads-one-task-each.md) — keep threads small and single-purpose; a feature is a cluster of short threads, not one mega-thread.
- [specify-dont-ask](./specify-dont-ask.md) — under-specification is the failure mode; lead the agent like a fast capable peer, and beware the speed trap.
- [trust-is-a-passing-test-suite](./trust-is-a-passing-test-suite.md) — engineer a definition-of-done and verification loop into the prompt; trust is a passing test suite, not a feeling.
- [version-control-as-the-safety-net](./version-control-as-the-safety-net.md) — git/staging is the safety net, not edit-by-edit approval gates that trap the agentic loop.
- [git-history-as-context-source](./git-history-as-context-source.md) — point the agent at commits and `git diff` to mine context, review, and locate code.
- [ship-constantly-own-what-you-merge](./ship-constantly-own-what-you-merge.md) — Amp's team principles: optimize for speed, ship weekly, you-merge-it-you-own-it.
