# Content Type Addition Workflow

Simon Willison demonstrates a complete workflow for adding new content types through a deceptively short but comprehensive prompt sequence.

## Case Study: Blog-to-Newsletter Tool Enhancement

Adding "beats" content type to blog-to-newsletter tool - content posted elsewhere (releases, tools built, museums visited) that should be included in generated newsletter.

## Three-Part Prompt Pattern

### 1. Reference Repository Cloning
```
Clone simonw/simonwillisonblog from github to /tmp for reference
```

**Pattern rationale**: Coding agents can clone code from GitHub. Best way to explain a problem is often having them look at relevant code. Using `/tmp` ensures they don't accidentally include reference code in their own commit later.

### 2. Feature Implementation Reference
```
Update blog-to-newsletter.html to include beats that have descriptions - similar to how the Atom everything feed on the blog works
```

**Pattern rationale**: 
- Referencing specific filename (`blog-to-newsletter.html`) tells agent which of 200+ HTML apps to modify
- Referencing existing implementation ("similar to how the Atom everything feed works") saves describing logic details
- Specifying filter criteria ("beats that have descriptions") leverages existing editorial distinction

### 3. Validation and Testing
```
Run it with python -m http.server and use `uvx rodney --help` to test it - compare what shows up in the newsletter with what's on the homepage of https://simonwillison.net
```

**Pattern rationale**:
- **Static server setup**: `python -m http.server` prevents issues with applications that fetch data and break when served as file from disk
- **Agent-friendly tooling**: `uvx rodney --help` provides browser automation with help output designed to teach agents everything needed
- **Validation mechanism**: Comparing newsletter results to blog homepage provides confidence verification since recent content matches new requirements

## Implementation Result

The agent correctly added a UNION clause to SQL query filtering out draft beats and beats with empty `note` columns, plus appropriate JavaScript handling for beat type display.

This demonstrates how short, well-structured prompts can achieve substantial work when leveraging agent capabilities for repository exploration, implementation pattern recognition, and validation.

*Sources: [Adding a new content type to my blog-to-newsletter tool](https://simonwillison.net/guides/agentic-engineering-patterns/adding-a-new-content-type/)*