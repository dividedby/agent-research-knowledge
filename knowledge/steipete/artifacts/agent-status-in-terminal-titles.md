# Agent Status In Terminal Titles

When orchestrating a fleet ([[parallel-agent-fleet-on-main]]), the binding constraint stops being model capability and becomes *knowing which agent is doing what*. Six tabs all reading "claude" is terminal roulette — and it turns dangerous under skip-permissions, where guessing wrong means approving the wrong agent's action.

The solution evolved through a telling failure. The first attempt was a wrapper that force-reset each terminal's title in a background loop, but the agent kept overwriting it — the wrapper and the agent fought for the title, and the agent won. The fix was to invert ownership: have the agent *self-report*. Instruct it in the global agent file to call a title command — formatted as "current action — context" — whenever it starts a task, switches focus, or hits a long-running operation.

Self-reporting beats forced titles because the agent knows its own state and updates the title with real semantic content: PR numbers, file names, the actual thing it's doing. No external watcher can synthesize that. Surfacing the initial topic, session ID, and elapsed time in the status line further aids recovery when you're juggling many agents, and doubles as a self-regulation signal — an agent that has to name its current action stays oriented.

The terminal title and status line together become the orchestration dashboard for a parallel fleet: a glanceable map of who's doing what. It's the read-side complement to [[remote-terminal-supervision]]'s intervene-side, and another expression of [[stay-in-the-loop-active-steering]] at fleet scale.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-commanding-your-claude-code-arm-288d80f0.md — https://steipete.me/posts/2025/commanding-your-claude-code-army/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-command-your-claude-code-army-reload-942bf3f0.md — https://steipete.me/posts/command-your-claude-code-army-reloaded/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-optimal-ai-development-workflow-3f7be26f.md — https://steipete.me/posts/2025/optimal-ai-development-workflow/
