# Know The Limits Of Current Agents

Honest engineering with agents means naming what they reliably fail at and designing around it — not over-trusting benchmarks. Three limits matter most.

First, LLMs can't follow execution flow much beyond a sequential script. The moment you have multiple processes, IPC, client-server boundaries, or concurrency, they lose the thread. Second, they lack taste: hand them an open design problem and they regress to the mean "best-practices" over-engineered solution ([[agents-are-merchants-of-complexity]]). Third, their *effective* context degrades around 100k tokens regardless of the advertised window — the big number on the box is not the number you get.

The consequence is a division of labor. Automate the mechanical, verifiable parts: faithful line-by-line porting, getters and setters, transferring documentation, anything where correctness is checkable by eye. Reserve human judgment for what genuinely needs a brain — translating Java generics into C++ templates, navigating idiomatic differences between languages, the decisions where there is a *right* answer that only understanding produces.

The throughline is that you cannot delegate context management to the model. Its effective window is smaller than advertised and it has no instinct for what to load. So you design the context deliberately — curate what goes in, structure it, treat it as an engineering artifact rather than a chat history. That is the discipline of [[prompts-are-code]]: the prompt and its context are inputs you author, version, and own, precisely because the model won't manage them for you.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-06-02-prompts-are-code-c112d6f9.md — https://mariozechner.at/posts/2025-06-02-prompts-are-code
