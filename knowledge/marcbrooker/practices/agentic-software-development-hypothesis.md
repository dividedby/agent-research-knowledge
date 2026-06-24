# The agentic-software-development hypothesis

Brooker's central claim about *where coding agents will and won't win*, stated as
a falsifiable hypothesis and refined through successive objections. It is the
load-bearing idea the rest of his agent writing hangs off.

## The hypothesis, in three forms

- **Weak form:** any coding task for which a *complete specification* is
  available will become trivial.
- **Strong form:** any coding task for which a *deterministic oracle* is
  available will become trivial.
- **Strongest form:** any coding task for which a *non-adversarial ("pythic")
  oracle* exists will become trivial.

The progression answers its own objections. *Few meaningful tasks have a
complete specification* pushes weak → strong (an oracle that can *judge* a result
is cheaper to come by than a spec that *describes* it). *Most oracles aren't
deterministic* pushes strong → strongest (a probabilistic but non-adversarial
checker — one that isn't actively trying to be fooled — is enough).

## The same idea restated as feedback

The hypothesis is equivalent to a control-theory observation: **an agent is a
feedback loop wrapped around an LLM**, and a feedback loop can extract excellent
behaviour from a flawed component (his EE-class example: an op-amp plus a
multiplier turns a voltage into its square root — "multipliers can become square
rooters"). The move from smart-autocomplete IDEs to agents *is* the move of the
feedback from the human (edit → build → test → back to the IDE) into the loop
itself. Most debate about long-term agent capability argues about *open-loop*
model quality; Brooker thinks that's the *less* important half. An oracle is just
the source of the feedback signal; "a task has a non-adversarial oracle" and "a
task has effective feedback available" are the same statement.

## The feedback-loop hypothesis (the practical corollary)

> In the long term, coding agents will find tasks with effective feedback
> 'easy', and tasks without effective feedback 'hard'. The availability of
> accurate feedback will determine the limits on their capabilities.

This is deliberately counter-intuitive about *what* is easy. The common
intuition is that UIs/SaaS are easy and systems software is hard. The feedback-
loop hypothesis says the opposite: a CRUD website's only real oracle is a human
(slow, squishy, inconsistent), whereas a systems component with an API,
liveness, and safety properties has a *machine* oracle — compilers (Rust),
property-based tests, model checkers (TLA+), benchmarks — so iteration needs no
human in the loop. Hence "SaaS is hard, systems software is easy." Observed
already: agents excel at performance work (good benchmarks exist) and Rust (the
compiler is loud, immediate feedback), and struggle at architecture ("I know it
when I see it" feedback) and concurrency ("it silently corrupted data at
runtime" feedback).

## Why it matters

The actionable consequence is not "wait for better models" but **build the
oracle**: the engineering frontier is constructing the feedback loops
(specifications, compile-time tools like Rust/Hydro/Verus, model-checkers, sims,
property tests) that turn a not-yet-trivial task into a trivial one. This is the
bridge from the hypothesis to his advocacy for specification (see
`specification-is-the-future-of-programming.md`).

## Sources

- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-05-20-hypothesis.html-eb755504.md` — origin: https://brooker.co.za/blog/2026/05/20/hypothesis.html
- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-05-18-whats-easy-whats-hard.htm-6446687f.md` — origin: https://brooker.co.za/blog/2026/05/18/whats-easy-whats-hard.html
