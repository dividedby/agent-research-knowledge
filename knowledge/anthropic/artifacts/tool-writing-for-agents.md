# Write tools for agents, not for developers

A tool is a new kind of software: a contract between a deterministic system and a
*non-deterministic* agent. Unlike `getWeather("NYC")` called by code, an agent
might call the right tool, answer from memory, ask a clarifying question, or
misuse the tool entirely. So tools must be *designed for agents* — give the
agent-computer interface (ACI) as much engineering attention as you'd give a
human-computer interface. A recurring mistake is thin wrappers that merely expose
existing API endpoints, because agents have different "affordances" than code.

The guiding principles:

- **Build a few high-impact tools, not many thin ones.** More tools isn't better;
  bloated or overlapping tool sets create ambiguous decision points. The test: if
  a human engineer can't say definitively which tool to use in a situation,
  neither can the agent. Target specific high-impact workflows that mirror your
  eval tasks.
- **Consolidate to match how the agent thinks.** Because agent context is scarce
  while computer memory is cheap, a tool should do the agent's work *for* it
  rather than return raw data to sift token-by-token. Prefer `search_contacts`
  over `list_contacts`; collapse `list_users`+`list_events`+`create_event` into a
  `schedule_event`; return a `get_customer_context` instead of three lookups.
  This offloads computation from the agent's context back into the tool call.
- **Namespace to disambiguate.** Group related tools under common prefixes
  (`asana_search`, `jira_search`) so the agent picks correctly among many; prefix
  vs. suffix has measurable, model-dependent effects — choose by eval.
- **Return high-signal, agent-legible content.** Drop low-level identifiers
  (`uuid`, `mime_type`, `256px_image_url`) in favor of `name`, `file_type`,
  `image_url`. Resolving cryptic UUIDs to semantic names (or 0-indexed IDs)
  measurably cuts hallucination. Offer a `response_format` enum
  (`concise`/`detailed`) so the agent controls verbosity.
- **Budget the token cost of responses.** Implement pagination, filtering, range
  selection, truncation with sensible defaults (Claude Code caps tool responses
  at 25,000 tokens). When truncating, *steer* the agent toward token-efficient
  strategies, and make error responses actionable prompts ("try a narrower
  search") rather than opaque tracebacks.
- **Prompt-engineer the descriptions and specs.** These load into context and
  steer behavior, so write them like onboarding a new hire: make implicit context
  explicit, name parameters unambiguously (`user_id` not `user`), enforce with
  strict data models. Choosing the right format also matters — diffs demand
  knowing chunk line counts up front; code-in-JSON needs escaping that code-in-
  Markdown doesn't; pick what's easy for the model to *write*, and let absolute
  filepaths replace relative ones to avoid whole classes of error.

Response *structure* (XML vs JSON vs Markdown) affects performance too — models
favor formats matching their training data — so there's no one-size-fits-all;
select it by eval.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-writing-tools-for-agents-4f67b063.md` — https://www.anthropic.com/engineering/writing-tools-for-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-building-effective-agent-7d24e5fa.md` — https://www.anthropic.com/engineering/building-effective-agents
