# Place prompt-cache points yourself

Anthropic makes you pay for caching and manage cache points *explicitly*.
Ronacher initially found the manual management dumb — why doesn't the platform
do it? — and fully came around: explicit cache control is now strongly
preferred, because it makes cost and cache utilization predictable in a way the
auto-caching platforms (hit-and-miss in his experience) never are.

His concrete placement in an Anthropic-backed agent:

- **One cache point after the system prompt.**
- **Two cache points at the start of the conversation,** the last of which
  *moves up with the tail* of the conversation, plus incremental optimization
  along the way.

A direct design consequence: because the system prompt and tool selection now
have to be **mostly static** to preserve the cache, anything dynamic — the
current time, for instance — is fed in as a *later* message rather than baked
into the system prompt, which would otherwise trash the cache. This static-prefix
constraint is the same one that makes tool loadouts hard to change mid-conversation
and underpins [[skills-over-deferred-tool-loading]].

The control unlocks moves that are hard otherwise: splitting a conversation to
run in two directions simultaneously, and context editing. The catch he's
explicit about: **context editing automatically invalidates caches**, with no
way around it — so it's unclear when the token savings of trimming the context
outweigh the cost of a cache trash. This control is one of the reasons he argues
for [[build-your-own-agent-abstraction]] (caching is much easier targeting
Anthropic's SDK directly) and a worked example of the [[llm-apis-as-state-sync]]
view: a cache point is hidden derived state you're forced to manage by hand.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-11-21-agents-are-hard-01c828c6.md — https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-12-13-skills-vs-mcp-29850730.md — https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/
