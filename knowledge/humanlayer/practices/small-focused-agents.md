# Small, focused agents

The "give it a goal and a bag of tools, loop until done" pattern fails for the same
reason every time: agents get lost when the context window gets long. Past roughly
10–20 turns the history becomes a mess the LLM can't recover from — it spins out,
retrying the same broken approach. A 90%-success agent is still a web app that
crashes on 10% of page loads: nowhere near "good enough to put in customer hands."

HumanLayer's structural answer is to keep each agent **small and focused** — scoped
to a single domain and **3–10 (maybe 20) steps**. Smaller scope means a shorter
context window, which means the model stays in the zone where it performs. The agent
is one block inside a larger, mostly *deterministic* system, not the whole system.

Two complementary tools enforce this:

- **Micro agents inside a deterministic DAG.** Most of the workflow is ordinary
  software; the LLM is dropped in only at the points where its judgment earns its
  keep (e.g. parsing a human's plaintext feedback into the next workflow step). The
  deploy bot is the canonical example: deterministic code deploys, tests, and gates
  on human approval, and the agent only handles the 5–10-step human-in-the-loop slice.
- **Sub-agents as context firewalls.** Sub-agents are *not* about anthropomorphizing
  roles — they are about context control. A delegated task runs in its own window;
  the parent never sees the intermediate `Glob`/`Grep`/`Read` churn, only the final
  condensed result. That keeps the parent's window clean across work that would
  otherwise blow a single window. Good sub-agent output is a tight summary plus
  source citations (`filepath:line` or URLs) so the parent can confirm without
  re-reading the sources. Spend the expensive model on the orchestrating parent and
  cheaper models on the discrete sub-tasks.

The objection — *won't smarter models make this unnecessary?* — HumanLayer answers
"no, and also yes": as models improve they'll reliably handle a bit more of a larger
DAG, so you slowly widen scope. But small-and-focused is what gets results *today*,
and it's the same discipline you already know from refactoring large deterministic
codebases. Find the edge of the model's reliable capability and stay just inside it.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-12-factor-agents-00e2e139.md`
  — origin: https://www.humanlayer.dev/blog/12-factor-agents (Factor 10: Small, Focused Agents)
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-skill-issue-harness-engineerin-313aa20b.md`
  — origin: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-long-context-isnt-the-answer-dc10c427.md`
  — origin: https://www.humanlayer.dev/blog/long-context-isnt-the-answer
