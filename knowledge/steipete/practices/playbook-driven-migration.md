# Playbook Driven Migration

For large AI-assisted migrations, a mechanical "convert all of this" prompt yields code that is technically correct but misses the point. The agent reproduces the old idiom in new syntax — XCTest "wearing a Swift Testing costume" — instead of exploiting the target's real capabilities. Correct-but-pointless is the default failure mode, and you have to design against it.

Hand the agent a curated PLAYBOOK instead: before/after patterns, best practices, common pitfalls, and concrete examples. Notably *not* just API docs — that's the thing it needs least, since the API surface is the part it can already infer. This matters most for emerging tech underrepresented in training data, where you must supply the idioms that don't exist in the model's priors yet. See [[feed-agents-current-docs-as-markdown]].

Run it as a tight loop: periodically stop, compile, fix build errors, commit, confirm green locally and on CI, then continue. Long unverified runs let drift accumulate; frequent checkpoints keep it bounded.

Be ruthless about scope precision. "Improve the tests" lets the agent invent new ones; harden it to "refactor the EXISTING tests." The create-vs-convert gap is exactly what an agent fills wrongly when the instruction leaves it ambiguous — it will manufacture work you didn't ask for. When something breaks, paste the raw error verbatim and let the agent fix it rather than pre-diagnosing; your diagnosis just narrows its search prematurely.

Migration also doubles as an architecture-improvement opportunity — the forced pass over every file is a chance to fix structure you'd otherwise never revisit.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-migrating-700-tests-to-swift-te-ddcf01e3.md — https://steipete.me/posts/2025/migrating-700-tests-to-swift-testing/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-live-coding-session-building-ar-6d007535.md — https://steipete.me/posts/2025/live-coding-session-building-arena/
