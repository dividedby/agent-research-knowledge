# Human-in-the-Loop Escalation

Autonomous agents periodically hit decisions they should not make alone —
ambiguous requirements, design approvals, security calls. Beads gives this its
own first-class channel rather than letting agents either guess or stall: an
issue labeled `human` is a request for human input, and a small command surface
turns "an agent needs a person" into trackable, queryable work.

## A label becomes a queue

The escalation primitive is just the ordinary issue model with a `human` label —
no new entity. The `bd human` command family treats those labeled beads as a
work queue aimed at people:

- `bd human list` — the inbox of issues awaiting human intervention (filterable
  by status).
- `bd human respond <id> --response "…"` — the resolution path: records the
  human's answer as a comment and closes the issue with reason "Responded", so
  the agent that filed it can read the decision and proceed.
- `bd human dismiss <id>` — close without answering (reason "Dismissed") when the
  question is moot.
- `bd human stats` — counts pending / responded / dismissed, making the human's
  backlog measurable like any other queue.

Because a response is a comment plus a close, the decision lands *on the bead the
agent is blocked on* — the answer travels back through the same graph the
question came from, with full provenance.

## Two faces of the same word: an inbox and an audience filter

`bd human` (no subcommand) does something different and telling: it prints a
focused ~15-command menu for *human operators*, explicitly because bd has 70+
commands "many for AI agents, integrations, and advanced workflows." The tool
knows most of its surface area is for agents, and deliberately carves out a small
human-facing slice. The same word names both the escalation queue and the
audience-narrowed help — a consistent stance that humans and agents are distinct
users of the system, each given a tailored, minimal surface.

This pairs with the gate model: a `human`-type gate blocks workflow on a manual
decision, while the `human` label/queue is how that pending decision is surfaced,
answered, and closed. Together they make "wait for a person" a structured,
auditable state rather than a stalled agent.

## Sources

- `sources/steveyegge/beads/docs-CLI_REFERENCE.md-3efcf9fe.md` (lines 3226-3318, `bd human` and subcommands; lines 149-153, TOC) — origin: https://github.com/steveyegge/beads/blob/848d0d7b6c933a00bd3d06a9a7c2de4368a2a8db/docs/CLI_REFERENCE.md
