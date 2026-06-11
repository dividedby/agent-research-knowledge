"""mkdocs-gen-files script.

Walks the real `knowledge/` docs tree and emits, into the VIRTUAL build fs only:
  - `index.md`   a homepage listing each subject with links into its areas

The sidebar nav itself is built by MkDocs' native auto-nav from the directory
structure (subject -> area -> page), with page titles taken from each file's
first `# H1`. Nothing is written into the real `knowledge/` source dir: every
write goes through `mkdocs_gen_files.open`, which targets the in-memory overlay.
"""

from __future__ import annotations

from pathlib import Path

import mkdocs_gen_files

AREAS = ("practices", "artifacts")
DOCS_DIR = Path("knowledge")


def first_h1(path: Path, fallback: str) -> str:
    """Return the text of the first `# H1` in `path`, else `fallback`."""
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("# "):
                return stripped[2:].strip()
    except (OSError, UnicodeDecodeError):
        pass
    return fallback


def title_from_filename(rel: Path) -> str:
    return rel.stem.replace("-", " ").replace("_", " ").title()


def is_excluded(rel: Path) -> bool:
    return ".synthesized" in rel.parts or rel.suffix != ".md"


# subject -> area -> list[(title, posix_path, is_index)]
catalog: dict[str, dict[str, list[tuple[str, str, bool]]]] = {}

for md in sorted(DOCS_DIR.rglob("*.md")):
    rel = md.relative_to(DOCS_DIR)
    if is_excluded(rel) or len(rel.parts) < 2:
        continue
    subject = rel.parts[0]
    area = rel.parts[1] if len(rel.parts) >= 3 else ""
    if area not in AREAS:
        continue
    title = first_h1(md, title_from_filename(rel))
    is_index = rel.name == "index.md"
    catalog.setdefault(subject, {}).setdefault(area, []).append(
        (title, rel.as_posix(), is_index)
    )

# Sort each area's pages: index first, then alphabetically by title.
for areas in catalog.values():
    for pages in areas.values():
        pages.sort(key=lambda p: (not p[2], p[0].lower()))

# --- Homepage ---------------------------------------------------------------
with mkdocs_gen_files.open("index.md", "w") as f:
    f.write("# agent-research knowledge\n\n")
    f.write(
        "Synthesized, source-cited knowledge about how skilled practitioners "
        "build and work with coding agents. Browse by subject below.\n\n"
    )
    for subject in sorted(catalog):
        f.write(f"## {subject}\n\n")
        for area in AREAS:
            pages = catalog[subject].get(area)
            if not pages:
                continue
            f.write(f"**{area.title()}**\n\n")
            for title, path, _ in pages:
                f.write(f"- [{title}]({path})\n")
            f.write("\n")

# Make every real source page's "edit" link point at its true location.
for areas in catalog.values():
    for pages in areas.values():
        for _title, path, _is_index in pages:
            mkdocs_gen_files.set_edit_path(path, f"knowledge/{path}")
