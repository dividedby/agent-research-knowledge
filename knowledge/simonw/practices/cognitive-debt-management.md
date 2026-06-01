# Cognitive Debt Management

Simon Willison identifies cognitive debt as a key challenge in agentic engineering - when we lose track of how code written by agents works.

## The Problem of Cognitive Debt

When we lose track of how agent-written code works, we take on **cognitive debt**. For simple operations (fetching data from database, outputting JSON), implementation details often don't matter and we can make solid guesses from trying the feature.

However, when core application details become a black box we don't fully understand, we can no longer confidently reason about it. This makes planning new features harder and eventually slows progress like accumulated technical debt.

## Interactive Explanations as Solution

One of Willison's favorite ways to pay down cognitive debt is by building **interactive explanations** - having agents create visual, animated, or interactive demonstrations of how code works.

### Word Cloud Algorithm Example

When Claude Code built a Rust CLI tool for word clouds, the explanation "Archimedean spiral placement with per-word random angular offset" wasn't intuitive. Willison requested:

1. A linear walkthrough of the codebase (helped understand Rust structure)
2. An **animated explanation** by pasting the walkthrough into a new session

The resulting animation showed the algorithm attempting to place each word by showing a box, checking for intersections with existing words, and continuing outward in a spiral from center when collisions occurred.

## Implementation Strategy

Good coding agents can produce explanatory animations and interactive interfaces on demand to explain code - both their own code and code written by others. This helps make algorithm mechanics click intuitively.

The key is requesting these explanations when the cognitive load of understanding implementation details outweighs the simplicity of the interface, particularly for core application logic that affects future development decisions.

*Sources: [Interactive explanations](https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/)*