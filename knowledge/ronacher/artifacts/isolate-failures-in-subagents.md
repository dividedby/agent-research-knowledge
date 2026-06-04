# Isolate failures so they don't derail the loop

If you expect a lot of failures during code execution — and in an agent built on
code execution, you should — the failures must be kept out of the main loop's
context, or they derail it. Ronacher treats strict failure isolation as a
load-bearing building block of a real agent.

Two mechanisms:

- **Run iteration-heavy work in a subagent; report only the outcome.** A task
  that needs many tries runs in a subagent until it succeeds, and only the
  *success* comes back — plus a brief summary of approaches that *didn't* work.
  That residue matters: it's useful for the next task to learn what to steer
  away from, so you keep a digest of failures, not their full output. This is
  the same instinct as [[reinforcement-in-tool-responses]] — give the loop the
  lesson, not the noise.
- **Context editing to reclaim tokens.** Anthropic's context editing can remove
  failures that only hurt particular attempts and didn't drive toward
  completion, preserving tokens for later iterations. Ronacher hasn't had much
  success with it yet and flags two open problems: deciding *which* failures to
  keep (the agent still benefits from knowing what didn't work, just not the
  full state), and the hard cost — context editing **automatically invalidates
  the cache** ([[manual-prompt-cache-points]]), so it's unclear when the token
  savings beat the cache-trash cost.

The general shape — a sub-context that absorbs messy iteration and returns a
clean summary — recurs in his harness preferences: Pi's session trees let him
branch into a side-quest to fix a broken tool, then rewind, summarizing what
happened on the branch without polluting the main session
([[malleable-self-extending-agent]]).

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-11-21-agents-are-hard-01c828c6.md — https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
