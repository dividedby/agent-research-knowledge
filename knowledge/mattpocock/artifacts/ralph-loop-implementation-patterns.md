# Ralph Loop Implementation Patterns

Matt's Ralph loops implement autonomous agent execution through a simple bash loop pattern that can be adapted for different task sources and output formats. The core pattern enables agents to choose their own tasks from a backlog and work until completion.

## Core Loop Structure

The basic Ralph loop script runs the same prompt repeatedly:
- Agent looks at a plan file (PRD, JSON, or backlog)
- Agent looks at a progress file to see completed work
- Agent decides what to do next (highest priority)
- Agent explores codebase and implements the feature
- Agent runs feedback loops (tests, types, linting)
- Agent commits the code and updates progress

The key insight: **the agent chooses the task, not the human**. This differentiates Ralph from multi-phase planning where humans write new prompts for each phase.

## HITL vs AFK Modes

**Human-in-the-loop (HITL)** — Run once, watch, intervene. Best for learning Ralph patterns, refining prompts, and building confidence. Resembles pair programming where human can steer and contribute.

**Away-from-keyboard (AFK)** — Run in bounded loops with max iterations. For bulk work and low-risk tasks once prompts are proven. Always cap iterations to prevent runaway costs with stochastic systems.

The progression: start with HITL to learn and refine, go AFK once you trust your prompt, review commits when you return.

## Task Source Flexibility

Ralph can pull tasks from multiple sources:
- Local PRD files (markdown, JSON)
- GitHub Issues
- Linear sprint boards  
- Beads task files
- Any system with discrete, prioritizable work items

The agent maintains the same task selection logic regardless of source — it picks what to work on next based on priority and blocking relationships.

## Progress Tracking Mechanics

**Progress file** (`progress.txt`) short-circuits exploration between iterations. Contains:
- Tasks completed in current session
- Decisions made and reasoning
- Files changed
- Blockers encountered
- Notes for next iteration

**Commit discipline** — Agent commits after each feature, providing clean git log and diff context for future iterations.

**Completion signaling** — Agent outputs `<promise>COMPLETE</promise>` when PRD is finished, allowing loop termination detection.

## Loop Customization Patterns

**Test Coverage Loop** — Agent finds uncovered lines, writes tests until coverage hits target
**Linting Loop** — Agent fixes lint errors one by one, running linter between iterations
**Duplication Loop** — Agent identifies code clones, refactors into shared utilities
**Entropy Loop** — Agent scans for code smells and cleans them up systematically

Any task fitting "look at repo, improve something, commit" works with Ralph. Only the prompt changes, the loop structure remains constant.

## Quality Control Integration

Ralph loops integrate with feedback systems:
- Pre-commit hooks block commits unless all checks pass
- TypeScript type checking must be clean
- Tests must pass before progress is recorded
- Linting errors block completion

This enforces quality without human intervention — the agent cannot declare success while feedback loops are failing.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-getting-started-with-ralph-7f6ee75f.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-tips-for-ai-coding-with-ralph-wiggum-440a70a9.md