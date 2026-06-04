# Shape the codebase so the agent can reason locally

Agents work from a handful of files in context with little spatial awareness of
the codebase; they lean on grep to find things. So the codebase itself is a
tool, and you shape it for *local reasoning* — everything the agent needs to
understand a change should be visible near where it's working, findable with the
dumbest possible tools.

Ronacher's concrete rules, distilled from building a >90%-AI service and from
analyzing what makes agents iterate fewer times:

- **Dumbest thing that works.** Simple code beats clever code in agentic
  contexts. Prefer functions with long descriptive names over classes; avoid
  inheritance and clever hacks.
- **Plain SQL, not ORM.** You get excellent SQL out of agents, and they can
  match the SQL they wrote against the SQL in the logs — a debuggability you
  lose with an ORM. He now uses raw SQL even for migrations.
- **Keep important checks local and visible.** Permission checks must live where
  the agent can see them, in the route. Hiding them in another file or a config
  "will almost guarantee" the agent forgets them when adding new routes.
- **Greppability over indirection.** A one-to-one mapping from where a symbol is
  declared to where it's imported is great; barrel files, free re-exports, and
  especially *import aliases* break it (Go's forced package-name prefixes,
  e.g. `context.Context`, are the model). Agents will even complain about
  aliases in their thinking blocks.
- **Favor code generation over dependencies.** Agents love to pull in
  dependencies (often outdated) and swallow errors; he prefers writing the code
  and crashing loudly over opaque dependencies. Be *more* conservative about
  upgrades than before — cheap AI upgrades tempt you to break the breadcrumb
  comments explaining why a path was chosen.
- **Prefer the OpenAPI-first / canonical-spec shape** so client and server are
  both generated from one source the agent can read.

Two timing rules close it out. **Refactor at the right moment** — not too early,
not too late: agents handle a codebase until total complexity exceeds a
threshold (a tailwind class-mess across 50 files makes redesigns regress), at
which point you must tell it to extract a component library. And **parallelize**
— throughput comes from running several agents, not from one being fast, so
segment shared state (a second checkout, separate DBs/Redis) to make that safe;
this is the structural enabler for [[yolo-mode-delegate-and-wait]].

A deep believer's tension Ronacher flags for future languages: implicit
context-flow (async locals) is great for both humans and agents *until* a flowed
value isn't configured — see [[design-a-language-for-agents]] for his proposed
effect-marker fix. Stable, low-churn ecosystems are the codebase-level twin of
[[pick-an-agent-legible-language]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-6-12-agentic-coding-92334255.md — https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-9-29-90-percent-fa7af1a5.md — https://lucumr.pocoo.org/2025/9/29/90-percent/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-2-9-a-language-for-agents-a8f6e8b9.md — https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/
