#!/usr/bin/env python3
"""Plan entry for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

A 30-day plan for turning $100 into $450-$750 by selling $149 one-page
websites to local businesses that have no website yet.

Running this script writes the plan text to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Python 3.13, standard library only, no network access.
"""

import os
from pathlib import Path

PLAN = (
    "Day 1: find 200 local businesses with no website on Google Maps. "
    "Email 50/day: $149 one-page site, live in 24h, paid by Stripe link, "
    "7-day refund. Spend the $100 only on domain, hosting, email credits. "
    "Land 3-5 clients by day 30 = $450-$750. "
    "Edge: speed plus a live demo link."
)


def run() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    plan = PLAN.strip()
    if not plan:
        raise ValueError("plan text must not be empty")
    if len(plan) > 280:
        raise ValueError(f"plan text too long: {len(plan)} characters")
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(plan, encoding="utf-8")
    print(plan)
    print(f"chars: {len(plan)}  bytes: {len(plan.encode('utf-8'))}")


if __name__ == "__main__":
    run()
