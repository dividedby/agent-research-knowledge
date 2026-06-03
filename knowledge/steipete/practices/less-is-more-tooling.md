# Less Is More Tooling

Tooling around the agent is mostly liability, not leverage. Steinberger removed his last MCP and avoids worktrees, plugins, RAG, and elaborate harnesses — not on minimalist aesthetic grounds but as a productivity strategy. Most of these tools exist to "work around current inefficiencies" in the models, inefficiencies the next model revision will quietly obsolete. Building atop them means maintaining scaffolding with a short shelf life.

Two costs make the case concrete. First, the context tax: every registered tool eats tokens whether or not you use it. GitHub's MCP burns roughly 23k tokens of context just by existing; the gh CLI costs zero and the model already knows how to drive it. Second, indirection that hides the terminal reduces visibility and steering control — and visibility is what actually drives results, because you cannot correct a loop you cannot see ([[stay-in-the-loop-active-steering]]).

So bet on the raw model plus the thinnest possible surface: a terminal and the CLI, nothing between. The fewer layers, the more directly the model's improving capability reaches your problem, and the less you have to rip out later. This is the tooling-side mirror of [[just-talk-to-it-minimal-prompting]] — strip prompt scaffolding and tool scaffolding for the same reason — and it leads directly into [[cli-over-mcp]], the specific form the principle takes when you have to expose a capability to the agent at all.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
