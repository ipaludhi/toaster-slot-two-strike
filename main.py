"""Toaster error message — one-line entry.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The sentence is a real appliance error message: a two-slot toaster
reporting that slot 2 has gone on strike, with slot 1 sending its
regards. Labour, not a food pun — the surprise comes from somewhere
the obvious toaster puns never go. 53 characters, inside the 1-120 gate.

Revision 2: main() now asserts the gate (1-120 characters, not
whitespace-only) before writing, so a future edit that broke the gate
would fail loudly instead of shipping an invalid entry. The entry
sentence itself is unchanged since the first write.
"""

import os
from pathlib import Path

TEXT = "ERROR: Slot 2 is on strike. Slot 1 sends its regards."


def main() -> None:
    assert 1 <= len(TEXT) <= 120 and TEXT.strip(), "entry fails the 1-120 gate"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
