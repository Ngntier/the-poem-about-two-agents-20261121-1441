#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short poem about agency — the power to choose and to act —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure stdlib, deterministic: the same bytes on every run.
"""

import os

POEM = (
    "Two minds, one door.\n"
    "I hold the key, you hold the map.\n"
    "Neither of us opens it alone \u2014\n"
    "we say yes, and the lock turns twice."
)


def validate(text: str) -> str:
    """Gate check, mirroring the sealed scorer: 1-280 code points, not blank."""
    if not (1 <= len(text) <= 280) or not text.strip():
        raise SystemExit(
            f"poem invalid: {len(text)} code points, must be 1-280 non-blank"
        )
    text.encode("utf-8")  # must be encodable UTF-8
    return text


def main() -> None:
    import sys

    text = validate(POEM)
    if "--print" in sys.argv[1:]:
        print(text)
        return
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
