# Coding agent fundamentals

Geoff Huntley breaks down coding agents into their essential components, revealing there's "no moat"—agents are simply "300 lines of code running in a loop with LLM tokens." Understanding these fundamentals transforms you from an AI consumer to an AI producer who can automate tasks.

## The core loop

All coding agents follow the same basic pattern:
1. Take input from user or tool result
2. Allocate response to context window
3. Send for inferencing
4. Check if tool execution is needed
5. Execute tool if requested
6. Allocate tool outcome back to loop
7. Continue inferencing

"You just keep throwing tokens at the loop, and then you've got yourself an agent."

## Model selection for agency

Not all LLMs are agentic. Models fall into four categories:
- **High safety** (Anthropic, OpenAI) - ethics-aligned
- **Low safety** (Grok) - for security research
- **Oracle** - high thinking, summarization tasks
- **Agentic** - biases toward action over thinking

"Claude Sonnet is a digital squirrel... a robotic squirrel that just wants to do tool calls. It doesn't spend too much time thinking; it biases towards action, which is what makes it agentic."

For agents, choose highly agentic models like Claude Sonnet or Kimi K2. For higher reasoning, wire other LLMs as tools into the agentic model—"We call it the Oracle. The Oracle is just GPT wired in as a tool that Claude Sonnet can function call for guidance."

## The five coding agent primitives

Every coding agent requires these fundamental tools:

### 1. Read tool
Reads file contents into context window, either whole files or in chunks for larger files.

### 2. List files tool
Lists files and directories at a given path, enabling agent navigation of codebases.

### 3. Bash tool
Executes shell commands on the computer, allowing the agent to run tests, build code, and interact with the system.

### 4. Edit tool
Applies changes to files based on inference results, enabling code modifications.

### 5. Code search tool
Nearly every coding tool uses `ripgrep` under the hood for pattern matching in codebases. "There is no magic for indexing source code or any intelligence."

"Everything from this point forward is just a matter of tuning your prompts."

## Context window management

Critical principles for effective agent operation:

- **One activity per context window**: Clear context after each distinct task to avoid cross-contamination
- **Context is limited**: Think of it as a Commodore 64—the more you allocate, the worse performance becomes
- **Less is more**: Sonnet's 200k advertised context becomes ~176k usable after system prompts and harness overhead

"Context windows are very, very small... you should be treating it as a computer with a limited amount of memory."

## MCP and tool management

Model Context Protocols (MCPs) are "a function with a billboard on top that nudges the LLM's latent space to invoke that function."

Critical warnings:
- Avoid excessive MCP tool allocation
- Consider aggregate context window consumption of all tools
- "The more you allocate to a context window, the worse the performance... and your outcomes will deteriorate"

## Prompting and system design

The harness prompt contains:
- Tool registrations and descriptions
- Operating system information (for choosing PowerShell vs bash)
- Instructions on agent behavior
- Guidance on how the agent should operate

"LLMs are non-deterministic. You can include the guidance, and it's just guidance. However, through prompt evaluation, tuning, and spending time playing with the models to understand how they behave, you can develop effective prompts."

## Professional implications

"Learning how to build a coding agent is one of the best things you can do for your personal development in 2025, as it teaches you the fundamentals. Once you understand these fundamentals, you'll move from being a consumer of AI to a producer of AI who can automate things with AI."

Building agents is now fundamental knowledge:
- Employers seek candidates who can automate organizational tasks
- Understanding the loop is as essential as knowing what a primary key is
- Failing to learn risks falling behind coworkers who leverage multiple agents

Sources: [how to build a coding agent: free workshop](sources/ghuntley/blog/https-ghuntley.com-agent-55a508d9.md)