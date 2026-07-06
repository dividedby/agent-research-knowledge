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

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-90-ac057f6a.md` — *Joy & Curiosity #90* intro: "Agents in Orbs" — remote agents in ephemeral sandboxes reframed as async functions rather than remote-controlled machines; the "run all the tests, fix all the bugs, then push" prompting habit (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-90)
