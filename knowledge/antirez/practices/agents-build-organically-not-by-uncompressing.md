# Agents build organically — the "uncompressed copy" is a myth

A mental model antirez insists you internalize before reasoning about agent output:
a coding agent does **not** "uncompress" memorized code from its weights. Watching
one work makes this obvious — it builds the way a human does. In his clean-room
Z80/ZX-Spectrum experiment the agent implemented instruction classes
incrementally, wrote its own instrumentation to "look" at what the emulated CPU was
doing step by step, hit bugs, and fixed them through integration tests, debugging
sessions, dumps, and printf calls. The result passed ZEXDOC/ZEXALL in ~1200 lines
of readable C, and a separate adversarial session (Claude Code *and* Codex) tasked
with finding evidence of theft against every major Z80 implementation found none.

His evidence that it's assembly-of-knowledge, not retrieval: the *assembler* — the
most mechanical, most memorization-friendly step — is precisely where Anthropic's
clean-room compiler agent *failed*; yet with good documentation he can't see how an
agent could fail it, because it's a mechanical process the model can reason
through. Models can reproduce *over-represented* documents verbatim if explicitly
asked, but in normal operation they don't carry or spontaneously emit copies of
everything they saw; they assemble known techniques and patterns into new code.

Two consequences he draws:

- **Reimplementation is fair and organic, not copying.** Used to rewrite an
  existing system, agents "write the software in a very organic way, committing
  errors, changing design many times because of limitations that become clear only
  later, starting small and adding features progressively" — and you steer that
  chaos heavily with your prompts. You can even hand the agent the source purely so
  it can drive *away* from it, then have an agent verify no protected expression
  survived. Copyright protects expression, not ideas/behavior; the "uncompressed
  copy" fear is "consolatory because it's false."
- **Steering changes the result, so almost-zero-steering experiments mislead.**
  "Even never touching the code, a few hits here and there completely changes the
  quality of the result" — which is why he found Anthropic's near-zero-steering
  compiler run uncharacteristic of how agents are actually used. His own clean-room
  rule was about *information provenance* (no internet, no other source code during
  implementation), not about withholding *steering*: he steered the Spectrum's TAP
  loading extensively while keeping the implementation clean-room.

Because the output is genuinely new code assembled under his direction, he ships
automatic-programming work MIT-licensed without hesitation.

## Sources

- `sources/antirez/blog/http-antirez.com-news-160-3eec660b.md` — origin `http://antirez.com/news/160` (the Z80/Spectrum/CP-M clean-room experiment; organic incremental building; the assembler-failure argument against memorization)
- `sources/antirez/blog/http-antirez.com-news-162-5272d862.md` — origin `http://antirez.com/news/162` (AI reimplementations: organic rewriting, the "uncompressed copy" illusion, copyright on expression not ideas)
