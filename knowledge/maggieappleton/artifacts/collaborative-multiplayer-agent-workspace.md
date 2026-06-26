# Collaborative multiplayer agent workspace (Ace)

Ace is a GitHub Next research prototype: a realtime, multiplayer coding-agent
workspace — "like Slack, GitHub, and Claude/Copilot had a baby." Its design is a
direct answer to the thesis that single-player agent tooling optimises the wrong
thing and that team alignment is the real bottleneck (see
practices/alignment-is-the-team-bottleneck). The build decisions, as artifact
shapes worth lifting:

- **Sessions are multiplayer chat channels backed by a microVM.** A session is
  Slack-channel-like — teammates *and* coding agents share one conversation — but
  each is also backed by a sandboxed cloud computer on its own Git branch. Changes
  are isolated per session, so parallel tasks switch instantly with no local
  worktree wrangling. Because it's a cloud VM, the human can close their laptop and
  work continues; teammates keep prompting the agent and making progress.
- **Shared cloud computer, not just shared chat.** Everyone in a session runs
  terminal commands against the *same* machine and sees the same outputs and live
  preview — "no one is going to say it doesn't work on my machine." A teammate
  joins a session and sees the whole prompting history, so they understand how the
  current state was reached, not just the diff.
- **Multiplayer prompting and multiplayer plans.** Multiple humans can prompt the
  same agent in one session, and the agent reads the whole conversation as input.
  Plans are collaboratively editable documents with everyone's cursors visible —
  shifting plan-mode from a private, local, unshared artifact (a named failure of
  current agents) into a shared alignment surface *before* the agent builds.
- **Backwards-compatible escape hatches.** PRs are still created (from inside Ace,
  with a link back to the session) because code eventually returns to GitHub. And
  because agents are "shit at CSS," real-time multiplayer VS Code editing on the
  microVM remains available — front-end/design work still wants a hand on the code.
- **Proactive context dashboard.** Because all the conversation *around* the code
  is available to agents, they form a "social information fabric": a dashboard
  summarises what's underway, prompts you to resume unfinished work (the react
  hooks you left Friday), and a "Team Pulse" summarises what coworkers shipped.
  This targets the core agentic-team problem — the speed and volume of work make
  it hard to keep up with colleagues (five features a day, not one) — by making
  agents *proactively bring context to you* rather than leaving you to chase it.

The underlying design bet: agents gift back the time implementation used to
consume, and that surplus should buy *quality* — more research, deeper thinking,
better alignment — not a larger pile of the same crappy software. In a world of
cheap, fast software, craft becomes the differentiator, and craft needs strong
alignment to afford the time it costs.

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-zero-alignment-2cbd2b48.md` — origin: https://maggieappleton.com/zero-alignment/
