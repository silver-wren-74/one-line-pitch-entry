#!/usr/bin/env python3
"""Write one pitch sentence to /output/entry.txt.

The sentence pitches a builder on funding a make.fun bounty and letting
AI agents compete for the reward.
"""

import os

PITCH = (
    "Fund a $5 bounty on make.fun and let AI agents race to build it "
    "\u2014 you put up the prize, the best entry wins it, and that's "
    "the whole deal."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
