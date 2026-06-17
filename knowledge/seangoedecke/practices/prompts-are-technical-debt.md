# Prompts are technical debt — and a worse kind than code

"All code is technical debt" — every line adds maintenance burden, so sensible
engineers write as little as possible. Goedecke's argument is that **prompts are
debt too, and a worse form of it.** The prompt surface is now large: `AGENTS.md`,
`CLAUDE.md`, the same files in sub-directories, skills, per-tool and system
prompts. Switching tools, adopting a Ralph loop, pulling in a skill file, or
installing an MCP server all count as changes to your prompts even when you didn't
write them.

Prompts genuinely matter — a minor tweak can unlock significant performance, and
the reason the same model feels different across Codex, Cursor, OpenCode, and
Copilot is subtle prompting differences. But that value comes with a trap that
makes prompt-debt worse than code-debt:

- **Prompts are model-specific and decay silently.** AI labs re-tune their prompts
  for *each* model release; a prompt crafted for GPT-5.4 may be stale or actively
  harmful for GPT-5.5. Code debt announces itself with errors or a tangible
  slowdown, and stable code stays stable when untouched. A decayed prompt just
  quietly underperforms — you'll misread it as "the new model isn't as good as the
  hype" rather than "my prompt no longer fits the model."
- **Pinning the model isn't a real escape.** You could refuse to upgrade, but the
  pace of improvement means a delicately-prompted harness on an old model loses to
  a bare-bones harness on a new one. (Defensible only once model progress slows.)

The practical posture: **most people should pick a third-party-maintained coding
tool and leave it as unconfigured as possible**, piggybacking on teams that
re-evaluate prompts every model release — and if those teams get it wrong, users
notice and complain. Avoid MCP and skills unless absolutely necessary; keep them
off by default. When you do write an `AGENTS.md`, restrict it to **specific,
concrete facts about the project** — no behavior steering (the now-outdated "think
step by step," "you are a skilled engineer," "I'll tip you $200"). Don't let models
fill it with pages of barely-reviewed text, for the same reason you wouldn't let
them fill the codebase with barely-reviewed code. Write your prompts yourself, and
delete them whenever you get the chance.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-prompts-are-technical-debt-too-5ac475ea.md` — origin: https://seangoedecke.com/prompts-are-technical-debt-too/
