# Put human review where the leverage is: research and plans, not code

When an agent writes most of your code, reviewing every line stops scaling — and it
turns out to be the wrong place to spend attention anyway. HumanLayer's leverage
argument: a bad line of *code* is one bad line; a bad line of a *plan* can spawn
hundreds of bad lines of code; a bad line of *research* — a misunderstanding of how
the system works or where something lives — can spawn *thousands*, because the plan
and then the code are built on top of it.

So **focus human effort on the highest-leverage artifacts**: review the research and
the plan, where a correction is cheap and prevents a cascade, rather than the code,
where you're paying to catch errors after they've already propagated. The two BAML
plans illustrate it — the no-research plan and the with-research plan "both would
have worked," but the researched one fixed the bug in the *right* place with testing
that matched codebase conventions. The difference was upstream.

This also reframes what code review is *for*. Following Blake Smith, the most
important function of review is **mental alignment** — keeping the team's
understanding of how the code is changing, and why, in sync. The biggest pain on a
team shipping 2,000-line AI PRs every few days wasn't correctness; it was the author
*losing touch with what the product was and how it worked*. When everyone ships far
more code, an ever-larger share of the codebase is unfamiliar to any given engineer
at any moment, so you must have a process that (1) keeps people on the same page and
(2) lets them quickly learn unfamiliar areas. For most teams that's PRs and internal
docs; for HumanLayer it became the specs, plans, and research themselves — readable
200-line artifacts that stand in for spelunking 2,000 lines of Go or 40 files of
daemon code.

The mindset shift is uncomfortable (it took the team ~8 weeks): you stop reading
every line of generated code and let the spec become the source of truth — read the
tests carefully, trust the reviewed plan for the rest. The spec-driven framing
(Sean Grove's "specs are the new code") is that throwing away your prompts and
keeping only the compiled code is like checking in a JAR and deleting the source.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-advanced-context-engineering-cf42508e.md`
  — origin: https://www.humanlayer.dev/blog/advanced-context-engineering
