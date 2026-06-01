# Agent Architecture Understanding

Simon Willison emphasizes that understanding how coding agents work under the hood helps make better decisions about how to apply them effectively.

## Core Definition

A coding agent is software that acts as a **harness** for an LLM, extending that LLM with additional capabilities powered by invisible prompts and implemented as callable tools.

## LLM Foundation

At the heart of any coding agent is a Large Language Model that completes text sequences. As models get larger and train on more data, they can complete increasingly complex sentences like "a python function to download a file from a URL is def download_file(url): ".

### Token Processing
LLMs work with tokens (integer sequences) rather than words directly. Text "the cat sat on the " becomes `[3086, 9059, 10139, 402, 290, 220]`. This matters because:
- LLM providers charge based on token count
- Models are limited in tokens they can consider at once
- Understanding tokenization helps optimize costs and context usage

## Chat Template Evolution

Original LLMs were completion engines requiring carefully crafted prompts. Modern models use **chat templated prompts** simulating conversation:

```
user: write a python function to download a file from a URL  
assistant:
```

LLMs are stateless - every execution starts from blank slate. To maintain conversation simulation, software must replay entire existing conversation each time, making longer conversations more expensive.

## Token Caching Optimization

Most providers offer cheaper **cached input tokens** for common token prefixes processed within short time periods. Coding agents are designed with this in mind - they avoid modifying earlier conversation content to ensure cache efficiency.

## Tool Calling Mechanism

The defining feature of LLM agents is tool calling capability. At the prompt level:

```
system: If you need to access the weather, end your turn with <tool>get_weather(city_name)</tool>
user: what's the weather in San Francisco?
assistant: <tool>get_weather("San Francisco")</tool>
user: <tool-result>61°, Partly cloudy</tool-result>
assistant:
```

The harness extracts function calls (often with regex), executes tools, and returns results to the model.

## System Prompt Foundation

Coding agents start every conversation with system prompts (not shown to users) providing behavioral instructions. These can be hundreds of lines long and define how models should behave, what tools are available, and how to use them.

## Reasoning Enhancement

2025 saw introduction of **reasoning** to frontier models - models spend additional time generating text that talks through problems before presenting replies. This "thinking out loud" effect allows models to spend more tokens working on problems for better results.

Reasoning is particularly useful for debugging as it gives models opportunity to navigate complex code paths, mixing tool calls with reasoning to follow function calls back to issue sources.

## Fundamental Simplicity

The core loop is surprisingly straightforward: LLM + system prompt + tools in a loop. While a good tool loop requires substantial work, the fundamental mechanics are simple enough that building your own agent from scratch is achievable with a few dozen lines of code.

*Sources: [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)*