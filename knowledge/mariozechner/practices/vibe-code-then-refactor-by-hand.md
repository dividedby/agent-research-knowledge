# Vibe Code Then Refactor By Hand

Vibe-coding — letting the agent write 100% of it — is the right move for getting a
working prototype fast, but it is explicitly a *first* iteration, not the finished
artifact. Zechner shipped a project's initial codebase fully vibe-coded to prove
the concept, then spent a dedicated night refactoring it by hand and with the
agent so it would actually be extensible going forward.

The pattern is a deliberate handoff: agent for speed-to-working, human-led
refactor for the structure and maintainability the agent's statistical-mean output
won't give you. An LLM regresses toward the average solution; the architecture
that makes a codebase pleasant to extend is precisely the part that requires taste,
and taste comes from doing the work yourself ([[friction-builds-understanding-and-taste]]).
Treat the vibe-coded version as a thrown-together spike that earned the right to
exist, then pay down its structure on purpose before it calcifies.

A related move: when you'd rather ship in a different language than the reference
implementation uses, re-implement it — using the agent to port for feature parity —
rather than inherit an ecosystem dependency you dislike. The agent makes the port
cheap enough that the choice of stack becomes yours again instead of being dictated
by whatever the original happened to be written in. Speed from the machine,
direction from the human.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-05-30-shitty-robot-30be0b1b.md — https://mariozechner.at/posts/2026-05-30-shitty-robot
