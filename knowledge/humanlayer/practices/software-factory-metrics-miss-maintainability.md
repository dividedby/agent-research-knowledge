# Software-factory metrics miss the point: maintainability, not throughput

Judging an agent-driven engineering effort by one-shot test pass rate, token spend, or
completed-task count measures activity, not the thing that actually matters: whether
the codebase stays easy to change. HumanLayer names this as the core failure mode once
you scale past a single harness to a "software factory" — many agents, many teams, a
real codebase that has to keep evolving. A factory can look productive on all three
counters and still be quietly burying the codebase in complexity that only shows up as
lost velocity later.

The building blocks they point to instead sit above the single-harness level:
composable compute, development environments, harnesses, sessions, plans, artifacts,
review, and human control. None of these is a number you can dashboard; they're the
levers you actually have to design well to keep "the code stays maintainable" true over
time, rather than levers that just move a throughput metric.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-humanlayer-resources-56fd92bf.md`
  — origin: https://www.humanlayer.dev/blog/humanlayer-resources
