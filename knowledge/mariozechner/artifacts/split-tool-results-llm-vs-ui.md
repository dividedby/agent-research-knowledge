# Split Tool Results Llm Vs Ui

A tool's return should be split into **two channels**: the content the LLM sees (text/JSON, kept minimal) and structured data for UI rendering. This serves two ends at once — the UI never has to reverse-parse the model's textual output, and the model never pays tokens for display-only detail.

In `pi-ai` a tool's `execute` returns both an `output` string for the model and a `details` object (or separate content blocks) for the UI. Arguments are validated up front via TypeBox/AJV before the tool runs, and attachments (images) are returned in each provider's native format so they round-trip correctly across backends.

The deeper principle is a clean separation between **"what the agent reasons over"** and **"what the human sees."** Conflating them forces one of two bad outcomes: either the UI scrapes structure back out of prose the model wrote for itself, or the model's context bloats with formatting and detail that only exist for a screen. Splitting the channels lets each side get exactly what it needs at its natural fidelity. Most unified LLM APIs lack this separation, which is part of why pi-ai keeps its own. This pairs naturally with the [[unified-llm-api-leaky-abstraction]] and with [[observability-is-the-feature]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
