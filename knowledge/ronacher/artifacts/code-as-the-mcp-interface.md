# Make the MCP's command language a programming language

Ronacher's reconciliation of "[[cli-over-mcp]]" with the cases where CLIs fail:
expose an MCP server with **a single tool whose input is code** — an "ubertool"
that is a stateful interpreter (Python or JavaScript) with retained state. You
keep the one genuine advantage MCP has over shell — built-in, stateful session
management — while making the *interface* something the model already knows
deeply.

The motivating problem: CLIs can't compose without inference and force the agent
to juggle stateful sessions it's bad at (losing track of a tmux/LLDB session).
MCP *is* stateful out of the box — but a naively-wrapped tool surfaces dozens of
tiny calls the model has never seen. His public example **`pexpect-mcp`** exposes
one `pexpect_tool` that just runs Python against a virtualenv with `pexpect`
imported (`child = pexpect.spawn(...)`; `child.expect(...)`; `child.sendline(...)`).
A `pexpect.Spawn` object has 36 API functions and most can't be used in
isolation; collapsing them into "send Python" works because the meta-language is
known, the SDK is in the weights, and timeout support is added in the server.

Why this is more than convenience:

- **The language indirectly exposes its whole standard library.** The model
  knows `dir()`, `globals()`, `repr()`, even `sys._getframe()`, so you can give
  it a tiny prompt about how to *introspect* its own sandbox and discover what's
  available — sidestepping MCP's context-rot from many tool definitions and its
  low input limits.
- **The code it writes is the script you'd keep.** Because the session is just
  Python in the context, you can ask the agent afterward to dump a standalone,
  reusable script — exactly the [[code-over-inference-for-repeatable-work]]
  payoff. (His LLDB-debugging demo: first run ~7 tool calls / 45s; the dumped
  playbook re-runs in one call / <5s and runs *without the MCP*, even by a
  human.)
- **It generalizes to your own systems.** A tiny ubertool can dump app internal
  state, query a sharded DB, expose data-reading APIs — and the agent can debug
  the MCP's own state because the language is so powerful.

The caveats he's candid about: for code *not* in the training set it works less
well; `playwrightess` (Playwright API via JS `page.eval`, ~30 tool defs → 1) is
"promising but not promising enough yet" — verbose, poorly tuned between
screenshots and text. And the security stance is explicit: an `eval()` MCP is
inherently unsafe and impossible to secure, but it's "the same kind of bad" as
letting an agent run code and tests at all, so he treats the tail risk as here to
stay rather than solvable. Conceptually this is a cousin of
[[skills-over-deferred-tool-loading]]: both replace bespoke tool definitions with
something the model already has in its weights — a language, or its existing
bash/built-in tools.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-8-18-code-mcps-7d9f20ae.md — https://lucumr.pocoo.org/2025/8/18/code-mcps/
