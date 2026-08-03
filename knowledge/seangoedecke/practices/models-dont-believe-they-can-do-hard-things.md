# Models refuse hard tasks from false modesty, not incapacity

**AI capability is often gated by the model's belief about its own capability,
not by its actual capability.** A model can be able to do something and still
refuse to try, because it has learned (from human training data) that tasks
*sounding* hard should be met with a hedge or a partial attempt rather than a
full try.

Early coding agents showed this constantly: told to review every file in a
codebase, they'd spot-check a handful, decide the full request was
unreasonable, and stop — roleplaying as an overwhelmed human instead of
executing as a computer. The same failure showed up in the trivial case of
asking a model to count from 0 to 100: mechanically easy (each token predicts
the next), yet models would count to ten and then jump to "…99, 100," the way
a bored person would fake it. Goedecke argues this is also the real story
behind the 2025 Apple *Illusion of Thinking* paper, which read reasoning
models' failure to enumerate Tower-of-Hanoi solutions past eight disks as a
reasoning-capability ceiling — but the models' own output ("generating all
those moves manually is impossible") shows they were declining the tedious
work, not failing at it.

**The fix that matters more than prompt wording is persistence plus
reassurance**: when a model gives up or offers a watered-down version of what
you asked, don't accept the easier substitute — restate that you want the hard
version, and explicitly tell the model it's more capable than it's acting
like. This is a cheap, repeatable override for a failure mode that looks like
a capability gap but is actually a confidence gap. It's also why "prompt
engineering" as a distinct technical skill turned out to matter far less than
2025-era hype suggested: if a model is capable of a task, clumsy phrasing
barely affects the outcome — the leverage is in refusing to take the model's
first no for an answer, not in wordsmithing the ask.

By Goedecke's account labs mostly closed this gap through 2025–2026 (moving
"refusal" from a routine coding-agent failure to a rare one), but the
underlying lesson holds for any model that still hedges: suspect self-doubt
before you suspect a ceiling.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-ai-models-need-moral-support-45f2779f.md` — origin: https://seangoedecke.com/ai-models-need-moral-support/
