# An orb is a collaboration surface, not just a VM

A remote agent sandbox earns a name of its own — Amp calls theirs "orbs" — once
it stops being "a VM the agent runs on" and becomes an addressable, shareable,
orchestrable unit. The mechanism (sleep on idle, wake on demand, free while
asleep) is table stakes, already the whole story in
[disposable-environments-unlock-parallel-agents](../practices/disposable-environments-unlock-parallel-agents.md).
What makes the primitive worth a name is what sits on top of that mechanism:

- **A portal turns any HTTP surface into a shared, annotatable window.**
  Anything in the sandbox that speaks HTTP and listens on a port becomes
  something a human can open, annotate, and message the agent about — and each
  portal gets its own shareable URL, so a teammate can look at exactly what's
  running without pulling the branch or reproducing the environment locally.
- **The whole thread is a shareable, multiplayer object.** The orb's entire
  conversation with the agent has its own URL a teammate can open read-only, or
  join as a participant — a *multiplayer orb* where a human, their teammates,
  and the agent are all in the same chat. Feedback stops being "pull my branch
  and read the diff" and becomes "open this link."
- **Wake is a trigger, not just a request.** Because idle orbs sleep for free,
  wake can be driven by more than a new prompt: a schedule ("every 45 minutes
  for the next 8 hours") is enough for the agent to arrange its own recurring
  wake-ups, with no separate cron infrastructure for the user to own.
- **Agents can spawn and message peer orbs, not just in-process subagents.**
  An agent can ask to spin up *other* orbs — full separate remote
  environments, each running its own agent — and those agents pass messages
  and files to each other. This is a different scaling axis than
  [subagents-as-context-isolated-tools](./subagents-as-context-isolated-tools.md):
  a subagent shares the box and returns a summary into the caller's context; a
  peer orb is an independent environment the caller merely triggered and can
  now communicate with, closer to a distributed system of agents than a single
  agent's tool call.

The design lesson generalizes past Amp's product: once a disposable remote
sandbox is cheap enough to spin up at will, the return on investment shifts
from "make the sandbox faster/cheaper" to "make the sandbox a first-class,
addressable object" — something with a URL, an audience, a schedule, and
peers — because that's what turns solo remote execution into a shared,
orchestrable surface for a team.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-orbs-explained-3061c351.md` — origin: https://ampcode.com/notes/orbs-explained
