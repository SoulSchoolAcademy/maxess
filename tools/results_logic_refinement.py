from pathlib import Path
import re

p = Path('code')
s = p.read_text(encoding='utf-8')
MARK = 'MAXESS RESULTS LOGIC REFINEMENT'
if MARK in s:
    print('Results logic refinement already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS LOGIC REFINEMENT
   Truthful score geometry, stronger hierarchy, less dashboard.
========================================================= */
.results-final .rf-hero h1{max-width:980px;margin-inline:auto;}
.results-final .rf-hero p{color:#c6c2ca;}
.results-final .rf-band{color:#d5d1da;}
.results-final .rf-section{border-top-color:rgba(255,255,255,.08);}
.results-final .rf-analysis{display:block;max-width:940px;margin:0 auto;}
.results-final .rf-analysis-side{display:none!important;}
.results-final .rf-analysis h2{max-width:880px;}
.results-final .rf-lead{max-width:860px;color:#d0ccd4;}
.results-final .rf-fingerprint{padding-top:52px;}
.results-final .rf-radar{margin-top:16px;}
.results-final .rf-radar .label{fill:#c0bbc4;}
.results-final .rf-fingerprint p{color:#b9b5bd;}
.results-final .rf-story span{color:#98939e;}
.results-final .rf-story p{color:#b9b5bd;}
.results-final .rf-insight p,.results-final .rf-process > p,.results-final .rf-masters > p,.results-final .rf-next p{color:#b7b2ba;}
.results-final .rf-gauge{max-width:700px;margin-top:24px;}
.results-final .rf-gauge svg{overflow:visible;}
.rf-logical-gauge .track{fill:none;stroke:#2d2b33;stroke-width:22;stroke-linecap:round;}
.rf-logical-gauge .fill{fill:none;stroke:url(#rfLogicalGauge);stroke-width:22;stroke-linecap:round;filter:drop-shadow(0 0 13px rgba(138,92,255,.35));}
.rf-logical-gauge .tick{stroke:#5b5662;stroke-width:2;}
.rf-logical-gauge .tick.major{stroke:#8e8995;stroke-width:3;}
.rf-logical-gauge .tick-label{fill:#8f8994;font:800 11px system-ui,sans-serif;letter-spacing:.02em;}
.rf-logical-gauge .needle{stroke:#fff;stroke-width:5;stroke-linecap:round;filter:drop-shadow(0 0 7px rgba(255,255,255,.45));}
.rf-logical-gauge .hub{fill:#09070d;stroke:#b895ff;stroke-width:3;filter:drop-shadow(0 0 10px rgba(138,92,255,.45));}
.rf-logical-gauge .score{fill:#fff;font:1000 76px system-ui,sans-serif;letter-spacing:-.065em;}
.rf-logical-gauge .label{fill:#9f99a5;font:900 10px system-ui,sans-serif;letter-spacing:.16em;}
@media(max-width:620px){.results-final .rf-fingerprint{padding-top:38px}.results-final .rf-gauge{max-width:640px}}
'''

SCRIPT = r'''
<!-- MAXESS RESULTS LOGIC REFINEMENT -->
<script>
(function(){
  'use strict';
  const marker='maxessResultsLogicRefinementMounted';
  const root=document.getElementById('resultsView');
  if(!root) return;

  const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

  function renderLogicalGauge(target, score){
    const value=Math.max(0,Math.min(100,Math.round(Number(score)||0)));
    const cx=300,cy=255,r=176;
    const start=150*Math.PI/180;
    const end=390*Math.PI/180;
    const angle=start+(end-start)*value/100;
    const point=(a,rr)=>[cx+rr*Math.cos(a),cy+rr*Math.sin(a)];
    const startPoint=point(start,r);
    const endPoint=point(end,r);
    const valuePoint=point(Math.max(start+0.0001,angle),r);
    const needlePoint=point(Math.max(start+0.0001,angle),126);
    const span=angle-start;
    const largeArc=span>Math.PI?1:0;
    const track=`M ${startPoint[0]} ${startPoint[1]} A ${r} ${r} 0 1 1 ${endPoint[0]} ${endPoint[1]}`;
    const fill=span<0.001
      ? `M ${startPoint[0]} ${startPoint[1]}`
      : `M ${startPoint[0]} ${startPoint[1]} A ${r} ${r} 0 ${largeArc} 1 ${valuePoint[0]} ${valuePoint[1]}`;
    let ticks='';
    for(let i=0;i<=10;i++){
      const a=start+(end-start)*i/10;
      const inner=r-13, outer=r+10;
      const p1=point(a,inner),p2=point(a,outer);
      ticks += `<line class="tick ${i%5===0?'major':''}" x1="${p1[0]}" y1="${p1[1]}" x2="${p2[0]}" y2="${p2[1]}"/>`;
    }
    const labels=[0,25,50,75,100].map(v=>{
      const a=start+(end-start)*v/100;
      const q=point(a,r+31);
      return `<text class="tick-label" x="${q[0]}" y="${q[1]}" text-anchor="middle" dominant-baseline="middle">${v}</text>`;
    }).join('');
    target.innerHTML=`<svg class="rf-logical-gauge" viewBox="0 0 600 390" role="img" aria-label="MAXESS score ${value} out of 100">
      <defs><linearGradient id="rfLogicalGauge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5b2bb7"/><stop offset=".62" stop-color="#8a5cff"/><stop offset="1" stop-color="#b795ff"/></linearGradient></defs>
      <path class="track" d="${track}"/>
      <path class="fill" d="${fill}"/>
      ${ticks}${labels}
      <line class="needle" x1="${cx}" y1="${cy}" x2="${needlePoint[0]}" y2="${needlePoint[1]}"/>
      <circle class="hub" cx="${cx}" cy="${cy}" r="16"/>
      <text class="score" x="${cx}" y="${cy-4}" text-anchor="middle">${value}</text>
      <text class="label" x="${cx}" y="${cy+27}" text-anchor="middle">MAXESS SCORE</text>
    </svg>`;
  }

  function refine(){
    if(!root.classList.contains('visible')) return;
    const page=root.querySelector('.results-final');
    if(!page || page.dataset[marker]==='1') return;
    page.dataset[marker]='1';

    const hero=page.querySelector('.rf-hero');
    const fingerprint=page.querySelector('.rf-fingerprint');
    const analysis=page.querySelector('.rf-analysis');
    const insight=page.querySelector('.rf-insight');
    const gauge=page.querySelector('.rf-gauge');
    const storyStrong=page.querySelector('.rf-story:not(.opportunity)');
    const storyOpportunity=page.querySelector('.rf-story.opportunity');

    /* 1. The report follows the human questions: score -> see yourself -> understand. */
    if(hero && fingerprint && analysis) hero.parentNode.insertBefore(fingerprint,analysis);

    /* 2. Remove the arbitrary side panel. The report gets one clear narrative column. */
    page.querySelector('.rf-analysis-side')?.remove();

    /* 3. Use the actual score in the hero copy and make the statement about discovery, not the gauge. */
    const scoreText=gauge?.querySelector('.score')?.textContent?.trim()||'0';
    const heroTitle=hero?.querySelector('h1');
    const heroCopy=hero?.querySelector('p');
    if(heroTitle) heroTitle.textContent='This is what we discovered about you.';
    if(heroCopy) heroCopy.textContent=`Your MAXESS score is ${scoreText}/100. ${heroCopy.textContent.replace(/^[^.]+\.\s*/,'')}`;

    /* 4. The score visualization is geometrically truthful: 0 = lower-left, 50 = top, 100 = lower-right. */
    if(gauge) renderLogicalGauge(gauge,scoreText);

    /* 5. Make the report explain the graph instead of presenting another dashboard tile. */
    const analysisTitle=analysis?.querySelector('h2');
    const analysisLead=analysis?.querySelector('.rf-lead');
    const strongest=storyStrong?.querySelector('h3')?.textContent?.trim()||'your strongest capability';
    const opportunity=storyOpportunity?.querySelector('h3')?.textContent?.trim()||'your highest-leverage opportunity';
    const strongestCopy=storyStrong?.querySelector('p')?.textContent?.trim()||'';
    const opportunityCopy=storyOpportunity?.querySelector('p')?.textContent?.trim()||'';
    if(analysisTitle) analysisTitle.textContent=`Your natural advantage is ${strongest}.`;
    if(analysisLead) analysisLead.innerHTML=`${esc(strongestCopy)} <em>Your highest-leverage opportunity is ${esc(opportunity)}.</em> ${esc(opportunityCopy)}`;

    /* 6. The fingerprint becomes the first analytical reveal, not something buried below a panel. */
    const fpTitle=fingerprint?.querySelector('h2');
    const fpCopy=fingerprint?.querySelector('p');
    if(fpTitle) fpTitle.textContent='Your AI capability fingerprint.';
    if(fpCopy) fpCopy.textContent='This shape shows how your five core AI capabilities work together. The words below it explain what the shape means.';

    /* 7. Neutralize the pink/lavender report-copy feeling. Purple is reserved for emphasis. */
    page.querySelectorAll('.rf-kicker,.rf-band').forEach(el=>{el.style.color=el.classList.contains('rf-kicker')?'#b895ff':'#d5d1da';});

    /* 8. Replace the generic insight copy with a transparent, assessment-grounded statement. */
    const quote=insight?.querySelector('blockquote');
    const insightCopy=insight?.querySelector('p');
    if(quote) quote.textContent=`Your next gain does not require becoming good at everything. It starts with turning ${strongest} into a repeatable strength while deliberately improving ${opportunity}.`;
    if(insightCopy) insightCopy.textContent='That is the point of the report: recognize what is already working, identify the leverage point, and choose what to improve next.';
  }

  const observer=new MutationObserver(refine);
  observer.observe(root,{attributes:true,attributeFilter:['class']});
  refine();
})();
</script>'''

body='</body>'
idx=s.rfind(body)
if idx<0: raise RuntimeError('body closing tag missing')
style_idx=s.rfind('</style>')
if style_idx<0: raise RuntimeError('stylesheet closing tag missing')
s=s[:style_idx]+CSS+'\n'+s[style_idx:]
s=s[:idx]+SCRIPT+'\n'+s[idx:]
if s.count(MARK)!=1: raise RuntimeError('logic refinement marker count invalid')
p.write_text(s,encoding='utf-8')
print('Applied MAXESS Results logic refinement')
