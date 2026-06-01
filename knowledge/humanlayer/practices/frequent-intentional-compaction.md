# Frequent intentional compaction

The naive way to drive a coding agent is chatbot-style: talk back and forth until you
run out of context, give up, or the agent starts apologizing. The slightly-smarter
way is to start a fresh session when you drift off track. **Intentional compaction**
is the deliberate version of that: before the window fills, you distill what's
happened into a structured artifact and continue from a clean window.

What you're compacting is everything that bloats context but isn't the *result*:
file-search churn, code-flow exploration, edits, test/build logs, huge JSON tool
blobs. A good compaction artifact captures the durable distillate — research findings
and relevant codebase patterns, the specific files to change and how, and the
testing/verification approach — not the transcript that produced them.

HumanLayer's mature form, **frequent intentional compaction**, designs the *entire
workflow* around context management, holding utilization in the **40–60% range**.
Their structure is a three-(ish)-stage **research → plan → implement** loop, where
each stage's output is a compacted markdown artifact that seeds the next with a fresh
window:

- **Research** — understand the relevant files, how information flows, likely causes.
- **Plan** — exact steps, exact files and edits, precise verification per phase.
- **Implement** — step through the plan phase by phase, compacting status back into
  the plan file after each verified phase. (Only this stage needs a git worktree;
  the rest happens on main.)

Sub-agents are the same idea applied mid-task: a sub-agent does the
finding/searching/summarizing in its own window and returns a compaction-shaped
result, so the parent never accumulates the noise (see *small-focused-agents*).

The payoff is real and bounded. With this workflow HumanLayer shipped expert-approved
PRs into a 300k-LOC Rust codebase neither author knew, and 35k LOC of features in
~7 hours that the maintainers estimated at 3–5 senior-engineer days each. But it is
**not magic**: it works only when you stay deeply engaged (they threw out a wrong
research doc and re-ran it with more steering), and it has hard limits — a 7-hour
attempt to strip Hadoop from parquet-java failed because the research didn't go deep
enough through the dependency tree. Frequent intentional compaction makes the agent
*better*; what makes it good enough for hard problems is the human review built into
the high-leverage stages (see *review-research-and-plans-not-code*).

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-advanced-context-engineering-cf42508e.md`
  — origin: https://www.humanlayer.dev/blog/advanced-context-engineering
