# Domain expertise, not prompting technique, is the real skill

The skill that determines how much value you extract from an LLM is expertise
in the domain you're prompting for — not a transferable set of prompting
tricks. Because everyone talks to the same model, it looks like "skilled
prompters" get the same results as first-time users, which feeds the belief
that prompting has no skill component. That's wrong: the skill is invisible
because it's domain knowledge wearing a prompting costume.

Terence Tao's public conversation with ChatGPT about a counterexample to the
Jacobian Conjecture makes the gap visible. Goedecke, a skilled programmer but
not a mathematician, "couldn't get to where Tao gets, even with unlimited
tokens to burn" — on the same model. Tao's surface habits are copyable but not
sufficient on their own: short messages that respond to the gist rather than
line-by-line; terse model output, because signalling expertise shunts the
model into "talking-to-mathematicians" mode instead of "explaining-to-amateurs"
mode; indirect pushback ("this looks more complex than I was hoping for")
rather than flat contradiction; and Tao supplying nearly all the next steps
himself rather than taking the model's suggestions. Mimicking the *pattern* of
these moves without the underlying mathematics doesn't reproduce the result —
the leverage comes from actually understanding the domain well enough to pull
the right idea out of a multi-paragraph reply, propose an alternate
formulation, and recognize what "looks weird."

The same mechanism operates one level down, in ordinary codebase work: a good
theory of your own codebase lets you push an LLM much harder than unfamiliarity
does, because you can say "no, I think it could be simpler here," or "but
don't we already do X?," or "can we express this in these familiar terms?" —
challenges that require already knowing the answer's shape. This is a special
case of a broader stance Goedecke holds: system-design problems are dominated
by concrete specifics, not generic principles, so familiarity with a specific
codebase beats a deep general understanding of software systems.

Why this matters: it implies human expertise doesn't get devalued as models
get stronger — it becomes the bottleneck. The information needed for a good
answer is usually already "in the model"; the difficult part is communicating
exactly what kind of solution is wanted, and only a domain expert can do that
precisely. Without domain knowledge you can still get *something* useful out
of an LLM — that's not nothing — but domain knowledge is what lets you wring
far more value from the identical model. Most real work is a mix: expertise in
some areas, none in others, and the prompting leverage tracks which is which.

Pushback on this claim usually points to counterexamples where an inexpert
prompt still produced an expert-grade result — e.g. OpenAI's own
mathematical-discovery prompts weren't written by mathematicians. That doesn't
refute the claim; it relocates the expertise. OpenAI still had a team of expert
mathematicians checking and filtering the model's proposed discoveries before
anything shipped, and that review step isn't currently skippable. When the
prompt itself looks inexpert, look downstream: the domain expertise cost didn't
disappear, it moved to verifying and filtering the output.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-llms-reward-expertise-c0260885.md` — origin: https://seangoedecke.com/llms-reward-expertise/
