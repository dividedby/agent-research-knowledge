# Don't build separate tools for AI agents — the good human tools are already the good agent tools

Most attempts to build "X, but for AI agents" are a bad bet, because agents
use a computer the same way human engineers do — entering text, making API
calls, reading and viewing images, prioritizing and delegating — and tools
good for one are pound-for-pound good for the other. That's not an intrinsic
fact about how AI has to work (more inhuman agent designs are possible), but
it's true of how today's agents actually work, so redesigning a tool "for
agents" mostly just reproduces the human-shaped tool you started with — a
redesigned Jira ends up looking like Jira.

Two more forces cut against a from-scratch agent-native tool. Existing tools
carry a training-data advantage a new tool has to overcome before its own
design merit even counts: if a new tool is 20% better in the abstract but the
model's existing fluency with the incumbent is worth more than that 20%, the
incumbent still wins. This is why a new programming language "designed for
AI agents" is a hard sell — the model has billions of tokens of embedded
idiom in existing languages that a novel language can't match no matter how
clean its design. And the field doesn't yet know what good agent ergonomics
even look like: plausible-sounding claims (agents prefer statically-typed
languages for the tight feedback loop) have equally plausible counter-stories
(that same language's boilerplate clogs the context window), and the
ergonomics keep shifting under fast-moving capabilities like compaction.

What's actually worth doing is narrower than a redesign: exposing information
in plain text or Markdown, building a functional API, shipping an MCP server
or CLI alongside the UI. These lower the friction for an agent to use a tool
that was already built for humans — "building for AI agents" today mostly
means prioritizing the API over the UI, not changing what the product is. And
that edge may not be durable either: as agents get better at computer use, the
gap between tools-for-AI and tools-for-humans keeps closing.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-dont-build-tools-for-ai-agents-0f45c604.md` — origin: https://seangoedecke.com/dont-build-tools-for-ai-agents/
