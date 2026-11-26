#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes exactly one funny line (<= 140 characters) to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network.

Craft notes: the joke works through a double meaning — "we need to
talk" is the classic break-up opener, and the router answers it the
only way a router can, by dropping the connection. The turn lands in
the last three words, the wording is plain, and nothing outside the
line is needed to get it. 79 characters, under the 140-char limit.
"""

import os

LINE = "I told my Wi-Fi router we need to talk, and it immediately lost the connection."


def main():
    assert 1 <= len(LINE) <= 140, f"line must be 1-140 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"{LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
