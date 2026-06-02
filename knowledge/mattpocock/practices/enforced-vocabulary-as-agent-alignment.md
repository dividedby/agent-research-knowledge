# Enforced vocabulary: precise language as a coordination mechanism

Sandcastle maintains a comprehensive vocabulary defined in `CONTEXT.md` that establishes exact terminology for every concept in the system, paired with explicit "avoid" terms that are forbidden. This isn't documentation — it's a coordination mechanism that ensures agents, maintainers, and users speak the same language about the same concepts, preventing drift and ambiguity that degrades both human and agent effectiveness over time.

## Vocabulary as operational consistency

The vocabulary defines not just what to call things, but what NOT to call them. "Agent" is the AI coding tool; avoid "RALPH", "the bot", "Claude" (too specific). "Sandbox" is the isolation boundary; avoid "container" (too specific), "Docker sandbox" (ambiguous with Claude's feature), "workspace". Each concept gets one canonical term and a blacklist of alternatives that cause confusion.

This precision serves agents more than humans — an agent that sees "container" in one place and "sandbox" in another will treat them as potentially different concepts, leading to confused reasoning. Humans can bridge synonym gaps; agents cannot reliably do so without explicit instruction.

## Context-scoped precision prevents namespace collision

The vocabulary is deliberately bounded to the Sandcastle context. "Branch strategy" means the configuration controlling how agent changes relate to branches within this system; it doesn't claim to define branching strategies globally. "Host" means the developer's machine where Sandcastle runs; it's not a networking or deployment term.

This scoping prevents the vocabulary from becoming too generic (useless) or too broad (unmaintainable). Each term is defined precisely enough to be operationally useful within the problem domain without trying to encompass all possible meanings across all contexts.

## Lifecycle boundaries get explicit names

The vocabulary assigns distinct names to conceptually different phases that might otherwise be conflated. "Iteration" is one agent invocation producing at most one commit; "run" would be ambiguous with the `run()` function. "Source branch" is where the agent works; "target branch" is where merge-to-head merges to. "Bind-mount sandbox provider" versus "isolated sandbox provider" capture fundamentally different data flow patterns.

These distinctions matter operationally — the difference between bind-mount and isolated determines whether data flows via filesystem mounts or git sync, affecting everything from performance to failure modes.

## Progressive disclosure through enforced consistency

Rather than frontload all vocabulary, the glossary works through progressive disclosure — agents encounter terms just-in-time and can trust that the same term always means the same thing. An agent seeing "worktree" in an ADR and "worktree" in the code can confidently assume they refer to the same concept defined in `CONTEXT.md`.

This consistency makes the vocabulary a navigation aid rather than a burden. Agents can explore by following terms between documents, knowing the vocabulary forms a reliable map rather than a collection of locally-defined synonyms.

## Anti-drift through explicit forbiddance  

The "avoid" lists aren't suggestions — they're architectural constraints that prevent terminology drift. "RALPH" is banned not because it's unclear, but because using it alongside "agent" fractures the conceptual model. "Workspace" is forbidden because it's too ambiguous across different tools and contexts.

This negative space is as important as the positive definitions. It closes off attractive but problematic alternatives that would slowly erode the vocabulary's precision if allowed to creep in through casual usage.

## Domain vocabulary scales to comprehensive coverage

The course-video-manager project demonstrates the ultimate evolution of this practice — a 750-line domain vocabulary covering every concept from course structure to video export, with multiple revisions tracked over time. Terms like "Ghost Lesson" (database entity without filesystem presence), "Materialization Cascade" (chain reaction creating on-disk representations), and "Export Hash" (SHA256 determining re-export need) show the precision possible when vocabulary discipline is applied comprehensively.

This scale reveals the practice's true power: once agents and humans share exact language for every domain concept, complex reasoning becomes possible. The agent can distinguish "Ghost Section" (derives real-ness from containing real lessons) from "Materialize" (creating on-disk representation) without conceptual drift, enabling sophisticated domain reasoning that would be impossible with loose terminology.

## Mature entries carry the contract, not just the name

A later course-video-manager revision shows the glossary outgrowing pure
term↔synonym mapping: the entries now encode each concept's *behavioral
contract*. The most load-bearing axis is **derived vs stored** — "Pitch State",
"Deliverable Status", and "Video Warning" are each explicitly *derived, never
stored*, while "Lesson Authoring Status" and "Export Hash" are explicitly
persisted. Entries also state cross-entity invariants ("Lesson Authoring Status"
is in a biconditional with `fsStatus` — a real lesson always has a status, a
Ghost Lesson never does), give whole algorithms when a term names one
("Dependency Group" is defined as a within-section, contiguous, directed-backward
walk), and pin the rule to the implementing code ("Ghost Section" real-ness is
"never inferred from the path prefix — see `sectionHasRealLessons` in
`section-path-service.ts`"). Declaring where a value's truth lives — derived on
read vs written to a column — is exactly the disambiguation an agent needs before
it can safely reason about or mutate state, so the glossary becomes the home for
those rules rather than leaving them to be re-discovered in the code each session.

## Revision tracking preserves vocabulary evolution

Domain vocabularies evolve as understanding deepens, and Matt tracks these changes through revision fingerprints within the same document. The course-video-manager CONTEXT.md shows three revisions across dates, capturing how concepts like "Pitch Desk State" evolved into "Pitch State" and how definitions became more precise over time.

This evolution tracking serves both historical context and operational clarity — agents can see not just what terms mean now, but how they've changed, preventing confusion when encountering older usage in code or documentation.

## Sources

- `sources/mattpocock/sandcastle/CONTEXT.md.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/CONTEXT.md
- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md