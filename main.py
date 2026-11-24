#!/usr/bin/env python3
"""Everyday Wonder — one sentence about a small everyday moment made strange.

Writes the line to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "When a stranger says my name, it sounds borrowed, "
    "like a coat I lent out years ago and forgot I owned."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
