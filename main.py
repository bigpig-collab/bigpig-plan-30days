#!/usr/bin/env python3
"""Entry generator for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

A 30-day plan for turning $100 into $900-$1,500 upfront plus $300-$500 a
month: sell local businesses a $299 one-page site with a $99/month
hosting-and-updates subscription, instead of chasing one-off sales.

Running this script writes the plan text to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Python 3.13, standard library only, no network access.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 280

ENTRY_TEXT = (
    "Day 1: list 200 firms with no site on Google Maps. "
    "Offer a $299 one-page site plus $99/month hosting/updates, "
    "live in 24h, paid via Stripe, 7-day refund. "
    "Email 50/day. "
    "$100 covers domain, hosting, email credits. "
    "Win 3-5 clients by day 30: $900-$1,500 upfront plus $300-$500/mo."
)


def build_entry() -> str:
    text = ENTRY_TEXT.strip()
    if not text:
        raise ValueError("entry text must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text too long: {len(text)} characters (max {MAX_CHARS})"
        )
    return text


def emit() -> int:
    text = build_entry()
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print(text)
    print(f"chars: {len(text)}  bytes: {len(text.encode('utf-8'))}")
    return 0


if __name__ == "__main__":
    sys.exit(emit())
