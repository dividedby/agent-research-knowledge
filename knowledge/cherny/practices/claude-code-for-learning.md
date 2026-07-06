# Claude Code as a learning tool, not just a builder

The same session that writes code can teach you the code, if you point it that
way on purpose. Cherny's team treats "explain this to me" as a first-class use
of the harness — not a detour from building, and not something that needs a
separate tool outside the agent you already have open.

Four ways they do it:

- **Explanatory/Learning output style.** Set it in `/config` to have Claude
  narrate the *why* behind its changes as it works, instead of a terse diff-only
  stream — turning ordinary usage into a running explanation.
- **Generate a visual HTML presentation** of unfamiliar code. Framed as
  "surprisingly good slides" — a concrete artifact you can page through, not just
  a paragraph of prose.
- **Ask for ASCII diagrams** of an unfamiliar protocol or codebase. A diagram
  forces the model to commit to a structure, which is often where a prose
  explanation would stay vague.
- **A spaced-repetition learning skill.** You explain your understanding back to
  Claude, it asks follow-up questions to find the gaps, and stores the result —
  a custom skill built on top of the harness (see
  [[skills-as-the-unit-of-reuse]]), not a built-in feature.

The principle: **ramping up on unfamiliar code is a task you can delegate output
from, the same way you'd delegate a feature** — ask for the artifact that
teaches (slides, a diagram, a quiz) instead of just asking questions and reading
answers. It costs nothing extra since the same session already has the context
loaded from doing the work.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
