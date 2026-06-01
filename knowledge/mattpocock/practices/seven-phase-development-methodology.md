# Seven-Phase Development Methodology

Matt structures all AI-assisted development through seven distinct phases that consistently lead to shipping quality work. This methodology applies across different AI coding approaches (Ralph loops, plan mode, manual prompting) and scales from massive projects to narrow, focused tasks.

## The Seven Phases

**Phase 1: The Idea** — The problem statement or feature concept that triggers the development process. Can be as large as an entire app or as small as a specific bug fix.

**Phase 2: Research (Optional)** — Create `RESEARCH.md` assets for external dependencies or difficult exploration phases. Cache information that's hard for agents to access repeatedly (APIs, documentation).

**Phase 3: Prototyping (Optional)** — Essential when imposing taste on the outcome. Create multiple variations on throwaway routes to explore different approaches before committing to implementation.

**Phase 4: Product Requirements Document (PRD)** — Describe the destination clearly using behavioral requirements. Focus on what users will see and how it will behave, not implementation details.

**Phase 5: Implementation Planning (Kanban Board)** — Break down the PRD into tickets with blocking relationships. Enable parallelization by finding all non-blocking tickets for simultaneous agent execution.

**Phase 6: Execution** — Run coding agents to execute all tickets. Can be sequential for simple cases or parallelized with multiple agents on non-blocking tickets.

**Phase 7: Quality Assurance** — Agent creates QA plan for human review. Typically reveals issues requiring iteration back to phases 5-7 until reaching production quality.

## Phase-Specific Practices

**Research assets are ephemeral** — Cache information only for the duration of the sprint. Research can go stale and cause wrong turns if kept too long.

**Prototyping enables taste** — Use throwaway routes to impose design preferences. Concrete examples in prototypes are more valuable than abstract descriptions in PRDs.

**PRDs describe endpoints, not journeys** — Focus on the end state that users experience. Save implementation details for the Kanban breakdown.

**Kanban enables parallelization** — Well-structured boards allow multiple agents to work simultaneously on non-blocking tickets.

**AFK execution requires complete context** — With proper research, prototypes, PRD, and tickets, agents can work autonomously without constant human intervention.

## Iterative Nature

Phases 5-7 typically require multiple iterations. Each QA review surfaces new issues that become additional Kanban tickets, leading back to execution. This is expected and healthy for reaching production quality.

The methodology accounts for this iteration by treating QA as a quality gate that generates more work rather than a final checkpoint.

## Framework Agnosticism

The methodology works across different AI coding tools and approaches. The specific implementation (skills, prompts, tools) varies, but the seven-phase structure provides consistent progress toward shipping quality work.

This makes it valuable for teams using different AI coding setups or individuals working across multiple tools.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-my-7-phases-of-ai-development-8d95cfb2.md