# Skills need a token-free, harness-agnostic import syntax

Matt's standing design complaint about the current skills model is that there is
**no way for one skill to reference another without paying a context-load cost**.
Today the only handle a skill has on a sibling is its `description`, which loads
every turn (see `invocation-axis-user-vs-model`). What's missing is a separate
**import** affordance — distinct from `description` — that lets a skill point at
another skill *without* dragging that skill's body or trigger phrasing into
context.

## A flat set of importable modules, not a tree

The right mental model, Matt argues, is **not a tree of parent/child skills** —
where a sub-skill's description only enters context after its parent fires — but a
**flat set of modules that can import each other**, the way code modules do. He is
explicit about what the feature is *not*: it should not "automatically load the
other into context." It's a *pointer*, resolved on demand, not eager inlining.
The single sentence he reduces it to: **skills need to be able to import other
skills without imposing a token cost.**

## The harness resolves the link before the model sees it

His proposed mechanism keeps the resolution out of the model entirely. The author
writes a bare invocation in a skill body:

```
Invoke /skill-name
```

and the **harness rewrites it, before sending to the model**, into a path link:

```
Invoke [/skill-name](../path-to-skill/SKILL.md)
```

So the import is a *harness-agnostic syntax* the author can rely on across
harnesses — currently "there's no way to do it" — and the cost is paid only if
the agent actually follows the link (the extra turn to read the file), never as
standing description load. The catch he names himself is **relocation**: a raw
relative path breaks if the skill moves, which is why this wants to be a first-
class linker/installer concern, not hand-written paths.

## Why the workaround solutions are rejected

Matt has dismissed the proposed alternatives, each for a concrete reason:

- **Copy shared skills into each skill's `references/` (or git submodules).**
  Forces duplication across every consumer and "git submodules is a grim
  solution." His counter-pointer: distribution mechanisms like `npx skills add`
  already exist for sharing — duplication shouldn't be the answer.
- **Keep skills model-invocable with a "don't invoke unless asked" description.**
  Still loads the description every turn — "the token waste of that approach [is]
  very annoying."
- **Route each skill in its own isolated context with the harness handling
  routing.** Matt calls building this "overkill" — the import is a lightweight
  pointer, not a whole sub-agent routing layer.

This is a wishlist for the skills *substrate* rather than a built artifact, but it
sharpens the design constraint the rest of his skill conventions already dance
around: composition must not cost context load.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067533288017715471-7ee925d2.md` — origin: https://x.com/mattpocockuk/status/2067533288017715471
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067533513042128977-677489d3.md` — origin: https://x.com/mattpocockuk/status/2067533513042128977
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067535125064073513-84d61550.md` — origin: https://x.com/mattpocockuk/status/2067535125064073513
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067539408274755642-5760d46a.md` — origin: https://x.com/mattpocockuk/status/2067539408274755642
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067556500441084282-e310c6f3.md` — origin: https://x.com/mattpocockuk/status/2067556500441084282
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067594606963740880-a38b569f.md` — origin: https://x.com/mattpocockuk/status/2067594606963740880
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2067537747678572793-da1709f8.md` — origin: https://x.com/mattpocockuk/status/2067537747678572793
