#!/usr/bin/env python3
"""The One-Line Exit — make.fun entry.

Writes the funniest single-line resignation letter (86 characters)
to /output/entry.txt.

The letter was chosen from 24 original candidates (12 in round one,
10 challengers in round two, plus 2 controls) scored against the judge
brief: a real one-line resignation, a surprise turn, a specific
workplace voice, and a quotable line. The two controls — a generic
this-job-is-terrible complaint and a famous-song retelling — scored
far below the winner, so neither pattern was used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

TEXT = "I resign. The meetings could have been emails, and the emails could have been silence."


def main() -> None:
    # Competition gate: the letter must be UTF-8 text, 1-140
    # characters, and not whitespace-only. Validate before writing.
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 140 and text.strip(), "text violates gate"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
