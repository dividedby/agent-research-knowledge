# Deep Modules and Gray-Box Architecture

Matt advocates for restructuring codebases into "deep modules" — modules with lots of implementation controlled by simple interfaces. This architectural pattern makes codebases more navigable for agents while reducing cognitive load for humans through strategic abstraction boundaries.

## The Agent Navigation Problem

Agents see codebases as undifferentiated module collections — disparate functions, variables, and components with no mental grouping. While humans understand logical boundaries (authentication, video editing, CRUD forms), agents see only a web of interconnected shallow modules.

This creates three problems: poor feedback loops (no fast feedback), hard navigation (agents struggle to find files and understand testing), and cognitive burnout (humans patch agent/codebase interactions manually).

## Deep vs Shallow Modules

**Shallow modules** have big interfaces with little implementation — many small modules that export frequently and import from each other.

**Deep modules** have tiny interfaces with lots of implementation — large chunks of functionality controlled by carefully designed entry points.

The transition from shallow to deep:
- Many small interconnected modules → Few large modules with simple interfaces
- Difficult to navigate and test → Clear boundaries and test seams  
- Cognitive overhead to understand relationships → Progressive disclosure of complexity

## Gray-Box Module Pattern

Matt's "gray-box modules" establish a ownership model:
- **Human owns the interface** — Design and control the public API
- **Agent owns the implementation** — Delegate internal code to AI
- **Tests keep it honest** — Lock down behavior through comprehensive tests

This creates natural seams where humans focus on design decisions while agents handle implementation details. As long as tests pass, the human doesn't need to inspect the internals.

## Progressive Disclosure for Agents

Each module gets its own folder with a clear public interface. Agents can see all services on the filesystem, read their types, and understand their purpose without digging into implementation.

This provides **progressive disclosure of complexity** — the interface explains what the module does, and agents can drill down into implementation only when necessary.

## Implementation Benefits

**Improved navigability** — Clear module boundaries on the filesystem make codebases self-documenting for agents.

**Reduced cognitive burnout** — Instead of tracking hundreds of interrelated modules, humans manage seven or eight chunks. The mental map becomes radically simpler.

**Better feedback loops** — Modules with clear interfaces are easier to test at appropriate boundaries.

**Agent-friendly architecture** — Good practices that have worked for humans for 20 years also work excellently for AI.

## Language Support

Some languages make enforcing module boundaries easier than others. In TypeScript, boundaries are hard to enforce naturally. Matt increasingly uses Effect.ts because it makes modularizing codebases simple through its service-oriented architecture.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-how-to-make-codebases-ai-agents-love-1ba6d0b5.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-ways-ai-coding-has-rewired-my-brain-dc20954e.md