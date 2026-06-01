# Instruction budget

A model can only follow so many instructions reliably before adherence collapses.
HumanLayer calls this the **instruction budget**, and treats it as a hard, finite
resource you spend — not a soft preference.

What the budget looks like in practice:

- Frontier thinking models follow roughly **150–200 instructions** with reasonable
  consistency. Smaller and non-thinking models follow far fewer.
- Degradation is **uniform, not local**. As you add instructions, the model doesn't
  start ignoring the *newest* ones while honoring the rest — adherence drops across
  *all* of them at once. One bloated section weakens every other instruction in the
  prompt.
- Models bias toward the **peripheries**: the very start (system prompt + CLAUDE.md)
  and the very end (most recent user message). The middle gets attended to least.
- Claude Code's own system prompt already spends **~50 instructions** before you add
  anything — roughly a third of the budget gone before your CLAUDE.md, skills, MCP
  tools, or messages.

The budget reframes several things as *costs*, not free additions:

- **Every MCP tool description is an instruction.** Connecting tools the agent
  doesn't need spends budget on text it processes without benefit — and pushes the
  agent toward the "dumb zone" faster.
- **Every CLAUDE.md line that isn't universally applicable is waste**, because it's
  paid on every session yet relevant to few.
- **Smaller models are a trap for multi-step work**: their adherence decays
  *exponentially* with instruction count, where frontier models decay roughly
  linearly. Don't hand a complex plan to a small model.

The budget is also why **long context windows are not a capability upgrade** — the
budget stays fixed while the window grows, so more room just dilutes adherence. See
*long-context-isnt-the-answer* for that argument, and *writing CLAUDE.md* practices
for how to spend the budget well.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-writing-a-good-claude-md-2fad0803.md`
  — origin: https://www.humanlayer.dev/blog/writing-a-good-claude-md
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-long-context-isnt-the-answer-dc10c427.md`
  — origin: https://www.humanlayer.dev/blog/long-context-isnt-the-answer
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-skill-issue-harness-engineerin-313aa20b.md`
  — origin: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
