# A fast, cheap classifier model as an agent-loop primitive

Not every decision inside an agent's loop needs a full LLM call: for choosing
among a fixed, known set of options — "should I click here or there," "which
line do I jump to next," "which model should handle this prompt" — a tiny
model trained only to emit typed, probabilistic decisions from unstructured
state (Ball calls Jev "a smart if-statement") does the job orders of magnitude
faster and cheaper than routing the same choice through a generalist LLM.

Why it matters: this class of decision used to require either an LLM call
(slow, priced for open-ended generation, overkill for a fixed choice) or a
custom fine-tuned model — the investment it took to match Cursor's
autocomplete quality while Ball's team built Zed's Edit Predictions. A
purpose-built decision model collapses that to a single ~200ms API call, so
the primitive becomes cheap enough to drop in anywhere a loop needs a
fixed-option pick: Ball had an agent build a shell-autocomplete tool and a
Neovim plugin (`hunch.nvim`) that predicts the next line to jump to, both
powered by the same classifier, and prototyped switching an agent's
underlying model per-prompt (the "Amp Dial") the same way.

The general lesson for agent/harness builders: reserve the full LLM/agent call
for open-ended reasoning and generation, and route the many small "pick one of
N" sub-decisions threaded through the loop to a dedicated fast/cheap decision
model instead — once the latency and cost drop enough, it stops being a
specialized ML investment and becomes a default component you reach for at
every branch point.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-100-5709a014.md` — *Joy & Curiosity #100* opening on Jev, a fast/cheap fixed-choice decision model ("a smart if-statement"): building a shell autocomplete and the `hunch.nvim` next-line predictor with it, and prototyping model-switching via the Amp Dial (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-100)
