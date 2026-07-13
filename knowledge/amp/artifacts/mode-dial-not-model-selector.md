# A mode dial, not a model selector

Amp exposes agent modes as a single difficulty dial — "how hard is this task?"
— instead of a model picker that expects the user to already know which model
fits. A model selector demands model-literacy and freezes the interface to
today's model lineup; a task-difficulty dial stays stable as models turn over,
because Amp — not the user — wires the model(s), system prompts, tools, and
reasoning effort behind each mode, and can rewire that combination whenever
better models ship without changing what the user does.

Why this shape:

- **One question replaces many.** Picking "which model" requires knowing each
  model's strengths; picking "how hard" only requires knowing your own task.
- **The wiring is disposable, the interface isn't.** Because a mode is a
  bundle (model + prompt + tools + effort) rather than a raw model name, Amp
  can swap what's behind `high` or `ultra` as the field moves, and the user's
  mental model never goes stale.
- **The dial is extensible, not just a fixed set of presets.** Agent mode
  plugins let you define custom modes with your own model, prompt, and tools,
  and they sit alongside the built-in modes rather than replacing them —
  removing knobs from the *default* experience, not from Amp itself.
- **Don't interrogate the agent about itself.** LLMs self-report their own
  model name unreliably, and forcing the system prompt to correct that wastes
  tokens and degrades performance. The dial and the Models page are the
  authoritative UI for "what's actually running" — check there, not the chat.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-fif-dc1eb004.md` — origin: https://ampcode.com/notes/fif
