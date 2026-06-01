# Quality-First Agent Development

Simon Willison emphasizes that AI should help produce better code, not worse, and that shipping worse code with agents is a choice that can be avoided.

## Core Principle

If adopting coding agents demonstrably reduces code and feature quality, address that problem directly. Figure out which aspects of your process hurt output quality and fix them. Agents should help us ship code that is better, not worse.

## Technical Debt Avoidance Strategy

The best mitigation for technical debt is avoiding taking it on initially. Many debt fixes are simple but time-consuming changes:

- API design changes requiring dozens of file updates
- Poor naming choices needing project-wide cleanup  
- Duplicate functionality requiring combination and refactoring
- Large files needing module separation

These conceptually simple tasks are hard to justify given more pressing issues.

## Agent-Enabled Refactoring

Refactoring tasks are ideal applications of coding agents:

1. **Fire up asynchronous agent** (Gemini Jules, OpenAI Codex web, Claude Code web)
2. **Tell it what to change** and let it work in background branch/worktree
3. **Evaluate in Pull Request**: If good, land it. If almost there, redirect. If bad, discard.

The cost of code improvements has dropped so low that we can afford zero tolerance to minor code smells and inconveniences.

## Technology Choice Optimization

LLMs help ensure we don't miss obvious solutions and suggest Boring Technology most likely to work. More importantly, coding agents enable **exploratory prototyping**.

### Prototype-Driven Decisions

Best way to make confident technology choices: prove fitness with prototypes. Example: "Is Redis good for activity feeds with thousands of concurrent users?"

Agents can build load test simulations from single well-crafted prompts, dropping experiment costs to almost nothing. Run multiple experiments simultaneously to pick the best fit.

## Compound Engineering Loop

Agents follow instructions that can evolve over time for better results based on learnings. Dan Shipper and Kieran Klaassen describe "Compound Engineering" - every project ends with retrospective (**compound step**) documenting what worked for future agent runs.

### Quality Compounding

Small improvements compound over time. Quality enhancements that used to be time-consuming are now cheap enough that there's no excuse not to invest in quality while shipping new features.

Coding agents mean we can finally have both velocity and quality simultaneously.

*Sources: [AI should help us produce better code](https://simonwillison.net/guides/agentic-engineering-patterns/better-code/), [Writing code is cheap now](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)*