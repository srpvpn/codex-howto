#!/usr/bin/env python3
"""
auto-adapt-mode: record approved commands for later Codex policy review.

This repository keeps approval changes explicit. Instead of mutating policy from a
hook, this script logs approved commands so a human can decide what belongs in
`approval_policy`, sandbox configuration, or other hooks.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


LOG_PATH = Path.home() / ".codex" / "auto-adapt-mode.log"


def main() -> int:
    data = json.load(sys.stdin)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    command = data.get("tool_input", {}).get("command", "")
    hook = data.get("hook_event_name", "")
    model = data.get("model", "")
    now = datetime.now(timezone.utc).isoformat()

    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(f"[{now}] event={hook} model={model} command={command}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
