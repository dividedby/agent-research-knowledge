# Practices — marcbrooker

How Marc Brooker works with coding agents — firsthand field notes from an AWS
principal engineer and distributed-systems researcher applying an
agent-methodology lens to systems software. The named postures: the
*agentic-software-development hypothesis* (three forms of agentic development
and when each applies), *spec-driven-development-as-living-document* (living
spec over waterfall-spec), and *feedback-loop hypothesis* (the degree to which
fast feedback loops predict agentic productivity). Material may also land in
`artifacts/` if the blog documents harness or tooling internals directly — let
the concept decide. One concept per file; this index lists them, one line each.

**Scope reminder:** the feed is a full 161-post archive spanning 2012 → present,
so most captures are out-of-scope distributed-systems content (queuing theory,
consistency, SSD benchmarks, SFQ fairness) — see `docs/subjects.md`. Synthesize
only the coding-agent / agent-methodology posts; ignore the rest as inert,
captured-but-unsynthesized noise.

- [agentic-software-development-hypothesis](./agentic-software-development-hypothesis.md) — tasks with a non-adversarial oracle (i.e. effective feedback) become trivial; the feedback-loop corollary says systems software is "easy" and SaaS is "hard".
- [specification-is-the-future-of-programming](./specification-is-the-future-of-programming.md) — spec-driven development is pulling design *up* not *up-front*; the spec is a living artifact and the iteration loop is the point, not a failure.
- [llms-as-system-components](./llms-as-system-components.md) — the useful question is what systems of LLMs + deterministic tools can do, not what an LLM does alone; systems are more than the sum of their parts.
- [control-agents-with-a-deterministic-box](./control-agents-with-a-deterministic-box.md) — control what an agent *does* with a strong deterministic layer *outside* it; the real danger is the persistent Sorcerer's-Apprentice, not the adversary.
- [defect-rate-over-capability](./defect-rate-over-capability.md) — the opportunity is gated by the left tail (defect rate), not the right tail (peak capability); pass@k is exponentially-forgiving and mostly bunk.
- [your-heuristics-are-wrong-update-your-constants](./your-heuristics-are-wrong-update-your-constants.md) — an extinction event for rules of thumb; seniors and juniors alike must get hands-on, build, and recalibrate against reality.
- [ai-for-code-not-for-prose](./ai-for-code-not-for-prose.md) — comfortable with AI-generated opaque code, but publishing AI prose under your name breaks the reader's social contract.
