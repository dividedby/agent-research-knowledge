# Have the agent write and maintain its own tools as skills

Ronacher has migrated all his MCPs — Playwright, Linear, Sentry — to **skills**,
and his preferred move when the agent needs a capability it lacks is not to
download an extension but to *ask the agent to write its own tool as a skill*.
The biggest benefit is control: when the tool breaks or needs a feature, he asks
the agent to adjust it. "Because the agent maintains it, it works out better,"
even if the skill is buggy.

Why skills beat the MCP alternatives for *his* workflow:

- **Skills don't load tool definitions.** A skill is just a short summary of
  what capabilities exist plus a pointer to a manual file. The tools stay the
  same — bash and the agent's built-ins — and the model's RL-trained tool-calling
  ability carries over to the newly-described tools. (The mechanics of why this
  outperforms even Anthropic's deferred MCP loading are in
  [[skills-over-deferred-tool-loading]].)
- **MCP servers won't hold API stability.** They trim tool definitions to save
  tokens and change syntax at will — the Sentry MCP once switched its query
  syntax wholesale to natural language. Great for the model, but it silently
  broke Ronacher's hand-written usage notes. Skills that document an unstable
  MCP rot without warning; a tool *you* own changes only when you change it.
- **Exposing an MCP via CLI doesn't rescue it.** Tools like Steinberger's
  `mcporter` make MCP calls look like a CLI (`mcporter call 'linear.create_comment(...)'`),
  but the model has no idea the tools exist, so you're back to writing and
  maintaining manual skill summaries anyway — over an unstable surface.

This is the practice-side expression of [[cli-over-mcp]] and
[[code-over-inference-for-repeatable-work]]: the agent's functionality should be
malleable, local, and under your control. It reaches its purest form in the
[[malleable-self-extending-agent]] (Pi), where the agent extends *itself* — e.g.
replacing all browser-automation MCPs with a hand-built skill that just drives
CDP — and where skills are disposable: he throws them away when no longer
needed.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-12-13-skills-vs-mcp-29850730.md — https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-1-31-pi-e44c11e9.md — https://lucumr.pocoo.org/2026/1/31/pi/
