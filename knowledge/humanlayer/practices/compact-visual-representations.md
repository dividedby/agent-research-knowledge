# Prefer compact visual representations over prose

When an agent needs to *communicate* about code structure, sequence, or
design — not just execute it — ask it to answer in compact visual forms
(component trees, call stacks, state/sequence diagrams, shallow file-tree
layouts, pseudocode, type/signature sketches) instead of walls of
explanatory prose.

Prose forces slow, effortful analytical reading; shape-based representations
exploit fast visual pattern-recognition, so the same information lands in a
fraction of the reading time. The bigger payoff is upstream of that: asking
for a component tree or call stack *before* implementation forces a
discussion of the code's shape — the types, signatures, and call structure —
which is the program-design step teams most often skip when working with
agents. The same forms work in reverse too: post-hoc, to explore a large
diff and decide what to dig into during review.

Concretely, match the form to the artifact: component trees for frontend
state/module boundaries, call stacks for orchestration and backend
control-flow, file-tree layouts (one line of responsibility per entry) for
"where does this live" and refactor scoping, pseudocode for algorithmic
logic, type/signature sketches for interfaces that don't exist yet, and
mermaid state/sequence diagrams for control flow. Diff syntax (`+`/`-`) works
across any of these when most of the shape is unchanged — apply it to a
component tree, call stack, or file layout the same way you'd apply it to
code.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-show-me-skill-758bdab3.md` — origin: https://www.humanlayer.dev/blog/show-me-skill
