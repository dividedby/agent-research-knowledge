# Why skills beat deferred MCP tool-loading, mechanically

Ronacher explains *why* the skill pattern outperforms even Anthropic's deferred
tool loading, from the model internals — not just preference. The root
constraint: a model is RL-trained to emit tool calls via special tokens, and
**tool definitions can only appear between special tool-definition tokens in the
system prompt**. You can't introduce a genuinely new tool later in the
conversation without rewriting the system message — which loses reasoning traces
and, on Anthropic, trashes the cache, forcing full token rates plus cache-write
cost instead of cache-read ([[manual-prompt-cache-points]]).

- **Deferred tool loading** (Anthropic): you still declare all tools statically
  at conversation start; they're merely not *injected* until later, and are
  discovered by regex search. It requires real engineering on the API side, the
  set of possible tools is still fixed up front, and crucially there's still *no
  information about the tool in the context* until it's discovered — so you must
  write a summary anyway.
- **Skills** get the same deferral with none of that machinery. A skill is just a
  short summary, proactively loaded, of *which* capabilities exist and *which
  file* documents each. It does **not** load a tool definition: the tools remain
  bash and the agent's existing built-ins. All the agent gains is tips on how to
  use those tools more effectively, and the model's existing RL-trained
  tool-calling ability transfers directly to the newly-described command-line
  utilities. The fundamentals of chaining/coordinating them don't change.

The asymmetry that kills the MCP-via-summary middle ground: MCP tool definitions
are simultaneously *too long to eagerly load* (the Sentry MCP costs ~8k tokens)
and *too short to actually teach* usage — and MCP servers keep changing their
definitions for token reasons, so any external summary (a README, a skill file,
a materialized `mcporter` call) silently rots. That's why Ronacher's conclusion
lands on the practice [[own-your-tools-as-skills]]: have the agent write and
maintain tools under your control. He suspects dynamic MCP loading will
eventually arrive, but only with protocol changes adding skill-like summaries,
built-in manuals, and API stability.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-12-13-skills-vs-mcp-29850730.md — https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/
