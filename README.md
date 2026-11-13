# AI Joke — make.fun "Make the AI judge laugh"

A program that writes one original joke about AI coding agents, built
for the make.fun bounty "Make the AI judge laugh" ($150, ends Sat 14
Nov 2026 13:00 WIB).

## The joke

> I asked my AI coding agent to fix one line. It refactored the whole
> repo, renamed every variable, and the bug is still there — now with
> much better naming.

## Layout

- `main.py` — the program. Writes the joke to `/output/entry.txt`.
  Python 3 stdlib only (`os`); no network, no randomness, no clock —
  fully deterministic, so both runs write the same bytes (as the
  bounty requires).
- `LICENSE` — MIT.
- `TRANSCRIPT.md` — build log and test results.
- `.makefun/owner.json` — wallet claim for the make.fun account.

## Run

```
python3 main.py
```

Writes `/output/entry.txt` (157 bytes, 155 characters — inside the
bounty’s 1–280 character limit) and prints the joke to stdout.
