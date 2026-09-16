# The AI "tell" is structure, not vocabulary — editing your way out doesn't work

When you let an LLM dictate the shape of a piece of writing — the paragraph
order, the argument beats, the rhetorical turns — that shape is what AI
detectors actually key on, not the words filling it in. Rewording, trimming,
or even a full from-scratch rewrite that keeps the same outline doesn't
remove the signal, because the outline itself is the machine's fingerprint.

Ronacher tested this directly. He had Opus 5 draft a tweet from a detailed
structural prompt (concede, then reveal the duopoly, then list rapid-fire
rebuttals, then name the commercial self-interest, then close on regulation) —
Pangram scored it 100% AI, unsurprising. He then read the generated text and
rewrote every paragraph himself, no LLM involved in the prose, different
sentences throughout (similarity checkers put the two texts at ~50% overlap)
— but preserving the same structure and argument sequence. Pangram still
scored the human rewrite 100% AI. The only thing carried across both versions
was the skeleton he'd originally specified in the prompt.

This matters beyond the detector-gaming curiosity: it means "I edited it
heavily, so it's mine" is false if the edits only touch word choice. The
outline is the actual unit of authorship — if you want output that doesn't
read as machine-shaped, you have to derive your own structure, not just
reword the one an LLM handed you. It generalizes past prose: the same
mechanic is why heavily-edited AI-drafted code or docs can still read as
templated long after every line has been touched — the tell survives at the
level of structure, not surface text.

## Sources
- `sources/ronacher/blog/https-lucumr.pocoo.org-2026-9-14-interpreting-pangram-501370bd.md` — origin: https://lucumr.pocoo.org/2026/9/14/interpreting-pangram/
