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
and docs session forever. His global `AGENTS.md` (which travels across every
repo, not just one project) holds to the same three-line ceiling: the execution
environment (WSL), one line recording that he dislikes `AskUserQuestion` — "and
that's it."

## Scars are too broad a category; cap pointers at three

Pushing back on a rival minimalism scheme built around "scars" (a line recording
a past mistake), Matt calls the category itself too broad: **"scars is too broad
and can lead to sediment. Devs will call a bruise a scar and immediately dump a
correction in AGENTS.md."** Without a sharp definition of what counts, every
annoyance gets misfiled as a permanent lesson, and the file accretes the exact
sediment the rest of this discipline exists to prevent. He also softens his own
"pointers only" rule with one carve-out: if part of the app is touched far more
often than the directory structure would suggest, **a single pointer there earns
its place** — the undiscoverable-and-global bar can be met by "which file matters
most," not only by environment facts. But the carve-out is capped, not open-ended:
"mostly just pointers to the top 3 (no more) most important docs will do the
trick and save a ton of tokens" — a fixed budget on pointers themselves, so the
progressive-disclosure escape hatch doesn't quietly regrow into the doc-dump it
replaced.

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

Pushed to its limit, this reframes what a skill even *is*: at root, "that's what
skills are" — a context pointer you add into `AGENTS.md`, not a piece of bespoke
machinery. You can get most of the value without the formal apparatus by just
pointing `AGENTS.md` at the relevant context; the slash (`/`) syntax is a
welcome affordance for *finding* those pointers, not a prerequisite for having
them. Reference knowledge follows the same shape under a different filename: a
`RESOURCES.md` holds a resource and **says how to query it**, so the agent pulls
it in on demand — e.g. a knowledge base "used during teaching sessions, a thing
to query against." The pointer-doc, not the inlined instruction, is the unit.
In the same spirit Matt keeps a `CODING_STANDARDS.md` *separate* from the root
file: standards are relevant only to sessions that write code, so they live in
their own pulled-in doc rather than burning budget on every session.

## Context window phases and hardwired constraints

The agent's context window divides into flexible and hardwired phases. The **system prompt** (containing `CLAUDE.md`) is hardwired at startup, while exploration, implementation, and testing are flexible — a simple task needs little exploration, bug-free code needs little testing. But everything in `CLAUDE.md` inflates the hardwired portion, leaving less room for actual work and increasing costs.

This creates a **globality problem**: every instruction applies to every session regardless of relevance. A React pattern rule added after a frontend session burns budget in all subsequent backend, docs, and database sessions. The natural feedback loop of "agent does something wrong → add rule to file" creates growing files that hurt performance through irrelevant context.

## Pruning AGENTS.md is deeper work than it looks

Matt underestimated his own topic while building the course version of this
material: he added a section on "pruning an AGENTS.md file" expecting "a
short, simple video," and it turned out to be "the longest and most in-depth
in the whole course." The discipline above reads like a short checklist, but
applying it — deciding line by line what's undiscoverable-and-global versus
what's sediment — is evidently harder in practice than the rules make it
sound.

## Deterministic enforcement over prose rules

When enforceable constraints can be encoded as PreToolUse hooks (that exit with code 2 to block actions), they should become hooks rather than prose instructions. A hook that blocks `npm` and requires `pnpm` is both deterministic and costs zero instruction budget, while a prose rule only lowers the odds and consumes budget on every session.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-never-run-claude-init-4c8085b5.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-a-complete-guide-to-agents-md-e11c36f3.md  
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-my-agents-md-file-for-building-plans-yo-12a7f93d.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-how-to-use-claude-code-hooks-to-enforce-c827626c.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/course-video-manager/CLAUDE.md.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2061685783342256491-4bba91f0.md` — origin: https://x.com/mattpocockuk/status/2061685783342256491
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2061707663088529896-786519e4.md` — origin: https://x.com/mattpocockuk/status/2061707663088529896
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2061712630071362011-02e73004.md` — origin: https://x.com/mattpocockuk/status/2061712630071362011
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062528961855287580-6a45a883.md` — origin: https://x.com/mattpocockuk/status/2062528961855287580
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072439606394462470-3adde750.md` — origin: https://x.com/mattpocockuk/status/2072439606394462470
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2072439857935221124-7c642dea.md` — origin: https://x.com/mattpocockuk/status/2072439857935221124
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082060853319213481-07a7c588.md` — origin: https://x.com/mattpocockuk/status/2082060853319213481
