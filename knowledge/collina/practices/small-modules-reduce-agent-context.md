# Small modules reduce what an agent needs to hold in context

Keeping interfaces small and narrowly scoped isn't just a human-readability
convention — it directly reduces how much context a coding agent needs to
hold to work correctly. npm's ecosystem of many small, single-purpose
modules locks most implementation complexity inside each module's boundary,
so an agent assembling functionality only has to reason about a package's
public API surface, not its internals. That's the trade-off that makes
AI-assisted development and the "small modules" culture of npm fit together
so well at ecosystem scale: the AI can reason about tiny, well-scoped APIs
and assemble them swiftly instead of holding a large system's internals in
its head.

The same logic applies inside a single codebase, not just across package
boundaries: module boundaries that hide complexity behind small, well-named
APIs are cheaper for an agent to work with than large, tangled files, because
the agent's context window — not its raw capability — is the actual
constraint being economized. Designing for small, legible interfaces pays
off for agent-assisted work the same way it always has for human
maintainers.

## Sources

- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-nodejs-easy-to-learn-h-2fc23ee1.md` — origin: https://adventures.nodeland.dev/archive/nodejs-easy-to-learn-hard-to-master-perfect-for-ai/
