# Prefactor Before the Easy Change

When Matt's PRD-decomposition workflows break a spec into ordered sub-issues,
the first slices are not feature work — they are **prefactoring**. Both the
interactive `to-issues-project` skill and the headless `to-issues-prd` AFK prompt
were revised to fold in Kent Beck's maxim verbatim: *"Make the change easy, then
make the easy change."*

## Exploration earns its keep by finding the prefactor

The codebase-exploration step that precedes drafting slices shifted from
*optional* ("explore the repo if you haven't") to *expected* ("explore the
codebase to ground the breakdown in the real shape of the files you'll be cutting
through"). The reason the revision gives it teeth: exploration is where you spot
the restructuring that would make the feature a small change. You are not reading
the code to understand it — you are reading it to find the move that makes the
real work trivial.

## Prefactoring is its own slice, first in the list

The slice rules now mandate sequencing, not just granularity:

- *"Any prefactoring should be done first, in its own slice(s) at the start of the
  list."* (interactive skill)
- *"Prefactoring should be done before feature work."* (AFK prompt)

Because sub-issues run in **list order**, each in its own fresh agent session on a
shared branch, a prefactor that isn't its own leading slice never happens — the
feature session inherits the un-eased codebase and either skips the cleanup or
balloons past a single session's budget. Making the prefactor a discrete, ordered
slice is what guarantees the "make the change easy" half actually lands before the
"make the easy change" half.

## Why this matters more for agents

A human carrying a feature across days will naturally pause to clean up first; an
amnesiac agent picking up slice N has no such instinct and no memory of intending
to. Encoding the prefactor as an explicit early slice substitutes for the
judgment the agent can't hold across sessions — the same move as
[[tracer-bullets-over-horizontal-layers]] (force small vertical cuts the agent
won't choose on its own) and [[treat-the-agent-as-an-amnesiac-engineer]]
(design the workflow around the missing memory). Notably, the revision dropped the
older "prefer many thin slices over few thick ones" guidance in both files:
ordering discipline (prefactor first) now carries the weight that raw thinness
used to.

The rule has since propagated into the canonical public skills-repo: its
`to-issues` skill now adds a step to "look for opportunities to prefactor the code
to make the implementation easier" with the same Beck maxim, and its slice rules
mandate "any prefactoring should be done first" — the same ordering discipline,
now in the shipped skill rather than only the course-video-manager variants.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/course-video-manager/.claude-skills-to-issues-project-SKILL.md-7f209ac1.md — https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.claude/skills/to-issues-project/SKILL.md (revision 2026-06-03)
- `sources/mattpocock/skills-repo/skills-engineering-to-issues-SKILL.md-04f1cc54.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/to-issues/SKILL.md (revision 2026-06-17)
- /home/runner/work/agent-research/agent-research/sources/mattpocock/course-video-manager/.sandcastle-to-issues-prd-prompt.md-a986a929.md — https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/to-issues-prd/prompt.md (revision 2026-06-03)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062139630955184170-1a58ad17.md` — origin: https://x.com/mattpocockuk/status/2062139630955184170
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062151546616291780-0cb9e767.md` — origin: https://x.com/mattpocockuk/status/2062151546616291780
