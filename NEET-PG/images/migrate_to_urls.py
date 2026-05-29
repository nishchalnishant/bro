#!/usr/bin/env python3
"""
Migrate image references in NEET-PG markdown files from local paths to URLs.

For each ![alt](../../images/filename.jpg):
  - Commons URL in url_map.py  → replace src with direct Commons URL
  - Radiopaedia URL            → keep local src, append *(Source: Radiopaedia)* link
  - None                       → leave unchanged

Run from any directory. Dry-run by default; pass --apply to write changes.
"""

import os
import re
import sys

# ── load the URL map ────────────────────────────────────────────────────────
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from url_map import DIRECT_URLS

NEET_PG = os.path.normpath(os.path.join(HERE, ".."))

IMG_RE = re.compile(
    r'(!\[([^\]]*)\])'          # group 1: ![alt], group 2: alt text
    r'\(\.\.\/\.\.\/images\/'   # literal ../../images/
    r'([^)]+\.jpg)'             # group 3: filename
    r'\)'                        # closing )
)

def migrate_line(line):
    """Return (new_line, list_of_changes)."""
    changes = []

    def replace(m):
        alt     = m.group(2)
        fname   = m.group(3)
        url     = DIRECT_URLS.get(fname)

        if url is None:
            return m.group(0)  # no change

        if "radiopaedia.org" in url:
            # Keep local image, append source link
            new = f"{m.group(0)} *([Source: Radiopaedia]({url}))*"
            changes.append(("radiopaedia-link", fname))
            return new
        else:
            # Commons — replace src directly
            new = f"![{alt}]({url})"
            changes.append(("commons-url", fname))
            return new

    new_line = IMG_RE.sub(replace, line)
    return new_line, changes


def process_file(path, apply=False):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    file_changes = []
    for lineno, line in enumerate(lines, 1):
        new_line, changes = migrate_line(line)
        new_lines.append(new_line)
        for kind, fname in changes:
            file_changes.append((lineno, kind, fname))

    if file_changes and apply:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    return file_changes


def main():
    apply = "--apply" in sys.argv

    if not apply:
        print("DRY RUN — pass --apply to write changes\n")

    total_commons = 0
    total_radio   = 0
    total_files   = 0

    for root, dirs, files in os.walk(NEET_PG):
        # skip the images dir itself
        dirs[:] = [d for d in dirs if d != "images"]
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            path = os.path.join(root, fname)
            changes = process_file(path, apply=apply)
            if changes:
                rel = os.path.relpath(path, NEET_PG)
                total_files += 1
                c = sum(1 for _, k, _ in changes if k == "commons-url")
                r = sum(1 for _, k, _ in changes if k == "radiopaedia-link")
                total_commons += c
                total_radio   += r
                print(f"{rel}: {c} commons, {r} radiopaedia")
                if not apply:
                    for lineno, kind, img in changes[:6]:
                        print(f"  line {lineno:4d}  [{kind}]  {img}")
                    if len(changes) > 6:
                        print(f"  ... and {len(changes)-6} more")

    print(f"\n{'Applied' if apply else 'Would change'}: "
          f"{total_files} files, "
          f"{total_commons} commons replacements, "
          f"{total_radio} radiopaedia source links added")


if __name__ == "__main__":
    main()
