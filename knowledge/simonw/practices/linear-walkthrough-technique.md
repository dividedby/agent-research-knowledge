# Linear Walkthrough Technique

Simon Willison uses coding agents to create structured walkthroughs of codebases for understanding complex or forgotten code implementations.

## Use Cases

Linear walkthroughs are useful when you need to understand:
- Existing code you need to get up to speed on
- Your own code where you've forgotten details  
- Code you "vibe coded" and need to understand how it actually works

## Implementation Pattern

Frontier models with the right agent harness can construct detailed walkthroughs to help understand how code works. The process typically involves:

1. Point agent at repository or codebase
2. Request structured walkthrough of the implementation
3. Agent analyzes code and creates comprehensive documentation

## Case Study: SwiftUI Slide Presentation App

Willison vibe coded a SwiftUI slide presentation app using Claude Code and Opus 4.6, then realized he didn't understand how it worked. He prompted a new Claude Code session:

```
Create a linear walkthrough of this SwiftUI codebase using Showboat - use sed or grep or cat or whatever you need to include snippets of code you are talking about
```

### Key Techniques

- **Showboat integration**: Using `showboat note` and `showboat exec` commands to create structured documentation
- **Code snippet inclusion**: "use sed or grep or cat or whatever you need" ensures agents include actual code rather than risk hallucinations or mistakes
- **Systematic analysis**: Agent talks through all source files in detail

## Learning Benefits

The resulting walkthrough provided clear, actionable explanations about how the code works. Even a 40-minute vibe coded toy project became an opportunity to:
- Explore new ecosystems (SwiftUI)
- Pick up language-specific tricks (Swift)  
- Understand architectural patterns
- Absorb implementation details

## Skill Development Impact

If concerned that LLMs might reduce learning speed, this pattern demonstrates how agent-assisted walkthroughs can accelerate skill acquisition by providing structured exploration of unfamiliar code and ecosystems.

*Sources: [Linear walkthroughs](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/)*