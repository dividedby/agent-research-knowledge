# Just-in-time context: load references, not data

Rather than pre-loading all potentially relevant data into the context window up
front (the embedding-based pre-inference retrieval pattern), let the agent hold
**lightweight identifiers** — file paths, stored queries, web links — and
dynamically pull the actual data in at runtime using tools. This mirrors human
cognition: we don't memorize a corpus, we keep an index (file systems, inboxes,
bookmarks) and retrieve on demand.

The payoff is more than storage efficiency. A reference carries **metadata that
is itself a signal**: a file named `test_utils.py` in `tests/` implies a
different purpose than the same name in `src/core_logic/`. Folder hierarchies,
naming conventions, file sizes, and timestamps all let the agent infer how and
when to use information before it ever reads the contents. This enables
**progressive disclosure** — the agent assembles understanding layer by layer
through exploration, keeping only what's needed in working memory and discovering
the next-relevant context as each step informs the next.

Claude Code is the worked example: `CLAUDE.md` is dropped in up front (cheap,
always-relevant), while `glob`/`grep`/`head`/`tail` let it navigate and retrieve
files just-in-time — sidestepping stale indexes and complex syntax trees, and
querying large databases without ever loading full objects into context.

The trade-off is real: runtime exploration is slower than pre-computed retrieval,
and a poorly-equipped agent can waste context chasing dead-ends. So the most
effective agents often go **hybrid** — retrieve a little up front for speed,
explore autonomously for the rest. The right boundary depends on the task
(more static domains like legal/finance tolerate more up-front retrieval), and
as models get smarter the trend is toward less human curation and more
autonomous navigation.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-effective-context-engine-42516bb9.md` — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
