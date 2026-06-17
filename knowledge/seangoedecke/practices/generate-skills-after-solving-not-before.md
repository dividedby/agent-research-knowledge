# Have the agent write the skill *after* it solves the problem, not before

LLM "skills" — a short task-specific prompt plus helper scripts — are useful to
agents, but a recent paper found that *LLM-authored* skills provide no benefit on
average. Goedecke's diagnosis: the paper had the model write skills the wrong way —
*before* attempting the task. That's just a dressed-up "make a plan / think step by
step," and current reasoning models already plan before they act, so it adds
nothing. Worse, a skill written up front **bakes in the model's wrong initial
assumptions**.

The correct move is the inverse: **let the agent solve the problem the hard way,
then ask it to write the skill afterward.** The value of an LLM-generated skill is
distilling the *hard-won* knowledge the agent gained by iterating on the problem
for millions of tokens — not the knowledge it already had from training data.

His worked example: getting Codex to clamp features in an 8B open-source model
(à la Golden Gate Claude) took many iterations to discover non-obvious facts —
extract from ~halfway through the layers (the final layernorm is too late), and
train the SAE on far more than 10k activations (until features explain >50% of
variance). Only *after* clamping worked did he have Codex summarize the process
into a skill. A fresh Codex instance then got clamping working on a different model
immediately. Had he asked for the skill at the start, it would have encoded the
wrong assumptions (extracting from the final layernorm) and helped nothing.

The caveat is scope: this is pointless for genuinely one-off tasks — but few tasks
truly are.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-generate-skills-afterwards-283f8f35.md` — origin: https://seangoedecke.com/generate-skills-afterwards/
