# Hallucination is two failure modes, not one

"Confidently-wrong model output" splits into two flavors with different causes,
and naming them separately matters because they trace to opposite knowledge
gaps. **Factuality** hallucination invents facts: the model has no contextual
knowledge to ground the answer — a fact past its knowledge cutoff, an
unfamiliar API — and its parametric knowledge fills the gap with a
plausible-sounding guess instead of an honest "I don't know." **Faithfulness**
hallucination is the opposite failure: the correct information is already
sitting in the loaded context, and the model drifts from or contradicts it
anyway.

The distinction routes the fix. A factuality gap is closed by loading more —
docs, search results, primary sources — so the model has real contextual
knowledge to ground on instead of a parametric guess. A faithfulness gap isn't
a knowledge problem at all; the fact was already present, so loading more
context doesn't help. Treating both as "the model made something up" and
reaching for the same fix (dump in more context) helps one failure mode and
does nothing for the other.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md` — origin: https://www.aihero.dev/ai-coding-dictionary
