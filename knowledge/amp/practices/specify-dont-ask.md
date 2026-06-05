# Specify, don't ask

Agents can now solve nearly anything you can *specify*, so the primary failure
mode is **under-specification**. An unrestricted prompt yields unrestricted
results — almost never what you wanted. Give the agent direction, not a question.

The mental model: treat the agent as a capable peer who moves at 10x your speed
but has never seen your codebase. Its only limits are the tools it can reach, the
feedback loops it can see, and *your ability to lead it*. So you put everything
you know into the prompt — architecture, where the traps are, where the relevant
code lives, what a good test is, the trade-offs. Writing a good prompt is where
*all* your software knowledge comes together; agents don't make this knowledge
obsolete, they consume it.

How it shows up:

- **Direction over questions.** Not `Why isn't the back button working?` but
  `The back button on the settings page doesn't navigate. Reproduce it locally,
  find the bug, fix it, check your own work.`
- **Name the traps you foresee.** Tell it where preferences are stored, which
  existing component to match, which tests to run — the context that turns the
  same task into a different outcome.
- **Don't fight the agent's first draft by micromanaging.** If output is rarely
  good enough, the lever is a *more detailed prompt* and a better `AGENTS.md`,
  not edit-by-edit approval.
- **Iterate by reference, then commit.** Amp's own prompts walk in steps — point
  at a file/commit/cookbook URL, ask the agent to analyze current logic, confirm
  understanding, *then* "Okay, make that change!" — rather than firing one vague
  instruction.

## The speed trap

The failure that follows success: the agent moves faster than your ability to
*verify* its output. It emits 500 lines across six files in seconds — and breaks
the auth flow. This is not a hallucination; the agent reasoned correctly from
what you gave it. You just didn't lead it one step further. When you're in the
speed trap you spend more time debugging the agent's "solutions" than writing the
code yourself would have taken. The escape is not slowing the agent down with
approvals — it's specifying a definition of done and engineering feedback loops
into the prompt so the agent can verify itself before handing back.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-how-to-pair-with-an-agent-450a7fb3.md` — origin: https://ampcode.com/notes/how-to-pair-with-an-agent
- `sources/amp/chronicle/https-ampcode.com-notes-how-i-use-amp-60b3bca7.md` — origin: https://ampcode.com/notes/how-i-use-amp
- `sources/amp/chronicle/https-ampcode.com-notes-fif-dc1eb004.md` — origin: https://ampcode.com/notes/fif
