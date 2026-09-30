# AI for code, not for prose — the reader's social contract

Brooker draws a sharp, deliberate line: he is "100% comfortable" with AI-generated
*code* but refuses to publish AI-generated *prose under his name*. The asymmetry is
the point, and it follows directly from his view of what code is *for*.

## The line

- **Prose:** none of the human-readable text on his blog (or his work docs) is
  AI-written, by policy. He uses agents heavily *around* writing — brainstorming,
  research, summarizing, fact-checking, markup, finding references, analyzing data
  — and for editing/critique (but *less* than he used to, because over-use breeds
  a defensive "block every exit" style that obscures communication, the same way
  writing to pre-empt bad HN/Reddit comments does).
- **Code:** almost all the code on his blog over the last two years is 100% AI-
  generated, "mostly vibe-coded slop, to be honest," and he's comfortable heading
  to a world where code is *opaque to humans* and all that matters are its
  *properties*.

## Why the asymmetry

The reasoning hinges on what each artifact is *for*. Publishing prose under your
name is a **social contract**: it signals you deeply understand and own what you
wrote and that you respect the reader's time, in exchange for their full
engagement. AI-generated prose breaks it — if you generate a doc from a prompt and
the reader summarizes it back down with their own LLM, nothing was achieved; you
could have just sent the prompt and let them explore with their own agent (a
better use of their time). As an org leader he wants *function over form*: "if you
have half a page of thoughts, give me half a page" — don't pad to five with
Claude's thoughts; if he wants Claude's opinion he'll ask for it himself, with his
own context.

Code is different because he no longer believes code primarily exists to **share
ideas between people**. He held that belief deeply three years ago and has since
abandoned it: sharing ideas between people remains vital, but there are now better
vehicles for it, free of the accidental complexity of a codebase (this is the same
move as raising the abstraction to specification — see
`specification-is-the-future-of-programming.md`). So code can be opaque slop as
long as its properties hold; prose cannot, because prose *is* the idea-sharing
medium whose value is the human ownership behind it.

## The bar is conditional on the project's purpose

"Comfortable with opaque code" is not unconditional — it's calibrated to *why*
the project exists. Building a small ML classifier for his own education, he let
an agent write every line, but at each step made sure the core ideas and
insights were his, or at least that he understood them: "I might not set such a
bar for a project at work, but for this project the outcome was mostly about me
learning." When the point of a project is to ship working properties, opacity is
fine (the core claim above); when the point is to *learn* the domain, he
deliberately raises the bar back up, using the agent less as an opaque author and
more as an on-demand tutor — asking it to step him through concepts and then quiz
his understanding, "like having a custom textbook about exactly this problem at
just the right level." The lesson generalizes: don't apply one fixed
comfort-with-opacity setting everywhere — set it per project, based on whether
the artifact or the understanding is the actual deliverable.

## Sources

- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-06-18-my-blog-and-ai.html-9a7ec3a0.md` — origin: https://brooker.co.za/blog/2026/06/18/my-blog-and-ai.html
- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-09-28-engineering-system-one.ht-efc2d098.md` — origin: http://brooker.co.za/blog/2026/09/28/engineering-system-one.html
