# Choosing an effort level

`/effort` is a compute dial, not a quality dial: it buys more independent
judgement and self-verification, not a smarter model. Thariq's framing (Claude
Code) is a time budget handed to a person — told to finish in 12 hours, they try
hard and use their own judgement; told to finish in 1 hour, they hand you the
best version that fits and expect you to iterate. Claude behaves the same way:
"higher effort will involve Claude taking more independent action for judgement
and verification," not more raw capability.

**Match the level to how much you want to stay in the loop, not to task
difficulty alone.** Thariq's rule of thumb on Opus 5.5 / Fable 5.1:

- **low** — sketching, brainstorming, an easy change; quick responses that keep
  you in the loop.
- **medium** — regular day-to-day feature work; the default for most software
  engineering.
- **high** — fixing a bug or chasing edge cases, where verification matters (e.g.
  a brownfield bug fix).
- **max** — full autonomous hand-off on hard problems: end-to-end build and
  verification, or finding security vulnerabilities. "Basically only if I want
  zero input."

The **why**, from Terminal-Bench 3.0 runs comparing low vs. max on the same
tasks: extra effort overwhelmingly closes the "missed a case" failure bucket
(edge cases the low run never tested for) but barely moves "made the wrong
call" — a model that picked the wrong approach doesn't get un-wrong by thinking
longer about it. So effort is worth spending on tasks with **many hidden edge
cases and no one watching**, not on tasks blocked by an architectural
misjudgment — that needs a better brief or a fresh attempt, not more compute.
Sensitivity also varies sharply by domain: security and hardware tasks gained
20-40 points of pass rate from low→top effort, while rule-following
"operations" work barely moved — cranking effort on a task that's already well
specified just burns tokens.

A recurring high-leverage shape for feature work: **interview at default, build
at low, verify at high.** Have Claude interview you on the spec first, implement
at low effort while you're actively checking the gist and iterating, then switch
to high effort for the verification pass — because switching effort **does not
break the prompt cache**, so raising it just for the check is free to try mid-
conversation.

This sits underneath [[delegate-dont-pair-program]]'s "think harder once instead
of bouncing back to you" and pairs directly with
[[verification-is-the-number-one-tip]]: effort is the dial that decides how much
of that self-verification loop Claude runs before it hands work back.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
