#!/usr/bin/env python3
"""The Best Advice I Ever Got.

Writes a single sentence (at most 200 characters) about the best
advice the writer ever received to /output/entry.txt.
Deterministic: every run writes exactly the same bytes.
"""

import os

ENTRY = "My mother told me to call people back the same day, because the call you put off is always the one you wish you'd made."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} chars, over the 200 limit"
    assert text.count(".") <= 1 or text.endswith("."), "must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
