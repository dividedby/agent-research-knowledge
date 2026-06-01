# Subagent Patterns

Simon Willison describes subagents as a simple but effective way to handle larger tasks without burning through the main coding agent's valuable context window.

## Core Concept

LLMs are restricted by their context limit - typically around 1,000,000 tokens max, with better quality results below 200,000. Subagents provide fresh context windows by dispatching fresh copies of the agent to achieve specified goals with new prompts.

When a coding agent uses a subagent, it effectively dispatches a fresh copy of itself to achieve a specified goal, with a new context window that starts with a fresh prompt.

## Claude Code's Explore Pattern

Claude Code uses subagents extensively as standard practice. For new tasks against existing repos, it first needs to explore the repo to understand its shape and find relevant information.

The main agent constructs a prompt and dispatches a subagent for exploration, which returns a description of findings. The main agent prompts itself with good taste in prompting strategies.

Example explore subagent prompt:
```
Find the code that implements the diff view for "chapters" in this Django blog. I need to find:
- Templates that render diffs (look for diff-related HTML/CSS with red/green backgrounds) 
- Python code that generates diffs (look for difflib usage or similar)
- Any JavaScript related to diff rendering
- CSS styles for the diff view (red/green line backgrounds)
```

## Parallel Subagents

Subagents can provide significant performance boosts by running multiple subagents simultaneously, potentially using faster and cheaper models like Claude Haiku to accelerate tasks.

Example prompt: "Use subagents to find and update all of the templates that are affected by this change."

## Specialist Subagents

Some coding agents allow subagents with custom system prompts or tools for specialized roles:

- **Code reviewer agent**: Review code and identify bugs, feature gaps, or design weaknesses
- **Test runner agent**: Run tests and hide verbose output from main agent, reporting only failure details  
- **Debugger agent**: Specialize in debugging problems, spending tokens on reasoning through codebase and running diagnostic code snippets

## Usage Guidelines

While it's tempting to break up tasks across many specialist subagents, remember the main value is preserving root context and managing token-heavy operations. The root coding agent is capable of debugging or reviewing its own output provided it has tokens to spare.

The principle advantage is working with fresh context to avoid spending tokens from the parent's available limit, not necessarily capability differences.

*Sources: [Subagents](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)*