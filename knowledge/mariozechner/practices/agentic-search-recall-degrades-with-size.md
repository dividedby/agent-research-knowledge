# Agentic Search Recall Degrades With Size

Before an agent can change or reuse code, it must first *find* all the relevant code. Call this agentic search, and treat it as the precondition for everything else the agent does. If the find step is incomplete, every downstream edit inherits the gap.

Here is the uncomfortable property: regardless of mechanism — ripgrep driven through bash, an LSP server, a vector database, a codebase index — the bigger the codebase, the lower the recall. No retrieval trick escapes this. And it is more fundamental than context-window limits: even with infinite context you still have to *locate* the right code before you can load it, and locating is where the misses happen.

Low recall is the root cause of the duplication-and-inconsistency booboos ([[agents-are-merchants-of-complexity]]). The agent doesn't deliberately reinvent the wheel — it simply never sees the existing wheel. It searches, misses the helper that already does the job, and writes a second one. Scale the codebase and the miss rate climbs, so the duplication compounds exactly where the system is largest and least forgiving.

What actually fixes recall is a human who understands the codebase. That person steers the agent straight to the relevant code, supplies the names and paths the search would have missed, and as a result sharply reduces the massaging the agent's output needs afterward. The expensive part of agent work is cleaning up after low recall; investing your own understanding up front is what avoids paying it. This is one more reason the human must hold the global view rather than delegate it.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-03-25-thoughts-on-slowing-t-e9b43800.md — https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down
