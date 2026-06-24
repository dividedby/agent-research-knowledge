# LLMs as system components, not as the system

Brooker's systems-builder reframe: the interesting question is not what an LLM
can do *alone* but what a *system* of LLMs and deterministic tools can do
together. "Systems, fundamentally, are more than the sum of their components."

## The argument

The discourse around the *Illusion of Thinking* paper asked whether an LLM can
scalably play Towers of Hanoi. Brooker's cheeky answer (he had Kiro just *build*
the game) reframes the question: the useful one is **can systems built with LLMs
do it?** — and the answer has been yes for several model generations. As a system
builder he cares about LLMs + code interpreters, + databases, + browsers, + SMT
solvers. Such systems can do things LLMs alone can't *and never will*, and can do
shared tasks orders of magnitude cheaper and faster. Even the trivial case is
illustrative: an LLM that writes a `count_rs` snippet has built a system that
reliably counts characters — something the bare model fails at, and a model that
could would cost ~six orders of magnitude more per example.

This scales from trivial (`count`, `sum`, `grep`) to powerful (SMT solvers, ILP,
MCMC). The flagship example is **Bedrock Automated Reasoning Checks**: the LLM
extracts *rules* from documents and *facts* from a response — the messy-natural-
language job it's good at — and an SMT solver verifies logical consistency — the
precise-formal-reasoning job *it's* great at. Neither component can do the whole
job; the composed system can.

## The principle and the consequence

> LLMs are more powerful, more dependable, more efficient, and more flexible when
> deployed as a component of a carefully designed system.

The consequence for builders: the fundamentals of systems thinking aren't
obsoleted by LLMs, they're *more relevant than ever* — you've been handed a
powerful new component, not a replacement for design. This is the same vantage as
the feedback-loop hypothesis (the deterministic tools you compose in are exactly
the oracles that make a task "easy") and the box (the deterministic layer is also
where control lives).

## Consistent with the Bitter Lesson

Brooker pre-empts the obvious objection. Composing LLMs with SMT/databases isn't
"building in how we think we think" (Sutton's warning). Giving an agent a code
interpreter or an SMT solver doesn't encode *human* discoveries into the model —
it gives the agent access to **the things computer science has learned about how
the universe works**, as tools of discovery. Sutton isn't claiming that
generating-and-executing code is worse than doing the same task with linear
algebra.

## Sources

- `sources/marcbrooker/blog/http-brooker.co.za-blog-2025-08-12-llms-as-components.html-bc7f0f7c.md` — origin: https://brooker.co.za/blog/2025/08/12/llms-as-components.html
