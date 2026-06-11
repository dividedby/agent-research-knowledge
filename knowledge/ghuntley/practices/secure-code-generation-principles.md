# Secure code generation principles

Geoff Huntley outlines fundamental principles for achieving secure code generation with AI, emphasizing what not to do and building up from first principles rather than relying on superficial tooling solutions.

## The MCP server fallacy

Huntley strongly warns against believing that secure code generation can be achieved through MCP (Model Context Protocol) servers or similar tooling approaches:

"If anyone pitches you on the idea that you can achieve secure code generation via an MCP tool or Cursor rules, run, don't walk."

This represents a fundamental misunderstanding of how security should be integrated into AI-powered development workflows.

## The transition to AI-generated code

"I haven't written code by hand for nine months. I've generated, read, and reviewed a lot of code, and I think perhaps within the next year, the large swaths of code in business will no longer be artisanal hand-crafted."

The shift from manually written to AI-generated code is accelerating rapidly, making secure code generation practices critical for the entire industry.

## The fundamental question

As the industry moves toward predominantly AI-generated codebases, the central challenge becomes: "How do I make the agent generate secure code?"

This question requires moving beyond traditional security approaches designed for human developers to new methodologies appropriate for AI-driven development.

## Anti-pattern: Tool-based security theater

Huntley's conversation with a "stealth startup" pitching MCP-based security illustrates a common misconception that security can be bolted onto AI development through additional tools or context rules.

The core problem with this approach:
- Treats security as an external constraint rather than an integrated practice
- Assumes that prompt engineering or tool restrictions can guarantee security
- Ignores the fundamental need for architectural and process changes

## Building from first principles approach

Rather than relying on tools to enforce security, Huntley advocates for "building up from first principles"—developing security practices that are native to AI-driven development workflows.

This implies:
- Understanding the unique security challenges of AI-generated code
- Developing new review and validation processes appropriate for AI output
- Creating security practices that work with, rather than against, AI development patterns

## The code review paradigm shift

The transition to AI-generated code necessitates fundamental changes in how security is ensured, moving away from traditional human-centric review processes to new methodologies designed for the scale and nature of AI-generated codebases.

## Sources

[anti-patterns and patterns for achieving secure generation of code via AI](https://ghuntley.com/secure-codegen/) — `sources/ghuntley/blog/https-ghuntley.com-secure-codegen-8fe2a042.md`