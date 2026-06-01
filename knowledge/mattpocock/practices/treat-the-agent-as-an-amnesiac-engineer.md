# Treat the agent as an amnesiac engineer

The mental model under all of Matt's process is that an agent is not a
super-powered developer but **a competent engineer with no memory** — "the guy
from Memento", a new starter who walks into the codebase every session asking
"okay, what am I doing?" You're spawning twenty-plus of these new starters a day.
Two consequences follow, and they pull in tension: treat them *like* engineers,
but design around the amnesia.

## Treat them like engineers — so process matters more, not less

The most reliable way Matt has found to raise output quality is to treat agents as
humans (with weird constraints) and give them the discipline good human engineers
already use: plan before coding, work in tracer-bullet slices, build feedback
loops, do TDD, design deep modules. None of this is AI-specific — it's
twenty-year-old good practice — but agents make it *non-negotiable* where humans
could sometimes skate by. "Process has never been more important": skills exist to
encode that process so the amnesiac follows the same strict path every time.

## Design around the amnesia — and keep your own judgement

Because nothing carries between sessions, the *environment* must carry the
context: a clean, navigable codebase the agent re-reads (it out-votes any
instruction file), a progress file plus git history for loops, just-in-time
exploration instead of stale docs. The flip side is a hard line on what you must
*not* delegate. Matt builds bespoke personal software where the AI does only the
**grunt work** — transcription, format-shifting, boilerplate — while he reviews
every user-facing output and keeps all the thinking: "the moment you start
delegating your thinking to an LLM, you're screwed." The agent takes work off your
hands without taking over your judgement. This is also why he leans toward
*meta-programming* — investing effort in defining and automating his own
processes (triage, prioritisation, the grunt work) so the fleet of amnesiac
engineers runs itself, while the human stays at the wheel.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-5-agent-skills-i-use-every-day-056774d5.md` — origin: https://www.aihero.dev/5-agent-skills-i-use-every-day
- `sources/mattpocock/aihero/https-www.aihero.dev-how-to-make-codebases-ai-agents-love-1ba6d0b5.md` — origin: https://www.aihero.dev/how-to-make-codebases-ai-agents-love
- `sources/mattpocock/aihero/https-www.aihero.dev-ways-ai-coding-has-rewired-my-brain-dc20954e.md` — origin: https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain
- `sources/mattpocock/aihero/https-www.aihero.dev-personal-software-is-insane-in-the-age--3d6a74ea.md` — origin: https://www.aihero.dev/personal-software-is-insane-in-the-age-of-ai-u2hx2
