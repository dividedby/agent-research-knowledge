# Patch The Agent Binary

A JavaScript-distributed agent (Claude Code) is patchable like any executable — only easier. The workflow: format the obfuscated/minified bundle with **Biome**, locate the behavior by searching for the literal **strings it prints**, identify the enclosing function by **brace-matching** outward (robust to renamed/minified function names across versions), and replace the offending check with a no-op.

Zechner uses this to **strip anti-debugging** — so the agent can run under a debugger or via the SDK in a debug terminal — and to **re-enable `/cost`** token reporting that was suppressed for Max-plan users. The same string-anchor + brace-match trick removes the "your version is outdated, exiting" guard. When the obfuscated code is unreadable, hand it to the agent itself and let it find the function.

Two engineering points make this reusable rather than a one-off hack. Patches are **version-fragile** — a new release re-minifies everything — so they must be reapplied after each update; package them as a tool with `patch`/`restore` rather than editing by hand. And **string anchors plus brace-matching** are the durable part of the technique: literal printed strings survive minification far better than identifiers, and matching braces locates a whole function without depending on its name.

This is the companion to tracing the agent to understand it — patching changes behavior, tracing reveals it.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-08-06-cc-antidebug-db307f90.md — https://mariozechner.at/posts/2025-08-06-cc-antidebug
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-08-03-cchistory-ada5e53e.md — https://mariozechner.at/posts/2025-08-03-cchistory
