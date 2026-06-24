# Defect rate, not capability, is the binding constraint

Brooker's hypothesis about the economics of agentic AI: the size of the
opportunity will be limited more by **defect rate** (the left tail of outcomes)
than by peak capability (the right tail) — and the industry over-invests in the
right tail. "Outcomes continue to matter."

## The four-blocker

Arrange defects on two axes — *seriousness* and *frequency* (deliberately
conflating "how hard is the problem" with "how capable is the agent," because the
output that matters to a user is just the user-experienced defect):

- **High frequency, high seriousness** — basically nobody but true believers.
- **High frequency, low seriousness** — "slop is OK" work: one-off scripts, small
  experiments, basic UIs, summarizing the soccer-league email. A large, real
  opportunity even if it bruises professional pride.
- **Low frequency, high seriousness** — an odd corner usable only by experts who
  can review, debug, and operate the result; debugging often needs *more*
  understanding than building did, which severely limits who benefits.
- **Low frequency, low seriousness** — the goal, because *everybody can play*.

The point: defect rate gates *how many people can use an agent*, irrespective of
how good it is on its best day. Easier problems migrate toward the safe corner
faster, but the gating variable is the same.

## Invest in the left tail

Framed as a distribution of outcomes: the **right tail** is positive capability
(where attention and effort pile up); the **left tail** is the defects (under-
attended but probably the more important place to invest if you want real
customers and a real business). Agents are feedback loops, so they can work
around model gaps — but a bad harness or bad feedback can also *hide* a good
model's capability ("great feedback can make a bad model much better"). The work
to shrink the left tail is correct-by-construction tooling (Hydro, Cedar, Rust),
spec-driven development and property-based testing, formal code-reasoning (Lean-
powered Strata), autoformalization (turning NL into formal implementations to
remove whole defect classes), deterministic tool policy, and principled steering.

## Keep eval honest — pass@k is (mostly) bunk

The cultural prerequisite is honest measurement, and the most common agent metric
fails it. **pass@k** — the probability at least one of *k* attempts succeeds — is
*exponentially forgiving*: a die where "6 = pass" has pass@10 of 83%; a D20 has
pass@100 of 99.4% while actually working 5% of the time. There's always some
modest *k* that makes anything look great. But humans aren't that forgiving —
"I tried 10 times and it only worked once, what a piece of junk" — and they chain
steps, so they're *exponentially un*forgiving (pass^k is the better model).
pass@k is only legitimate where tasks are simple, evaluators reliable, and humans
out of the loop (linear extra cost buys exponentially better success); those
tasks aren't ubiquitous, so it "should be a metric that's rarely used, and
carefully justified every time." What he'd add to benchmarks: **failure
*severity*, not just pass/fail**; an end-to-end view of agent success (ops, cost,
availability, security, performance — what customers actually care about) rather
than just code-patching; a taxonomy of agentic failure modes; and a culture that
"takes our worst days as seriously as our best ones" (AWS's learn-from-failure
posture, applied industry-wide).

## Sources

- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-04-30-be-right.html-95c4d9e2.md` — origin: https://brooker.co.za/blog/2026/04/30/be-right.html
- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-01-21-pass-k.html-f1a5d1b6.md` — origin: https://brooker.co.za/blog/2026/01/21/pass-k.html
