# CLAUDE.md is an instruction budget, not a doc dump

Matt's stance on the project instruction file (`CLAUDE.md` / `AGENTS.md`) is
aggressively minimalist, and it follows from two scarce resources rather than
taste. First, the file lands in the **system prompt**, which is hardwired the
moment the agent starts — unlike the flexible exploration/implementation/testing
phases, every token here is spent on *every* task whether relevant or not, so it
directly shrinks the room left for real work. Second, models have an **instruction
budget** distinct from the context window: a frontier thinking model follows only
~150–400 instructions with consistency (smaller and non-thinking models fewer),
and every sentence in the file is an instruction competing for that ceiling.

## Never run `/init`

The headline rule: never run the `init` command, and delete any auto-generated
file you find. Everything `init` emits is either trivially discoverable from
source (command listings duplicate `package.json`; framework names are obvious
from config and imports) or actively harmful: documented file paths and service
locations **go stale the instant code moves and then mislead the agent**, which
reads them with none of a human's skepticism. For an agent that re-reads the file
every request, stale docs don't just waste tokens — they *poison context*. This is
the same doc-rot Matt warns about generally: don't stuff the repo with markdown;
let the agent generate its own just-in-time documentation during exploration,
which is always current because it reflects the live code.

## What actually belongs: undiscoverable AND globally relevant

The bar for a line earning its place is that it must be **both** undiscoverable
from the codebase **and** relevant to essentially every session. Matt's entire
personal `CLAUDE.md` is six words — `you are on WSL on Windows` — there only
because WSL's path resolution is something the agent genuinely can't infer. The
"global" trap is the failure mode: the agent does something you dislike in a
frontend session, you add a rule, and now that rule burns budget in every backend
and docs session forever.

## Progressive disclosure instead of one big file

The constructive alternative is to push everything else down a discovery tree.
Keep a tiny root file (one-sentence project description that acts as a role
prompt, non-default package manager, non-standard build/typecheck commands) that
*links* to focused docs — `docs/TYPESCRIPT.md`, `docs/TESTING.md` — written with a
light touch ("for TypeScript conventions, see…", no all-caps "ALWAYS"). Those load
only when relevant; references can nest one level further; monorepos use
per-package `AGENTS.md` files that merge at the relevant scope. **Skills are
themselves a form of progressive disclosure** — steering you'd otherwise cram into
the global file becomes a skill the agent pulls in only when it applies. The rule
for any new line: root file only if it touches every task, else a separate file or
a skill.

A real product repo shows the end state: `course-video-manager`'s entire root
`CLAUDE.md` is three pointer stanzas — Backlog, Triage labels, Domain docs — each a
sentence that defers to a `docs/agents/*.md` file ("Issues and PRDs live as GitHub
issues… See `docs/agents/backlog.md`"). The root file carries only what's both
global and undiscoverable (which tracker, that `ready-for-agent` is spelled
`Sandcastle` here, that the layout is single-context with ADRs under `docs/adr/`);
everything else is a link the agent follows when the task needs it.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-never-run-claude-init-4c8085b5.md` — origin: https://www.aihero.dev/never-run-claude-init
- `sources/mattpocock/aihero/https-www.aihero.dev-a-complete-guide-to-agents-md-e11c36f3.md` — origin: https://www.aihero.dev/a-complete-guide-to-agents-md
- `sources/mattpocock/aihero/https-www.aihero.dev-my-agents-md-file-for-building-plans-yo-12a7f93d.md` — origin: https://www.aihero.dev/my-agents-md-file-for-building-plans-you-actually-read
- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md
