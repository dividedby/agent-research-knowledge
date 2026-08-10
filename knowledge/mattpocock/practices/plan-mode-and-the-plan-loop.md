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

The same preference shapes how he gives *feedback*: Matt gives it **via text**
(dictated), not screenshots — he rates **dictation as fast and vision as
disappointing**. Even where a visual workflow is the obvious move, he'd rather
describe the problem in words than feed the agent an image, because the text
channel is both quicker for him to produce and more reliable for the agent to act
on than current vision is.

## Configure the planner for legibility

Three small `AGENTS.md` rules make plans usable, and they recur verbatim across
Matt's writing: **be extremely concise, sacrificing grammar for concision**; **end
with a list of unresolved questions** (forcing the agent to surface edge cases,
error handling, and ambiguity before proceeding); and **put the numbered
step-by-step summary last**, because in a terminal you read the bottom first. The
honest caveat: on a codebase you know cold, plan mode can be slower right now — but
Matt uses it anyway, optimising for compounding skill, lower fatigue, and reach
into unfamiliar code rather than raw speed on familiar ground.

## The rush-to-asset critique, and grill-me as the fix

Matt's harshest read on plan mode isn't about the priming mechanics above — it's
that the mode rushes. Asked what he'd build into his own harness, his answer
names the exact failure: **"The issue with plan mode is the rush towards a plan
— the rush to create an asset."** Shown the destination too early, the agent
races to produce the deliverable rather than sit in the slower work of
alignment: **"showing the agent the final state too quickly leads to it
rushing… a sycophantic rush to create an asset means the real value, alignment,
gets skipped."** The plan document isn't the point; the shared understanding
behind it is — racing to the document is the same sycophancy failure mode he
diagnoses in agent behavior generally.

The concrete symptom is under-interviewing: **"I find it frustrating that
[plan mode] doesn't actually plan enough. It doesn't ask enough clarifying
questions. It jumps to conclusions. Then it presents you with a too-large plan
that most folks don't read."** His fix isn't a better plan-mode prompt but a
different tool — **"Better to just have a conversation with the agent, like you
would with a human. `/grill-me` can help there."** — routing the actual
alignment work to the grilling primitive (`align-before-building-grilling`) and
treating plan mode's document as, at best, the context-priming side-effect
credited above, not the mechanism that gets you aligned.

## Opus 5: code quality held, but planning conversation got worse

A new model can move the two halves of this workflow in opposite directions.
Asked whether he can even use Opus 5, Matt's answer splits the model's
performance along exactly the seam this doc already draws between code output
and planning conversation: "It is pretty good at writing code, just very bad
at talking." He sharpens the same split later, unprompted: "One underrated
part of Opus 5 is that the code it produces is good actually. My AFK runs have
absolutely not degraded, just the HITL planning has become a nuisance." So the
rush-to-asset critique above isn't only a skill-design problem to fix with
`grill-me` — a specific model can make the human-in-the-loop planning
conversation itself worse to sit through, independent of whether its eventual
code is any weaker.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-plan-mode-introduction-3aa9bfe5.md` — origin: https://www.aihero.dev/plan-mode-introduction
- `sources/mattpocock/aihero/https-www.aihero.dev-my-agents-md-file-for-building-plans-yo-12a7f93d.md` — origin: https://www.aihero.dev/my-agents-md-file-for-building-plans-you-actually-read
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067936649904820322-d4f8f252.md` — origin: https://x.com/mattpocockuk/status/2067936649904820322
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067938767164338538-c7e28c82.md` — origin: https://x.com/mattpocockuk/status/2067938767164338538
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081672829016084727-b2e5829c.md` — origin: https://x.com/mattpocockuk/status/2081672829016084727
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081676095368085646-d0d3ae60.md` — origin: https://x.com/mattpocockuk/status/2081676095368085646
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081796528260198766-5aaa1c0d.md` — origin: https://x.com/mattpocockuk/status/2081796528260198766
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082076477018005644-1a7de231.md` — origin: https://x.com/mattpocockuk/status/2082076477018005644
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085682292421185570-5356f355.md` — origin: https://x.com/mattpocockuk/status/2085682292421185570
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2086082988631007374-33a7f57a.md` — origin: https://x.com/mattpocockuk/status/2086082988631007374
