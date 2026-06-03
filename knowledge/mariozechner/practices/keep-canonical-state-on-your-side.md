# Keep Canonical State On Your Side

For closed SaaS LLMs, treat the provider as a black box that computes over *your*
canonical log. Store the full session yourself — messages, tool calls, file
references — and accept that anything the provider hides is opaque, lossy, derived
scratchpad you can never replay: thinking traces, server-side tool-result blobs,
prefix-cache keys, Responses-API session stores, VM and container state. Your log
is the source of truth ([[prompts-are-code-state-on-disk]]); their hidden state is
disposable.

The "messages" abstraction is not a leaky veneer over something simpler — it's
baked into model weights via the chat template. A "purer" token or state API
wouldn't fix hidden-state problems; it would just move the complexity around. So
don't wait for a cleaner primitive. Provider-given opaque blobs are fine to echo
back, like an HTTP-only cookie, but they make your state provider-specific:
switching providers means dropping their blobs and re-uploading your files from
the canonical log you kept.

The one genuinely catastrophic case is provider-managed **execution
environments** — where the agent builds up container state to do its task. That
state is invisible, unrecoverable, and tied to one vendor. The only safe design is
to manage the execution environment yourself, so its state lives in your canonical
log too. Design this way and provider portability falls out for free: you can move
between providers because you never depended on anything they refused to hand you
back. Own your state, rent only the compute.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-22-armin-is-wrong-f614910b.md — https://mariozechner.at/posts/2025-11-22-armin-is-wrong
