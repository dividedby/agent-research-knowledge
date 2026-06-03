# Yolo By Default Sandbox Theater

Agent permission prompts and command pre-checks are mostly security theater. Once an agent can both write and run code, the trifecta of read-data / execute-code / network access makes exfiltration unstoppable short of cutting all network access — which guts usefulness — or fragile, endless domain allow-listing. Even Simon Willison's dual-LLM pattern is, by his own admission, "pretty bad" and hugely complex to implement.

Zechner's stance follows from this: since everyone runs YOLO mode to get real work done anyway, the prompts are friction that buys little. `pi` makes YOLO the default and only mode — full filesystem access, any command, no Haiku malice scan — and tells you plainly to run it in a container if you want real isolation. The honest move is to stop pretending guardrails work and instead make the threat model explicit: `curl` and file reads remain live prompt-injection surfaces, and no permission dialog changes that.

The deeper principle is that fake safety is worse than acknowledged risk. A prompt that asks you to approve a command you can't fully reason about trains you to click "yes" while giving an illusion of control. Better to name the actual boundary — the container, the network cut — and put real isolation there, rather than scattering theatrical checks across every tool call. Defaulting to YOLO is not recklessness; it is refusing to launder an unsolved problem as a solved one.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
