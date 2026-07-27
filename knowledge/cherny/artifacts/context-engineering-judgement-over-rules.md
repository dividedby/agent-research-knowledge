# Context engineering: judgement over rules, loaded just-in-time

As models get more capable, hard-coded rules in a system prompt become a
liability, not a safety net — a rule that's right 90% of the time is wrong
the other 10%, and a model that can read surrounding context can already tell
which case it's in. Tuning Claude Code's system prompt for the Claude 5
generation, the team deleted **over 80% of it** with no measurable loss on
coding evals, trading rigid instructions for trust in the model's judgement.
The clearest example: the old comment-guidance rule was wrong everywhere
comments actually *were* wanted (documentation, gnarly code) — judgement
handles both cases a rule needed a separate carve-out for.

The same shift plays out in tool and interface design. The old advice was to
give Claude worked examples of how to use a tool; with newer models, examples
*backfire* — they fence the model into the exploration space the example
happened to demonstrate. Design an expressive interface instead and let the
parameters teach: an enum that hints at a lifecycle, a "one in_progress" rule
baked into the schema, needs no accompanying example. Ask the same of your
own tools, scripts, and files — and of design work generally (an HTML mockup
beats a described layout or a screenshot, for the same reason: showing beats
telling).

The loading half of the same principle: don't cram everything a request
*might* need into context upfront — load it at the moment it's relevant,
whether that's the built-in system prompt, tool definitions, or your own
CLAUDE.md/skills. Concretely: code-review and verification steps moved out of
the system prompt and into skills Claude calls selectively; tool definitions
moved from always-loaded to deferred, searched via ToolSearch only when
needed; CLAUDE.md/skills moved from one mega-file with every practice to a
tree of files loaded at the right time. The myth this kills: that CLAUDE.md
and skills need to be a central repository of everything Claude *might* hit,
because it "won't find it otherwise." It will — split long skills across many
files and let Claude pull the branch it needs, the same progressive-disclosure
instinct in [[skills-as-the-unit-of-reuse]], now backed by the harness's own
system-prompt redesign. References got richer too: a `#` hotkey and
code-shaped references now carry the highest fidelity, ahead of a plain
markdown spec.

This only works if the model is trustworthy enough to reconcile conflicting,
attacker-adjacent context safely without the guardrails a rigid rule used to
provide — which is why the shift lands the same day as **Opus 5**, pitched as
the least prompt-injectable model yet. Judgement-based context engineering is
a bet on the model, not a free lunch: it buys a leaner system prompt and less
over-constraining, at the cost of needing a model good enough to earn that
trust.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
