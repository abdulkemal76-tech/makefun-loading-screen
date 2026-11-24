#!/usr/bin/env python3
"""Loading Screen Gold: writes one loading-screen tip to /output/entry.txt.

Entry: a single tip of at most 200 characters, aimed at stressed
developers and AI coding agents, sharp and funny enough to land mid-build.
"""

import os

TIP = (
    "Tip: if the build has sat at 97% for ten minutes, it is not loading. "
    "It is deciding whether to fail now or after you walk away."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
