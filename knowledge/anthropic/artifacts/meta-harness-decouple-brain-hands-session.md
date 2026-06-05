# Meta-harness: decouple brain, hands, and session

Because every harness encodes assumptions that go stale as models improve, the
durable design isn't a harness but a **meta-harness** — a small set of interfaces
general enough to outlast any particular implementation, the way an OS virtualized
hardware into `process`/`file`/`read()` abstractions that survived decades of
changing hardware. Managed Agents applies this by virtualizing an agent into three
independently-replaceable components:

- **The brain** — Claude plus the loop that calls it and routes its tool calls.
- **The hands** — sandboxes and tools that perform actions.
- **The session** — the append-only log of everything that happened.

The original coupled design put all three in one container, which created a *pet*:
if the container failed the session was lost, and debugging a stuck session meant
shelling into a container that also held user data. Decoupling turns each into
**cattle**, interchangeable and independently recoverable:

- **The harness leaves the container.** It calls the sandbox like any tool —
  `execute(name, input) → string` — and provisions one only when needed. A dead
  container surfaces as a tool-call error Claude can retry; no nursing. This also
  collapsed time-to-first-token (p50 down ~60%, p95 over 90%), because a session
  that never touches a sandbox no longer pays container-setup cost up front.
- **The harness itself is recoverable.** Because the session log lives *outside*
  the harness, nothing in the harness must survive a crash — a new one reboots,
  fetches the event log, and resumes from the last event.
- **Context lives outside the window.** The session is a context object the brain
  interrogates via `getEvents()` — positional slices it can rewind or re-read.
  This avoids the trap of *irreversible* compaction/trimming decisions (you can't
  know which tokens future turns need); the session guarantees durable,
  interrogable context, while arbitrary context engineering (cache-friendly
  organization, transformation) is pushed into the harness, which can't be
  predicted for future models.
- **Many brains, many hands.** Each hand is just `execute(...)` — a container, a
  phone, a Pokémon emulator — and no hand is coupled to any brain, so brains can
  pass hands to one another. Scaling to many brains is just starting many
  stateless harnesses.

A structural security payoff falls out: in the coupled design, credentials sat in
the same container as Claude's generated code, so a prompt injection only had to
make Claude read its own environment. The fix is to make tokens **unreachable from
the sandbox** — clone a repo with its token at init and wire it into the git
remote so `push`/`pull` work without the agent ever handling the token; for custom
tools, hold OAuth tokens in a vault and proxy MCP calls so the harness never sees
credentials. The principle: don't bet on what Claude "can't" do with a token —
remove the token from reach.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-managed-agents-f90fa6ca.md` — https://www.anthropic.com/engineering/managed-agents
