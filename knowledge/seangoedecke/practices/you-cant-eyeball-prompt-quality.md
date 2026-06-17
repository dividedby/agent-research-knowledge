# You can't eyeball prompt quality — build a benchmark

The famous o3 "GeoGuessr" prompt — an elaborate, iteratively-grown prompt that
supposedly unlocked o3's ability to geolocate photos — **did not actually help**.
Goedecke built a 200-image benchmark (Wikimedia Commons, Geograph, iNaturalist),
ran o3 against it twice (fancy prompt vs. a plain "think carefully about where this
was taken"), and the basic prompt did *better* on average despite the fancy prompt
being 10x longer. o3 was already good at the task; the elaborate prompt rode on the
model's baseline ability and got the credit.

The transferable lesson is a discipline for working with agents: **when a model is
already decent at a task, you can pile on an elaborate prompt without changing
performance, and easily fool yourself that the prompt is doing the work.** Two
failure modes compound this:

- **Vibes-based evaluation.** Playing around in a chat window can't distinguish "the
  prompt helped" from "the model was going to get it anyway." The only honest answer
  is a benchmark: a fixed eval set run with and without the change. Benchmarks can
  mislead too, but they beat vibes.
- **Asking the model to grade itself.** Iterating by asking the model "what should I
  add to fix this mistake?" and "did that tweak help?" is worthless — models happily
  invent stories about their own reasoning and almost always say "yes, that helped a
  lot." This is exactly how the GeoGuessr prompt was grown, and exactly why it
  didn't work.

A secondary observation: the benchmark was cheap to build (≈6 hours, ≈$15) *because*
a strong agent did the heavy lifting — the same agent capability that makes prompts
hard to evaluate by feel also makes the rigorous check nearly free, so there's
little excuse not to run it.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-the-o3-geoguessr-prompt-did-not-work-d8c46783.md` — origin: https://seangoedecke.com/the-o3-geoguessr-prompt-did-not-work/
