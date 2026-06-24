# Verification is the number-one tip

Cherny names this explicitly as his #1 tip, and it is the only principle he
restates verbatim across multiple threads: **give Claude a way to verify its own
output, and it will iterate until the result is great.** Everything else is
secondary.

The mental model he uses: an agent without a way to check its work is like an
engineer asked to build a website but forbidden from opening a browser — the
result won't look good. Give it the browser and it writes code and iterates until
it does. The job of the human is to *supply the feedback loop*, not to inspect
each step.

Verification is domain-specific, and the practice is to wire up the right closer
per domain:

- **Backend** — make sure Claude knows how to start your server/service and
  exercise it end-to-end.
- **Frontend** — the Claude Chrome/Chromium extension drives a real browser to
  test UI changes and iterate until they look right; the Desktop app can auto-start
  and test web servers.
- **Mobile** — an iOS/Android simulator MCP.
- **Desktop apps** — computer use.
- **General** — bash commands, test suites, "diff behavior between main and your
  feature branch," `/goal` conditions.

Two compounding reasons it matters more over time. (1) For long-running and
parallel work, verification is *what lets you walk away* — "when you come back to
a task, you know the code works." A fleet of agents is only trustworthy if each
one self-checks. (2) As models improve (Cherny's note on Opus 4.7/4.8), giving
Claude a way to verify "has always been a way to 2-3x what you get out of Claude,
and with newer models it's more important than ever" — the model now catches its
own bugs instead of declaring victory early, but only if it can observe outcomes.

This is the foundation under [[parallel-agents-are-the-productivity-unlock]] and
[[autonomous-unattended-operation]]: parallelism and autonomy are only safe
because each agent closes its own loop.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
