# Practices — mariozechner

How Mario Zechner approaches building and working with coding agents, from the
builder-of-the-harness side: empirical design notes on agent tool-harness
construction — a minimal read/write/edit/bash core, the extension model over
baked-in features, and the MCP-vs-CLI tooling trade-off — plus a hype-free read
on what current agents can and can't be trusted to do. One concept per file;
this index lists them, one line each.

- [stay-in-the-loop-not-agent-armies](./stay-in-the-loop-not-agent-armies.md) — the human is a feature: a natural rate-limiter on compounding "booboos"; agent-army autonomy removes that bottleneck and you feel the pain too late.
- [nobody-has-cracked-agentic-coding](./nobody-has-cracked-agentic-coding.md) — after a year of daily use nobody knows how to do this properly; distrust anyone selling "the solution", and hold all workflow advice (including your own) loosely.
- [observability-is-the-feature](./observability-is-the-feature.md) — being able to inspect and intervene mid-stream is the point; reject opaque sub-agents, hidden context injection, and black-box background processes.
- [minimal-harness-by-subtraction](./minimal-harness-by-subtraction.md) — build the harness by subtraction: every feature must earn its place with a real need, because creature-comfort features add tracked state and hidden behavior.
- [mcp-vs-cli-tool-design-decides](./mcp-vs-cli-tool-design-decides.md) — empirically MCP-vs-CLI barely matters; token-efficient output and clear example-rich docs decide outcomes, and CLI's composability/Haiku-scan economics tip the edge.
- [context-gathering-before-implementation](./context-gathering-before-implementation.md) — gather context first in an observable session, distill to an artifact, then seed a fresh implementation session; mid-session sub-agents are a black box within a black box.
- [prompts-are-code](./prompts-are-code.md) — program the LLM like a slow unreliable computer: prompt = program, pre-compute context deterministically, bake tested commands and negative guards into the prompt.
- [trace-the-agent-to-understand-it](./trace-the-agent-to-understand-it.md) — monkeypatch fetch to read what a closed agent actually sends, and diff system prompts across versions; behavior changes are usually prompt/tool edits, not the model.
- [keep-canonical-state-on-your-side](./keep-canonical-state-on-your-side.md) — own the full session log; treat provider-hidden state as opaque derived scratchpad, and self-manage execution environments so their state lives in your log.
- [yolo-by-default-sandbox-theater](./yolo-by-default-sandbox-theater.md) — permission prompts are theater once an agent can write and run code; make the threat model explicit and isolate with a container instead of pretending guardrails work.
- [commit-hook-checks-over-lsp-diagnostics](./commit-hook-checks-over-lsp-diagnostics.md) — force type/lint gates as a commit hook so the agent must fix its own errors, rather than flooding context with advisory diagnostics it may ignore.
- [lean-on-model-priors](./lean-on-model-priors.md) — expose a thin execute-code primitive and let the model write standard code against APIs it already knows; a ~225-token README beats a 13–18k-token MCP.
- [agents-are-merchants-of-complexity](./agents-are-merchants-of-complexity.md) — agents reproduce cargo-cult complexity and decide locally (blind to the whole codebase), so write the system-defining architecture and APIs by hand.
- [know-the-limits-of-current-agents](./know-the-limits-of-current-agents.md) — name what agents reliably fail at (non-sequential flow, taste, ~100k effective context) and split labor: mechanical to the agent, judgment to the human.
- [agentic-search-recall-degrades-with-size](./agentic-search-recall-degrades-with-size.md) — finding all relevant code is the prerequisite to changing it, and recall falls as the codebase grows — the root cause of duplication, fixed by a human who knows the code.
- [evaluation-functions-optimize-what-they-measure](./evaluation-functions-optimize-what-they-measure.md) — agent self-optimization improves only the one metric you hand it, ignoring quality/correctness; harvest the ideas, implement properly.
- [agents-for-domain-experts-on-good-tasks](./agents-for-domain-experts-on-good-tasks.md) — agents are effective for an expert who can verify stage outputs, on scoped, loop-closable, non-mission-critical tasks; structure work as inspectable file-in/file-out pipelines.
- [manual-testing-only-trustworthy-oracle](./manual-testing-only-trustworthy-oracle.md) — agent-written tests inherit the same blind spots as the agent code, so a human manually testing the product is the only reliable final quality gate.
- [friction-builds-understanding-and-taste](./friction-builds-understanding-and-taste.md) — writing the system-defining parts by hand is friction on purpose: it's where understanding, taste, and retained agency come from, which models can't replace.
- [vibe-code-then-refactor-by-hand](./vibe-code-then-refactor-by-hand.md) — fully vibe-code the prototype to prove the concept, then refactor by hand for the structure and maintainability the statistical-mean output won't give you.
- [contributor-trust-bottleneck](./contributor-trust-bottleneck.md) — popular OSS draws a firehose of agent-generated PRs; throttle merges into dedicated review time and loosen only as individuals earn trust.
