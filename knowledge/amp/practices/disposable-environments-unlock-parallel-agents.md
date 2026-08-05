# Disposable environments unlock parallel agents

The ceiling on how many agents you run at once, and how long you let each one
run unsupervised, usually isn't the model's capability — it's the friction of
managing local checkouts, worktrees, and port conflicts. Remove that friction
(spin up an isolated, ephemeral, scale-to-zero sandbox per task instead of a
local checkout) and someone who resisted running more than one or two agents at
a time starts spawning one for every papercut they notice: a sandbox that costs
nothing to create and nothing to leave running removes the reason to hesitate.

Two behaviors follow directly from removing that friction, not from a better
model:

- **Volume.** Every small annoyance becomes worth delegating, because the
  marginal cost of a new agent is a disposable environment, not a checkout you
  have to track, keep unblocked, and eventually clean up.
- **Tolerance for scope and duration.** With no local ports, browsers, or disk
  space at stake, an agent producing hundreds of lines of code or running for
  twenty, thirty minutes stops being something to babysit — it isn't taking up
  anything you'll have to reclaim if it goes long.

This shifts the real bottleneck from "how many agents can I manage" to "how do
I review what they produced" — which only stays tractable if you also demand
proof of work rather than reviewing raw diffs (see
[trust-is-a-passing-test-suite](./trust-is-a-passing-test-suite.md)). Removing
friction without also raising the evidence bar just produces more unreviewable
output faster.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-what-i-want-to-tell-you-about-orbs-dc428f37.md` — origin: https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs
