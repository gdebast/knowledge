"""Build the concept index of the knowledge notes.

Scans every Markdown file under SoftwareEngineer/ (except folders starting
with "_"), turns each heading into a concept entry and writes
_index/concepts.md: one table row per concept, with its chapter path,
keywords and a clickable link to the exact line.

Keywords are extracted automatically from the section's own content
(imported symbols and packages, hook names, inline code) and can be
completed by hand in _index/aliases.json.

Usage (from anywhere):
    py SoftwareEngineer/_index/build_index.py          # regenerate the index
    py SoftwareEngineer/_index/build_index.py --check  # exit 1 if index is stale
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

INDEX_DIR = Path(__file__).resolve().parent
NOTES_ROOT = INDEX_DIR.parent
OUTPUT_FILE = INDEX_DIR / "concepts.md"
ALIASES_FILE = INDEX_DIR / "aliases.json"

MAX_KEYWORDS = 12

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
MD_ESCAPE_RE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|<>~=])")
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
# import X from "pkg" | import { a, b as c } from 'pkg' | import X, { a } from "pkg"
IMPORT_RE = re.compile(r"""^\s*import\s+(?:type\s+)?(.+?)\s+from\s+["']([^"']+)["']""")
SIDE_EFFECT_IMPORT_RE = re.compile(r"""^\s*import\s+["']([^"']+)["']""")
HOOK_RE = re.compile(r"\b(use[A-Z]\w*)\b")
IDENTIFIER_RE = re.compile(r"^[A-Za-z_$][\w$.]*(\(\))?$")


@dataclass
class Concept:
    file: Path  # relative to NOTES_ROOT
    line: int  # 1-based line of the heading
    level: int
    title: str
    parents: list[str]
    keywords: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)


def clean_heading(raw: str) -> str:
    text = MD_ESCAPE_RE.sub(r"\1", raw)
    text = re.sub(r"\*\*|__", "", text)  # bold markers
    return text.strip().rstrip(":").strip()


def add_keyword(bucket: list[str], word: str) -> None:
    word = word.strip()
    if word and word.lower() not in (k.lower() for k in bucket):
        bucket.append(word)


def keywords_from_section(lines: list[str]) -> list[str]:
    """Extract keywords from one section body (heading excluded)."""
    found: list[str] = []
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            m = IMPORT_RE.match(line)
            if m:
                names, package = m.groups()
                if package.startswith((".", "/")):
                    continue  # local module of the example: not a concept
                add_keyword(found, package)
                for name in re.split(r"[{},]", names):
                    name = name.strip()
                    if not name or name.startswith("* as"):
                        continue
                    name = name.split(" as ")[0].replace("type ", "").strip()
                    if IDENTIFIER_RE.match(name):
                        add_keyword(found, name)
                continue
            m = SIDE_EFFECT_IMPORT_RE.match(line)
            if m:
                if not m.group(1).startswith((".", "/")):
                    add_keyword(found, m.group(1))
                continue
            for hook in HOOK_RE.findall(line):
                add_keyword(found, hook)
        else:
            for code in INLINE_CODE_RE.findall(line):
                code = code.strip()
                if len(code) <= 40 and IDENTIFIER_RE.match(code):
                    add_keyword(found, code)
    return found[:MAX_KEYWORDS]


def parse_file(path: Path) -> list[Concept]:
    rel = path.relative_to(NOTES_ROOT)
    lines = path.read_text(encoding="utf-8").splitlines()

    headings: list[tuple[int, int, str]] = []  # (index, level, title)
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if m:
            title = clean_heading(m.group(2))
            if title:
                headings.append((i, len(m.group(1)), title))

    concepts: list[Concept] = []
    stack: list[tuple[int, str]] = []  # (level, title) of open ancestors
    for n, (i, level, title) in enumerate(headings):
        while stack and stack[-1][0] >= level:
            stack.pop()
        end = headings[n + 1][0] if n + 1 < len(headings) else len(lines)
        concepts.append(
            Concept(
                file=rel,
                line=i + 1,
                level=level,
                title=title,
                parents=[t for _, t in stack],
                keywords=keywords_from_section(lines[i + 1 : end]),
            )
        )
        stack.append((level, title))
    return concepts


def load_aliases() -> dict[str, dict[str, list[str]]]:
    if not ALIASES_FILE.exists():
        return {}
    data = json.loads(ALIASES_FILE.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


def apply_aliases(concepts: list[Concept], aliases: dict[str, dict[str, list[str]]]) -> list[str]:
    """Attach hand-written aliases; return warnings for keys matching nothing."""
    by_key = {(c.file.as_posix(), c.title.lower()): c for c in concepts}
    warnings = []
    for file_key, entries in aliases.items():
        for title, words in entries.items():
            concept = by_key.get((file_key, title.lower()))
            if concept is None:
                warnings.append(f"aliases.json: no heading '{title}' in {file_key}")
                continue
            for w in words:
                add_keyword(concept.aliases, w)
    return warnings


def cell(text: str) -> str:
    return text.replace("|", "\\|")


def render(concepts: list[Concept]) -> str:
    out = [
        "# Concept index",
        "",
        "<!-- GENERATED by build_index.py - do not edit by hand. -->",
        "<!-- Add aliases in aliases.json, then run: py SoftwareEngineer/_index/build_index.py -->",
        "",
        "One row per heading of the notes. *Keywords* are extracted from the section",
        "content; *aliases* (in italics) come from `aliases.json`.",
        "",
    ]
    files = sorted({c.file for c in concepts}, key=lambda p: p.as_posix().lower())
    out.append(f"{len(concepts)} concepts in {len(files)} files.")
    out.append("")
    for f in files:
        out.append(f"- [{f.as_posix()}](#{slug(f.as_posix())})")
    out.append("")

    for f in files:
        out += [f"## {f.as_posix()}", "", "| Concept | Chapter | Keywords | Link |", "|---|---|---|---|"]
        for c in (c for c in concepts if c.file == f):
            link_target = "../" + c.file.as_posix()
            indent = "&nbsp;&nbsp;" * (c.level - 1)
            words = [cell(k) for k in c.keywords] + [f"*{cell(a)}*" for a in c.aliases]
            out.append(
                f"| {indent}{cell(c.title)} "
                f"| {cell(' > '.join(c.parents))} "
                f"| {', '.join(words)} "
                f"| [L{c.line}]({link_target}#L{c.line}) |"
            )
        out.append("")
    return "\n".join(out)


def slug(text: str) -> str:
    text = re.sub(r"[^\w\- ]", "", text.lower())
    return text.replace(" ", "-")


def collect() -> tuple[list[Concept], list[str]]:
    files = sorted(
        p
        for p in NOTES_ROOT.rglob("*.md")
        if not any(part.startswith(("_", ".")) for part in p.relative_to(NOTES_ROOT).parts)
    )
    concepts: list[Concept] = []
    for p in files:
        concepts += parse_file(p)
    warnings = apply_aliases(concepts, load_aliases())
    return concepts, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="exit 1 if concepts.md is out of date")
    args = parser.parse_args()

    concepts, warnings = collect()
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    content = render(concepts) + "\n"

    current = OUTPUT_FILE.read_text(encoding="utf-8") if OUTPUT_FILE.exists() else ""
    if args.check:
        if current != content:
            print("concepts.md is out of date: run build_index.py", file=sys.stderr)
            return 1
        print("concepts.md is up to date.")
        return 0

    if current == content:
        print(f"concepts.md unchanged ({len(concepts)} concepts).")
    else:
        OUTPUT_FILE.write_bytes(content.encode("utf-8"))  # LF endings on every OS
        print(f"Wrote {OUTPUT_FILE.relative_to(NOTES_ROOT)} ({len(concepts)} concepts).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
