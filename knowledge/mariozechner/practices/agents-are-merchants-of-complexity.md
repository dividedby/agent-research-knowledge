# Agents Are Merchants Of Complexity

Agents are *merchants of complexity*. Trained on a sea of bad architectural decisions and cargo-cult "best practices," they reproduce that complexity the moment you let them architect — regressing to an over-engineered statistical-mean solution that has no taste. Left to design, they reach for the abstraction, the indirection, the pattern, because that is what the training distribution rewards.

The deeper problem is that every agent's decisions are inherently *local*. An agent never sees the other agents' runs, the full codebase, or the prior decisions that shaped the system. So it duplicates code, invents abstractions for abstraction's sake, and quietly seeds inconsistencies. Each run is locally plausible and globally corrosive.

This compounds. You arrive at the same unrecoverable mess as a human enterprise codebase — except reached in weeks instead of years, and without the organizational scar tissue that slowly evolved to cope with it. The mess lands all at once, with no team that understands how it got there.

The remedy is to hold the global view in a human head. Anything that defines the *gestalt* of the system — its architecture, its APIs, the seams between modules — should be written by hand. Hand off the mechanical fill-in, never the shape of the whole. The friction of writing those parts yourself is not waste; it is how you keep taste and a coherent mental model of the system ([[friction-builds-understanding-and-taste]]). The local blindness behind the duplication is itself rooted in poor recall — see [[agentic-search-recall-degrades-with-size]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-03-25-thoughts-on-slowing-t-e9b43800.md — https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down
