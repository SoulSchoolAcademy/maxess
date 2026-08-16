from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "nayanetpagecode"
OUTPUT = ROOT / "MAXESS-RESULTS-10-GROOVE.html"
PREFIX = "#maxess-results-v16 "


def find_matching(text: str, opening: int) -> int:
    depth = 0
    quote = None
    escape = False
    for i in range(opening, len(text)):
        ch = text[i]
        if quote:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
    raise ValueError("unbalanced CSS braces")


def split_selector_list(prelude: str) -> list[str]:
    parts=[]
    current=[]
    depth=0
    quote=None
    escape=False
    for ch in prelude:
        if quote:
            current.append(ch)
            if escape:
                escape=False
            elif ch == "\\":
                escape=True
            elif ch == quote:
                quote=None
            continue
        if ch in "\"'":
            quote=ch
            current.append(ch)
        elif ch in "([":
            depth+=1
            current.append(ch)
        elif ch in ")]":
            depth=max(0,depth-1)
            current.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(current).strip())
            current=[]
        else:
            current.append(ch)
    if current:
        parts.append("".join(current).strip())
    return [p for p in parts if p]


def scope_block(css: str, start: int = 0, stop: int | None = None, keyframes: bool = False) -> tuple[str, int]:
    end_limit = len(css) if stop is None else stop
    out=[]
    pos=start
    while pos < end_limit:
        brace=css.find("{",pos,end_limit)
        semi=css.find(";",pos,end_limit)
        close=css.find("}",pos,end_limit)
        if close >= 0 and (brace < 0 or close < brace) and (semi < 0 or close < semi):
            out.append(css[pos:close])
            return "".join(out), close
        if brace < 0:
            out.append(css[pos:end_limit])
            return "".join(out), end_limit
        if semi >= 0 and semi < brace:
            out.append(css[pos:semi+1])
            pos=semi+1
            continue
        prelude=css[pos:brace]
        closing=find_matching(css,brace)
        inner=css[brace+1:closing]
        stripped=prelude.strip()
        if stripped.startswith("@"):
            lower=stripped.lower()
            if "keyframes" in lower:
                scoped_inner,_=scope_block(inner,0,len(inner),True)
                out.append(prelude+"{"+scoped_inner+"}")
            elif lower.startswith(("@media","@supports","@container","@layer","@document")):
                scoped_inner,_=scope_block(inner,0,len(inner),keyframes)
                out.append(prelude+"{"+scoped_inner+"}")
            else:
                out.append(prelude+"{"+inner+"}")
        elif keyframes:
            out.append(prelude+"{"+inner+"}")
        else:
            selectors=split_selector_list(prelude)
            scoped=[]
            for selector in selectors:
                if selector.startswith(PREFIX) or selector.startswith("#maxess-results-v16"):
                    scoped.append(selector)
                else:
                    scoped.append(PREFIX+selector)
            out.append(",".join(scoped)+"{"+inner+"}")
        pos=closing+1
    return "".join(out),pos


def process() -> None:
    source=OUTPUT.read_text(encoding="utf-8")
    foundation=FOUNDATION.read_text(encoding="utf-8")
    if not source.endswith(foundation):
        raise SystemExit("BLOCKED: candidate does not end with the authoritative foundation")
    tower=source[:-len(foundation)]
    marker='<style id="maxess-results-v16-css">'
    start=tower.find(marker)
    if start < 0:
        raise SystemExit("BLOCKED: Results CSS marker missing")
    content_start=start+len(marker)
    end=tower.find("</style>",content_start)
    if end < 0:
        raise SystemExit("BLOCKED: Results CSS closing marker missing")
    css=tower[content_start:end]
    scoped,_=scope_block(css)
    OUTPUT.write_text(tower[:content_start]+scoped+tower[end:]+foundation,encoding="utf-8",newline="\n")
    print("RESULTS CSS NAMESPACE PASS")


if __name__ == "__main__":
    process()
