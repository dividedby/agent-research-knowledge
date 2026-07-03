# Practices — collina

Matteo Collina (Fastify co-creator, Node.js TSC member) is a working
open-source maintainer applying agents at real maintainer scale, not a harness
builder or essayist working solo. His newsletter documents concrete
division-of-labor on Node.js core work (the node:vfs PR, built largely with
Claude Code) plus the governance friction that followed — a DCO/AI-provenance
controversy in the Node.js project — and frames the maintainer's job as
judgment and review, non-outsourceable to the agent. The additive vantage: a
maintainer-at-scale voice on real core-project PRs and governance friction, not
a harness builder or solo essayist. Corpus-anchored via the accepted proposal
(#466).

Material skews here (practices — division-of-labor on real PRs, maintainer
judgment/accountability framing, governance friction); `artifacts/` stays
sparse until the deferred `mcollina/skills` Source (his own skills-repo
convention) lands as a separate proposal. One concept per file; this index
lists them, one line each.

- [judgment-is-the-scarce-resource](./judgment-is-the-scarce-resource.md) — AI collapses the cost of implementation; judging/reviewing its output, not producing it, is what's now scarce and valuable.
- [build-judgment-by-coding-first](./build-judgment-by-coding-first.md) — you can only develop the judgment to review AI code by first writing code and living through its failures yourself.
- [small-modules-reduce-agent-context](./small-modules-reduce-agent-context.md) — small, narrowly-scoped module APIs cut how much context an agent needs to hold to reason correctly.
- [guardrails-over-gates-for-ai-shipped-code](./guardrails-over-gates-for-ai-shipped-code.md) — once AI outpaces manual review capacity, correctness has to be enforced by platform defaults, not review gates.
- [human-accountability-for-ai-generated-code](./human-accountability-for-ai-generated-code.md) — DCO-style provenance rules don't need to change for AI code; they were always about who answers for it, not how it was written.
- [review-before-commit-not-after-push](./review-before-commit-not-after-push.md) — move the review checkpoint earlier, to before commit, because by PR time the agent's approach is already locked in.
- [personal-skills-encode-preferences-to-cut-ai-slop](./personal-skills-encode-preferences-to-cut-ai-slop.md) — a repeated correction is a signal to write the preference once into a loadable skill instead of re-arguing it every session.
