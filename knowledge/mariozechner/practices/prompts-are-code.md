# Prompts Are Code

Treat an LLM not as a chat partner but as an extremely slow, unreliable computer
you program in natural language. The classic computing model maps directly: the
prompt is the program — sequential steps, loops, conditionals, even goto — its
inputs come from prepared docs, user clarifications, and tool outputs, tools are
imported library functions, and tool calls are I/O. This reframe matters because
developers already think in inputs–state–outputs and abstractions; the fuzziness
of natural language tricks them into "just hoping for the best" instead of
engineering.

Two disciplines follow. First, **pre-compute context deterministically** with a
real script rather than letting the agent explore. Zechner's porting plan runs
`git diff`, LSP type extraction, and dependency ordering *before* the LLM starts —
exploration is non-deterministic, burns tokens, and may miss files. Second, **bake
exact, tested commands into the prompt** as a vetted standard library: `jq`
progress queries, compile commands the model can invoke verbatim. Pair these with
defensive negative instructions ("for other languages we cannot compile
individual files and should not try") to stop the non-deterministic executor from
wasting turns chasing dead ends.

State lives on disk, not in the conversation ([[prompts-are-code-state-on-disk]]),
and human STOP-and-confirm checkpoints gate each step so a wrong turn is caught
before it compounds. The throughline: stop anthropomorphizing the model and start
programming it — with the same care you'd give any flaky, expensive runtime.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-06-02-prompts-are-code-c112d6f9.md — https://mariozechner.at/posts/2025-06-02-prompts-are-code
