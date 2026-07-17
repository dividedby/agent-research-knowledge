# Automation as leverage: fix the class, not the instance

A correction fixes one run; automation fixes every run after it. Cherny's stance
on agent-era engineering discipline: the habit of pouring time into automating
your own work — vim macros, lint rules, e2e suites — hasn't changed, it has
gotten *more* valuable, because now automation compounds across an entire fleet
of agents instead of just your own hands.

Three reasons he gives for why this matters more now, not less:

- **It speeds up the whole fleet, not just you.** Infra and DevX automation used
  to multiply one engineer's output; running many parallel agents means every
  one of them is sped up too, so the payoff stops being linear (see
  [[parallel-agents-are-the-productivity-unlock]]).
- **It eliminates a class of bug, not one instance.** There's a real difference
  between a chat correction and infrastructure: a correction fixes the run in
  front of you, encoded infrastructure (a lint rule, a hook, a check) fixes
  every future run. This generalizes the "write it down, don't re-prompt" habit
  in [[compounding-memory]] — a CLAUDE.md rule fixes the next session; a
  hook or lint rule fixes every session, including ones you never see.
- **It lets other people contribute, not just you.** The reason this is
  genuinely new rather than a rehash of "automate your job": the knowledge you
  can now encode as infrastructure isn't limited to lint rules, types, and
  tests — it can capture *nearly all* domain knowledge, so an agent (or a new
  human) works productively with **zero additional context from the
  prompter.** That's CLAUDE.md, skills, and code-review automation
  ([[compounding-memory]], [[skills-as-the-unit-of-reuse]],
  [[customization-checked-into-git]]) treated as one continuous practice
  rather than three separate features.

The punchline, and the sharpest form of the principle: **"a rejected PR is a
failure of automation."** If a human reviewer has to catch something by hand,
that's a gap that should have been a lint rule, a hook, or a documented
convention — not evidence the contributor (human or agent) needed closer
supervision. The team's stated goal is every engineer writing the CLAUDE.md's,
REVIEW.md's, skills, and docs that let agents work in their codebase with zero
extra context, so Claude writes better code, review catches issues
automatically, and the next contributor ramps up faster.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
