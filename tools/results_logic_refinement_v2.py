from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARK = 'MAXESS RESULTS LOGIC REFINEMENT V2'
if MARK in s:
    print('Results logic refinement V2 already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS LOGIC REFINEMENT V2
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

SCRIPT = r'''
<!-- MAXESS RESULTS LOGIC REFINEMENT V2 -->
<script>
(function(){
  'use strict';
  var root=document.getElementById('resultsView');
  if(!root) return;
  var marker='maxessResultsLogicRefinementV2Mounted';
  function esc(v){return String(v==null?'':v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function renderGauge(target,score){
    var value=Math.max(0,Math.min(100,Math.round(Number(score)||0)));
    var cx=300,cy=255,r=176,start=150*Math.PI/180,end=390*Math.PI/180;
    var angle=start+(end-start)*value/100;
    function point(a,rr){return [cx+rr*Math.cos(a),cy+rr*Math.sin(a)];}
    var sp=point(start,r),ep=point(end,r),vp=point(Math.max(start+0.0001,angle),r),np=point(Math.max(start+0.0001,angle),126);
    var span=angle-start,largeArc=span>Math.PI?1:0;
    var track='M '+sp[0]+' '+sp[1]+' A '+r+' '+r+' 0 1 1 '+ep[0]+' '+ep[1];
    var fill=span<0.001?'M '+sp[0]+' '+sp[1]:'M '+sp[0]+' '+sp[1]+' A '+r+' '+r+' 0 '+largeArc+' 1 '+vp[0]+' '+vp[1];
    var ticks='';
    for(var i=0;i<=10;i++){
      var a=start+(end-start)*i/10,inner=r-13,outer=r+10,p1=point(a,inner),p2=point(a,outer);
      ticks+='<line class="tick '+(i%5===0?'major':'')+'" x1="'+p1[0]+'" y1="'+p1[1]+'" x2="'+p2[0]+'" y2="'+p2[1]+'"/>';
    }
    var labels='';
    [0,25,50,75,100].forEach(function(v){var a=start+(end-start)*v/100,q=point(a,r+31);labels+='<text class="tick-label" x="'+q[0]+'" y="'+q[1]+'" text-anchor="middle" dominant-baseline="middle">'+v+'</text>';});
    target.innerHTML='<svg class="rf-logical-gauge" viewBox="0 0 600 390" role="img" aria-label="MAXESS score '+value+' out of 100">'
      +'<defs><linearGradient id="rfLogicalGauge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5b2bb7"/><stop offset=".62" stop-color="#8a5cff"/><stop offset="1" stop-color="#b795ff"/></linearGradient></defs>'
      +'<path class="track" d="'+track+'"/><path class="fill" d="'+fill+'"/>'+ticks+labels
      +'<line class="needle" x1="'+cx+'" y1="'+cy+'" x2="'+np[0]+'" y2="'+np[1]+'"/>'
      +'<circle class="hub" cx="'+cx+'" cy="'+cy+'" r="16"/>'
      +'<text class="score" x="'+cx+'" y="'+(cy-4)+'" text-anchor="middle">'+value+'</text>'
      +'<text class="label" x="'+cx+'" y="'+(cy+27)+'" text-anchor="middle">MAXESS SCORE</text></svg>';
  }
  function refine(){
    if(!root.classList.contains('visible')) return;
    var page=root.querySelector('.results-final');
    if(!page || page.dataset[marker]==='1') return;
    page.dataset[marker]='1';
    var hero=page.querySelector('.rf-hero'),fingerprint=page.querySelector('.rf-fingerprint'),analysis=page.querySelector('.rf-analysis'),insight=page.querySelector('.rf-insight'),gauge=page.querySelector('.rf-gauge');
    var storyStrong=page.querySelector('.rf-story:not(.opportunity)'),storyOpportunity=page.querySelector('.rf-story.opportunity');
    if(hero&&fingerprint&&analysis) hero.parentNode.insertBefore(fingerprint,analysis);
    var side=page.querySelector('.rf-analysis-side'); if(side) side.remove();
    var scoreText=gauge&&gauge.querySelector('.score')?gauge.querySelector('.score').textContent.trim():'0';
    var heroTitle=hero&&hero.querySelector('h1'),heroCopy=hero&&hero.querySelector('p');
    if(heroTitle) heroTitle.textContent='This is what we discovered about you.';
    if(heroCopy){var old=heroCopy.textContent;heroCopy.textContent='Your MAXESS score is '+scoreText+'/100. '+old.replace(/^[^.]+\.\s*/,'');}
    if(gauge) renderGauge(gauge,scoreText);
    var analysisTitle=analysis&&analysis.querySelector('h2'),analysisLead=analysis&&analysis.querySelector('.rf-lead');
    var strongest=storyStrong&&storyStrong.querySelector('h3')?storyStrong.querySelector('h3').textContent.trim():'your strongest capability';
    var opportunity=storyOpportunity&&storyOpportunity.querySelector('h3')?storyOpportunity.querySelector('h3').textContent.trim():'your highest-leverage opportunity';
    var strongestCopy=storyStrong&&storyStrong.querySelector('p')?storyStrong.querySelector('p').textContent.trim():'';
    var opportunityCopy=storyOpportunity&&storyOpportunity.querySelector('p')?storyOpportunity.querySelector('p').textContent.trim():'';
    if(analysisTitle) analysisTitle.textContent='Your natural advantage is '+strongest+'.';
    if(analysisLead) analysisLead.innerHTML=esc(strongestCopy)+' <em>Your highest-leverage opportunity is '+esc(opportunity)+'.</em> '+esc(opportunityCopy);
    var fpTitle=fingerprint&&fingerprint.querySelector('h2'),fpCopy=fingerprint&&fingerprint.querySelector('p');
    if(fpTitle) fpTitle.textContent='Your AI capability fingerprint.';
    if(fpCopy) fpCopy.textContent='This shape shows how your five core AI capabilities work together. The words below it explain what the shape means.';
    page.querySelectorAll('.rf-kicker,.rf-band').forEach(function(el){el.style.color=el.classList.contains('rf-kicker')?'#b895ff':'#d5d1da';});
    var quote=insight&&insight.querySelector('blockquote'),insightCopy=insight&&insight.querySelector('p');
    if(quote) quote.textContent='Your next gain does not require becoming good at everything. It starts with turning '+strongest+' into a repeatable strength while deliberately improving '+opportunity+'.';
    if(insightCopy) insightCopy.textContent='That is the point of the report: recognize what is already working, identify the leverage point, and choose what to improve next.';
  }
  new MutationObserver(refine).observe(root,{attributes:true,attributeFilter:['class']});
  refine();
})();
</script>'''

style_idx=s.rfind('</style>')
body_idx=s.rfind('</body>')
if style_idx<0 or body_idx<0: raise RuntimeError('required HTML boundary missing')
s=s[:style_idx]+CSS+'\n'+s[style_idx:]
s=s[:body_idx]+SCRIPT+'\n'+s[body_idx:]
if MARK not in s: raise RuntimeError('logic refinement V2 marker missing')
p.write_text(s,encoding='utf-8')
print('Applied MAXESS Results logic refinement V2')
