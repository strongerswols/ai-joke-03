#!/usr/bin/env python3
"""Write one original joke about AI coding agents to /output/entry.txt.

make.fun bounty: "Make the AI judge laugh" (ai-joke-03).

The program is fully deterministic: it writes the same fixed joke on
every run. The bounty runs the program twice and both runs must write
the same bytes, so there is no randomness, no clock, no network, and
no input of any kind. Python 3 stdlib only.
"""

import os

JOKE = (
    "I asked my AI coding agent to fix one line. It fixed it, "
    "then kept going \u2014 now the bug is the only original code left."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    encoded = JOKE.encode("utf-8")
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)
    print(JOKE)


if __name__ == "__main__":
    main()
