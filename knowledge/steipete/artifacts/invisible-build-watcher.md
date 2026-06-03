# Invisible Build Watcher

Loop iteration speed is the dominant variable in agentic engineering, so the highest-leverage tooling attacks build latency directly. Agents frequently forget to rebuild before testing and then waste an entire session debugging code they already fixed — chasing a stale binary. A background file-watcher (Poltergeist) that rebuilds on every save means a fresh binary is always waiting by the time the agent gets around to testing, eliminating the whole class of "already-fixed" debugging.

Two design properties make this work. First, the tool is *invisible*: it auto-detects the project and fades into the background, so it doesn't add a step the agent (or you) has to remember — the moment a rebuild becomes something to invoke, it gets skipped. Second, it's *agent-aware*: it detects whether a human or an agent invoked it and steers the agent toward correct usage inline, rather than polluting the rules file with yet another instruction the model may ignore. Guidance delivered at the point of use beats guidance buried in [[agent-file-as-organizational-scar-tissue]].

The payoff scales with compile time: it's largest on slow compilers, where a forgotten rebuild costs the most. This is also why fast-iterating stacks are chosen in the first place — keeping the loop tight is a deliberate architectural decision, not an accident of language taste.

This is a concrete case of [[engineer-the-codebase-for-agents]]: shape the environment so the agent's natural behavior produces correct, fast feedback. It closes the rebuild loop the same way [[close-the-loop-with-purpose-built-tools]] closes the others.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-poltergeist-ghost-keeps-builds--36395e11.md — https://steipete.me/posts/2025/poltergeist-ghost-keeps-builds-fresh/
