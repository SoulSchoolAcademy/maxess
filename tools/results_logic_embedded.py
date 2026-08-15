from pathlib import Path
import re

p = Path('code')
s = p.read_text(encoding='utf-8')
MARK = 'MAXESS RESULTS LOGIC EMBEDDED'
if MARK in s:
    print('Results logic embedded pass already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS LOGIC EMBEDDED
   One Results authority. Truthful score geometry. Human hierarchy.
========================================================= */
.results-final .rf-hero h1{max-width:980px;margin-inline:auto;}
.results-final .rf-hero p{color:#c6c2ca;}
.results-final .rf-band{color:#d5d1da;}
.results-final .rf-analysis{display:block;max-width:940px;margin:0 auto;}
.results-final .rf-analysis-side{display:none!important;}
.results-final .rf-analysis h2{max-width:880px;}
.results-final .rf-lead{max-width:860px;color:#d0ccd4;}
.results-final .rf-fingerprint{padding-top:52px;}
.results-final .rf-radar{margin-top:16px;}
.results-final .rf-radar .label{fill:#c0bbc4;}
.results-final .rf-fingerprint p,.results-final .rf-story p,.results-final .rf-insight p,.results-final .rf-process > p,.results-final .rf-masters > p,.results-final .rf-next p{color:#b9b5bd;}
.results-final .rf-gauge{max-width:700px;margin-top:24px;}
.rf-logical-gauge .track{fill:none;stroke:#2d2b33;stroke-width:22;stroke-linecap:round;}
.rf-logical-gauge .fill{fill:none;stroke:url(#rfLogicalGauge);stroke-width:22;stroke-linecap:round;filter:drop-shadow(0 0 13px rgba(138,92,255,.35));}
.rf-logical-gauge .tick{stroke:#5b5662;stroke-width:2;}
.rf-logical-gauge .tick.major{stroke:#8e8995;stroke-width:3;}
.rf-logical-gauge .tick-label{fill:#8f8994;font:800 11px system-ui,sans-serif;}
.rf-logical-gauge .needle{stroke:#fff;stroke-width:5;stroke-linecap:round;filter:drop-shadow(0 0 7px rgba(255,255,255,.45));}
.rf-logical-gauge .hub{fill:#09070d;stroke:#b895ff;stroke-width:3;filter:drop-shadow(0 0 10px rgba(138,92,255,.45));}
.rf-logical-gauge .score{fill:#fff;font:1000 76px system-ui,sans-serif;letter-spacing:-.065em;}
.rf-logical-gauge .label{fill:#9f99a5;font:900 10px system-ui,sans-serif;letter-spacing:.16em;}
@media(max-width:620px){.results-final .rf-fingerprint{padding-top:38px}.results-final .rf-gauge{max-width:640px}}
'''

GAUGE = r'''function speedometer(score){
    const c=Math.max(0,Math.min(100,Math.round(Number(score)||0))),cx=300,cy=255,r=176;
    const start=150*Math.PI/180,end=390*Math.PI/180,angle=start+(end-start)*c/100;
    const point=(a,rr)=>[cx+rr*Math.cos(a),cy+rr*Math.sin(a)];
    const sp=point(start,r),ep=point(end,r),vp=point(Math.max(start+0.0001,angle),r),np=point(Math.max(start+0.0001,angle),126);
    const span=angle-start,largeArc=span>Math.PI?1:0;
    const track='M '+sp[0]+' '+sp[1]+' A '+r+' '+r+' 0 1 1 '+ep[0]+' '+ep[1];
    const fill=span<0.001?'M '+sp[0]+' '+sp[1]:'M '+sp[0]+' '+sp[1]+' A '+r+' '+r+' 0 '+largeArc+' 1 '+vp[0]+' '+vp[1];
    let ticks='';
    for(let i=0;i<=10;i++){const a=start+(end-start)*i/10,inner=r-13,outer=r+10,p1=point(a,inner),p2=point(a,outer);ticks+='<line class="tick '+(i%5===0?'major':'')+'" x1="'+p1[0]+'" y1="'+p1[1]+'" x2="'+p2[0]+'" y2="'+p2[1]+'"/>';}
    let labels='';
    [0,25,50,75,100].forEach(v=>{const a=start+(end-start)*v/100,q=point(a,r+31);labels+='<text class="tick-label" x="'+q[0]+'" y="'+q[1]+'" text-anchor="middle" dominant-baseline="middle">'+v+'</text>';});
    return '<svg class="rf-logical-gauge" viewBox="0 0 600 390" role="img" aria-label="MAXESS score '+c+' out of 100"><defs><linearGradient id="rfLogicalGauge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5b2bb7"/><stop offset=".62" stop-color="#8a5cff"/><stop offset="1" stop-color="#b795ff"/></linearGradient></defs><path class="track" d="'+track+'"/><path class="fill" d="'+fill+'"/>'+ticks+labels+'<line class="needle" x1="'+cx+'" y1="'+cy+'" x2="'+np[0]+'" y2="'+np[1]+'"/><circle class="hub" cx="'+cx+'" cy="'+cy+'" r="16"/><text class="score" x="'+cx+'" y="'+(cy-4)+'" text-anchor="middle">'+c+'</text><text class="label" x="'+cx+'" y="'+(cy+27)+'" text-anchor="middle">MAXESS SCORE</text></svg>';
  }'''

new_script = GAUGE + '\n  function radar'
pattern = r'function speedometer\(score\)\{[\s\S]*?\n  \}\n  function radar'
if not re.search(pattern,s):
    raise RuntimeError('speedometer function boundary not found')
s = re.sub(pattern,new_script,s,count=1)

INSERT_ANCHOR = "    root.querySelector('#rfMaster')?.addEventListener('click',()=>trial?.click());"
if INSERT_ANCHOR not in s:
    raise RuntimeError('Results mount anchor not found')

REFINE = r'''
    /* =========================================================
       MAXESS RESULTS LOGIC EMBEDDED
       Score -> fingerprint -> advantage -> opportunity -> insight.
    ========================================================= */
    const logicalFingerprint=root.querySelector('.rf-fingerprint');
    const logicalAnalysis=root.querySelector('.rf-analysis');
    if(logicalFingerprint && logicalAnalysis) logicalAnalysis.parentNode.insertBefore(logicalFingerprint,logicalAnalysis);
    root.querySelector('.rf-analysis-side')?.remove();
    const logicalHero=root.querySelector('.rf-hero');
    const logicalHeroTitle=logicalHero?.querySelector('h1');
    const logicalHeroCopy=logicalHero?.querySelector('p');
    if(logicalHeroTitle) logicalHeroTitle.textContent='This is what we discovered about you.';
    if(logicalHeroCopy) logicalHeroCopy.textContent='Your MAXESS score is '+score+'/100. '+logicalHeroCopy.textContent.replace(/^[^.]+\.\s*/,'');
    const logicalStrong=root.querySelector('.rf-story:not(.opportunity)');
    const logicalOpportunity=root.querySelector('.rf-story.opportunity');
    const logicalStrongName=logicalStrong?.querySelector('h3')?.textContent?.trim()||'your strongest capability';
    const logicalOpportunityName=logicalOpportunity?.querySelector('h3')?.textContent?.trim()||'your highest-leverage opportunity';
    const logicalStrongCopy=logicalStrong?.querySelector('p')?.textContent?.trim()||'';
    const logicalOpportunityCopy=logicalOpportunity?.querySelector('p')?.textContent?.trim()||'';
    const logicalAnalysisTitle=logicalAnalysis?.querySelector('h2');
    const logicalAnalysisLead=logicalAnalysis?.querySelector('.rf-lead');
    if(logicalAnalysisTitle) logicalAnalysisTitle.textContent='Your natural advantage is '+logicalStrongName+'.';
    if(logicalAnalysisLead) logicalAnalysisLead.innerHTML=esc(logicalStrongCopy)+' <em>Your highest-leverage opportunity is '+esc(logicalOpportunityName)+'.</em> '+esc(logicalOpportunityCopy);
    const logicalFingerprintTitle=logicalFingerprint?.querySelector('h2');
    const logicalFingerprintCopy=logicalFingerprint?.querySelector('p');
    if(logicalFingerprintTitle) logicalFingerprintTitle.textContent='Your AI capability fingerprint.';
    if(logicalFingerprintCopy) logicalFingerprintCopy.textContent='This shape shows how your five core AI capabilities work together. The words below it explain what the shape means.';
    const logicalInsight=root.querySelector('.rf-insight');
    const logicalQuote=logicalInsight?.querySelector('blockquote');
    const logicalInsightCopy=logicalInsight?.querySelector('p');
    if(logicalQuote) logicalQuote.textContent='Your next gain does not require becoming good at everything. It starts with turning '+logicalStrongName+' into a repeatable strength while deliberately improving '+logicalOpportunityName+'.';
    if(logicalInsightCopy) logicalInsightCopy.textContent='That is the point of the report: recognize what is already working, identify the leverage point, and choose what to improve next.';
'''
s = s.replace(INSERT_ANCHOR,REFINE+'\n'+INSERT_ANCHOR,1)

style_idx=s.rfind('</style>')
if style_idx<0: raise RuntimeError('stylesheet closing tag missing')
s=s[:style_idx]+CSS+'\n'+s[style_idx:]

# Safety checks: embedded pass must be present; repeated occurrences are expected because the label appears in CSS and the runtime annotation.
if MARK not in s:
    raise RuntimeError('embedded refinement marker missing')
if s.count('rf-logical-gauge')<1:
    raise RuntimeError('logical gauge CSS missing')

p.write_text(s,encoding='utf-8')
print('Applied MAXESS embedded Results logic')
