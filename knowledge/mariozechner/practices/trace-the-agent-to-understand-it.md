# Trace The Agent To Understand It

To use a closed coding agent well, instrument it and read what it actually sends
instead of guessing from behavior. Zechner monkeypatches `fetch` inside Claude
Code to record every request/response pair, exposing the real system prompt, tool
definitions, and the hidden augmentations injected into your first user message.
He deliberately chooses the "stupid idiot way" — monkeypatch `fetch` — over a MITM
proxy because it's simpler and captures everything, including out-of-band Haiku
calls the on-disk transcript omits: whimsical wait messages, conversation titles,
terminal-title topic detection, and an LLM-judges-LLM safety check on bash
commands. What the agent shows you is a fraction of what it does
([[observability-is-the-feature]]).

The companion practice: a coding agent's system prompt and tool definitions are a
**moving target**. The vendor edits them release to release, and those edits change
behavior — tightened security framing, anti-emoji rules, a Grep tool rewritten to
forbid raw `grep`/`rg`, a dropped project-tree injection. So extract and **diff**
prompts across versions. When an agent suddenly behaves differently, suspect a
prompt or tool change, not the model.

The reframe is to treat the prompt as observable, versioned surface area worth
monitoring — the same way you'd track a dependency's changelog. The prompt is the
real program ([[prompts-are-code]]); the only way to know what you're running is
to read it off the wire, version it, and watch it move.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-08-03-cchistory-ada5e53e.md — https://mariozechner.at/posts/2025-08-03-cchistory
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-08-06-cc-antidebug-db307f90.md — https://mariozechner.at/posts/2025-08-06-cc-antidebug
