#!/usr/bin/env python3
"""Normalize generated MAXESS Results artifacts for readable, verifiable delivery.

The presentation builder owns semantics. This pass only adds safe structural
line breaks between markup tags so the generated artifacts remain inspectable
and satisfy the repository's artifact-size/line-count quality gates.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "MAXESS-RESULTS-FINAL-GROOVE.html",
    ROOT / "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html",
    ROOT / "MAXESS-RESULTS-10-GROOVE.html",
    ROOT / "MAXESS-RESULTS-GROOVE-EMBED.html",
    ROOT / "MAXESS-RESULTS-GROOVE-EMBED-9.95.html",
]

def format_markup(text: str) -> str:
    text = re.sub(r">\\s*<", ">\n<", text)
    text = re.sub(r"</style>", "\n</style>\n", text, flags=re.I)
    text = re.sub(r"</script>", "\n</script>\n", text, flags=re.I)
    return text.strip() + "\n"

for path in FILES:
    if not path.exists():
        raise SystemExit(f"Missing artifact: {path}")
    path.write_text(format_markup(path.read_text(encoding="utf-8")), encoding="utf-8")
    data = path.read_text(encoding="utf-8")
    print(f"{path.name}: {len(data.splitlines())} lines / {len(data.encode())} bytes")
