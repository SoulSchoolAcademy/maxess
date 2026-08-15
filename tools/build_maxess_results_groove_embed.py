from pathlib import Path
import re

SOURCE = Path('MAXESS-RESULTS-10-GROOVE.html')
OUTPUT = Path('MAXESS-RESULTS-GROOVE-EMBED.html')

ROYAL_STYLE_RE = re.compile(r'<style\s+id=["\']MAXESS_RESULTS_ROYAL_9_95_CSS["\'][^>]*>.*?</style>', re.I | re.S)
ROYAL_MAIN_RE = re.compile(r'<main\s+id=["\']royal-results-995["\'][^>]*>.*?</main>', re.I | re.S)
SCRIPT_RE = re.compile(r'<script\b[^>]*>.*?</script>', re.I | re.S)


def build():
    page = SOURCE.read_text(encoding='utf-8')
    style_match = ROYAL_STYLE_RE.search(page)
    main_match = ROYAL_MAIN_RE.search(page)
    scripts = SCRIPT_RE.findall(page)
    if not style_match:
        raise SystemExit('Royal 9.95 stylesheet missing')
    if not main_match:
        raise SystemExit('Royal 9.95 Results main missing')
    if not scripts:
        raise SystemExit('No script blocks found')

    # The final script in the document is the authoritative Royal Results controller.
    royal_script = scripts[-1]

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
#maxess-groove-embed #royal-results-995{display:block!important;min-height:100vh!important;width:100%!important;max-width:none!important;}
</style>'''

    final = '\n'.join([
        '<div id="maxess-groove-embed" data-maxess-groove-embed="1">',
        preflight,
        style_match.group(0),
        main_match.group(0),
        royal_script,
        '</div>',
    ])
    OUTPUT.write_text(final, encoding='utf-8')

    forbidden = [
        (r'<!doctype\s', 'doctype'),
        (r'<html(?:\s|>)', 'html shell'),
        (r'<head(?:\s|>)', 'head shell'),
        (r'<body(?:\s|>)', 'body shell'),
        (r'<iframe(?:\s|>)', 'iframe'),
    ]
    for pattern, label in forbidden:
        if re.search(pattern, final, flags=re.I):
            raise SystemExit(f'Groove embed contains forbidden {label} markup')

    checks = {
        'royal_layer': 'MAXESS_RESULTS_ROYAL_9_95' in final,
        'royal_root': 'id="royal-results-995"' in final,
        'result_contract': 'MAXESS-RESULTS-CONTRACT-1' in final,
        'naya_masters': 'const MASTERS=' in final,
        'five_dimensions': all(x in final for x in ['Direction','Communication','Evaluation','Iteration','Systems Thinking']),
        'full_bleed': 'width:100vw!important' in final,
        'no_iframe_tag': not bool(re.search(r'<iframe(?:\s|>)', final, flags=re.I)),
        'no_legacy_results_root': 'id="m9-results"' not in final,
        'no_legacy_nayanet_frame': 'm9-nayanet-frame' not in final,
        'substantial': len(final.splitlines()) >= 2500 and len(final.encode('utf-8')) >= 70000,
    }
    for name, ok in checks.items():
        print(f'{name}: {"PASS" if ok else "FAIL"}')
    if not all(checks.values()):
        raise SystemExit('GROOVE EMBED RELEASE GATE FAILED')
    print(f'GROOVE EMBED BUILD PASS: {len(final.splitlines())} lines / {len(final.encode("utf-8"))} bytes')


if __name__ == '__main__':
    build()
