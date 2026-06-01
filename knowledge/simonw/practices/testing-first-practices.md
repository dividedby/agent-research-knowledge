# Testing-First Practices

Simon Willison emphasizes that automated tests are no longer optional when working with coding agents, and testing should come first in agent workflows.

## "First Run the Tests" Pattern

Any time starting a new session with an agent against an existing project, start with a variant of prompting the agent to run the tests. This practice:

- Forces the agent to figure out how to run the tests, making it likely to run tests in the future
- Gives the agent a rough indication of project size and complexity through test counts  
- Puts the agent in a testing mindset, encouraging it to expand tests later
- Provides four words that encompass substantial software engineering discipline already baked into models

## Why Tests Are Vital with Agents

The old excuses for not writing tests - time consuming and expensive to constantly rewrite while a codebase rapidly evolves - no longer hold when an agent can knock them into shape in just a few minutes.

Tests are vital for ensuring AI-generated code does what it claims to do. If code has never been executed, it's pure luck if it actually works when deployed to production.

## Tests as Learning Tools

Tests are a great tool to help get agents up to speed with existing codebases. When you ask Claude Code or similar about an existing feature, they'll likely find and read the relevant tests first.

Agents are already biased towards testing, but the presence of an existing test suite almost certainly pushes the agent into testing new changes it makes.

## Manual Testing Integration

Just because code passes tests doesn't mean it works as intended. Manual testing reveals issues that automated tests miss - code might crash on startup, fail to display crucial UI elements, or miss details tests failed to cover.

Getting agents to manually test code is valuable and frequently reveals issues not spotted by automated tests. When agents find something that doesn't work through manual testing, use red/green TDD to fix it, ensuring the new case ends up covered by permanent automated tests.

*Sources: [First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/), [Agentic manual testing](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/)*