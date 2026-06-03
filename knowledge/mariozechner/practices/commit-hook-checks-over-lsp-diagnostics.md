# Commit Hook Checks Over Lsp Diagnostics

Feeding an agent LSP diagnostics or rich code-exploration output is often unhelpful. It fills the context window with possibly-irrelevant noise, and — crucially — it doesn't reliably get errors fixed: diagnostics are advisory, and an agent can read them and move on without acting.

Far more effective is forcing type checking, linting, and similar gates into a **commit hook**. Now the agent meets a hard, external pass/fail signal it cannot route around: the commit fails, so it is compelled to fix its own errors before proceeding. Correctness enforcement is pushed to a deterministic gate that lives outside the context window, where it can't be argued with, ignored, or buried under unrelated tokens.

The generalizable instinct is to convert advisory information into a binary boundary. Anything you genuinely require — types pass, lint clean, tests green — belongs at a gate that returns yes or no, not in a stream of suggestions the model weighs against everything else competing for attention. This keeps the context lean and the behavior predictable: the agent only sees the gate's verdict, not a wall of diagnostics, and the verdict is unambiguous.

It is the same move as precomputing context rather than letting the agent flail through exploration ([[context-gathering-before-implementation]]): do the deterministic work in a place the model can't fudge, and let it spend its context budget on the actual problem.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-12-22-year-in-review-2025-cbb5c6d1.md — https://mariozechner.at/posts/2025-12-22-year-in-review-2025
