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
html,body{margin:0!important;padding:0!important;background:#020204!important;min-height:100%!important;}
body{overflow-x:hidden!important;}
#maxess-groove-embed{width:100%!important;min-height:100vh!important;display:block!important;background:#020204!important;color:#fff!important;}
#maxess-groove-embed #m9-results{display:block!important;min-height:100vh!important;}
#maxess-groove-embed #royal-results-995{display:block!important;min-height:100vh!important;}
#maxess-groove-embed .m9-results,.maxess-groove-embed .m9-results{width:100%!important;max-width:none!important;}
#maxess-groove-embed iframe{display:none!important;}
</style>'''

    out = [
        '<div id="maxess-groove-embed" data-maxess-groove-embed="1">',
        preflight,
        styles,
        body,
        scripts,
        '</div>',
    ]
    final = '\n'.join(out)
    OUTPUT.write_text(final, encoding='utf-8')

    if '<!doctype' in final.lower() or '<html' in final.lower() or '<head' in final.lower() or '<body' in final.lower():
        raise SystemExit('Groove embed still contains document shell tags')
    if '<iframe' in final.lower():
        raise SystemExit('Groove embed contains an iframe')
    if 'MAXESS_RESULTS_ROYAL_9_95' not in final:
        raise SystemExit('Royal Results layer missing from Groove embed')
    if 'MAXESS-RESULTS-CONTRACT-1' not in final:
        raise SystemExit('Result Contract missing from Groove embed')
    if 'const MASTERS=' not in final:
        raise SystemExit('Naya Masters data missing from Groove embed')
    if len(final.splitlines()) < 3000:
        raise SystemExit('Groove embed unexpectedly small')
    if len(final.encode('utf-8')) < 90000:
        raise SystemExit('Groove embed unexpectedly small in bytes')
    print(f'GROOVE EMBED BUILD PASS: {len(final.splitlines())} lines / {len(final.encode("utf-8"))} bytes')


if __name__ == '__main__':
    build()
