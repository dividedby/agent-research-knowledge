# Codebase porting methodology

Geoff Huntley outlines a systematic Ralph-based approach for porting codebases between programming languages, emphasizing specification-driven transformation over direct translation.

## The three-stage porting process

### Stage 1: Test specification extraction
Run a Ralph loop to compress all tests into specification documents:
- "Study every file in tests/** using separate subagents and document in /specs/*.md"
- Link original implementations as citations in specifications
- Creates language-agnostic test specifications with traceability

### Stage 2: Product functionality specification
Execute separate Ralph loop for product code documentation:
- "Study every file in src/* using separate subagents per file"
- Link implementations as citations in specifications
- Ensures comprehensive coverage of product functionality
- Maintains reference links to original source

### Stage 3: Target language implementation
Within the same repository, run classic Ralph loop:
- Create TODO file for implementation tasks
- Execute one task per loop iteration (most important first)
- Agent can study specifications and follow citations to reference source code
- Configure target language for strict compilation for best outcomes

## Key theoretical principles

**Citation-driven specifications**: The methodology relies on citations within specifications that "tease the file_read tool to study the original implementation during stage 3."

**Decoupling through abstraction**: Stages 1 and 2 "transform a code base into high level PRDs without coupling the implementation from the source language."

**Specification as bridge**: Specifications serve as the translation layer between source and target languages, capturing intent without implementation details.

## Benefits of the approach

- **Language independence**: Specifications capture behavior without language-specific implementation details
- **Traceability**: Citations maintain links to original source for verification
- **Systematic coverage**: Separate subagents ensure comprehensive documentation
- **Incremental implementation**: Ralph loop in stage 3 enables manageable, iterative development
- **Quality assurance**: Strict compilation in target language catches errors early

## Practical considerations

**Repository structure**: All three stages occur within the same repository to maintain citation links and enable cross-referencing.

**Subagent utilization**: Using separate subagents for each file in stages 1 and 2 ensures focused, thorough analysis without context contamination.

**Implementation prioritization**: Stage 3 TODO generation and execution follows Ralph's "most important thing per loop" principle.

**Strict compilation**: Configuring target language for maximum strictness improves translation quality and catches issues early.

This methodology demonstrates how Ralph loops can systematically tackle complex, multi-stage transformations while maintaining quality and traceability throughout the porting process.

Sources: [porting software has been trivial for a while now](https://ghuntley.com/porting/) — `sources/ghuntley/blog/https-ghuntley.com-porting-c1d70add.md`