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

## Sources

- `sources/mattpocock/sandcastle/CONTEXT.md.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/CONTEXT.md