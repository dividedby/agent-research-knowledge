# Agents as async functions, not remote controls

Once an agent runs in an ephemeral, disposable sandbox, the right mental model
stops being "a remote-controlled version of my local machine" and becomes an
async function call: fire it off, let it run the whole task to completion on
its own, and pick up the result later — in parallel with other calls.

Why the reframe holds: ephemerality removes the two things that made "remote
control" the honest model in the first place — state and resource contention.
A shared build server you SSH into still carries files and jobs left behind by
other sessions; a disposable sandbox doesn't, so it stops mattering whether the
work happens over there or right here. Ball's own analogy: teams moving from a
single shared build server to a VM-based build system didn't change what a
build *is*, but state stopped being a shared, finite resource — and that's what
actually changed behavior. Same shift with agents: once the environment is
disposable and self-contained (it can pull in `ffmpeg` or whatever it needs on
demand instead of requiring a bespoke pre-baked dev setup), the agent needs less
handholding, and you stop caring which machine it's on — you start caring only
about firing off many of them and moving between them.

The load-bearing prompting habit this produces: end the prompt with the whole
loop, not just the task — "...and now run all the tests, fix all the bugs you
run into, then push" — so the agent closes itself out to a working, pushed
state without you supervising the tail end, then switch straight to another
agent while it finishes. Parallelism here isn't babysitting several terminals;
it's dispatching several self-completing async calls and coming back only once
each is actually done.

The shift generalizes past any one person's habit. When Ball's whole team met up
and had to wipe their laptops beforehand, at least five people forgot to port
their dotfiles over — not because anything was lost, but because they'd
stopped touching a local dev environment at all, working entirely in
ephemeral sandboxes. That's the async-function reframe holding at team scale,
not just as one person's workflow trick.

The individual-level mirror of that team story: over two weeks Ball shipped a
new provider backend, an admin bug-triage area, resource-usage warnings across
three services, a hidden browser game with custom assets, a microphone
selector, a hand-written explainer page, and theme preferences — and did every
bit of it in orbs, never touching his local dev environment. The corollary he
flags is affective, not just behavioral: after weeks of not `git pull`ing, doing
it again out of habit starts to feel *"yucky, dirty, unclean"* — the local
checkout has stopped being home base and become the thing that feels foreign.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-90-ac057f6a.md` — *Joy & Curiosity #90* intro: "Agents in Orbs" — remote agents in ephemeral sandboxes reframed as async functions rather than remote-controlled machines; the "run all the tests, fix all the bugs, then push" prompting habit (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-90)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-94-d80affdd.md` — *Joy & Curiosity #94* intro: the Amp team wiping laptops before a meetup and forgetting to port dotfiles because they only work in orbs now (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-94)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-95-0c3b0985.md` — *Joy & Curiosity #95* intro: two weeks of shipped features built entirely in orbs with no local dev environment; local git checkouts starting to feel "yucky, dirty, unclean" (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-95)
