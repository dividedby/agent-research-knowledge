# Pick a language the agent reads well

Language choice is an agentic-coding decision, not just a taste decision. The
agent performs dramatically better when the language is (a) well represented in
the model's weights, (b) backed by good build tooling, and (c) low-churn. All
three matter independently: Zig is underrepresented *and* fast-moving (passable
only if you point the agent at docs); Swift is well-represented but its
Mac/iOS build tooling is so painful the agent flounders anyway.

For new backend work Ronacher strongly recommends **Go**, for reasons that are
all really about agent legibility:

- **Explicit context flow.** Go's `context.Context` is a copy-on-write data bag
  that visibly threads through call sites, so the agent always knows how to pass
  state down — no magic.
- **Cached, incremental tests.** `go test` runs straightforwardly and figures
  out what to re-run itself. (In Rust, agents trip over `cargo test` invocation
  syntax; this stalls the loop — see [[shape-the-codebase-for-local-reasoning]].)
- **Deliberate simplicity.** Rob Pike's "for developers not equipped to handle a
  complex language" — substitute "agents." Structural interfaces mean a type
  conforms if it has the methods, with little surprise for the LLM.
- **Low ecosystem churn.** Go and Flask are model favorites *because* they're
  stable; the model is far less likely to emit outdated patterns.

Python, his original choice, is a cautionary contrast: agents struggle with its
magic (pytest fixture injection, wrong-event-loop async), and worse, the *loop
itself* is slow because the agent constantly spawns processes and the
interpreter is slow to boot. Frontend caveats follow the same rule — TanStack's
`$param.tsx` filenames confuse the agent because of shell interpolation.

Crucially, the cost of code is now so low that ecosystem breadth matters less:
Ronacher reaches for TypeScript over Python not because he prefers it but
because the agent does better, and if a library is missing he just has the agent
*port* one from another language. This loosens the historic lock-in and is why
he expects new, deliberately agent-friendly languages to emerge — see
[[design-a-language-for-agents]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-6-12-agentic-coding-92334255.md — https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-2-9-a-language-for-agents-a8f6e8b9.md — https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/
