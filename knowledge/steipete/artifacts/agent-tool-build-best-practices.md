# Agent Tool Build Best Practices

Design tools for the agent as caller, not for a precise human operator. The constraints are different: the caller can't ask you what went wrong, can't read a man page mid-task, and pays tokens for every byte of description and every failed retry.

Keep the tool surface small and each tool powerful. Agents degrade past roughly forty tools, and every tool description permanently occupies context, so consolidate rather than proliferate — the [[less-is-more-tooling]] principle applied at the API boundary.

Parse input leniently — Postel's law for agents. Advertise a strict schema, but accept parameter aliases, case-insensitive, partial, and fuzzy matches, and infer intent rather than rejecting malformed input. Every rejection is a wasted, token-burning round-trip; meeting the agent halfway is cheaper than a clean error.

Make tools self-describing and recoverable. Every parameter carries a description with its default and whether it's required. The tool reports its own version and offers a health or `doctor` subcommand. Misconfiguration surfaces a corrective message that tells the caller how to fix it, instead of crashing — because the caller has no human to consult.

Keep stdout and stderr clean: log to files only. Stray output corrupts the JSON-RPC channel that MCP rides on, and a single rogue print can break the whole session.

Finally, offload bulky or specialized work to a sub-model and return only the distilled answer, keeping the primary agent's context lean. These rules underpin [[native-core-thin-distribution-wrapper]] and the helpers in [[close-the-loop-with-purpose-built-tools]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-mcp-best-practices-500319cb.md — https://steipete.me/posts/2025/mcp-best-practices/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-peekaboo-mcp-lightning-fast-mac-9aac2401.md — https://steipete.me/posts/2025/peekaboo-mcp-lightning-fast-macos-screenshots-for-ai-agents/
