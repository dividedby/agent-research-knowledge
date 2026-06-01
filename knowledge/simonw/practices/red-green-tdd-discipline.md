# Red/Green TDD Discipline

Simon Willison advocates for "Use red/green TDD" as a succinct way to get better results from coding agents, emphasizing test-first development as a perfect fit for agent workflows.

## Core TDD Approach

TDD (Test Driven Development) ensures every piece of code is accompanied by automated tests that demonstrate the code works. The most disciplined form is test-first development: write automated tests first, confirm they fail, then iterate on implementation until tests pass.

## Perfect Fit for Coding Agents

Test-first development provides excellent protection against common coding agent risks:
- Writing code that doesn't work
- Building unnecessary code that never gets used  
- Missing comprehensive test coverage for regression protection

As projects grow, the chance that new changes break existing features grows with them. A comprehensive test suite is the most effective way to keep features working.

## The Red/Green Process

**Red phase**: Confirm tests fail before implementing code
**Green phase**: Confirm tests now pass after implementation

Skipping the red phase risks building tests that already pass, failing to exercise and confirm the new implementation.

## Universal Model Understanding

Every good model understands "red/green TDD" as shorthand for the much longer instruction: "use test driven development, write the tests first, confirm that the tests fail before you implement the change that gets them to pass."

This makes it a powerful four-word prompt that encompasses substantial software engineering discipline already baked into the models.

## Integration with Manual Testing

When agents find issues through manual testing, using red/green TDD to fix them ensures the new case ends up covered by permanent automated tests, preventing regression.

*Sources: [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/), [First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/)*