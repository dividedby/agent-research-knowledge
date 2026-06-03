# Local Models For Private Agents

A capable voice agent can run **entirely on local hardware** — an M1 Max with 64GB — and it's worth the effort specifically when privacy matters: here, a kid talking to a toy, where nothing should leave the device.

The concrete stack: a small **MoE LLM** served by `llama.cpp` (which handled up to four simultaneous users out of the box); a fast **STT** model (Parakeet TDT, int8 ONNX, ~50x real-time); and a cloning-capable **TTS**.

The hard part isn't the LLM — it's the **speech-to-speech UX**. Two pieces carry it. First, **streaming the LLM's first complete sentence to TTS** via a regex sentence chunker, so audio starts playing before the model finishes generating — otherwise latency feels broken. Second, a **custom barge-in detector**: a ring-buffer reference plus correlation against the speaker bleed, built from scratch because off-the-shelf echo cancellation degraded the audio below STT-usable quality. Off-the-shelf wasn't a shortcut; it was a regression.

Architecturally, inference workers talk to the server over **stdio with simple binary framing**, which keeps each worker swappable and self-contained — you can replace the STT or TTS model without touching the orchestration. The lesson is that local, private agents are achievable today on consumer silicon; the cost isn't model capability but the real-time audio plumbing around it.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2026-05-30-shitty-robot-30be0b1b.md — https://mariozechner.at/posts/2026-05-30-shitty-robot
