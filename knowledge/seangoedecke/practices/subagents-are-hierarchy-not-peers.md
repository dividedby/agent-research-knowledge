# Subagent delegation is hierarchy, not peer coordination

Every current instance of models "working together" — subagents included — is
explicitly hierarchical: an orchestrator dispatches bounded, scoped tasks to
subordinate instances, not a negotiation between equals. There are basically no
current instances of models working together as true peers, let alone
conceiving of each other as the same entity. That's worth naming because it's
not an incidental detail of today's tooling — it's the shape all current agent
research is converging on.

The reason is architectural, not a temporary training gap: every new model
release makes an individual model more agentic *within a single conversation*
(more tool use, longer loops, better judgment about when to stop), not better
at *working with* other model instances as collaborators. Nothing in the
training or product incentives points toward peer coordination — the entire
trajectory is "one smarter conversationalist," stamped out in parallel, not
"many minds negotiating." A country of geniuses in a datacenter, not pieces of
a single mind.

This shows up concretely in how coding-agent harnesses are built: the
orchestrator retains the goal, the plan, and the authority to decide when a
subtask is done; a subagent gets a scoped, one-directional instruction and
reports back — it doesn't get to renegotiate the orchestrator's objective or
treat another subagent's task as partly its own. If you're designing a
multi-agent coding setup and reach for peer-to-peer negotiation between
instances (shared scratchpads where agents bargain, agents empowered to
override each other's priorities), you're building against the grain of how
these systems currently work, not with it — hierarchy isn't a stopgap to
engineer away, it's the load-bearing structure.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-help-peer-1a1983a7.md` — origin: https://seangoedecke.com/help-peer/
