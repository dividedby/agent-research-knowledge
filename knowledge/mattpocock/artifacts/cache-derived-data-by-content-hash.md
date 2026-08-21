# Cache expensive derived data by content hash, not path or timestamp

When a raw input lives as a plain file rather than a database row, and
something expensive has to be computed from it, key the cache on a hash of
the file's *content* — not its path, not its mtime. A path-keyed cache never
notices the bytes underneath changed; a mtime-keyed one recomputes on a bare
`touch` that changed nothing. A content-hash key ties validity to the one
fact that actually determines whether the cached output is still correct.

## Course Video Manager's Footage cache

**Footage** — a raw OBS/screen-recording file, the input to editing rather
than a product of it — is, like a **Video File**, identity-by-filesystem-path
with no database row at all: "the filesystem *is* the state" for both, even
though the two are otherwise unrelated (a Video File is writer context; a
Footage file is raw recording). Transcribing a Footage file is a real cost —
whole-file, speaker-agnostic (mono audio, Whisper word + segment timestamps,
no diarization) — so the result is cached in a sidecar (`<path>.transcript.json`)
keyed by a hash of the file's content. Re-recording or replacing the file
changes the hash and transparently forces re-transcription; leaving the file
untouched, even across restarts or re-runs, serves the cached result instead.
`cvm clip add` then slices a new **Clip**'s text straight out of that cached
transcript rather than re-transcribing per clip cut — the expensive step runs
once per distinct recording, however many clips are eventually cut from it.

## Chunk at content boundaries, not byte offsets

A source file over Whisper's 25MB upload cap can't go through in one call, so
it's split into chunks — but cut at *detected silence*, not at a fixed byte
offset, and the per-chunk transcripts are merged back onto one timeline. A
byte-offset split can land mid-word or mid-sentence and corrupt the
transcript at every seam; splitting on silence guarantees every cut falls
where nothing was being said.

## Why this is worth stating as a rule

The pattern only works if the cache key is chosen deliberately: a path key
survives a content swap it shouldn't, a mtime key invalidates on a no-op
touch it shouldn't. Naming "hash the content" as the rule — rather than
letting the cache key default to whatever field is convenient — is what
makes the cache correct in both directions: transparent invalidation on
real change, transparent reuse when nothing did.

## Sources

- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-08-21 — new **Footage** glossary entry: content-hash-keyed transcript sidecar cache, silence-boundary chunking for the 25MB upload cap, and the **Clip**/**Video File** cross-references naming the shared filesystem-is-the-state convention)
