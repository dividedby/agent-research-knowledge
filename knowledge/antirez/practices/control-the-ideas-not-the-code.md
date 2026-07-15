# Control the ideas, not the code

Once you trust the model, reading its output line-by-line is often the wrong
place to spend your attention. antirez's claim, stated bluntly: many
programmers now have *less* impact than they could, because they still look
at the code. The scarce resource isn't code-reading time — it's the design in
your head. If you control the ideas of the software, scanning the
implementation is frequently pointless.

Three reasons this isn't just a productivity shortcut:

1. **Volume.** LLMs can generate far more code than one person can review —
   nobody is reviewing 5,000 lines a day at real depth, model verbosity or not.
2. **The wrong grain.** LLMs write locally-optimal code and are comparatively
   weaker (though improving) at big ideas. Scanning function by function checks
   the grain the model is already strong at. It's faster and more informative
   to interrogate the design directly — prompt the model to explain "how does
   this part actually work?" and judge whether *that* model of the system is
   right — than to reconstruct the design by reading implementation line by
   line.
3. **Opportunity cost.** The working day is fixed at 8 hours. Time spent
   reading code is time not spent asking "what am I actually doing with this
   software, what direction should it take next" — plus doing QA. That
   thinking-and-testing work is what's structurally under-invested, not code
   review.

He holds himself to this and still finds it uncomfortable: he still reviews
every line of Redis's AI-generated code, line by line, but no longer believes
the review itself is where the value is — he keeps doing it "out of respect
for users" (many programmers still open Redis files and hand-modify them), not
because it catches more than the alternative. By his own account, a frontier
model's review pass on the same diff surfaces *more* subtle errors and race
conditions than his manual read does. If he had his hands free, the review
time would go to more QA and the next design idea instead.

The forward-looking replacement for code-as-source-of-truth: use an LLM to
write a **DESIGN.md** per data structure or subsystem — the ideas it embodies,
the implementation tricks, the design in human language — rather than relying
on future readers reconstructing intent from the diff. A future maintainer (or
their agent) opens the design doc, gets the right mental model, and asks their
agent what to do — a faster and more reliable path to "owning the ideas" than
reviewing the code that implements them.

This isn't vibe coding — vibe coding is *not* controlling the ideas at all,
just accepting the model's first design. The point here is the opposite: hold
the design tightly, but stop mistaking reading the implementation for holding
the design.

## Sources

- `sources/antirez/blog/http-antirez.com-news-169-b872d6d4.md` — origin: http://antirez.com/news/169
