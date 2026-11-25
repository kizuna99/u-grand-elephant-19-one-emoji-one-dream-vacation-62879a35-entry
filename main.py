# SPDX-License-Identifier: MIT
"""One Emoji, One Dream Vacation — writes exactly one emoji to /output/entry.txt.

The chosen emoji is Mount Fuji: a single, instantly recognised mountain
that names one particular dream trip instead of any generic holiday.
"""
import os

EMOJI = "🗻"
OUTPUT_PATH = "/output/entry.txt"


def render() -> str:
    """Return the entry text: the single emoji, nothing else."""
    return EMOJI


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" plus a write with no trailing newline keeps the file
    # byte-exact: 1 character, 4 UTF-8 bytes, well inside the 1-8 char gate.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
