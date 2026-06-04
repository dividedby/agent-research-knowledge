# Reinforcement: every tool response is a chance to re-steer the loop

A tool call doesn't just return the tool's data — it's an opening to feed extra
information back into the loop. Ronacher found reinforcement "does more heavy
lifting than expected" in building a real agent, precisely *because* the static
prefix is frozen for caching ([[manual-prompt-cache-points]]): the live way to
inject current state is in tool responses, not the system prompt.

Uses he names:

- **Re-anchor the objective.** Remind the agent of the overall goal and the
  status of individual tasks, so it doesn't drift after a long context.
- **Failure hints.** When a tool fails, return *how* the call might succeed next
  time.
- **Background state changes.** With parallel processing, inject what changed and
  is now relevant — and if a retry is operating off broken/recovered data, tell
  it to back off a few steps and redo an earlier one.
- **Self-reinforcement.** Sometimes the agent just needs to hear its own plan
  back. Claude Code's todo-write tool is *purely* a self-reinforcement device —
  an echo tool that takes the agent's task list and echoes it out, doing nothing
  else. That's enough to drive the agent forward better than leaving the
  task/subtask only at the start of a now-buried context.

The output tool is a special, harder case. Ronacher's agent isn't a chat session;
its intermediate messages are hidden, and it talks to the human via an explicit
**output tool** (which, in his case, sends an email), prompted on when to use it.
Two surprises: steering the *tone* of the output tool is much harder than just
using the main loop's text output (a downstream Gemini Flash tone-adjust pass
*hurt* quality, added latency, and leaked internal steps); and the agent
sometimes just *doesn't call it* — so he remembers whether it was called and, if
the loop ends without it, injects a reinforcement message to push the agent to
emit the output. Reinforcement is also the plumbing behind plan mode's "read-only"
behavior, which is enforced by injected reminders rather than disabled tools —
see [[plan-via-a-file-on-disk]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-11-21-agents-are-hard-01c828c6.md — https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-12-17-what-is-plan-mode-c0bb68c8.md — https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/
