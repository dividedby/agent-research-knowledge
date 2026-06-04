# Hand off the whole job, full permissions, and wait

Ronacher's default operating mode is what's colloquially called YOLO mode:
`claude --dangerously-skip-permissions` (aliased `claude-yolo`). He assigns a
job to an agent that effectively has full permissions, then *waits* for it to
finish, rarely interrupting unless the task is small. He watches it work.

The trade-offs he makes explicit:

- **Risk is real but manageable.** Move the dev env into Docker if you want a
  hard boundary; in practice he finds it works surprisingly well even
  un-dockerized as long as you can watch it. (His verdict on the unsolvable
  security tail: agents already run code and tests, which is "the same kind of
  bad" as `eval()`, so the protections are largely theater — see
  [[code-as-the-mcp-interface]].)
- **The IDE shrinks.** When the agent does the bulk of the work, the IDE's role
  collapses to final edits — to the point that this workflow *revived his Vim
  usage*, an editor with no AI integration at all.
- **Cheap model, full delegation.** He runs the cheaper Sonnet on a $100/mo Max
  plan and prefers its output to Opus; the leverage is in the delegation
  pattern, not the most expensive model.

This delegate-and-wait posture is *why* he never adopted Claude Code's plan
mode: YOLO mode didn't inherit permissions into plan mode, so it nagged for
approval constantly. Instead he plans by iterating with the agent on a file he
controls — see [[plan-via-a-file-on-disk]]. It also pairs with running several
agents at once: parallelization, not single-agent speed, is where throughput
comes from, so long as you can segment shared state (a second checkout, separate
DBs/Redis) — see [[shape-the-codebase-for-local-reasoning]].

The discipline that keeps this from becoming [[slop-loops-and-agent-psychosis]]
is that delegation never transfers accountability — see
[[agent-as-collaborator-you-stay-accountable]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-6-12-agentic-coding-92334255.md — https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-12-17-what-is-plan-mode-c0bb68c8.md — https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/
