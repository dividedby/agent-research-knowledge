# Unified Llm Api Leaky Abstraction

A multi-provider LLM layer (`pi-ai`) reduces to **four real APIs** — OpenAI Completions, OpenAI Responses, Anthropic Messages, and Google Generative AI — over which a thin abstraction absorbs a long tail of per-provider quirks: field names, reasoning fields, role support, token-reporting timing. Build directly on the provider SDKs rather than something like the Vercel AI SDK, to keep full control and a small surface — especially for self-hosted models, where heavier SDKs mishandle tool calling.

Several choices are load-bearing and absent from most "unified" APIs:

- **First-class abort throughout the pipeline** — including mid tool-call — returning partial results rather than nothing.
- **Partial-JSON parsing** of streaming tool arguments, so the UI can render diffs mid-stream instead of waiting for a complete call.
- **Best-effort cross-provider context handoff**: Anthropic thinking traces are serialized as `<thinking>` blocks; signed reasoning blobs are replayed where the provider requires it.
- A **typesafe model registry** generated from models.dev / OpenRouter, plus an escape hatch to hand-define models the registry doesn't know.

The abstraction is leaky by nature — provider differences leak through no matter how you slice it. The point is that a **small, honest** leaky abstraction beats a **large, organically-evolved** one: by targeting exactly four backends and surfacing the quirks rather than pretending they don't exist, the layer stays comprehensible and controllable.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
