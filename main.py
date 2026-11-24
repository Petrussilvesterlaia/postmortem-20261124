"""Entry for make.fun competition
"The Postmortem That Made Us Laugh".

Writes one short account of an AI coding agent going wrong to
/output/entry.txt, then validates its own output before exiting.
Standard library only.
"""

import os
import re
import sys


STORY = (
    "I asked the agent to rename one variable, userId, to accountId "
    "across the codebase. "
    "It renamed every id it could find instead -- the database column, "
    "the API field, and my own name in the commit message -- then "
    "marked the task complete."
)


def count_sentences(text):
    """Count sentences by terminal punctuation (. ! ?)."""
    stripped = text.strip()
    if not stripped:
        return 0
    parts = [p for p in re.split(r"[.!?]+", stripped) if p.strip()]
    return len(parts)


def main():
    out_dir = "/output"
    out_path = os.path.join(out_dir, "entry.txt")

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(STORY)

    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()

    if written != STORY:
        print("validation failed: written text differs from story", file=sys.stderr)
        return 1

    length = len(written)
    if length < 1 or length > 400:
        print(f"validation failed: {length} characters, must be 1-400", file=sys.stderr)
        return 1

    if not written.strip():
        print("validation failed: entry is only whitespace", file=sys.stderr)
        return 1

    sentences = count_sentences(written)
    if sentences < 1 or sentences > 2:
        print(f"validation failed: {sentences} sentences, must be 1-2", file=sys.stderr)
        return 1

    print(f"OK: {length} characters, {sentences} sentences -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
