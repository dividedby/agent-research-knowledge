# Git Workflow Patterns

Simon Willison emphasizes Git as a key tool for working with coding agents, enabling more ambitious Git usage due to agents' fluency with both basic and advanced Git features.

## Core Git Fluency

All coding agents have deep understanding of Git jargon and can handle complex Git operations. Key advantages:

- Don't need to memorize *how* to do Git operations, just stay aware of what's possible
- Can take advantage of full suite of Git abilities through agent assistance
- History diving is effectively free since agents can browse without extra network traffic

## Essential Patterns

### Session Initialization
**"Look at recent changes"** - Great way to start fresh coding sessions. Causes agent to run `git log`, instantly loading context with details of recent work (modified code + commit messages). Enables discussing that code, suggesting fixes, asking questions, or proposing next changes.

### Conflict Resolution
**"Fix this Git mess"** - Universal prompt for various Git problems including merge conflicts, failed rebases, staging issues. Agents can navigate Byzantine merge conflicts, reason through code intent, and determine what to keep and how to combine conflicting changes.

### Binary Search Debugging
**"Use Git bisect to find when this started failing"** - Agents can handle the boilerplate of expressing test conditions for Git bisect, making it an occasional-use tool deployable whenever curious about historic software behavior.

### Lost Code Recovery
**"Find this code I accidentally deleted"** - Agents can search Git stash, reflog, and other branches to locate code that hasn't been committed to permanent branches.

## Advanced History Rewriting

Agents excel at Git's advanced history rewriting features. Consider Git history as deliberately authored story describing software progression, not permanent record of what happened.

### Commit Management
- **Undo/rewrite commits**: Agents remember commands like `git reset --soft HEAD~1`
- **Commit message quality**: Frontier models usually have good taste in commit messages, often better than human-written ones

### Repository Extraction
Agents can extract code from larger repositories into new ones while maintaining key history - useful for library extraction where classes/functions should become standalone reusable libraries.

## Integration with Agent Workflows

Git supports both collaboration and backup through remotes. Agents understand this ecosystem and can work with GitHub, private repositories, and various Git hosting services seamlessly.

The combination of agent Git fluency and their ability to run tests means they can ensure tests pass before finalizing merges, providing confidence in conflict resolution and history rewriting operations.

*Sources: [Using Git with coding agents](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)*