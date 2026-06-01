# Agents are mostly software

The "12-factor agents" thesis: the good production agents are not "here's a prompt,
here's a bag of tools, loop until done." They are **mostly ordinary deterministic
software with LLM steps sprinkled in at the points where judgment is needed.** The
promise of agents — throw away the DAG, give the model the edges and let it find the
nodes — breaks down in practice because the pure tool-calling loop gets lost once the
context grows (the case for *small-focused-agents*). What survives is owning the
software around the model.

Stripped to essentials, an agent is four things you should *own*:

- a **prompt** (how to behave, what tools exist),
- a **switch statement** over the LLM's structured output,
- **accumulated context** (the event history), and
- a **for loop** that runs until a terminal step.

The factors are mostly instructions to keep control of each piece rather than ceding
it to a framework:

- **Own your prompts** (F2). Treat them as first-class code you can test, eval,
  iterate, and read — not a black box you can't tune. "I don't know the best prompt,
  but I want the flexibility to try EVERYTHING."
- **Own your context window** (F3). You don't have to use the standard
  role/message format; build whatever structure packs the most signal per token
  (see *context-is-the-only-lever*).
- **Tools are just structured outputs** (F4). A tool call is the model emitting JSON;
  deterministic code decides what to *do* with it. "Called a tool" doesn't obligate
  you to run one fixed function the same way every time — it's a clean split between
  the model's *decision* and your code's *action*.
- **Own your control flow** (F8). Because you own the loop, certain tool calls can
  break out of it — to wait for a human, a long-running job, or an approval. The
  most-wanted capability: pause/resume *between tool selection and tool invocation*,
  so a high-stakes call can be reviewed before it runs. Without it you're stuck
  blocking in memory, restricting agents to low-stakes work, or yolo-ing.
- **Unify execution and business state** (F5) and **launch/pause/resume via simple
  APIs** (F6). Infer execution state (current step, waiting, retries) from the event
  history itself, so the whole thread serializes, resumes, forks, and renders for a
  human trivially.
- **Compact errors into context** (F9). Feed an error/stack trace back and the model
  often self-heals — but cap retries (~3) and, past the threshold, restructure the
  context or escalate rather than letting it spin on the same failure.

Two factors are about reaching humans and systems: **contact humans with tool calls**
(F7) — model the request for human input as just another structured tool output, and
have humans answer via webhook so the agent resumes — and **trigger from anywhere**
(F11): let agents be kicked off by Slack, email, cron, or an outage (outer-loop
agents), do real work, and loop in a human only at the critical moment, which is what
makes higher-stakes operations safe to grant.

The throughline is the same as the rest of HumanLayer's practices: the model is a
*stateless reducer over context* (F12), so the reliability comes from the software you
wrap around it — owned prompts, owned context, owned control flow, small scope, and
human checkpoints at the high-stakes seams.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-12-factor-agents-00e2e139.md`
  — origin: https://www.humanlayer.dev/blog/12-factor-agents
