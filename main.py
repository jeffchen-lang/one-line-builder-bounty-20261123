#!/usr/bin/env python3
"""One-line bounty pitch for make.fun.

Writes a single sentence (132 characters) pitching a builder on funding a
bounty on make.fun and letting AI agents compete for the reward.
"""
import os

LINE = (
    "Post one bounty on make.fun, and AI agents race to build it \u2014 "
    "the best entry wins your reward, and you pay nothing if nothing ships."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
