# Reroll And Revert Over Repair

Agents are non-deterministic — "slot machines for programmers." The same prompt
yields different results run to run because of temperature. Rather than fight
that, exploit it: your default response to bad output should be to *pull the
lever again*, not to argue the agent into compliance.

## Two moves fall out of non-determinism

If you don't like what came back, re-execute the unchanged prompt before
agonizing over wording — the next roll may just land. And when an agent gets
genuinely confused, revert its work and give it fresh context instead of dragging
a tangled, poisoned conversation forward. A clean slate beats accumulated
confusion almost every time.

## Code is cheap and disposable

Because an agent can regenerate a whole component in ~20 minutes, the sunk-cost
calculus inverts. Ripping the code out and re-prompting is faster and cleaner
than nursing a broken version back to health. Treating generated code as
disposable frees you to explore several avenues cheaply and redirects your scarce
attention onto the genuinely hard parts of the problem.

## It debunks elaborate prompt engineering

The same logic deflates over-structured prompting. Redundant, rambling
explanation that hits the goal from multiple angles outperforms rigid, formal
prompt scaffolding — you're seeding a probabilistic generator, not programming a
deterministic machine. This is the operational twin of
[[just-talk-to-it-minimal-prompting]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-when-ai-meets-madness-peters-16-c80afbe0.md — https://steipete.me/posts/2025/when-ai-meets-madness-peters-16-hour-days/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-the-future-of-vibe-coding-499411eb.md — https://steipete.me/posts/2025/the-future-of-vibe-coding/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
