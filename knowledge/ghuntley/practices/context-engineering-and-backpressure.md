# Context engineering and backpressure

Geoff Huntley emphasizes that effective agent work requires understanding context engineering fundamentals and capturing "backpressure"—the resistance and feedback that emerges during agent interactions.

## Context allocation principles

"The more you allocate to a context window, the worse the performance of the context window will be, and your outcomes will deteriorate."

Key rules for context management:
- **One activity per context window** - Clear context after each distinct task
- **Minimal tool allocation** - Avoid excessive MCP servers or tools
- **Calculate aggregate consumption** - Consider total context used by all tools combined
- **Less is more** - Constrain rather than expand context usage

Real numbers for Claude Sonnet:
- Advertised: 200k tokens
- System prompt allocation: ~24k tokens  
- Usable for tasks: ~176k tokens
- With heavy MCP tools: potentially only 100k usable

## The MCP overallocation trap

At a San Francisco MCP event, Huntley observed widespread misunderstanding of context fundamentals despite $150-200k event spending. Microsoft's removal of the 128 tool limit in VS Code prompted the question: "Why would you need 128 tools or why would you want more than that?"

Cursor caps MCP tools at 40 for good reason—excessive tool allocation degrades performance.

"A common failure scenario I observe is people installing an excessive number of MCP servers or failing to consider the number of tools exposed by a single MCP tool or the aggregate context window allocation of all tools."

## Backpressure as engineering signal

"If you aren't capturing your back-pressure then you are failing as a software engineer."

Backpressure represents the resistance, friction, and feedback signals that emerge when working with agents. Rather than ignoring this resistance, skilled practitioners:
- Capture and analyze failure patterns
- Use backpressure as a signal for system improvement
- Apply engineering discipline to resolve recurring issues
- Treat resistance as valuable feedback for optimization

This concept connects to broader engineering principles in the "post loom/gastown era" and during Ralph loops—backpressure becomes a crucial signal for system health and improvement opportunities.

## Context window as scarce resource

Huntley frames context windows not as abundant computational resources but as severely constrained environments requiring careful resource management:

"It's best to think of them as a Commodore 64, and as such, you should be treating it as a computer with a limited amount of memory."

This scarcity mindset drives:
- Careful allocation of context to only essential elements
- Active management of tool and prompt overhead
- Strategic clearing of context between distinct tasks
- Recognition that performance degrades with overallocation

## Practical implications

For agent operators:
- Monitor context consumption actively
- Limit simultaneous tools and MCP servers
- Clear context between unrelated tasks
- Treat context window performance as a primary optimization target

For system design:
- Build tooling that minimizes context overhead
- Design prompts that efficiently use available tokens
- Create mechanisms to detect and respond to context pressure
- Engineer systems that degrade gracefully under context constraints

Sources: [too many model context protocol servers and LLM allocations on the dance floor](sources/ghuntley/blog/https-ghuntley.com-allocations-d8cf275f.md), [don't waste your back pressure](sources/ghuntley/blog/https-ghuntley.com-pressure-d34d2128.md)