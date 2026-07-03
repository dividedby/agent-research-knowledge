# Judgment is the scarce resource

When AI collapses the cost of writing code, the scarce and valuable skill
becomes judging whether that code is correct — not producing it. As
implementation gets cheap, and keeps getting cheaper (model competition never
lets up: every time a competitor ships a better model, it resets the value of
what a developer already knew how to squeeze out of the old one), the one
thing a faster model can't hand you is the accountability and domain
understanding needed to decide if its output is safe to ship. Someone still
has to answer for what breaks in production.

This is not a temporary bottleneck to be optimized away — it's the point.
Reviewing and assessing code written by someone (or something) else is what
open-source maintainers have always done: as a maintainer of Node.js,
Fastify, Pino, and Undici, Matteo Collina spends most of his time reviewing
pull requests from contributors he's never met, deciding if the work is good
enough. AI is "just another contributor" in that sense — one that types
fast — and the review discipline doesn't change because the author is a
model instead of a human. His own workflow: throw the incoming issue at AI
first (security fixes, bugs, new features), but review every line, every
behavior change, before it ships. The moment you stop reviewing is the moment
you stop being responsible for what you ship.

The same shift shows up in how the work gets paid for. As implementation
hours stop being the expensive part, consulting value shifts from selling
hours of typing to selling judgment directly — a fractional senior architect
reviewing a team's AI-assisted output a couple of days a week replaces the
traditional body-shop model of many junior-rate hours, because judgment, not
implementation speed, is what the client is actually buying now.

## Sources

- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-the-human-in-the-loop-05a52b07.md` — origin: https://adventures.nodeland.dev/archive/the-human-in-the-loop/
- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-the-economics-of-judgm-d00997e2.md` — origin: https://adventures.nodeland.dev/archive/the-economics-of-judgment/
- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-software-engineering-s-a3f9bb98.md` — origin: https://adventures.nodeland.dev/archive/software-engineering-splits-in-three/
