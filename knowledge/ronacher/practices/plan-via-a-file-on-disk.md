# Plan through a file on disk, not a special mode

Ronacher doesn't use Claude Code's plan mode. His planning workflow: get the
agent to ask clarifying questions, pull those questions into an editor, answer
them, and iterate on a handoff **markdown file** until he's happy — then act on
it. The spec lives on disk where he can *see, read, review, edit, and
manipulate* it before anything happens.

His reverse-engineering of Claude Code's plan mode is what justifies the
preference: plan mode turns out to be **just a prompt plus UX**. A "plan" is a
markdown file Claude writes into a plans folder with no structure beyond text;
the write/edit tools are never actually disabled — read-only behavior is
enforced purely by injected system reminders ("Plan mode is active… you MUST NOT
make edits"), and the agent even edits its own plan file with the normal edit
tool. Entering/exiting plan mode is itself a tool. So the "path towards spec
always goes via the file system" regardless — the integrated mode just wraps a
short canned prompt (some phased Understand → Design → Review → Final-Plan
guidance) in a confirmation UI. You could replicate most of it with a
slash-command that pastes the prompt; you'd only lose the UX.

The deeper conviction this exposes: Ronacher consistently asks **where a feature
has to be enforced by the harness versus where it emerges from the model**, and
prefers the latter. A separate UI mode for something natural language can
already do "takes away some of the magic." A file he controls keeps him *in
control* of the artifact in a way the integrated experience doesn't — which is
also why his go-to harness Pi has no plan mode, and why Amp is removing theirs.
This is the same instinct behind [[own-your-tools-as-skills]] and pairs with
[[yolo-mode-delegate-and-wait]], whose missing plan-mode permissions first
pushed him to this approach.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-12-17-what-is-plan-mode-c0bb68c8.md — https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/
