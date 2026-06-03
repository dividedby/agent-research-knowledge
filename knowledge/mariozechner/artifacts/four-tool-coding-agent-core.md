# Four Tool Coding Agent Core

An effective coding agent needs only four tools: **read**, **write**, **edit** (exact-match old/new text), and **bash**. Frontier models are RL-trained so heavily on coding harnesses that they inherently understand the role — bash subsumes `ls`/`grep`/`find`, and the file tools mirror schemas the model already knows. pi ships an optional read-only set (grep/find/ls) only to *restrict* the agent to exploration; it is disabled by default.

Paired with a sub-1000-token system prompt (tool list + a few guidelines, with `AGENTS.md` appended at the bottom), this core beats the ~10k-token prompts of Claude Code and opencode while holding its own on Terminal-Bench. The result is corroborated by Terminus 2 — a bare tmux interface with *no* tools at all — ranking competitively. The thousands of prompt tokens and dozens of tools that other harnesses ship are largely redundant with what the model already learned in training: they re-explain a job the model was trained to do, paying context tokens for the privilege.

The takeaway is that capability lives in the model, not the scaffold. Every tool and prompt line beyond the four-tool core should justify itself against the model's priors before being added. See [[minimal-harness-by-subtraction]] and [[lean-on-model-priors]].

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-11-30-pi-coding-agent-7c72f309.md — https://mariozechner.at/posts/2025-11-30-pi-coding-agent
