# Human-AI partnerships are for alignment, not capability

The chess "centaur" era — where human+AI beat either alone — doesn't describe
coding, because the human isn't making the code more *capable*. Frontier agents
already write code that's faster and has fewer bugs than an unassisted human's:
compiles cleanly, rarely races, handles platforms correctly. Vibe-coded output
at work is still bad, but not because the code is wrong — it's bad *taste*: code
that isn't maintainable, that satisfies invented requirements instead of real
ones, or that contradicts the system's long-term strategy. The human's value-add
is **alignment** — adapting generated code to an organization's specific
technical values — not capability.

This asymmetry is durable, not a temporary capability gap models will close.
Capability is well-understood how to train (scale, data, RL environments) and
is roughly universal: working code is working code regardless of which company
wrote it, which is exactly why it's easy to train for. Alignment has no
equivalent recipe, and it's inherently organization-specific — a model's RL
grader rewards generic proxies for good code (block comments over every
function, bulk low-value unit tests, decorative UI text) that don't track any
particular company's actual values, and those values differ enough between
companies that switching jobs "can almost feel like relearning the job." A
model would need to *adapt on the fly* to whichever organization's values are
in play, not just hit one fixed target — a much harder training problem than
capability, with no sign of being close to solved.

The practical corollary: since misalignment — not incapability — is the
observable failure mode, spend prompting effort stating your organization's
high-level values and priorities, to head off the generic-proxy behaviors
before they land in a PR, rather than treating agent output as a capability
problem to route around.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-human-ai-partnerships-are-for-alignme-4907a52e.md` — origin: https://seangoedecke.com/human-ai-partnerships-are-for-alignment-not-capability/
