"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a sailboat, for the dream
of sailing away — open water, wind, no itinerary. One glyph, 3 bytes of
UTF-8, nothing else.
"""

import os

ENTRY = "⛵"  # U+26F5 SAILBOAT

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts 1 to 8 characters of UTF-8 text; the entry is the
    # single sailboat glyph alone, with no trailing newline, so the file
    # is exactly the emoji and nothing else.
    assert len(ENTRY) == 1, "the entry must be exactly one character"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
