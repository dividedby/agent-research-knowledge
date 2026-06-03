# Prompts Are Code State On Disk

Context is **ephemeral** — it will be wiped by compaction or blown past ~100k tokens — so never treat the conversation as durable state. Serialize program state to disk in **LLM-friendly formats**: JSON for structured data the model surgically reads and updates with `jq`, Markdown for smaller unstructured data loaded whole.

The payoff is **resumability**. You can resume from any point with a fresh context, sidestepping context degradation, and a single state field (e.g. `portingState: pending | done`) lets a workflow pick up exactly where it stopped across sessions. The prompt file (`port.md`) is the **versioned program**; the JSON/MD files are the **mutable state** it reads and writes.

Plans and task lists belong in **version-controlled files** the agent reads and edits (`PLAN.md`, `TODO.md` with checkboxes), **not** in built-in plan/to-do modes. File-based state is visible, user-editable, shareable across fresh sessions, and survives as a reusable artifact; internal to-do state is one more thing the model must track and that no one else can see or fix.

A **discovered-conventions** file plus a running **"notes" scratchpad** (accumulating edge cases as they're hit) gets fed back into every later unit of work, so the agent doesn't relearn or re-violate them. This is the storage half of [[prompts-are-code]] — the prompt is the program, the disk holds the state, and together they make long workflows restartable instead of fragile.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-06-02-prompts-are-code-c112d6f9.md — https://mariozechner.at/posts/2025-06-02-prompts-are-code
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
