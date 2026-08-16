from pathlib import Path
import re

HTML = Path('MAXESS-RESULTS-10-GROOVE.html')
ENGINE = Path('MAXESS-RESULTS-EXPERIENCE.js')
NAYA = Path('MAXESS-RESULTS-NAYA-EXPERIENCE.js')
MARKER = 'MAXESS-WHOLE-SYSTEM-AAA-INLINE-1.0'
NAYA_MARKER = 'MAXESS-NAYA-EXPERIENCE-INLINE-1.0'


def strip_inline(html: str, marker: str, script_id: str) -> str:
    pattern = r'\s*<!-- ' + re.escape(marker) + r' -->\s*<script id="' + re.escape(script_id) + r'">.*?</script>\s*'
    return re.sub(pattern, '\n', html, flags=re.DOTALL | re.IGNORECASE)


def main() -> None:
    html = HTML.read_text(encoding='utf-8')
    engine = ENGINE.read_text(encoding='utf-8').strip()
    naya = NAYA.read_text(encoding='utf-8').strip()

    if not html.lstrip().lower().startswith('<!doctype html>'):
        raise SystemExit('BLOCKED — Results artifact is not a complete HTML document.')
    if html.lower().count('</body>') != 1:
        raise SystemExit('BLOCKED — Results artifact must contain exactly one </body> boundary.')
    if 'id="maxess-results-10"' not in html:
        raise SystemExit('BLOCKED — Results root not found.')
    if 'window.MAXESS_RESULT' not in html:
        raise SystemExit('BLOCKED — MAXESS_RESULT contract missing.')
    if 'MAXESS RESULTS — WHOLE-SYSTEM AAA PRESENTATION ENGINE' not in engine:
        raise SystemExit('BLOCKED — Whole-system presentation engine is not the expected artifact.')
    if 'MAXESS RESULTS — NAYA EXPERIENCE LAYER' not in naya:
        raise SystemExit('BLOCKED — Naya experience layer is not the expected artifact.')

    html = strip_inline(html, MARKER, 'maxess-whole-system-aaa-inline')
    html = strip_inline(html, NAYA_MARKER, 'maxess-naya-experience-inline')

    inline_engine = '\n<!-- ' + MARKER + ' -->\n<script id="maxess-whole-system-aaa-inline">\n' + engine + '\n</script>\n'
    inline_naya = '\n<!-- ' + NAYA_MARKER + ' -->\n<script id="maxess-naya-experience-inline">\n' + naya + '\n</script>\n'

    html, count = re.subn(r'</body>', inline_engine + inline_naya + '</body>', html, count=1, flags=re.IGNORECASE)
    if count != 1:
        raise SystemExit('BLOCKED — Could not locate the Results body boundary for assembly.')

    if 'data-maxess-build="whole-system-aaa-1.0"' not in html:
        html = html.replace(
            '<main id="maxess-results-10"',
            '<main id="maxess-results-10" data-maxess-build="whole-system-aaa-1.0"',
            1,
        )

    HTML.write_text(html, encoding='utf-8')

    final = HTML.read_text(encoding='utf-8')
    checks = {
        'whole-system marker': final.count(MARKER) == 1,
        'naya marker': final.count(NAYA_MARKER) == 1,
        'engine present': 'MAXESS RESULTS — WHOLE-SYSTEM AAA PRESENTATION ENGINE' in final,
        'naya layer present': 'MAXESS RESULTS — NAYA EXPERIENCE LAYER' in final,
        'build marker': 'data-maxess-build="whole-system-aaa-1.0"' in final,
        'result contract': 'window.MAXESS_RESULT' in final,
        'Naya image reference': 'i.postimg.cc/dVXw7sRN/' in final,
        'playground': 'mx-playground' in final,
        'single body': final.lower().count('<body') == 1 and final.lower().count('</body>') == 1,
        'complete document': final.lstrip().lower().startswith('<!doctype html>'),
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise SystemExit('BLOCKED — Assembly verification failed: ' + ', '.join(failed))

    print('ASSEMBLED COMPLETE GROOVE ARTIFACT')
    print('LINES:', len(final.splitlines()))
    print('BYTES:', len(final.encode('utf-8')))
    print('CHECKS: ALL PASS')


if __name__ == '__main__':
    main()
