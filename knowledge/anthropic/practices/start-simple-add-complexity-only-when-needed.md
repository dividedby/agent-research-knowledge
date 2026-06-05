# Start simple; add complexity only when it demonstrably helps

The most consistent piece of Anthropic's agent advice, and the one the rest of
the corpus reacts to: find the simplest solution that works, and increase
complexity only when it measurably improves outcomes. For many applications that
means not building an agentic system at all — a single optimized LLM call with
retrieval and good in-context examples is often enough. Agentic systems trade
latency and cost for task performance; spend that only when the trade pays.

This ranks the design space. Plain prompting < workflows (predictable, fixed
paths for well-defined tasks) < autonomous agents (LLMs using tools in a loop,
for open-ended problems where you can't hardcode the path). Reach for the
rightmost option only when the leftmost demonstrably falls short. Frameworks are
fine to get started, but they add abstraction that obscures the underlying
prompts and responses and tempts premature complexity — prefer calling the LLM
API directly, and if you use a framework, understand what's under the hood.

The principle has teeth for *harness maintenance*, not just initial design.
**Every component in a harness encodes an assumption about what the model can't
do on its own** — and those assumptions go stale as models improve. The
discipline is to stress-test them: remove one component at a time and measure the
impact. Anthropic's own long-running harness needed context resets to fight
Sonnet 4.5's "context anxiety"; on Opus 4.5 that behavior vanished and the resets
became dead weight. The sprint-decomposition scaffold that Opus 4.5 required was
dropped for Opus 4.6, which sustained two-hour coherent builds unaided. When a
new model lands, re-examine the harness: strip what's no longer load-bearing,
add what newly-unlocked capability makes possible. The space of useful harness
designs doesn't shrink as models improve — it *moves*.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-building-effective-agent-7d24e5fa.md` — https://www.anthropic.com/engineering/building-effective-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-harness-design-long-runn-2ef732b7.md` — https://www.anthropic.com/engineering/harness-design-long-running-apps
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-managed-agents-f90fa6ca.md` — https://www.anthropic.com/engineering/managed-agents
