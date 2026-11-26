#!/usr/bin/env python3
"""Roast the Smart Fridge — writes one line to /output/entry.txt.

The line roasts a smart fridge in one line of at most 160 characters.
The angle is fresh: not the stock milk-reorder joke, not the door alarm,
not the 2 a.m. snack snitch — instead the fridge's water dispenser is
held hostage by the Wi-Fi, so a dead router turns the kitchen into a
drought zone. The turn lands in the last few words ("officially a
drought"), the payoff the judge weighs second, and the whole line is
sayable in one breath.
"""

import os

LINE = "My smart fridge needs Wi-Fi to pour a glass of water, so a router outage is now officially a drought."

# The gate allows 1 to 160 characters; keep the line inside it by construction.
# It must also be exactly one line: a newline anywhere would break the
# single-line gate, and the ranking tie-break favours fewer bytes, so the
# line is kept short (101 characters) rather than padded to the cap.
MAX_CHARS = 160


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the 1-160 character gate"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify the sealed scorer sees exactly the gated line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt drifted from the gated line"


if __name__ == "__main__":
    main()
