# Tracer Bullets Over Horizontal Layers

Matt uses the tracer bullet technique from *The Pragmatic Programmer* to combat agents' natural tendency toward "slop" — building complete solutions all at once without validation. Tracer bullets force small, end-to-end slices of functionality that touch all system layers.

## The Slop Problem

Agents aim to please and tend to produce complete solutions in one leap: they build all API endpoints, complete request/response models, error handling, authentication, and logging before testing whether the basic connection works.

This "outruns the headlights" approach results in enormous chunks of code that need reworking. The agent builds entire layers in isolation without feedback loops to validate assumptions early.

## Tracer Bullets as Solution

Instead of building horizontal layers in isolation, tracer bullets build tiny vertical slices:

**Build one small feature end-to-end** — Cut through all integration layers with minimal functionality
**Test immediately** — Get feedback before building more  
**Move to next slice** — Use fresh context window for next feature
**Repeat** — Build incrementally with validation

This approach solves the "outrun its headlights" problem by building feedback loops into the process rather than churning out features blindly.

## Forcing Small Thinking

Agents must be explicitly prompted to think in tracer bullets since their natural inclination is toward big layers. Matt uses this specific prompt pattern:

"When building features, build a tiny, end-to-end slice of the feature first, seek feedback, then expand out from there. Tracer bullets allow you to test and validate your approach early, identifying potential issues before investing significant time in development."

## Context Window Constraints

Tracer bullets are non-negotiable with agents due to context window limitations. Unlike human developers who might remember their reasoning across multiple work sessions, agents lose context between conversations.

The discipline of small, validated slices becomes essential rather than optional when working within context window constraints.

## Implementation Strategy  

Matt breaks down complex features into tracer bullets by identifying the critical path first:
- What is the simplest end-to-end flow?
- Which integration points are riskiest?
- How can we validate assumptions fastest?

Each bullet validates one critical assumption before moving to the next slice.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-tracer-bullets-0575e91a.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-tips-for-ai-coding-with-ralph-wiggum-440a70a9.md