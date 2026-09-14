# As models get faster, dev-loop speed becomes the agentic bottleneck

Developer experience currently gets measured in seconds because the dominant
wait is thinking time — you're waiting on the model, not the tools around it
— so shaving milliseconds off a dev-server reload or file read is pointless
when it's not the bottleneck. That assumption breaks as inference speed rises:
a model generating at tens of tokens per second makes you wait on it like a
slow colleague, but ultra-fast inference (purpose-built chips running small
models at thousands of tokens per second) collapses generation time toward
zero. Once the model isn't the bottleneck, whatever *is* slow becomes the
whole story: reading a file in 100ms vs 10ms, or running tests in 500ms vs two
seconds, becomes the difference between a near-instant response and a
multi-minute wait.

This reframes tool and language choice for agentic codebases: there will be
real pressure toward fast-compiling, fast-testing languages (Golang is the
example) and toward tightly optimizing the dev loop specifically for agent
tool calls, not just human convenience. It also predicts a return of DevEx as
a discipline — largely cut down or eliminated through the 2010s once
companies stopped prioritizing engineer happiness — but this time justified by
agent throughput rather than developer happiness. The mechanism is durable
even if today's numbers are a preview: the model side of the wait keeps
shrinking, so investment that used to be wasted on shaving tool latency stops
being premature.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-slow-devex-will-bottleneck-fast-model-c7da4b62.md` — origin: https://seangoedecke.com/slow-devex-will-bottleneck-fast-models/
