# Agent Feedback Loops as Quality Gates

Matt structures his agent workflows around fast, deterministic feedback loops that serve as quality gates. Unlike human developers who might push through red states, agents excel when given clear pass/fail signals that prevent progress until issues are resolved.

## The Hierarchy of Feedback Loops

The feedback loop hierarchy prioritizes speed and determinism:

**Type checking** — TypeScript provides free feedback that catches errors agents would never find without testing in browsers. Essential for any TypeScript project.

**Unit tests** — Basic tests covering core functionality keep agents on track for logical errors. Agents don't get frustrated by test failures and will simply retry.

**Pre-commit hooks** — Enforce feedback loops before every commit using Husky. If any step fails, the commit is blocked and the agent gets an error message to adjust.

**Linting and formatting** — Use lint-staged with Prettier to auto-format code and catch style issues before commits.

## Integration Testing for Agents

Matt discovered that agents accelerate the need for integration testing. While humans might test manually, agents require automated end-to-end test suites that describe all user stories for proper validation.

The key insight: "Raising test boundaries lets you catch more bugs and work more comfortably with AI agents running code automatically."

This means testing at higher levels of abstraction — testing the whole feature workflow rather than individual functions.

## Feedback Loops as Constraints

When agents work autonomously (Ralph loops), feedback loops become non-negotiable constraints:

- Agents cannot commit if tests are red
- Type checking must pass with no errors  
- All linting must be clean
- Pre-commit hooks block bad commits entirely

This enforces quality without human intervention. The agent receives immediate feedback and must fix issues before proceeding.

## Why This Works for AI

Agents don't suffer from feedback fatigue the way humans do. When code fails type checking or tests, the agent simply tries again. This makes feedback loops incredibly powerful for AI-driven development.

The key is that feedback loops give agents actual context about what's working and what's not in the real world. Without these loops, agents work blind and produce lower quality code.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-essential-ai-coding-feedback-loops-for--3a500e40.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-ways-ai-coding-has-rewired-my-brain-dc20954e.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-tips-for-ai-coding-with-ralph-wiggum-440a70a9.md