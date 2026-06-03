# Interpreter As Sandbox And Csp Bypass

To run LLM-generated code in a hostile environment, ship a **statically-bundled JS parser + interpreter** rather than `eval`, `new Function`, or script injection. In a browser extension this buys two things at once.

First, **CSP bypass**: the interpreter and content script are static and serializable, so a site's Content Security Policy can't block them — there's no dynamic code for it to refuse.

Second, **sandboxing by construction**: interpreted code can only touch the scope object you hand it. JailJS uses Babel-standalone to parse, walks an ESTree AST in a big `switch` over ES5, transpiles ES6+/TS down to ES5, and exposes a deliberately minimal global set with `Function` and `eval` blocked.

The honest caveat is that true containment is a Sisyphean cat-and-mouse. Exposing real natives like `document` leaks `defaultView` → `window`; prototype-pollution tricks such as `this.constructor.constructor('return this')` try to climb back to the host. Proxying — or, better, exposing narrow custom functions (`getPageText`, `clickButton`) instead of raw natives — reduces surface, but trades away the model's training-knowledge of native APIs, so the agent gets worse at using them ([[lean-on-model-priors]]).

So the pattern is excellent for **capability injection and CSP bypass**, and adequate as soft sandboxing, but it **cannot be trusted as a security boundary** against a prompt-injected agent.

## Sources
- /home/runner/work/agent-research/agent-research/sources/mariozechner/blog/https-mariozechner.at-posts-2025-10-05-jailjs-f2aeaf25.md — https://mariozechner.at/posts/2025-10-05-jailjs
