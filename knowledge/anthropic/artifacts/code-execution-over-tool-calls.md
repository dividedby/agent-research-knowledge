# Let the agent orchestrate tools by writing code

Direct tool calling has two structural costs that compound as workflows grow:
every intermediate result flows back through the model's context (a 2-hour
transcript copied twice is 50K+ tokens; large data can exceed the window
entirely), and orchestration logic — loops, conditionals, joins, retries — has to
be expressed implicitly through the agent's turn-by-turn reasoning, one inference
pass per call. Both vanish if you let the agent **write code that calls the tools**
instead.

Present MCP servers as a **code API** rather than direct tool calls — e.g. a file
tree where each tool is a typed function the agent imports and calls (Cloudflare
calls the same idea "Code Mode"; the insight is that LLMs are excellent at writing
code, so play to that strength). The agent then:
- **Filters and transforms data in the execution environment** before anything
  reaches the model — fetch a 10,000-row sheet, `.filter()` it, log only the 5
  rows that matter. The Google-Drive-to-Salesforce example dropped 150K tokens to
  2K (a 98.7% saving).
- **Expresses control flow as code** — a `while` poll-loop, conditional trees,
  error handling — instead of alternating tool calls and sleeps through the agent
  loop, which also saves time-to-first-token (the environment evaluates the
  branch, not the model).
- **Keeps intermediate results out of context by default** — the model sees only
  what the code explicitly logs or returns. This enables a security pattern: the
  harness can tokenize PII so real values flow tool-to-tool through the execution
  environment but never enter the model's context.
- **Persists state and reusable code** — write intermediate results to files to
  resume later, and save working implementations as functions. Adding a `SKILL.md`
  to a saved function turns it into a reusable Skill, letting the agent grow its
  own toolbox of higher-level capabilities over time.

The API-level expression of this is **Programmatic Tool Calling**: mark tools with
`allowed_callers: ["code_execution_…"]`, and the agent emits a script run in a
sandbox that *pauses* for each tool call, processes the returned result in-
environment, and returns only the final output to the model — the 2,000 expense
line items never enter context, just the answer.

The trade-off is real: running agent-generated code needs a secure sandbox with
resource limits and monitoring, which is operational overhead direct tool calls
avoid. Reach for it when the token/latency/accuracy gains are substantial (large
intermediate data, multi-step orchestration), not for simple single-call tasks.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-code-execution-with-mcp-4dd2373a.md` — https://www.anthropic.com/engineering/code-execution-with-mcp
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-advanced-tool-use-fe2899cf.md` — https://www.anthropic.com/engineering/advanced-tool-use
