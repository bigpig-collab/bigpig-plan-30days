#!/usr/bin/env python3
"""Entry for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

Writes a 30-day, $100-budget money plan to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt). Python 3.13, stdlib only, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "Day 1: list 200 local firms with no website on Google Maps. "
    "Email 50/day: $149 one-page site, built and live in 24h, Stripe link, "
    "7-day refund. Spend $100 only on domain, hosting, email credits. "
    "Likely 3-5 clients by day 30 = $450-$750. "
    "Edge: win on speed + a live demo link."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be whitespace-only"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)
    print(f"chars: {len(text)}  bytes: {len(text.encode('utf-8'))}")


if __name__ == "__main__":
    main()
