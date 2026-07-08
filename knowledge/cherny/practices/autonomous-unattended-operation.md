# Autonomous, unattended operation

A late and recurring theme: composing Claude Code's primitives so an agent runs
for hours — or days — without babysitting, and tells you when it's done. Cherny
frames the end state as "the autonomous fleet," and "when I'm not coding, I'm
dispatching." The pieces are individually small but the *workflow that pulls them
together* is the concept.

The composable pieces:

- **Auto mode** — instead of approving every file write and bash command, or
  skipping permissions entirely, Claude routes each action to a safety classifier
  and decides on your behalf. Cherny argues this is arguably *safer* than reading
  every prompt yourself (a human rubber-stamps; the classifier actually checks).
  "No more permission prompts."
- **Focus mode** — hides intermediate work so you see only the final result;
  predicated on trusting the model to run the right commands.
- **Completion conditions and loops** — `/goal <condition>` keeps a session
  working until a predicate is true (Claude re-checks the transcript every time it
  tries to stop); `/loop` runs a prompt on an interval for up to ~3 days locally;
  `/schedule` (and Routines) runs recurring jobs *in the cloud*, surviving a closed
  laptop. A `Stop` hook gives programmatic control over when Claude may finish.
- **Notifications** — with auto + focus you watch less, so a `Stop` hook firing a
  Slack/system notification tells you when work is done.
- **Recaps** — short "what I did / what's next" summaries so returning to a
  long-running session needs no scrolling.

The pulled-together workflow Cherny describes: *start Claude in auto mode with
focus on; it runs autonomously, verifies its own work (`/go`), and notifies you
when done; you review the recap and the PR.* Mobile dispatch (Cowork Dispatch,
the iOS app, session teleporting via `&` / `--teleport`) extends the same loop to
"do work while away from a computer."

**Which loop when.** The Claude Code team's own framing: a loop is *an agent
repeating cycles of work until a stop condition is met* — everything from a
single prompt to a cloud Routine fits that definition, differing only in what
triggers it, what stops it, and how much of the loop you hand off to Claude:

- **Turn-based** — you hand off the check (a skill or test suite tells Claude
  *whether* an attempt worked; you still decide when to stop).
- **Goal-based** — you hand off the stop condition (`/goal <predicate>`); Claude
  re-checks the transcript against it every time it tries to stop, so it can't
  quietly settle for "good enough."
- **Time-based** — you hand off the trigger (`/loop` locally, `/schedule` in the
  cloud); work starts without you prompting it.
- **Proactive** — you hand off the prompt itself; a dynamic workflow runs
  recurring, well-defined work with no human writing the next instruction.

The four are a progression, not a menu: each step delegates one more piece of
the loop, and "proactive" composed with parallel agents is what the autonomous
fleet above actually is. Pick a loop by naming which piece — the check, the
stop condition, or the trigger — is *your* current bottleneck, rather than
reaching for the most autonomous option by default.

This concept sits on top of the rest: it requires
[[verification-is-the-number-one-tip]] (the agent must self-check to be trusted),
[[context-hygiene]] (the window must not rot over hours), and
[[parallel-agents-are-the-productivity-unlock]] (a fleet, not one session). The
*how* of running hundreds of parallel subagents safely is
[[dynamic-workflows]] in artifacts.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
