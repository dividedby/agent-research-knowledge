# Human accountability, not tool provenance, is what governance rules protect

Contribution-provenance frameworks like the Developer Certificate of Origin
(DCO) don't need new rules for AI-assisted code — they were never about *how*
code was produced, only about *who* is answerable for submitting it. A
compiler transforming code in ways you don't track, a template generator, a
Stack Overflow snippet pasted without much thought, and an AI assistant are
all "just another tool" from that angle: the DCO certifies that the
submitter has the right to contribute the code and takes responsibility for
it, not that every line is their unaided personal expression.

This is the answer three independent bodies converged on during the Node.js
DCO debate triggered by a ~19,000-line, AI-assisted core PR (a Virtual File
System built largely with Claude Code): the Linux kernel community (which
created the DCO), Red Hat's legal team, and the OpenJS Foundation all agreed
that AI doesn't break the DCO — accountability does the work the DCO was
always meant to enforce. What *does* change with AI is operational, not
legal: the bottleneck moves from writing the code to reviewing it, so
"I reviewed it" has to mean something concrete and checkable — can you
explain the design decisions, respond to feedback without re-consulting the
model, and maintain the code a year from now. A disclosure convention (an
"Assisted-by" tag, alongside the human's own sign-off) doesn't replace that
accountability — it calibrates how much scrutiny a reviewer applies and
builds trust on top of it. Authorship isn't diminished by using a tool that
executes your decisions: choosing the architecture, shaping the API from
reviewer feedback, and standing behind every line is what makes the
contribution yours, the same way a cook's dish is still theirs for having
used a machine to make the pasta.

## Sources

- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-who-is-responsible-for-827ca361.md` — origin: https://adventures.nodeland.dev/archive/who-is-responsible-for-ai-generated-code/
