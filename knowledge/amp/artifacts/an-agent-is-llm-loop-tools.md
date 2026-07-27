# An agent is an LLM, a loop, and tools defined as plain text

Building a fully capable code-editing agent is not a matter of hidden
architecture. It's an LLM, a loop that resends the growing conversation, and a
handful of tools each defined as a small text contract. Amp's own from-scratch
build gets a real, autonomous, file-editing agent in under 400 lines of Go —
most of it boilerplate. The sophistication that makes a production agent like
Amp "addictive and impressive" is elbow grease layered on top of this same
core (UI, tuned prompts, more tools, multi-agent) — not a different, more
exotic core. Knowing this matters because it sets the right expectation for
anyone building or extending a harness: don't over-plan the architecture
before building it: stand up the loop and the tool contract first, then add
capability incrementally on the same shape.

The mechanics:

- **The loop is the whole heartbeat.** Keep a growing conversation array; each
  turn, send the *entire* history to the model (the server is stateless — it
  only ever sees what's in the conversation you send), append the reply, print
  it, repeat. There's no other state to manage.
- **A tool is what turns a chat client into an agent.** Amp's working
  definition: an LLM with access to tools, giving it the ability to modify
  something outside the context window. Without tools it's just a chat
  window.
- **A tool is a text handshake, not magic.** Every tool the model can call
  boils down to a name, two natural-language descriptions (what the tool
  does, what its one input parameter means), a JSON input schema, and a local
  function that executes it. The descriptions get wrapped into a system
  prompt on the server; the model's "I want to use this" reply is just a
  specifically-shaped message. The mental model: agree on a signal ("wink if
  you want me to raise my arm"), watch for it, act on it, hand back the
  result as the next turn. There's no protocol magic underneath — whatever
  format you choose for a tool's output (plain strings, a trailing slash for
  directories, a two-header Markdown doc) works as long as the model can make
  sense of it; which format wins is found by experimentation, not spec.
- **The loop doesn't change shape to add tool use** — it just branches: when a
  reply contains a `tool_use` block, look the tool up by name in a local
  registry, run its function with the model-supplied input, and feed the
  result back as the next turn instead of waiting on the user.
- **Three tools are enough for real autonomy.** `read_file`, `list_files`, and
  a string-replace-based `edit_file` are enough for the model to *compose*
  them unprompted — list a directory, read the relevant files, then edit the
  right one — without ever being told that procedure. The combination is the
  model reasoning out its own plan once the primitives exist; you don't wire
  the sequence yourself.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-how-to-build-an-agent-156bac74.md` — origin: https://ampcode.com/notes/how-to-build-an-agent
