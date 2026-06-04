# A shared filesystem so tools have no dead ends

Most of Ronacher's agents are built on code execution and code generation, which
*requires a common place for the agent to store data*. His choice is a
filesystem — in his case a virtual one — that every tool can read from and write
to. This is the substrate that lets an agent compose tools, including subagents
and sub-inference.

The design rule is **no dead ends**. A dead end is a tool whose output can only
feed back into one other specific tool. An image-generation tool that can only
hand its image to one consumer is broken: you might next want to zip those images
with the code-execution tool, or unpack a zip and feed the images back to
inference to describe them, then back to code execution. The way out is that
every tool takes and returns *paths on the same virtual filesystem* — so an
`ExecuteCode` tool and a `RunInference` tool both operate over the same store,
the latter taking a `path` to a file the former wrote.

The cost is that every tool must be *built* to speak file paths into that shared
store rather than passing data inline — but that's exactly what buys
composability without the agent getting trapped. It's the agent-internals
counterpart to [[code-over-inference-for-repeatable-work]]: the filesystem is the
glue that lets code-execution steps and inference steps chain into a pipeline,
and it's the kind of derived/shared state [[llm-apis-as-state-sync]] argues the
APIs themselves mishandle.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2025-11-21-agents-are-hard-01c828c6.md — https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
