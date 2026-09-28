# Pepper agents with small clarifying questions in real time, not a batched review

Interrupt an agent's plan with short confirmation questions the moment
something sounds vague, rather than waiting to review the finished output —
the same discipline good listeners apply to human conversation ("so when you
say X, you mean Y?"), because a small misunderstanding compounds: everything
built on top of it becomes a misunderstanding in its own right, and by review
time it's tangled into a much larger error to untangle.

This matters more for agents than for reliable human collaborators because
agents fail differently now. Frontier models rarely make *code* mistakes
anymore — but they make *design* mistakes constantly: assuming two services
can talk when they can't, forgetting a constraint like dual cloud/on-prem
deployment. The cause is structural, not a capability gap: a model has no
continuous learning, so on every task it is effectively on its first day on
the system, without the incidental tenure a human picks up over weeks. Design
assumptions are exactly what tenure would normally correct, and nothing
catches a wrong assumption before it compounds except someone probing for it
while the plan is still being formed.

The concrete technique: ask small, specific questions aimed at the design, not
the code — "do we do X elsewhere in this codebase?", "does this service really
support that auth, or are you assuming we'd build it?", "why do we need to
touch this file at all?" — the moment a claim sounds suspiciously vague, rather
than batching questions for the end. Treat the hit rate as the signal for how
much vigilance is still warranted: today, roughly half of these questions turn
up a genuine mistake — reuse an existing subsystem, wrong auth path, an
unnecessary change — which is high enough that asking constantly is worth the
interruption; stop interrogating this hard only once that rate drops toward
zero.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-you-should-all-be-asking-way-more-que-4dfe7b0d.md` — origin: https://seangoedecke.com/you-should-all-be-asking-way-more-questions/
