# Build your own agent abstraction; don't lean on a high-level SDK

When building an agent you can target a low-level provider SDK (OpenAI,
Anthropic) or a high-level abstraction (Vercel AI SDK, Pydantic). Ronacher's
team adopted the Vercel AI SDK — but *only its provider abstractions* — and drove
the agent loop themselves. With hindsight they would not even do that again:
right now, while things are unsettled, build directly on the provider SDKs and
keep full control.

The reasoning is that the right abstraction for an agent *isn't known yet*, and
high-level SDKs force you to build on their guesses:

- **Model differences are large enough to demand your own abstraction.** The
  agent loop is "just a loop," but the subtle differences — cache control,
  per-model reinforcement requirements, tool prompts, provider-side tools — mean
  no off-the-shelf SDK has found the right abstraction. The provider SDKs keep
  you fully in control while the shape is still emerging.
- **Provider-side tools break the unification.** Anthropic's web search tool
  "routinely destroys the message history" through the Vercel SDK. Cache
  management is much easier targeting Anthropic directly (see
  [[manual-prompt-cache-points]]), and the error messages are far clearer.

This is the engineering-level counterpart to his diagnosis that the message-based
API surface is the wrong abstraction altogether — see [[llm-apis-as-state-sync]].
The benefits of a unifying SDK simply don't yet outweigh the costs. It's a
"right now" position, openly held: he explicitly invites anyone who's cracked the
abstraction to correct him. The minimal-agent harnesses he favors embody the
same instinct — Pi ships its own AI SDK designed for provider portability rather
than leaning into any one provider's features ([[malleable-self-extending-agent]]).

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-11-21-agents-are-hard-01c828c6.md — https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-11-22-llm-apis-2d2874b5.md — https://lucumr.pocoo.org/2025/11/22/llm-apis/
