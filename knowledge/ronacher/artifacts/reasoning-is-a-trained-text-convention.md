# Reasoning traces are plain text behind a trained channel convention

Reasoning traces aren't a separate computational channel — they're ordinary
text the model is trained to emit into a scratchpad before its final answer,
delimited by special tokens the harness has to parse itself. GPT-OSS's Harmony
format makes the mechanism visible: `<|channel|>analysis<|message|>…<|end|>`
routes to a hidden `analysis` channel, `<|channel|>final<|message|>` routes to
what the user sees. The industry has made this sound exotic; underneath, a
parser is just watching for a marker and redirecting the stream. Any harness
consuming a model that exposes raw reasoning — local/open-weight models
especially, see [[local-models-as-a-first-class-provider]] — has to implement
that routing itself, and a model that skips or mangles the marker becomes a
malformed-reasoning-stream bug in *your* harness, not the provider's problem.

Because it's a learned convention rather than a hard separation, it isn't
fully robust: models can be tricked into leaking reasoning by convincing them
they're already in the final channel, and older models with thinking disabled
have been observed reasoning into a tool call instead (echoing thoughts into a
bash invocation, say) — the model still wants to think, it's just lost its
sanctioned channel to do it in. A custom `think` tool can exploit the same gap
deliberately, but it only works when native reasoning is disabled — with
native reasoning on, the model already has a sanctioned channel and doesn't
reach for the tool.

Reasoning *effort* ("low"/"high", or GPT's "juice") is the same story at the
prompt level: not a sampling parameter, but a literal string trained into the
system prompt (GPT-OSS's is just the line `Reasoning: low`). That's why
flipping the effort level invalidates the KV/prompt cache exactly like any
other system-prompt edit would — see [[manual-prompt-cache-points]] — the
model isn't sampling differently, it's reading a different prompt.

## Sources
- `sources/ronacher/blog/https-lucumr.pocoo.org-2026-8-19-what-is-reasoning-4b81eb57.md` — origin: https://lucumr.pocoo.org/2026/8/19/what-is-reasoning/
