#!/usr/bin/env python3
"""Entry generator for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

A 30-day plan to turn $100 into $900-$1,500 plus $300-$500 a month:
sell local businesses a $299 one-page website with a $99/month
hosting-and-updates subscription. The edge is the recurring revenue,
not the one-off sale.

Running this script writes the plan text to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Python 3.13, standard library only, no network access.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 280

ENTRY_TEXT = (
    "Days 1-2: find 200 firms with no site on Maps. "
    "Sell a $299 one-page site, live in 24h plus $99/mo hosting/updates "
    "\u2014 Stripe link, 7-day refund. "
    "Email 50/day. "
    "$100 covers domain/hosting/email. "
    "Close 3-5 clients by day 30: $900-$1,500 plus $300-$500/mo. "
    "Edge: recurring revenue wins."
)


def validate(text: str) -> str:
    """Return the entry text, enforcing the non-empty and length rules."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry text must not be empty")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"entry text too long: {len(cleaned)} characters (max {MAX_CHARS})"
        )
    return cleaned


def write_entry(text: str, destination: Path) -> Path:
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "entry.txt"
    target.write_text(text, encoding="utf-8")
    return target


def emit() -> int:
    text = validate(ENTRY_TEXT)
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(text, destination)
    print(text)
    print(f"chars: {len(text)}  bytes: {len(text.encode('utf-8'))}")
    return 0


if __name__ == "__main__":
    sys.exit(emit())
