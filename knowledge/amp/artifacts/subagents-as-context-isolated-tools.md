# Subagents as context-isolated tools

A subagent is itself a tool: an agent the *main* agent can spawn, passing it a
prompt and a task, exactly as a human spawns an agent. (Amp's definition of an
agent: "an LLM with access to tools, giving it the ability to modify something
outside the context window" — a subagent is one of those tools.) Two properties
make it unlike any other tool in the box:

1. **It's an agent** — it makes its own decisions and autonomously pursues a
   task. You don't tell it "run this command"; you tell it "run this command 5
   times and report how the output changed."
2. **It has its own context window.** This is the load-bearing property. With a
   single agent, tokens spent fixing a compiler error are gone from the budget
   for the larger task. A subagent fixes the error in a *fresh* window and
   returns only a tiny summary — the main agent's context is barely touched, no
   matter how many attempts the fix took. The main agent can also spawn
   **multiple subagents in parallel**, delegating a plan's tasks instead of
   grinding them one-by-one and risking a token rabbit hole.

This commoditizes context-window management, which previously took real skill —
it lowers the bar enough that "classes of inception are now possible."

Design lessons from Amp building these:

- **Generic beats specialized.** Amp's long-standing subagent is the read-only
  *search agent* ("find where the auth logic is"). Attempts at other narrow,
  differently-prompted subagent *types* never paid off — either the search agent
  already covered the job, or it wasn't clear even to humans when to pick one
  over another, or the model just didn't invoke them. The version that worked was
  **generic** mini-Amps: subagents that can do anything the main agent can,
  including *write* and run commands.
- **Give the model what it wants.** Whether subagents get used is a property of
  the *model*, not just the wiring. Claude 3.7 Sonnet ignored them and did the
  work itself; Claude Sonnet 4 eagerly delegates whenever it spots a
  clearly-defined task. Amp's mantra — give the model what it needs — meant
  adding subagents back once the model wanted them.
- **Don't over-nudge yet.** Amp deliberately *hasn't* cranked subagent prompting
  in the system prompt, because the right workflow integration is still unknown.
  For now the best lever is being explicit per-task: "use a subagent for this,"
  "use a subagent implementing this in each of these files."

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-agents-for-the-agent-4fb42ef5.md` — origin: https://ampcode.com/notes/agents-for-the-agent
- `sources/amp/chronicle/https-ampcode.com-notes-200k-tokens-is-plenty-4df831c1.md` — origin: https://ampcode.com/notes/200k-tokens-is-plenty
