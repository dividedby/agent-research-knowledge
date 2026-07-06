# A tool schema is not a neutral contract — models have a learned prior for one

Tool-calling is not the model reasoning generally about an abstract JSON
contract; it's a special-token convention the model was RL-trained to reproduce,
and that training happens inside one specific harness. The closer your tool's
schema sits to that harness's canonical shape, the more reliably the model fills
it in; the further away, the more it fights you — and that fight gets *worse*,
not better, as models improve.

Ronacher traced a Pi bug (its edit tool takes a nested `edits[]` array of
`{oldText, newText}` objects) where Opus 4.8 and Sonnet 5 — not older Anthropic
models, not Haiku — kept appending invented extra keys (`requireUnique`, `kind`,
`matchCase`, `oldText2`, even a stray `event.0.additionalProperties`) inside each
edit object, failing validation. The real `oldText`/`newText` payloads were
always byte-correct; only trailing junk was wrong, and it appeared at the single
highest-entropy point in the call — right after closing a long escaped
multi-line string, where the model must decide `}` vs `, "..."`. His diagnosis:
Claude Code's own edit tool is flat (`file_path`, `old_string`, `new_string`,
`replace_all`), and modern Anthropic models are post-trained inside a harness
that looks like Claude Code. They learn not just the happy path but *what
mistakes that harness tolerates* — its client silently repairs malformed calls
(parameter aliases like `old_str`/`path`, Unicode-escape fixes, dropping unknown
keys) rather than hard-failing, so RL reward flows through slightly-malformed
calls too. A model with a stronger, better-trained prior for the dominant
harness's shape fights *harder* against a different one, because it has no
learned name for a nested array's extra optional field and free-samples one.

The fix that actually worked (turning on Anthropic's strict tool-call mode) is
also why the risk is durable: strict mode grammar-constrains the sample so
off-schema keys can't be emitted, but Anthropic caps tool-definition complexity
under strict mode — plausibly the reason Claude Code itself doesn't use strict
mode and instead leans on its permissive repair layer. Compare OpenAI's harmony
format, which puts a `<|constrain|>json` marker in-band so the inference stack
knows exactly when to switch into grammar-constrained sampling for a tool body;
Anthropic's ANTML-style format inlines top-level string params directly but
still requires the model to hand-write escaped JSON for nested array arguments,
which is where the failure concentrates.

The transferable lesson for anyone building a harness with its own tool schema:
you cannot assume a model's Claude-Code-trained tool-calling competence
transfers to your schema unless it's a close match to the dominant harness's
shape. Fighting a strong RL prior with a differently-shaped schema is probably
futile — your real choices are to shape your tools close to the canonical
form, build your own repair/tolerance layer the way Claude Code's client does,
or pay the strict-mode/grammar-constrained-decoding cost and accept its
complexity limits. The more of the field's post-training happens inside one
dominant harness, the more every other harness inherits its quirks by default.

## Sources
- `sources/ronacher/blog/https-lucumr.pocoo.org-2026-7-4-better-models-worse-tools-8622a31a.md` — origin: https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
