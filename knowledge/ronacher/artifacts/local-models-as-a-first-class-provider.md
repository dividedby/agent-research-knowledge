# Local models: pick one winner and polish the whole stack end-to-end

The gap that keeps local models out of coding agents is not model quality or
task complexity — it's that the stack is fragmented and *unfinished*. A hosted
provider is "paste a key and stop thinking about tokens"; running locally means
choosing an inference engine, model, quantization, chat template, context size,
and a pile of JSON configs across layers (llama.cpp, Ollama, LM Studio, MLX,
vLLM…), any one of which can quietly make the model worse or break it. The result
is people get an experience that's neither a fair evaluation of the model nor a
polished product, and effort scatters across too many half-working efforts.

Ronacher's diagnosis sharpens this into a harness-design principle. **"Making a
model runnable is not the same as making it feel finished."** His canonical
example is *tool parameter streaming*: most local stacks don't stream tool-call
arguments (only the final text), even though the completions API supports it. The
consequences are concrete and agent-specific — a slow local model that emits
nothing for five minutes is indistinguishable from a dead connection (so
inactivity timeouts become useless); you can't see the bash invocation being
assembled, so you can't interrupt it before tokens are wasted. "Tool parameter
streaming is as important as token streaming." Treat every such gap — malformed
reasoning stream, wrong tool-call format, a context window that isn't really
real, KV caches that don't work for a coding agent — as a **product bug to fix
no matter where in the stack it lives**, the way a hosted provider would.

The prescription is anti-generality: don't try to support every model. **Pick
one winner and polish it.** This is why Ronacher backs `ds4.c` (Salvatore
Sanfilippo's deliberately narrow native engine for DeepSeek V4 Flash on 128GB+
Macs — model-specific loading, Metal path, prompt rendering, KV handling, server
glue, tests; not a generic GGUF runner) and built **`pi-ds4`**, a Pi extension
making it a first-class provider: it registers `ds4/deepseek-v4-flash`, compiles
and starts `ds4-server` on demand, downloads/builds the runtime, picks the
quantization from the machine, holds a lease while Pi uses it, exposes logs, and
shuts down via a watchdog when idle. It deliberately exposes *no knobs* yet —
the goal is to set them automatically. The aim isn't to hide that local
inference is complex; it's to **put the complexity in one place** inside the
harness where it can be improved, then carry the learnings to the next
config — the same own-the-abstraction instinct as
[[build-your-own-agent-abstraction]] and [[malleable-self-extending-agent]],
applied to the inference layer so experimentation isn't locked behind a
hyperscaler subscription.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-5-8-local-models-7fee3c7e.md — https://lucumr.pocoo.org/2026/5/8/local-models/
