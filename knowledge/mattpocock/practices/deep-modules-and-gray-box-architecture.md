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

A shipped counter-example shows the boundary enforced anyway, without Effect's
service model: in `course-video-manager`, each package under `app/packages/` is
treated as a deep module — importable only through its entry points (the
package's root files), with everything under `lib/`/`tests/` private — and the
convention is backed by a `lint:boundaries` check that runs in pre-commit
alongside typecheck. The rule stops being a norm the agent might drift from and
becomes a gate a violating import can't get past, the same "prefer a
deterministic check over a hoped-for convention" instinct as
`deterministic-hooks-over-prose-rules`, applied at the architecture level instead
of the command-safety level.

That one-off repo convention has since been generalised into a shippable
skill, `setup-ts-deep-modules`: it wires [dependency-cruiser](https://github.com/sverweij/dependency-cruiser)
into any TypeScript repo with four `error`-level rules — outsiders may import
only a package's root files, a package's own files import each other freely,
tests may cross into any package's entry points but never subfolder internals
(not even their own), and no dependency cycles — so *any* subfolder is
private, not just a hardcoded `lib/`, and a new folder never needs a config
change. Its completion criterion is the tell: **"prove the rules bite"** —
temporarily add a deep import, run the lint, confirm it *fails*, revert, confirm
it passes again. A boundary config that has never been observed to fail on a
violation is unverified, not enforced; this closes the same gap `feedback-loop-is-the-work`
names for tests — a check that has never gone red hasn't proven it can.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-how-to-make-codebases-ai-agents-love-1ba6d0b5.md
- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-ways-ai-coding-has-rewired-my-brain-dc20954e.md
- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md (revision 2026-07-11, "Deep-module packages")
- `sources/mattpocock/skills-repo/skills-in-progress-setup-ts-deep-modules-SKILL.md-818cdfcd.md` — origin: https://github.com/mattpocock/skills/blob/391a2701dd948f94f56a39f7533f8eea9a859c87/skills/in-progress/setup-ts-deep-modules/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-07-11, origin https://github.com/mattpocock/skills/blob/85804e72bbb83120b3becba0edd22b91abf3aa52 — `setup-ts-deep-modules` listed)