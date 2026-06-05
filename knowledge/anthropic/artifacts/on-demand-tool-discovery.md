# Load tool definitions on demand, not all up front

As agents connect to dozens of MCP servers and hundreds of tools, loading every
tool definition into context up front becomes the bottleneck: 58 tools across five
servers is ~55K tokens before the conversation starts; add Jira (~17K alone) and
you pass 100K; Anthropic saw 134K tokens of tool definitions before optimization.
That overhead raises latency and cost, and — worse — degrades accuracy, because
the most common tool-use failures are wrong-tool selection and bad parameters,
which get harder as similar-named tools pile up.

The fix is **discovery instead of preload**. Provide all tool definitions to the
API but mark the long tail with `defer_loading: true`; the agent initially sees
only a **Tool Search Tool** (regex-, BM25-, or embedding-based) plus your
three-to-five most-used always-loaded tools. When the agent needs a capability it
searches ("github"), and only the matching definitions expand into context. This
cut token usage ~85% while keeping the full library reachable, and lifted MCP-eval
accuracy substantially (Opus 4 49%→74%, Opus 4.5 79.5%→88.1%). Critically it
**preserves prompt caching** — deferred tools are excluded from the initial prompt
entirely, so the cacheable system prompt and core tools are untouched, and the
deferred definitions only appear after a search.

A second discovery mechanism, used when tools are presented as code on a
filesystem, is to let the agent *explore* — list the `servers/` directory, read
only the specific tool files it needs (models are good at navigating
filesystems). Either way the cost is an added search/exploration step before
invocation, so it pays off when the context savings and accuracy gains outweigh
the extra latency — most valuable with large tool libraries, less so with a
handful of always-needed tools. Tool search matches on names and descriptions, so
clear, descriptive definitions are a prerequisite for good discovery.

A companion technique, **Tool Use Examples** (`input_examples`), addresses what
discovery doesn't: JSON Schema says what's structurally valid but can't express
usage patterns — date formats, ID conventions, which optional fields go together,
how nested objects relate to priority. Supplying a few concrete sample calls
teaches these by demonstration, improving complex-parameter accuracy 72%→90% in
internal testing.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-advanced-tool-use-fe2899cf.md` — https://www.anthropic.com/engineering/advanced-tool-use
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-code-execution-with-mcp-4dd2373a.md` — https://www.anthropic.com/engineering/code-execution-with-mcp
