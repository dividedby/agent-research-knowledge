# Prototype classification tasks with a general model, then distill the free dataset it left behind

A promptable general-purpose classifier (Goedecke's example is "Jev," a fast
"System One" model, but the same logic applies to structured-output calls
against any general LLM) is worth reaching for even when you know it isn't the
final answer, because using it in production quietly solves the two problems
that normally block a bespoke classifier: nobody on an ordinary engineering
team has the ML skillset to build one, and there's no labeled dataset to train
it on. A prompt sidesteps the first problem outright. Running that prompt in
production against real inputs *is* the second problem's solution — every
call logs an (input, decision) pair, so by the time you're satisfied with how
the general model is performing, you already have the training set for a
bespoke one, assembled as a side effect of shipping rather than as separate
up-front work.

This makes the migration off the general model close to free, and worth doing
once the feature is proven: a hand-built classifier for one specific task will
always be cheaper and faster than a general one, because the general model has
to encode knowledge for every task it might be asked to do, not just this one.
The general model's job was never to be the permanent answer — it's a cheap way
to find out whether the feature is worth a specialized answer at all, without
paying the ML cost up front on something that might not pan out. Only once
that's validated does it make sense to rent or develop the ML expertise a
bespoke model needs.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-system-one-models-can-train-their-own-fd56e9f6.md` — origin: https://seangoedecke.com/system-one-models-can-train-their-own-replacements/
