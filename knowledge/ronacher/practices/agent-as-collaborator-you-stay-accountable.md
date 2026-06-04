# The agent is a collaborator; you stay accountable

Ronacher's through-line across years of agentic coding: an LLM is a curious
collaborator or "a pretty good intern" that gets better month by month — not an
oracle and not a thing to blame. You delegate aggressively, but the final
outcome is *your fault and your fault alone*. "I won't blame the AI and I need
to spot check."

This is not the timid "you can't trust LLMs, check everything" position. It's
the same posture you'd take in a technical discussion with a smart peer: people
are routinely wrong for a few minutes until someone catches it, so you
cross-check *selectively*, not exhaustively. Hallucination is only a problem if
you stop using your own brain.

In practice this means the responsibility line never moves even when the volume
of generated code explodes. On a >90%-AI-written production service, Ronacher
still treats *every line as his own*: reviews it, shapes the architecture, owns
how it runs in production. The 10% he won't cede is exactly where his judgement
is load-bearing — system architecture, schema, database interaction, strong
invariants. He uses the AI as a *rubber duck* during design even when he doesn't
trust or need the answer, because the back-and-forth surfaces his own mistakes.

The corollary is that the tool does not absolve you of being a good engineer.
Agents operate on "conventional wisdom from the internet": they reach for
dependencies (often outdated), swallow errors, hide tracebacks, build
abstractions wildly inappropriate to the problem's scale, and recreate things
that already exist. Left unchecked you get opaque, unobservable systems. You
have to *fight* this with the same judgement you'd apply to your own code — see
[[shape-the-codebase-for-local-reasoning]] for the structural half and
[[you-are-the-bottleneck]] for where accountability ultimately binds.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-1-30-how-i-ai-1b7a9db7.md — https://lucumr.pocoo.org/2025/1/30/how-i-ai/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-9-29-90-percent-fa7af1a5.md — https://lucumr.pocoo.org/2025/9/29/90-percent/
