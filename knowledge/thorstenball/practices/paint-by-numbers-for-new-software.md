# Paint-by-numbers: supply the lines, let the agent fill the colors

A concrete mechanic Ball returns to for building something *new*: **you put in the
lines and numbers, then let the agent put in the colors — and you watch to make
sure it doesn't add lines and numbers you don't agree with.** This is the practical
answer to a tension he keeps hitting: agents are now good on a long leash, yet he
still finds himself writing some code by hand or steering tightly when building new.

The diagnosis of *why* is sharp. Agents are bad at writing **confident code** —
code that asserts "*this* is how this works, this can never be null." Instead they
write scared-mouse code full of "but what if this is null? what if the file was
overwritten? what if a client reconnects after a seven-year ping timeout?" And it
compounds: the second time an agent runs over a codebase already littered with
those what-ifs, it rightly concludes anything is possible here and nobody knows how
this works, so it adds *more* defensive questions where there should be statements.

So when the codebase is still blank pages and possibilities, there are no
"statements" yet for the agent to stand on — and supplying them (the lines and
numbers) is still human work. Hand-writing even ten or twenty lines is one good way
to do it, because you only truly bump into what you don't know when you have to
type something out: you write `clients: Client[]`, then stop and realize you never
need multiple clients, so it's `client: Client`. The agent would have silently
picked one.

The crucial nuance: **the lines and numbers might already exist** — in the training
data, in the framework, in the shape of what you're building. On a popular web
framework, there's already a request object, a known way migrations work, a known
restart behavior; plenty of statements are present, so you can let the agent loose.
The challenge with something genuinely new is to figure out what's true about your
idea and codebase, encode it (in the prompt, in types, in tests, in conventions),
and confirm the agent knows it too. Once it does, you can hand back the colors.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-81-09f84489.md` — *Joy & Curiosity #81* intro: paint-by-numbers programming; agents can't write confident code; statements-vs-what-ifs; when the lines already live in the framework/training data (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-81)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-76-cf332424.md` — *Joy & Curiosity #76* intro: writing code by hand to surface what you don't yet know; the `Client[]` vs `client: Client` example (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-76)
