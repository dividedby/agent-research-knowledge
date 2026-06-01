# Agentic Engineering Definition

Simon Willison defines **agentic engineering** as the practice of developing software with the assistance of coding agents - agents that can both write and execute code.

## Core Definition

**Agents run tools in a loop to achieve a goal**

The agent is software that calls an LLM with your prompt and passes it a set of tool definitions, then calls any tools that the LLM requests and feeds the results back into the LLM. For coding agents, those tools include one that can execute code.

Code execution is the defining capability that makes agentic engineering possible. Without the ability to directly run the code, anything output by an LLM is of limited value. With code execution, agents can start iterating towards software that demonstrably works.

## Human Role Evolution

Writing code has never been the sole activity of a software engineer. The craft has always been figuring out *what* code to write. The human role becomes:

- Navigate dozens of potential solutions and their tradeoffs
- Provide agents with the tools they need to solve problems
- Specify problems at the right level of detail  
- Verify and iterate on results until confident they address problems robustly
- Update instructions and tool harnesses based on learnings

Used effectively, coding agents help us be more ambitious with projects and produce more, better quality code that solves more impactful problems.

## Distinction from "Vibe Coding"

Agentic engineering is distinct from "vibe coding" (coined by Andrej Karpathy) which describes prompting LLMs to write code while you "forget that the code even exists." Vibe coding refers to unreviewed, prototype-quality LLM-generated code. Agentic engineering emphasizes bringing code up to production-ready standards.

*Sources: [What is agentic engineering?](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/), [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)*