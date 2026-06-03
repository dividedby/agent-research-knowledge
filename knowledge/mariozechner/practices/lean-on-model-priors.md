# Lean On Model Priors

The most token-efficient tool surface exploits what the model already knows. Rather than wrapping a domain in many bespoke tool descriptions, expose a thin "execute code" primitive and let the model write standard code against APIs it learned in training.

Zechner's browser tools are four tiny Node/Puppeteer CLIs — start, nav, eval, screenshot. The `eval` tool simply runs the model's JavaScript in the page's DOM context, so the model uses the DOM API it already knows instead of a custom interface invented for the occasion. The whole README is ~225 tokens, versus 13–18k for browser MCPs that spell out a custom tool per capability. The model's priors do the work the documentation would otherwise have to.

The same instinct shapes `pi`'s sub-1000-token system prompt — models already know what a coding agent is, so there's no need to re-explain it — and a screenshot tool that returns a file path the agent reads back with its own vision rather than a bespoke image-handling protocol.

The principle: conserve context by relying on the model's priors, and only define a custom API when the native one genuinely can't serve. Every custom interface you invent is documentation the model must load and reconcile against what it already knows; a thin execute primitive over a familiar API costs almost nothing and inherits the model's full training-time fluency. Prefer the surface the model has already seen ten thousand times to the one you'd have to teach it. See [[four-tool-coding-agent-core]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-02-what-if-you-dont-need-ab16af09.md — https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
