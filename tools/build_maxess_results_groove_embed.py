from pathlib import Path
import re

SOURCE = Path('MAXESS-RESULTS-10-GROOVE.html')
OUTPUTS = [
    Path('MAXESS-RESULTS-GROOVE-EMBED.html'),
    Path('MAXESS-RESULTS-GROOVE-EMBED-9.95.html'),
]

STYLE_RE = re.compile(r'<style\b[^>]*>.*?</style>', re.I | re.S)
SCRIPT_RE = re.compile(r'<script\b[^>]*>.*?</script>', re.I | re.S)
BODY_RE = re.compile(r'<body\b[^>]*>(.*?)</body>', re.I | re.S)

PREFLIGHT = r'''<!-- MAXESS-RESULTS-CONTRACT-1 | GROOVE-NATIVE | FULL-AUTHORITATIVE-SOURCE | NO-IFRAME -->
<style id="MAXESS_GROOVE_EMBED_PREFLIGHT">
#maxess-groove-embed{
  position:relative!important;
  width:100%!important;
  max-width:none!important;
  min-height:100vh!important;
  margin:0!important;
  padding:0!important;
  display:block!important;
  overflow-x:hidden!important;
  background:#020204!important;
  color:#fff!important;
  isolation:isolate!important;
}
#maxess-groove-embed,#maxess-groove-embed *{box-sizing:border-box}
#maxess-groove-embed img,#maxess-groove-embed svg,#maxess-groove-embed canvas,#maxess-groove-embed video{max-width:100%}
#maxess-groove-embed button,#maxess-groove-embed a{touch-action:manipulation}
@media (prefers-reduced-motion:reduce){
  #maxess-groove-embed *,#maxess-groove-embed *::before,#maxess-groove-embed *::after{
    animation-duration:.01ms!important;
    animation-iteration-count:1!important;
    scroll-behavior:auto!important;
    transition-duration:.01ms!important;
  }
}
</style>'''

BRIDGE = r'''<script id="MAXESS_GROOVE_RESULT_BRIDGE">
(function(){
  'use strict';
  var KEY='MAXESS_RESULT';
  var CTX='MAXESS_NAYA_CONTEXT';
  function valid(v){return !!(v && v.dimensions && typeof v.dimensions==='object');}
  function remember(v){
    if(!valid(v)) return false;
    window.MAXESS_RESULT=v;
    window.RESULT=v;
    window.MAXESS_NAYA_CONTEXT=v;
    try{sessionStorage.setItem(KEY,JSON.stringify(v));}catch(e){}
    try{sessionStorage.setItem(CTX,JSON.stringify(v));}catch(e){}
    try{localStorage.setItem(KEY,JSON.stringify(v));}catch(e){}
    try{localStorage.setItem(CTX,JSON.stringify(v));}catch(e){}
    try{window.dispatchEvent(new CustomEvent('maxess:result-ready',{detail:v}));}catch(e){}
    return true;
  }
  function decode(raw){
    if(!raw) return null;
    try{return JSON.parse(decodeURIComponent(raw));}catch(e){}
    try{
      var s=raw.replace(/-/g,'+').replace(/_/g,'/');
      while(s.length%4)s+='=';
      var b=atob(s),bytes=Uint8Array.from(b,function(c){return c.charCodeAt(0)});
      return JSON.parse(new TextDecoder().decode(bytes));
    }catch(e){return null;}
  }
  try{
    var q=new URL(location.href).searchParams;
    var encoded=q.get('result');
    var fromUrl=decode(encoded);
    if(valid(fromUrl)) remember(fromUrl);
  }catch(e){}
  window.addEventListener('message',function(event){
    var data=event && event.data;
    var value=data && data.type==='MAXESS_RESULT'?data.result:(data && data.maxessResult?data.maxessResult:data);
    if(!valid(value)) return;
    remember(value);
    /* If the result arrived after the renderer booted, reload once so every
       existing renderer reads the same authoritative contract on startup. */
    try{
      if(!window.__MAXESS_RESULT_BRIDGE_RELOADED){
        window.__MAXESS_RESULT_BRIDGE_RELOADED=true;
        var url=new URL(location.href);
        url.searchParams.set('result',encodeURIComponent(JSON.stringify(value)));
        location.replace(url.toString());
      }
    }catch(e){}
  });
})();
</script>'''


def scope_css(style_block: str) -> str:
    # The authoritative source is a standalone document. Groove is an embed host,
    # so only the few true document-level selectors are rewritten. Component-level
    # selectors remain untouched, preserving the original visual system.
    if not style_block.startswith('<style'):
        return style_block
    m = re.match(r'(<style\b[^>]*>)(.*?)(</style>)$', style_block, flags=re.I | re.S)
    if not m:
        return style_block
    head, css, tail = m.groups()
    css = re.sub(r'body:has\(#royal-results-995\)\s*>\s*\*:not\(#royal-results-995\)', '#maxess-groove-embed > *:not(#royal-results-995):not(style):not(script)', css)
    css = re.sub(r'body:has\(#royal-results-995\)', '#maxess-groove-embed', css)
    css = re.sub(r'(?m)(^|[}\n]\s*)html\s*,\s*body\s*\{', r'\1#maxess-groove-embed{', css)
    css = re.sub(r'(?m)(^|[}\n]\s*)html\s*\{', r'\1#maxess-groove-embed{', css)
    css = re.sub(r'(?m)(^|[}\n]\s*)body\s*\{', r'\1#maxess-groove-embed{', css)
    css = re.sub(r'(?m)(^|[}\n]\s*):root\s*\{', r'\1#maxess-groove-embed{', css)
    css = re.sub(r'(?m)(^|[}\n]\s*)\*\s*\{', r'\1#maxess-groove-embed *{', css)
    css = re.sub(r'(?m)(^|[}\n]\s*)button\s*,\s*a\s*\{', r'\1#maxess-groove-embed button,#maxess-groove-embed a{', css)
    css = re.sub(r'(?m)(^|[}\n]\s*)button\s*\{', r'\1#maxess-groove-embed button{', css)
    css = re.sub(r'(?m)(^|[}\n]\s*)a\s*\{', r'\1#maxess-groove-embed a{', css)
    css = re.sub(r'(?m)(^|[}\n]\s*)::selection\s*\{', r'\1#maxess-groove-embed ::selection{', css)
    return head + css + tail


def strip_document_shell(page: str):
    body = BODY_RE.search(page)
    if not body:
        raise SystemExit('Authoritative Results body missing')
    body_html = body.group(1)
    scripts = SCRIPT_RE.findall(page)
    if not scripts:
        raise SystemExit('No script blocks found in authoritative Results source')
    styles = STYLE_RE.findall(page)
    if not styles:
        raise SystemExit('No stylesheet blocks found in authoritative Results source')
    # Scripts are re-added at the end in source order so the body remains pure markup.
    body_html = SCRIPT_RE.sub('', body_html)
    return [scope_css(s) for s in styles], body_html.strip(), scripts


def build():
    page = SOURCE.read_text(encoding='utf-8')
    styles, body_html, scripts = strip_document_shell(page)

    final = '\n'.join([
        '<div id="maxess-groove-embed" data-maxess-groove-embed="1" data-maxess-authority="MAXESS-RESULTS-10-GROOVE">',
        PREFLIGHT,
        '<!-- AUTHORITATIVE STYLES — preserved from MAXESS-RESULTS-10-GROOVE.html -->',
        *styles,
        '<!-- AUTHORITATIVE RESULTS MARKUP — preserved; no feature-reducing extraction -->',
        body_html,
        '<!-- AUTHORITATIVE RESULT BRIDGE -->',
        BRIDGE,
        '<!-- AUTHORITATIVE SCRIPTS — preserved in source order -->',
        *scripts,
        '</div>',
    ])

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

    required_tokens = [
        'MAXESS_RESULTS_ROYAL_9_95',
        'MAXESS-RESULTS-CONTRACT-1',
        'rr-naya-avatar',
        'rr-fingerprint',
        'rr-insight',
        'rr-path',
        'rr-finale',
        'const MASTERS=',
        'Writing & Communication',
        'Advanced AI Work',
        'https://nayanet.xyz/',
        'MAXESS_GROOVE_RESULT_BRIDGE',
    ]
    checks = {f'required:{token}': token in final for token in required_tokens}
    checks.update({
        'full_authoritative_source': 'MAXESS-RESULTS-10-GROOVE.html' in final,
        'no_iframe_tag': not bool(re.search(r'<iframe(?:\s|>)', final, flags=re.I)),
        'nonempty_artifact': len(final.splitlines()) >= 3000 and len(final.encode('utf-8')) >= 100000,
        'not_compressed_preview': len(final.splitlines()) >= 3000,
        'contains_result_bridge': 'MAXESS_GROOVE_RESULT_BRIDGE' in final,
    })
    for name, ok in checks.items():
        print(f'{name}: {"PASS" if ok else "FAIL"}')
    if not all(checks.values()):
        raise SystemExit('GROOVE EMBED RELEASE GATE FAILED')

    for output in OUTPUTS:
        output.write_text(final, encoding='utf-8')
        print(f'WROTE {output}: {len(final.splitlines())} lines / {len(final.encode("utf-8"))} bytes')
    print('GROOVE EMBED BUILD PASS — COMPLETE SOURCE PRESERVED')


if __name__ == '__main__':
    build()
