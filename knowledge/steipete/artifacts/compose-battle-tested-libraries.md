# Compose Battle-Tested Libraries

Don't rebuild solved infrastructure — wire proven libraries together and let the agent handle the glue. The hard parts of most "simple" features are exactly where rolling your own costs weeks for a worse result.

Demark gets robust HTML-to-Markdown conversion by running a mature JS library (Turndown.js) inside a WKWebView for *real* DOM parsing, rather than hand-writing a parser that chokes on malformed HTML. VibeTunnel reached a full browser terminal in roughly a day by adopting Xterm.js — after two hours of a hand-rolled ANSI renderer ran into an endless wall of escape-sequence edge cases. ANSI sequences and malformed markup are the canonical traps: they look tractable, then bleed weeks into edge cases that mature libraries already handle.

Agents shift the build-versus-reuse line decisively toward reuse. The integration glue — the wiring, adapters, and plumbing between components — is precisely the cheap part now. So the skill becomes *selection and assembly*: pick the right components and let the agent stitch them together, instead of treating "use a library" as a fallback for when you can't write it yourself.

This also matches where agents are strongest: bootstrapping. An agent can get you roughly eighty percent into an unfamiliar library in minutes — far faster than reading the docs cold. The remaining work is human: a skilled engineer tests the integration, finds the edge cases the agent glossed over, and refactors the glue into something durable.

This is the build-vs-reuse counterpart to [[native-core-thin-distribution-wrapper]] — there you write the core, here you wrap someone else's — and it feeds [[close-the-loop-with-purpose-built-tools]], where assembled components become the agent's helpers.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-introducing-demark-html-to-mark-df97848b.md — https://steipete.me/posts/2025/introducing-demark-html-to-markdown-in-swift/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-vibetunnel-turn-any-browser-int-d1bfe9ac.md — https://steipete.me/posts/2025/vibetunnel-turn-any-browser-into-your-mac-terminal/
