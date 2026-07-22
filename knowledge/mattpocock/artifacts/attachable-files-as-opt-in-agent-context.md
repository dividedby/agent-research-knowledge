# Attach then curate: opt-in files as an agent-writer's side-channel context

When an LLM feature is fed a structured transcript of what happened, that
transcript can only ever cover what was *said*. Course Video Manager's "Article
Writer" needs more than that — a code sample that was referenced but never
narrated, prior research notes, a pasted chat log — so the fix is a side channel:
let the author attach arbitrary files to the same entity the writer already reads
(a Video's Transcript and its Beats), rather than contorting the transcript to
record things that were never actually filmed.

## The attachment is the filesystem, not a row about the filesystem

A **Video File** is a plain file living under the video's own directory, addressed
by a path relative to it — not a database row referencing a file. The directory
listing *is* the state, so attaching a file is the entire write and deleting one is
a real unlink; there's no `archived` flag and no restore, unlike most entities in
the system. That simplicity is deliberate: this is a side channel for the writer,
not a first-class domain object needing the soft-delete/versioning machinery the
rest of the app has.

## Default the checkbox by type, route images around it entirely

The writer's context picker doesn't dump every attached file into the model
unfiltered, and it doesn't force an all-or-nothing choice either — it pre-ticks by
extension. Known text-like extensions (`ts/tsx/js/jsx/json/md/mdx/txt/csv`) default
*on*; everything else is attached but starts *unticked*, requiring an explicit
opt-in. Images skip the checkbox model altogether and are passed to the writer as
images, not gated as attachable text.

This is the general shape for feeding an agent a curated, opt-in attachment set:
default-on the cheap, obviously-relevant kinds so the common case needs no manual
curation; default-off (but visible and available) the kinds more likely to be
noise, oversized, or irrelevant, so the author decides rather than the system
guessing; and route each modality through the channel actually suited to it
instead of forcing images through a text-oriented include/exclude filter.

## Sources

- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-07-22)
