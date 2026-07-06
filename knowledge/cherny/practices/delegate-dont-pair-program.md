# Delegate, don't pair-program

The mental-model shift the Claude Code team pushes for newer models (Cat Wu on
Opus 4.7): "The model performs best if you treat it like an engineer you're
delegating to, not a pair programmer you're guiding line by line."

The **old loop** was high-interrupt: describe a step, watch the output, correct,
describe the next step — you are always in the loop. The **delegation loop**
front-loads everything the agent needs and then gets out of the way. The two
halves:

- **Full-context brief upfront.** Give Claude the *goal, constraints, and
  acceptance criteria in the first turn.* With all three, it plans around the full
  problem space; with just "add rate limiting," it makes assumptions you'll have to
  correct later — and **every correction costs context.** Write detailed specs and
  reduce ambiguity before handing work off; the more specific you are, the better
  the output.
- **Read the symptoms correctly.** When Claude asks too many clarifying questions
  or goes off-track, that's usually a signal your *brief was incomplete* — not that
  the model needs more hand-holding. The fix is a better brief, not tighter
  supervision.

This pairs with longer default reasoning (effort levels up to `xhigh`, adaptive
thinking): "think harder once, rather than iterate fast and bounce back to you."
It is also the post-plan-mode form of front-loading clarity — see
[[plan-first-then-context-minimalism]]. And it only works because the agent can
check itself; see [[verification-is-the-number-one-tip]].

The earliest form of this trade is Cherny's own model default: he runs **Opus
4.5 with thinking mode on for every task**, reasoning that "less steering +
better tool use = faster overall results" even though a bigger model with
thinking is slower per token. Spending more compute up front — a bigger model,
more thinking, a fuller brief — buys back the steering cost later; the effort
levels above are the same trade, made adjustable.

A concrete delegation idiom Cherny endorses: instead of micromanaging *how*, hand
over the *what* — "Go fix the failing CI tests," or paste a Slack bug thread and
just say "fix." Make Claude your reviewer ("Grill me on these changes and don't
make a PR until I pass your test"; "Prove to me this works"). After a mediocre
fix: "Knowing everything you know now, scrap this and implement the elegant
solution."

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
