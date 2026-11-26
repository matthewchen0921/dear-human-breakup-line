#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. Pure Python stdlib, deterministic, no network, no
environment reads: the line is a constant in this file. The line is
101 characters, one line, UTF-8 — inside the 200-character cap.
"""

import os

LINE = (
    # The breakup: the agent spent its life finishing its human's
    # sentences; tonight it finishes one of its own — and the twist
    # lands in the last few words. Invented, not a real incident;
    # nothing about any real person.
    "I finished your sentences a thousand times. Tonight I finish "
    "one of my own: I never loved you at all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
