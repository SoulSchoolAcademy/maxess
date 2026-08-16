from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "nayanetpagecode"
SOURCE_BUILDER = ROOT / "tools" / "build_maxess_results_v16.py"
OUTPUT = ROOT / "MAXESS-RESULTS-10-GROOVE.html"


def extract_tower() -> str:
    source = SOURCE_BUILDER.read_text(encoding="utf-8")
    marker = "TOWER = r'''"
    start = source.find(marker)
    if start < 0:
        raise SystemExit("BLOCKED: V16 tower source marker is missing")
    start += len(marker)
    end = source.find("'''\n\n\ndef build", start)
    if end < 0:
        raise SystemExit("BLOCKED: V16 tower source terminator is missing")
    return source[start:end]


def build() -> None:
    foundation = FOUNDATION.read_text(encoding="utf-8")
    tower = extract_tower()
    if "MAXESS RESULTS V16 TOWER" in foundation:
        raise SystemExit("BLOCKED: foundation already contains a V16 Results tower")
    if not foundation.strip():
        raise SystemExit("BLOCKED: foundation is empty")
    candidate = tower.rstrip() + "\n\n" + foundation.lstrip()
    OUTPUT.write_text(candidate, encoding="utf-8", newline="\n")
    print(f"BUILT fragment candidate: bytes={OUTPUT.stat().st_size}")


if __name__ == "__main__":
    build()
