from pathlib import Path
import re

HTML = Path('MAXESS-RESULTS-10-GROOVE.html')
ENGINE = Path('MAXESS-RESULTS-EXPERIENCE.js')
NAYA = Path('MAXESS-RESULTS-NAYA-EXPERIENCE.js')
MARKER = 'MAXESS-WHOLE-SYSTEM-AAA-INLINE-1.0'
NAYA_MARKER = 'MAXESS-NAYA-EXPERIENCE-INLINE-1.0'


def main() -> None:
    html = HTML.read_text(encoding='utf-8')
    engine = ENGINE.read_text(encoding='utf-8').strip()
    naya = NAYA.read_text(encoding='utf-8').strip()

    if not html.lstrip().lower().startswith('<!doctype html>'):
        raise SystemExit('BLOCKED — Results artifact is not a complete HTML document.')
    if '</body>' not in html.lower():
        raise SystemExit('BLOCKED — Results artifact has no body closing boundary.')
    if 'id="maxess-results-10"' not in html:
        raise SystemExit('BLOCKED — Results root not found.')
    if 'window.MAXESS_RESULT' not in html:
        raise SystemExit('BLOCKED — MAXESS_RESULT contract missing.')
    if not engine.startswith('/*') or 'MAXESS RESULTS — WHOLE-SYSTEM AAA PRESENTATION ENGINE' not in engine:
        raise SystemExit('BLOCKED — Whole-system presentation engine is not the expected artifact.')
    if not naya.startswith('/*') or 'MAXESS RESULTS — NAYA EXPERIENCE LAYER' not in naya:
        raise SystemExit('BLOCKED — Naya experience layer is not the expected artifact.')

    # Remove prior copies so assembly is deterministic and repeatable.
    html = re.sub(
        r'\s*<!-- MAXESS-WHOLE-SYSTEM-AAA-INLINE-1\.0 -->\s*<script id="maxess-whole-system-aaa-inline">.*?</script>\s*',
        '\n', html, flags=re.DOTALL)
    html = re.sub(
        r'\s*<!-- MAXESS-NAYA-EXPERIENCE-INLINE-1\.0 -->\s*<script id="maxess-naya-experience-inline">.*?</script>\s*',
        '\n', html, flags=re.DOTALL)

    inline_engine = (
        '\n<!-- MAXESS-WHOLE-SYSTEM-AAA-INLINE-1.0 -->\n'
        '<script id="maxess-whole-system-aaa-inline">\n' + engine + '\n</script>\n'
    )
    inline_naya = (
        '\n<!-- MAXESS-NAYA-EXPERIENCE-INLINE-1.0 -->\n'
        '<script id="maxess-naya-experience-inline">\n' + naya + '\n</script>\n'
    )

    html = re.sub(r'</body>', inline_engine + inline_naya + '</body>', html, count=1, flags=re.IGNORECASE)
    html = html.replace(
        '<main id="maxess-results-10"',
        '<main id="maxess-results-10" data-maxess-build="whole-system-aaa-1.0"',
        1,
    )

    HTML.write_text(html, encoding='utf-8')

    final = HTML.read_text(encoding='utf-8')
    assert final.count(MARKER) == 1
    assert final.count(NAYA_MARKER) == 1
    assert 'MAXESS RESULTS — WHOLE-SYSTEM AAA PRESENTATION ENGINE' in final
    assert 'MAXESS RESULTS — NAYA EXPERIENCE LAYER' in final
    assert 'data-maxess-build="whole-system-aaa-1.0"' in final
    assert 'NAYA_IMAGE' in final
    assert 'mx-playground' in final
    assert 'naya-led-organic-1.0' in final
    assert final.count('<body') == 1
    assert final.lower().count('</body>') == 1
    print(f'ASSEMBLED COMPLETE GROOVE ARTIFACT: {HTML} — {len(final.splitlines())} lines / {len(final.encode("utf-8"))} bytes')


if __name__ == '__main__':
    main()
