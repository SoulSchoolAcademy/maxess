from pathlib import Path
import re

SOURCE = Path('MAXESS-RESULTS-10-GROOVE.html')
OUTPUT = Path('MAXESS-RESULTS-GROOVE-EMBED.html')

STYLE_RE = re.compile(r'<style\b[^>]*>.*?</style>', re.I | re.S)
SCRIPT_RE = re.compile(r'<script\b[^>]*>.*?</script>', re.I | re.S)
BODY_RE = re.compile(r'<body\b[^>]*>(.*?)</body>', re.I | re.S)


def build():
    page = SOURCE.read_text(encoding='utf-8')
    body_match = BODY_RE.search(page)
    if not body_match:
        raise SystemExit('Source has no <body>; cannot build Groove fragment')

    styles = '\n'.join(STYLE_RE.findall(page))
    scripts = '\n'.join(SCRIPT_RE.findall(page))
    body = body_match.group(1).strip()

    preflight = '''<style id="MAXESS_GROOVE_EMBED_PREFLIGHT">
#maxess-groove-embed{
  position:relative!important;
  left:50%!important;
  transform:translateX(-50%)!important;
  width:100vw!important;
  max-width:100vw!important;
  min-height:100vh!important;
  margin:0!important;
  padding:0!important;
  display:block!important;
  overflow-x:hidden!important;
  background:#020204!important;
  color:#fff!important;
}
#maxess-groove-embed #m9-results{display:block!important;min-height:100vh!important;width:100%!important;max-width:none!important;}
#maxess-groove-embed #royal-results-995{display:block!important;min-height:100vh!important;width:100%!important;max-width:none!important;}
#maxess-groove-embed .m9-results,.maxess-groove-embed .m9-results{width:100%!important;max-width:none!important;}
#maxess-groove-embed iframe{display:none!important;}
</style>'''

    final = '\n'.join([
        '<div id="maxess-groove-embed" data-maxess-groove-embed="1">',
        preflight,
        styles,
        body,
        scripts,
        '</div>',
    ])
    OUTPUT.write_text(final, encoding='utf-8')

    forbidden = [
        (r'<!doctype\\b', 'doctype'),
        (r'<html\\b', 'html shell'),
        (r'<head\\b', 'head shell'),
        (r'<body\\b', 'body shell'),
        (r'<iframe\\b', 'iframe'),
    ]
    for pattern, label in forbidden:
        if re.search(pattern, final, flags=re.I):
            raise SystemExit(f'Groove embed contains forbidden {label} markup')

    checks = {
        'royal_layer': 'MAXESS_RESULTS_ROYAL_9_95' in final,
        'result_contract': 'MAXESS-RESULTS-CONTRACT-1' in final,
        'naya_masters': 'const MASTERS=' in final,
        'full_bleed': 'width:100vw!important' in final,
        'no_iframe_string': '<iframe' not in final.lower(),
        'substantial': len(final.splitlines()) >= 3000 and len(final.encode('utf-8')) >= 90000,
    }
    for name, ok in checks.items():
        print(f'{name}: {"PASS" if ok else "FAIL"}')
    if not all(checks.values()):
        raise SystemExit('GROOVE EMBED RELEASE GATE FAILED')
    print(f'GROOVE EMBED BUILD PASS: {len(final.splitlines())} lines / {len(final.encode("utf-8"))} bytes')


if __name__ == '__main__':
    build()
