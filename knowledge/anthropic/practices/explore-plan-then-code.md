# Explore first, then plan, then code

Letting an agent jump straight to coding produces code that solves the wrong
problem. Separate exploration from execution: have the agent read files and
answer questions (plan mode — no changes), then produce a detailed implementation
plan you can edit directly, then switch to coding and let it implement against
that plan, then — once it checks out — have the agent commit with a descriptive
message and open the PR, closing the loop in the same session instead of a manual
handoff. The plan is a cheap, reviewable artifact at the point where a wrong
turn is still free to correct. Toggle plan mode itself with `Shift+Tab` (the
status bar confirms with `⏸ plan mode on`) or start the session already in it
via `claude --permission-mode plan`; leave it the same way — approve the plan or
press `Shift+Tab` again — to hand off into execution, so the phase you're in is
always a visible, reversible mode rather than an implicit assumption.

Planning is overhead, so spend it where it pays. It earns its cost when the
approach is uncertain, when the change spans multiple files, or when you're
unfamiliar with the code being modified. When the scope is clear and the fix is
small — a typo, a log line, a rename — skip it: if you could describe the diff in
one sentence, just ask for it.

This pairs with a second discipline: **specific, high-signal prompts**. The agent
can infer intent but can't read your mind. Scope the task (which file, which
scenario, testing preferences), point it at the source that answers the question
(a file via `@`, the git history of a confusing API), and reference existing
patterns to follow rather than describing them ("look at `HotDogWidget.php`,
follow that pattern"). Describe a bug by its symptom, likely location, and what
"fixed" looks like — and have it write a failing test first. Feed rich context
directly rather than describing where it lives: reference files with `@` (the
agent reads them before responding), paste/drag images, give doc URLs (allowlist
frequent domains via `/permissions`), pipe data in (`cat error.log | claude`), or
just tell the agent to fetch what it needs itself. The plan is a first-class
editable artifact — open it in your editor (`Ctrl+G`) and revise it before the
agent proceeds. And exploration runs both ways: ask the agent the questions you'd
ask another engineer about an unfamiliar codebase, let it interview *you* to
surface implementation/UX/edge-case tradeoffs you hadn't considered, and use the
open-ended `"what would you improve in this file?"` to surface things you didn't
know to ask. For a larger feature, don't stop at the interview — have the agent
write up a spec from it before you start implementing, so the plan you're
building against captures what the interview surfaced rather than living only in
the conversation.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-code-best-practic-4d249e2a.md` — https://www.anthropic.com/engineering/claude-code-best-practices
- `sources/anthropic/best-practices/https-code.claude.com-docs-en-best-practices-fb8dc53b.md` — https://code.claude.com/docs/en/best-practices
