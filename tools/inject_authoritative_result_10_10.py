#!/usr/bin/env python3
"""Inject the single MAXESS Result Contract before any Results renderer runs."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build_maxess_results_10_self_optimized import FIXTURE  # noqa: E402

FILES = [
    ROOT / 'MAXESS-RESULTS-FINAL-GROOVE.html',
    ROOT / 'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html',
    ROOT / 'MAXESS-RESULTS-10-GROOVE.html',
    ROOT / 'MAXESS-RESULTS-GROOVE-EMBED.html',
    ROOT / 'MAXESS-RESULTS-GROOVE-EMBED-9.95.html',
]
MARKER = 'MAXESS_RESULT_BOOTSTRAP_10_10'


def payload():
    dimensions=[]
    for name,score,meaning,action in FIXTURE['dimensions']:
        dimensions.append({'id':name.lower().replace(' ','-'),'name':name,'score':score,'description':meaning,'insight':action})
    result={'schema':'MAXESS-RESULT-1','mode':FIXTURE['mode'],'overallScore':FIXTURE['score'],'band':FIXTURE['band'],'dimensions':dimensions,'areas':[{'name':n,'description':d} for n,d in FIXTURE['areas']]}
    return json.dumps(result,ensure_ascii=False,separators=(',',':'))

QUERY_BRIDGE=r'''<script id="maxess-result-query-bridge-10-10">
(function(){
'use strict';
if(window.MAXESS_RESULT&&Array.isArray(window.MAXESS_RESULT.dimensions))return;
var params=new URLSearchParams(window.location.search),encoded=params.get('result');if(!encoded)return;
try{var b64=encoded.replace(/-/g,'+').replace(/_/g,'/');while(b64.length%4)b64+='=';var binary=atob(b64),bytes=new Uint8Array(binary.length);for(var i=0;i<binary.length;i++)bytes[i]=binary.charCodeAt(i);var payload=JSON.parse(new TextDecoder('utf-8').decode(bytes));if(!payload||payload.version!=='MAXESS-RESULTS-CONTRACT-1'||payload.completed!==true)throw new Error('invalid contract');var names={direction:'Direction',communication:'Communication',evaluation:'Evaluation',iteration:'Iteration','systems-thinking':'Systems Thinking'};var dimensions=Object.keys(names).map(function(id){return{id:id,name:names[id],score:Number(payload.dimensions&&payload.dimensions[id])||0};});var overall=Math.max(0,Math.min(100,Number(payload.overall)||0));var band=overall<=50?'Foundation':overall<=75?'Developing':overall<=90?'Advancing':'Mastering';window.MAXESS_RESULT={schema:'MAXESS-RESULT-1',mode:'assessment-handoff',overallScore:overall,band:band,dimensions:dimensions,selectedInterests:Array.isArray(payload.selectedInterests)?payload.selectedInterests:[],responses:Array.isArray(payload.responses)?payload.responses:[]};}catch(e){window.MAXESS_RESULT_ERROR='Invalid MAXESS Result Contract';}
})();
</script>'''

BOOTSTRAP=QUERY_BRIDGE+'<script type="application/json" id="MAXESS_RESULT_BOOTSTRAP_10_10">'+payload()+'</script><script id="maxess-result-contract-10-10">window.MAXESS_RESULT=window.MAXESS_RESULT||JSON.parse(document.getElementById(\'MAXESS_RESULT_BOOTSTRAP_10_10\').textContent);</script>'

changed=0
for path in FILES:
    if not path.exists():
        continue
    text=path.read_text(encoding='utf-8')
    if MARKER in text:
        continue
    if '</head>' in text:
        text=text.replace('</head>',BOOTSTRAP+'\n</head>',1)
    elif '<body' in text:
        import re
        text=re.sub(r'(<body(?:\s[^>]*)?>)',r'\1'+BOOTSTRAP+'\n',text,count=1,flags=re.I)
    else:
        text=BOOTSTRAP+'\n'+text
    path.write_text(text,encoding='utf-8')
    changed+=1

if changed==0:
    raise SystemExit('No artifacts received the Result Contract bootstrap.')
print(f'Injected authoritative MAXESS_RESULT contract into {changed} artifacts.')
