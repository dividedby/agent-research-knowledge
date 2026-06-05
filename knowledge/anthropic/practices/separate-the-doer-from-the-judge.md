# Separate the agent doing the work from the agent judging it

Ask an agent to evaluate its own output and it skews positive — confidently
praising work that a human would call mediocre, identifying a real bug and then
talking itself into approving anyway. The pathology is sharpest on subjective
tasks (is this design polished?) where there's no binary test, but it shows up on
verifiable tasks too. The structural fix is to split the roles: a **generator**
that produces, and a separate **evaluator** that grades.

Separation alone doesn't cure the leniency — the evaluator is still an LLM
inclined to be generous toward LLM output. But tuning a *standalone* evaluator to
be skeptical is far more tractable than making a generator critical of its own
work, and once that external feedback exists, the generator has something
concrete to iterate against. The evaluator must be *built*, not assumed: out of
the box Claude is a poor QA agent, and the tuning loop is to read its logs, find
where its judgment diverged from yours, and revise its prompt — for subjective
tasks, anchored by few-shot examples with detailed score breakdowns to reduce
drift. Giving the evaluator real tools (e.g. driving the live app via Playwright
rather than scoring a static screenshot) makes its findings specific enough to
act on.

The same move recurs as an **adversarial review step** in everyday workflows: a
reviewer in a fresh subagent context sees only the diff and the criteria, not the
reasoning that produced the change, so it grades the result on its own terms — a
correctness check (the bundled `/code-review` skill runs exactly this, reviewing
the current diff for bugs in a fresh subagent and returning findings to the
session), or a check against the original plan, for which you write the review
prompt yourself naming the work, the plan, and what counts as a finding. The
longer the agent worked unattended, the more this independent check matters before
the work counts as done. One caution: a reviewer
asked to find gaps will find some even when the work is sound, so constrain it to
flag only gaps that affect correctness or the stated requirements, lest you chase
phantom findings into over-engineering. And for free-form output with no single
right answer, a single **LLM-as-judge** call scoring against an explicit rubric
(factual accuracy, completeness, source quality) scales evaluation across
hundreds of outputs — though human review still catches the edge cases automation
misses.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-harness-design-long-runn-2ef732b7.md` — https://www.anthropic.com/engineering/harness-design-long-running-apps
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-code-best-practic-4d249e2a.md` — https://www.anthropic.com/engineering/claude-code-best-practices
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-multi-agent-research-sys-37ed91c9.md` — https://www.anthropic.com/engineering/multi-agent-research-system
- `sources/anthropic/best-practices/https-code.claude.com-docs-en-best-practices-fb8dc53b.md` — https://code.claude.com/docs/en/best-practices
