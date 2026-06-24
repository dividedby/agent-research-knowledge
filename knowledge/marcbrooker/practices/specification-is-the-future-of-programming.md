# Specification is the future of programming

Brooker's thesis that programming is converging on *specification* — crisply
stating what a program should do and what makes it right — with natural language
as the core "programming language," and that this is a continuation of a
four-decade trend, not a break from it. The implementation is *derived* from the
spec; the *how* matters less and less.

## Spec-driven development is not waterfall

The most common misreading he pushes back on: spec-driven development as a
return to up-front, big-design-first waterfall. His correction is a one-word
pivot — it isn't about pulling design **up-front**, it's about pulling design
**up**. The specification becomes an **explicit, versioned, living artifact** the
implementation flows *from*, kept in sync by being *upstream* of implementation
for most changes — not a static document frozen before coding starts. Software
is irreducibly iterative (discovering requirements *is* a goal of the process;
requirements are "complex, dynamically changing, internally conflicting, and
invariably incomplete"), so the spec is the thing you iterate on, with the loop
sped up by AI. He reads the Agile Manifesto not as high-minded ideals but as a
plain reflection that top-down design stopped working as software got complex.

A specification is "an explicit statement of requirements and key design
choices, separated from the low-level implementation" — a raising of abstraction
from code to words (and pictures, snippets, and occasionally mathematics). It can
be free-form or structured (RFC2119, EARS) and descend into exact notation (Lean,
TLA+) only where precision is needed.

## The loop is the point, not a failure

The naive view treats natural-language programming as a *one-shot* problem —
turn one ambiguous human sentence into one perfect program — and counts every
return trip around the loop as a failure. Brooker inverts this: **the trips
around the loop are fundamental to success, and always have been.** Programs have
*always* originated in natural-language requirements from people; the way teams
cope with that ambiguity is context plus conversation ("did you mean mean or
median?"). Vibe coding is the purest embodiment — a closed *yes-and / no-but*
loop where context accumulates and "the magic happens." Kiro-style spec-driven
development is the same loop, just more formal; property-based testing adds enough
structure to ratchet it forward. "The loop is the interaction" (echoing
*individuals and interactions over processes and tools*).

## Ambiguity doesn't doom it — and the escape hatches

The standard objection (Dijkstra, Lamport: natural language is ambiguous and
imprecise — Brooker's own *Bug in Paxos Made Simple* is an ambiguity bug) is
*true* but doesn't go far enough to kill the idea, because almost all programs
are *already* specified in natural language. Where exact answers genuinely matter
(safety properties, legal/compliance, security), two moves stay in the toolbox:
(1) **descend into symbolic representation** — Rust, SQL, TLA+ — which is not a
failure but the rare, deliberate "piercing through the layers"; and (2)
**neurosymbolic** approaches that put the human/specifier back in the loop to
review a *restatement* of the spec ("let me say that back to you to check I got
it"), combining the loose natural-language world with precise symbolic reasoning
inside the machine.

## Specifications are context

Once developed, a spec takes on a second life as **context future specifications
refer to**. Established shared meaning ("what we mean by *average*", "what we mean
by *authenticated*") is reused rather than rebuilt from zero each conversation —
"I don't give you directions to the restaurant starting at your birthplace." A
spec is also always-in-sync documentation, lets the same system be implemented in
multiple languages/frameworks, and — most importantly for delivery velocity —
gives an agent a **map** (versus the turn-by-turn directions of vibe-coding
prompts) so it can run autonomously for long stretches without a human in the
tight loop, and write better-tested code because it knows what "good" looks like.
The human keeps the *outer* loop: refining the spec and owning its internal
conflicts and trade-offs, where expertise actually lives.

## Sources

- `sources/marcbrooker/blog/http-brooker.co.za-blog-2025-12-16-natural-language.html-7752ad3e.md` — origin: https://brooker.co.za/blog/2025/12/16/natural-language.html
- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-04-09-waterfall-vs-spec.html-5b072e7b.md` — origin: https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec.html
