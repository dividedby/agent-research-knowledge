# Context Gathering Before Implementation

Mid-session sub-agents for context gathering are a smell. They signal you didn't plan ahead, and they're a black box within a black box: zero visibility into what they read, poor context transfer back to the parent, and painful debugging when the result is wrong. You've delegated the most important step — deciding what the model sees — to something you can't observe or steer.

The right move is to gather context **first**, in its own observable, steerable session. Distill it into an artifact, then start a fresh implementation session seeded with that artifact. The artifact is reusable: the next feature in the same area starts from the same distilled context instead of re-deriving it.

This matters because models are still poor at finding all the context they need. Trained to read file *fragments* rather than whole files, they miss things ([[agentic-search-recall-degrades-with-size]]) — so trusting an opaque sub-agent to gather context compounds a failure mode you can't even see. Doing the gathering in the open lets you catch the gaps.

`pi` accordingly has no sub-agent tool. If you genuinely need one, you ask `pi` to run itself via bash — optionally inside `tmux` for full observability — so even the nested agent stays inspectable. Spawning many parallel sub-agents to build features is an anti-pattern that produces garbage codebases: each one is an unsteered black box, and you can't merge what you couldn't watch. Separate the observable "understand" phase from the "build" phase, and keep the seam an artifact you can read.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-08-15-mcp-vs-cli-c4a760c5.md — https://mariozechner.at/posts/2025-08-15-mcp-vs-cli
