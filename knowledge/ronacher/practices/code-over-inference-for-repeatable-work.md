# For anything repeatable, generate code — don't loop on inference

The oldest engineering instinct — "replace yourself with a shell script" —
becomes, with LLMs, "replace yourself with *generated* code," not "replace
yourself with the LLM." The distinction is the whole point. Inference at every
step is expensive, slow, unreliable, and — fatally — *unverifiable*: getting an
LLM to compute or transform something "sort of works," but checking the result
can take as long as doing it yourself.

Code flips what you have to trust. When the LLM writes the *code* that does the
work, you review the **approach** — the formula, the AST transform, the pipeline
— not each output. You can rely on the machine to execute correct code
correctly, and you can even use a second LLM as a judge of the approach. So you
get back the engineer's normal ability to verify a process rather than hope the
model inferred right.

The canonical example: converting his blog from reStructuredText to Markdown.
He didn't trust the LLM to transform the prose directly (subtle regressions,
context exhaustion, silent reword). Instead he had it write a *pipeline*: parse
to an rST AST → convert to a Markdown AST → render HTML; then a second script
diffing old vs new HTML with principled allowances for known-acceptable
differences (footnotes render differently); then a third analysis script feeding
back into the loop. He ran it on 10 docs until diffs were low, then all of them.
Trust came from reviewing the mechanical approach, not the output.

Two structural payoffs:

- **Cost decouples from volume.** Inference cost scales with iteration steps and
  sample size, not document count — running over 15 docs vs 150 is roughly the
  same effort, because the final judge step already skips minor diffs.
- **The artifact is reusable and human-runnable.** Once written, the script runs
  100s of times with zero further inference, and you (a human, "not an MCP
  client") can run and debug it.

Automate the things that recur, not one-shots. This is the principle behind his
preference for [[cli-over-mcp]] (CLIs compose without inference) and for the
[[code-as-the-mcp-interface]] pattern (an MCP whose command language is just
Python). The residual cases where you can't escape per-step inference — e.g.
remote-controlling a browser you've never seen — are exactly where you keep the
agent in the loop; but for navigating *your own* app, have it write a Playwright
script instead.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-7-3-tools-d973b4d4.md — https://lucumr.pocoo.org/2025/7/3/tools/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-8-18-code-mcps-7d9f20ae.md — https://lucumr.pocoo.org/2025/8/18/code-mcps/
