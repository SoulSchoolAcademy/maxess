from pathlib import Path
import re

HTML = Path('MAXESS-RESULTS-10-GROOVE.html')
ENGINE = Path('MAXESS-RESULTS-EXPERIENCE.js')
MARKER = 'MAXESS-WHOLE-SYSTEM-AAA-INLINE-1.0'


def main() -> None:
    html = HTML.read_text(encoding='utf-8')
    engine = ENGINE.read_text(encoding='utf-8').strip()

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

    # Remove a prior copy of this exact inline engine so the operation is idempotent.
    html = re.sub(
        r'\s*<!-- MAXESS-WHOLE-SYSTEM-AAA-INLINE-1\.0 -->\s*<script id="maxess-whole-system-aaa-inline">.*?</script>\s*',
        '\n',
        html,
        flags=re.DOTALL,
    )

    # The existing HTML contains historical presentation code and the preserved
    # NayaNET foundation. We do not delete working foundation code. Instead we
    # install the authoritative whole-system renderer as the final Results pass,
    # immediately before </body>, so the final visible root is deterministic.
    inline = (
        '\n<!-- MAXESS-WHOLE-SYSTEM-AAA-INLINE-1.0 -->\n'
        '<script id="maxess-whole-system-aaa-inline">\n'
        + engine
        + '\n</script>\n'
    )
    html = re.sub(r'</body>', inline + '</body>', html, count=1, flags=re.IGNORECASE)

    html = html.replace(
        '<main id="maxess-results-10"',
        '<main id="maxess-results-10" data-maxess-build="whole-system-aaa-1.0"',
        1,
    )

    HTML.write_text(html, encoding='utf-8')

    final = HTML.read_text(encoding='utf-8')
    assert final.count(MARKER) == 1
    assert 'MAXESS RESULTS — WHOLE-SYSTEM AAA PRESENTATION ENGINE' in final
    assert 'data-maxess-build="whole-system-aaa-1.0"' in final
    assert final.count('<body') == 1
    assert final.lower().count('</body>') == 1
    print(f'ASSEMBLED: {HTML} — {len(final.splitlines())} lines')


if __name__ == '__main__':
    main()
