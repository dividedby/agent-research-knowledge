# LLM APIs are really a distributed state-sync problem

The message-based completion API is, in Ronacher's view, the wrong abstraction
for what's actually happening. Underneath, a model is just tokens through fixed
weights producing activations and a KV cache; there's no real "user" vs
"assistant" — only special role tokens injected by a prompt template. The right
mental model is **distributed state synchronization** between your side and the
provider's, and today's APIs were not designed with that mindset.

Why the message abstraction leaks:

- **Hidden, un-replayable state.** You never see the real tokens. The provider
  injects prompt templates, tool definitions, cache points, and out-of-band data
  you can't see; reasoning models hide reasoning tokens; search results come back
  as an *encrypted blob you must send back* to continue. There's also derived
  state (the KV cache) that replaying tokens won't reconstruct.
- **Quadratic cost from resend.** Completion APIs resend the entire history each
  turn — linear per request, quadratic cumulatively — which is *why* caching
  matters in the first place.
- **The Responses API trades one problem for a worse one.** Keeping history
  server-side turns the whole interaction into explicit state sync with very
  limited sync capabilities: unclear how long a conversation lives, what happens
  on divergence/corruption/network-partition, and he's seen it get stuck
  unrecoverably. Great for the provider (hides more state); painful for the user.
- **Intermediaries can't fully unify it.** OpenRouter and the Vercel AI SDK mask
  user-visible message differences but can't unify each provider's
  *incompatible hidden state* — the actual hard part. (This is the API-shape root
  of [[build-your-own-agent-abstraction]].)

The prescription: borrow from the **local-first movement**, which spent a decade
on shared-state-with-gaps — separating canonical state, derived state, and
transport; append-only logs synced incrementally instead of resent; CRDT-style
heal/merge. KV caches map to checkpointable derived state; prompt history to an
append-only log; hidden provider context to a replicated document with hidden
fields. A real standard should acknowledge hidden state, sync boundaries, replay
semantics, and failure modes — and crucially allow full replay from scratch if
the remote wipes its state (which the Responses API can't). The risk he warns
against: rushing to formalize MCP-era message conventions and locking in their
faults. Manual cache management ([[manual-prompt-cache-points]]) is the small,
concrete place this worldview already bites.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-11-22-llm-apis-2d2874b5.md — https://lucumr.pocoo.org/2025/11/22/llm-apis/
