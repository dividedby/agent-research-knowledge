# Generator–evaluator harness for autonomous building

A GAN-inspired harness structure for autonomous, multi-hour building: split the
work into a **generator** that produces and an **evaluator** that grades, looping
the evaluator's critique back as the generator's next input. It targets the
self-evaluation failure (agents praise their own mediocre work) by making the
critic a separate, skeptical agent — see the companion practice on separating the
doer from the judge.

Two domains validated the same shape. For **frontend design** (subjective, no
binary test) the move was to turn "is this beautiful?" — unanswerable
consistently — into "does this follow our design principles?", giving the model
concrete gradable criteria. Four weighted criteria (design and originality
weighted over craft and functionality, which the model already does well; generic
"AI slop" explicitly penalized) steered the generator toward aesthetic
risk-taking. The evaluator drove a live Playwright browser to study the page
before scoring, ran 5–15 iterations, and was calibrated with few-shot examples and
detailed score breakdowns to prevent drift. Notably, the criteria's *wording*
shaped output ("museum quality" pushed a particular convergence), and even the
first iteration beat an unprompted baseline — the criteria steer before any
feedback loop runs.

Carried to **full-stack development**, this became a **three-agent** system —
generator–evaluator plus a **planner** that expands a 1–4 sentence prompt into an
ambitious product spec. The planner is kept at the level of product context and
high-level design, *not* granular implementation, because spec errors cascade
downstream — constrain the deliverables, let the agents find the path. The
evaluator used Playwright to click through the running app like a user (out of the
box Claude is a poor QA agent — it took rounds of reading logs and revising the QA
prompt to make its judgment usable). A **sprint contract**, negotiated between
generator and evaluator before each chunk, bridges the high-level spec to testable
criteria; agents communicate via files.

The deepest lesson is about *when* the harness earns its cost. As the model
improved (4.5 → 4.6), pieces became dead weight: context resets (needed for 4.5's
context anxiety) were dropped on 4.6; the sprint construct was removed; the
evaluator moved to a single end-of-run pass. The evaluator is **not a fixed
yes/no** component — it's worth its cost only when the task sits beyond what the
current model does reliably solo, a boundary that moves outward with each model.
The harness was over 20× more expensive than a solo run ($200 vs $9 for the same
prompt) but produced a working app where the solo run's central feature was
broken — the cost buys capability at the edge of the model's reach.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-harness-design-long-runn-2ef732b7.md` — https://www.anthropic.com/engineering/harness-design-long-running-apps
