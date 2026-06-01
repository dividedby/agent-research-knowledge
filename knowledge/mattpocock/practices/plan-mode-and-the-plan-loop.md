# Plan mode and the plan loop

Matt uses Claude Code's **plan mode for almost everything, even small bug fixes**.
It's a restricted mode (read and explore allowed; edit, run, and test disallowed)
in which you iterate with the agent on *what* to build before any code exists. The
non-obvious benefit is mechanical: plan mode **primes the context window**. By the
time you exit, the agent has already read the files it will modify and discovered
how they connect — so you usually *don't* clear context between planning and
executing; the loaded files plus the explicit plan eliminate a swarm of failure
modes. "It's not just about the plan document, it's about priming the agent's
context."

## The four-step plan loop

Every change runs through **plan → execute → test → commit**, then repeat. Dropping
the planning step is the cardinal error — you're asking the agent to guess, and
you'll fight hallucinations. Planning forces clarity: it's a forcing function for
concrete requirements, the same way you wouldn't throw a vague ask at a human
colleague. Often, articulating what you want reveals you wanted something slightly
different — the agent is "the best rubber duck", available 24/7.

## Always dictate

Matt insists on **dictation** (Wispr Flow / Superwhisper) as the input method:
it's faster than typing, and AI doesn't need grammatically clean input —
especially in plan mode, where the agent rewrites your messy stream-of-
consciousness into a plan anyway. The sloppy early prompts don't matter once
they've been refined.

## Configure the planner for legibility

Three small `AGENTS.md` rules make plans usable, and they recur verbatim across
Matt's writing: **be extremely concise, sacrificing grammar for concision**; **end
with a list of unresolved questions** (forcing the agent to surface edge cases,
error handling, and ambiguity before proceeding); and **put the numbered
step-by-step summary last**, because in a terminal you read the bottom first. The
honest caveat: on a codebase you know cold, plan mode can be slower right now — but
Matt uses it anyway, optimising for compounding skill, lower fatigue, and reach
into unfamiliar code rather than raw speed on familiar ground.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-plan-mode-introduction-3aa9bfe5.md` — origin: https://www.aihero.dev/plan-mode-introduction
- `sources/mattpocock/aihero/https-www.aihero.dev-my-agents-md-file-for-building-plans-yo-12a7f93d.md` — origin: https://www.aihero.dev/my-agents-md-file-for-building-plans-you-actually-read
