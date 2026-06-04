# You are the bottleneck — because accountability can't be automated

Now that machines write code faster than humans can review it, the bottleneck
moves to review and, ultimately, to *accountability*. Ronacher's framing: this
isn't new. Historically, writing code was the expensive part and review felt
slow only because it sat in queues. The industrial revolution did the same dance
— remove the weaving bottleneck and yarn becomes the constraint; speed up
spinning and fibre does — and software did it too, from assembly to high-level
languages. But every prior step sped up *writing* without removing the core
skill of engineering: latency, physics, and algorithmic complexity still bite.

When one stage gets dramatically faster, an accumulating queue forms (OpenClaw
sat at >2,500 open PRs), and the only stable responses are **backpressure and
load shedding**: throttle the input. Pi does exactly this — auto-closing PRs
from untrusted contributors, taking OSS vacations. "You push against your
newfound powers until you can handle them."

But what's the final bottleneck if speed keeps climbing? If the machine writes
the code, the machine must *review* it too — so what reaches a human has already
passed the most capable possible machine review. The residual, irreducible step
is **accountability**: as long as we hold that non-sentient machines cannot be
accountable, a human must be able to understand the output and carry
responsibility for shipping it. Machines will ship relentlessly; humans
rubber-stamp in the morning.

The line Ronacher lands on, and the reason this is a *practice* and not just
commentary: "I too am the bottleneck now. But two years ago, I too was the
bottleneck. I was the bottleneck all along." The machine never changed that —
for as long as you carry responsibility, you are the constraint. This is the
macro statement of [[agent-as-collaborator-you-stay-accountable]] and the
structural reason the [[slop-loops-and-agent-psychosis]] failure mode is
unsustainable: pushing accountability upward, off the individual, is unsolved.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-2-13-the-final-bottleneck-419e6819.md — https://lucumr.pocoo.org/2026/2/13/the-final-bottleneck/
