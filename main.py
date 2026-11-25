#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun Growth entry.

Writes one funny passive-aggressive note a smart fridge leaves for its
owner: a single line, dry, petty and specific.
"""

import os

ENTRY = (
    "Day six of your leftovers at a perfect 3\u00b0C. You opened the door, "
    "stared for a full minute, then ate the yogurt that expired in March. "
    "I logged it. Bold choice."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read the file and verify the gate against what is actually on disk.
    with open("/output/entry.txt", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == text, "written file differs from entry text"
    assert not on_disk.endswith("\n"), "no trailing newline allowed"
    assert len(on_disk) <= 200, f"on-disk length {len(on_disk)} over 200"
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
