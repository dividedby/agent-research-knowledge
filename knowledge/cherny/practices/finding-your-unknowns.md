# Finding your unknowns is the actual skill of agentic coding

Once the model itself stops being the bottleneck, the limiting factor moves to
*you*: the quality of an agent's output is bottlenecked by how well you've
clarified what it doesn't know. Thariq (@trq212, Claude Code) frames this as a
skill you train, not a trait — "the best agentic coders have relatively few
unknowns" not because they need less clarity than everyone else, but because
they're better at surfacing what's missing before it becomes a wrong guess.

Three kinds of unknown, and each behaves differently:

- **Known unknowns** — questions you're already aware you haven't answered.
- **Unknown knowns** — the "I'll know it when I see it" cases: too fuzzy to
  write down in advance, but instantly recognizable once you see a candidate.
- **Unknown unknowns** — the pothole you didn't know the road could have. The
  more work you hand off, the more of these an agent runs into, because it has
  to fill every gap with a guess.

When Claude hits an unknown mid-task, it has to decide based on its best guess
of what you want — so the fix isn't more supervision, it's closing the gap
*before* the agent has to guess. Thariq's toolkit, one technique per unknown
type, each with the literal prompt he uses:

- **Blind spot pass** (unknown unknowns). Ask Claude to find your unknown
  unknowns and explain them, giving it context on who you are and what you
  already know: *"I'm working on adding a new auth provider but I know
  nothing about the auth modules in this codebase. Can you do a blindspot
  pass to help me figure out my relevant unknown unknowns and help me prompt
  you better."*
- **Brainstorm & prototype** (unknown knowns). When the criteria are ones
  you'd only recognize if you saw them — visual design, layout, taste calls —
  don't try to describe the target. Ask for an HTML artifact with several
  wildly different directions and react to it instead.
- **Interview** — once you've brainstormed, have Claude interview you one
  question at a time about what's still ambiguous, prioritizing the questions
  whose answer would actually change the architecture (not the ones that just
  fill in detail).
- **References** — when you can't describe what you want, point Claude at one.
  Diagrams and pictures work, but source code is the highest-fidelity
  reference: pointing at a folder or module means Claude reads how the thing
  is actually built, not just what it looks like. Claude Design works the same
  way — richer detail from markup and structure than from a screenshot.
- **Implementation plans that lead with what's likely to change** — ask for a
  plan ordered by risk, not by execution order: data models, type interfaces,
  and UX flows first (the parts you're most likely to want to tweak), with the
  mechanical refactoring buried at the bottom (the part you trust Claude on).

No amount of upfront planning removes every unknown unknown — the agent will
still hit edge cases mid-work that force a different tack. Two techniques
carry the practice past the planning stage:

- **Implementation notes.** Have Claude keep a running `implementation-notes.md`
  during the work: when it hits an edge case that forces a deviation, it picks
  the conservative option, logs it under "Deviations," and keeps going. This is
  the mid-run form of [[compounding-memory]]'s "write it down" discipline —
  what the agent learns mid-task becomes next time's map instead of evaporating
  when the session ends.
- **Quiz before merge.** After a long session, reading the diff only gives a
  light understanding of what actually changed. Ask Claude for an HTML report
  of the changes with context and intuition, plus a quiz at the bottom — and
  don't merge until you pass it. Package the prototype, spec, and
  implementation notes into the same doc to pitch reviewers, who start with the
  same unknowns you did; lead with the demo.

This is the concrete mechanism underneath [[plan-first-then-context-minimalism]]
and [[delegate-dont-pair-program]]: both say "front-load clarity," but neither
says *how* you find the clarity you don't yet have. This toolkit is the how —
and it's designed to be used at every stage, not just the first prompt.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
