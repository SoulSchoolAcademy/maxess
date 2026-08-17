/*
 MAXESS RESULTS — V21 FINISH PASS

 Purpose:
 - Refine the approved V20 Results experience in place.
 - Preserve the existing Groove/V20 architecture and authoritative MAXESS_RESULT.
 - Finish the hero, score, five mini-orbs, report narrative, Naya interpretation,
   strength/lever/next-move hierarchy, Masters personalization, and intentional print/PDF mode.
 - No replacement renderer. No hard-coded production result.

 Integration note:
 This file is designed to run against the existing V20 MAXESS Results DOM.
*/
(function(){
  'use strict';
  if(window.__MAXESS_V21_FINISH__) return;
  window.__MAXESS_V21_FINISH__=true;

  var root=document.getElementById('maxess-results-10');
  if(!root) return;

  var R=function(){return window.MAXESS_RESULT||{};};
  var esc=function(v){return String(v==null?'':v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});};
  var clamp=function(v){v=Number(v);return Number.isFinite(v)?Math.max(0,Math.min(100,v)):0;};
  var first=function(){for(var i=0;i<arguments.length;i++){var v=arguments[i];if(v!==undefined&&v!==null&&String(v).trim()!=='')return v;}return '';};
  var result=R();
  var score=clamp(first(result.overallScore,result.masterScore,result.score,result.overall));
  var dims=(Array.isArray(result.dimensions)?result.dimensions:[]).slice(0,5).map(function(d,i){return {id:first(d.id,String(i+1)),name:first(d.name,d.label,'Dimension '+(i+1)),score:clamp(first(d.score,d.value,d.percentage,0)),description:first(d.description,d.insight,d.interpretation)}});
  var profile=first(result.profile,result.user,result.person,result.identity)||{};
  var name=first(profile.name,profile.displayName,result.name,result.firstName,'');
  var band=function(s){return s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':'Foundation';};
  var strongest=dims.slice().sort(function(a,b){return b.score-a.score})[0]||null;
  var weakest=dims.slice().sort(function(a,b){return a.score-b.score})[0]||null;
  var avg=dims.length?dims.reduce(function(a,d){return a+d.score},0)/dims.length:score;

  function addStyle(){
    if(document.getElementById('maxess-v21-style')) return;
    var s=document.createElement('style');s.id='maxess-v21-style';
    s.textContent=`
#maxess-results-10 .v21-naya{width:min(900px,100%);margin:0 auto 8px;padding:18px 22px;border:1px solid rgba(255,255,255,.14);border-radius:26px;background:linear-gradient(145deg,rgba(255,255,255,.07),rgba(150,93,255,.10) 55%,rgba(0,0,0,.22));box-shadow:0 20px 60px rgba(0,0,0,.32),inset 0 1px rgba(255,255,255,.10);text-align:left;display:grid;grid-template-columns:auto 1fr auto;gap:16px;align-items:center}
#maxess-results-10 .v21-naya img{width:62px;height:62px;border-radius:50%;object-fit:cover;border:1px solid rgba(255,255,255,.24);box-shadow:0 8px 25px rgba(0,0,0,.35)}
#maxess-results-10 .v21-naya-kicker{font-size:10px;letter-spacing:.18em;font-weight:900;color:#cdb4ff;text-transform:uppercase}
#maxess-results-10 .v21-naya h1{margin:4px 0 4px;font-size:clamp(22px,3vw,34px);line-height:1;letter-spacing:-.045em}
#maxess-results-10 .v21-naya p{margin:0;color:rgba(255,255,255,.72);font-size:14px;line-height:1.45}
#maxess-results-10 .v21-listen{appearance:none;border:1px solid rgba(208,168,255,.60);border-radius:16px;padding:13px 18px;background:linear-gradient(145deg,#111116,#030305);color:#fff;font-weight:900;letter-spacing:.02em;box-shadow:0 12px 28px rgba(0,0,0,.45),inset 0 1px rgba(255,255,255,.20),0 0 0 1px rgba(150,93,255,.18);cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,filter .2s ease}
#maxess-results-10 .v21-listen:hover{transform:translateY(-2px);filter:brightness(1.08);box-shadow:0 16px 34px rgba(0,0,0,.5),inset 0 1px rgba(255,255,255,.25),0 0 22px rgba(150,93,255,.22)}
#maxess-results-10 .v21-listen:active{transform:translateY(1px);box-shadow:0 6px 16px rgba(0,0,0,.5),inset 0 2px rgba(0,0,0,.25)}
#maxess-results-10 .v21-listen:focus-visible{outline:2px solid #fff;outline-offset:3px}
#maxess-results-10 .v20-score{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center}
#maxess-results-10 .v20-score-label{margin-bottom:8px;color:rgba(255,255,255,.52);font-size:10px;letter-spacing:.20em;font-weight:900}
#maxess-results-10 .v20-score-orb{display:grid;place-items:center}
#maxess-results-10 .v20-score-orb .v13-score-orb{display:grid!important;place-items:center!important}
#maxess-results-10 .v20-score-orb .v13-score-number{position:relative!important;top:auto!important;left:auto!important;transform:none!important;display:block!important;margin:0!important;line-height:.78!important}
#maxess-results-10 .v20-score-orb .v13-score-label,#maxess-results-10 .v20-score-orb .v13-score-band{margin-top:12px!important}
#maxess-results-10 .v21-dimensions{width:min(1100px,100%);margin:18px auto 0;text-align:center}
#maxess-results-10 .v21-dimensions h2{margin:0;font-size:clamp(28px,4vw,52px);letter-spacing:-.05em}
#maxess-results-10 .v21-dimensions .v21-sub{margin:9px auto 18px;max-width:650px;color:rgba(255,255,255,.62);font-size:14px}
#maxess-results-10 .v21-orb-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px;align-items:start}
#maxess-results-10 .v21-dim-orb{appearance:none;border:1px solid rgba(255,255,255,.14);border-radius:22px;padding:12px 8px 14px;background:linear-gradient(145deg,#101016,#06060a);color:#fff;cursor:pointer;box-shadow:0 16px 42px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.10);transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease}
#maxess-results-10 .v21-dim-orb:hover,#maxess-results-10 .v21-dim-orb.is-active{transform:translateY(-4px);border-color:rgba(208,168,255,.55);box-shadow:0 22px 52px rgba(0,0,0,.34),0 0 24px rgba(150,93,255,.14),inset 0 1px rgba(255,255,255,.16)}
#maxess-results-10 .v21-dim-orb:focus-visible{outline:2px solid #fff;outline-offset:3px}
#maxess-results-10 .v21-mini-ring{width:92px;height:92px;margin:0 auto 10px;border-radius:50%;display:grid;place-items:center;background:conic-gradient(#a66cff var(--v21-p),rgba(255,255,255,.08) 0);box-shadow:inset 0 0 0 1px rgba(255,255,255,.18),0 0 22px rgba(150,93,255,.12)}
#maxess-results-10 .v21-mini-ring::before{content:"";grid-area:1/1;width:74px;height:74px;border-radius:50%;background:#08080d;box-shadow:inset 0 0 22px rgba(0,0,0,.8)}
#maxess-results-10 .v21-mini-score{grid-area:1/1;z-index:1;font-size:27px;font-weight:950;letter-spacing:-.06em}
#maxess-results-10 .v21-mini-name{display:block;min-height:32px;font-size:11px;font-weight:850;line-height:1.25;color:rgba(255,255,255,.86)}
#maxess-results-10 .v21-detail{margin:18px auto 0;max-width:820px;padding:18px 20px;border:1px solid rgba(255,255,255,.12);border-radius:20px;background:#050509;color:#fff;box-shadow:inset 0 1px rgba(255,255,255,.08),0 18px 50px rgba(0,0,0,.24)}
#maxess-results-10 .v21-detail strong{font-size:16px}.v21-detail p{margin:6px 0 0;color:rgba(255,255,255,.68);font-size:13px;line-height:1.55}
#maxess-results-10 .v21-report{width:min(920px,100%);margin:36px auto;padding:clamp(28px,5vw,64px);border:1px solid rgba(45,32,61,.16);border-radius:30px;background:linear-gradient(180deg,#fff,#faf8fd);color:#17131b;box-shadow:0 30px 90px rgba(0,0,0,.14);font-family:Georgia,'Times New Roman',serif}
#maxess-results-10 .v21-report-kicker{font-family:Inter,ui-sans-serif,system-ui,sans-serif;font-size:10px;letter-spacing:.20em;font-weight:900;color:#7042aa;text-transform:uppercase}
#maxess-results-10 .v21-report h2{margin:9px 0 4px;font-family:Inter,ui-sans-serif,system-ui,sans-serif;font-size:clamp(32px,5vw,58px);line-height:.95;letter-spacing:-.055em;color:#111}
#maxess-results-10 .v21-report-meta{font-family:Inter,ui-sans-serif,system-ui,sans-serif;color:#6c6570;font-size:12px;margin-bottom:28px}
#maxess-results-10 .v21-report .v21-letter-rule{height:1px;background:linear-gradient(90deg,#7042aa,rgba(112,66,170,0));margin:20px 0 28px}
#maxess-results-10 .v21-report p{font-size:17px;line-height:1.75;margin:0 0 17px}
#maxess-results-10 .v21-report h3{font-family:Inter,ui-sans-serif,system-ui,sans-serif;margin:30px 0 8px;font-size:18px;letter-spacing:.04em;text-transform:uppercase;color:#7042aa}
#maxess-results-10 .v21-report .v21-callout{margin:24px 0;padding:20px 22px;border-left:4px solid #7042aa;background:#f1ebf8;border-radius:0 16px 16px 0;font-family:Inter,ui-sans-serif,system-ui,sans-serif}
#maxess-results-10 .v21-report .v21-stage{display:inline-flex;padding:7px 11px;border-radius:999px;background:#17131b;color:#fff;font-family:Inter,ui-sans-serif,system-ui,sans-serif;font-size:10px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10 .v21-cta-strip{width:min(920px,100%);margin:28px auto 0;padding:26px;border-radius:26px;background:linear-gradient(145deg,#100b18,#050507);border:1px solid rgba(208,168,255,.22);box-shadow:0 24px 70px rgba(0,0,0,.28);text-align:center}
#maxess-results-10 .v21-cta-strip h3{margin:0;font-size:clamp(25px,3vw,40px);letter-spacing:-.04em}.v21-cta-strip p{max-width:650px;margin:10px auto 18px;color:rgba(255,255,255,.68);font-size:14px;line-height:1.55}
#maxess-results-10 .v21-pdf-actions{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin:28px auto 0}.v21-pdf-btn{appearance:none;border:1px solid rgba(255,255,255,.18);border-radius:14px;padding:12px 18px;background:#0a0a0e;color:#fff;font-weight:850;cursor:pointer;box-shadow:inset 0 1px rgba(255,255,255,.10),0 10px 28px rgba(0,0,0,.24)}.v21-pdf-btn.primary{background:linear-gradient(145deg,#111117,#030305);border-color:rgba(208,168,255,.48)}
#maxess-results-10 #maxess-v21-print-report{display:none}
@media(max-width:800px){#maxess-results-10 .v21-naya{grid-template-columns:auto 1fr;}.v21-naya .v21-listen{grid-column:1/-1;width:100%}#maxess-results-10 .v21-orb-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.v21-orb-grid .v21-dim-orb:last-child{grid-column:1/-1;max-width:50%;margin:auto;width:100%}}
@media(max-width:500px){#maxess-results-10 .v21-orb-grid{grid-template-columns:1fr}.v21-orb-grid .v21-dim-orb:last-child{grid-column:auto;max-width:none}.v21-report{padding:25px!important}.v21-report p{font-size:16px!important}}
@media print{
 @page{size:Letter;margin:.55in}
 body{background:#fff!important}
 #maxess-results-10{background:#fff!important;color:#111!important;overflow:visible!important}
 #maxess-results-10>*:not(#maxess-v21-print-report){display:none!important}
 #maxess-v21-print-report{display:block!important;color:#17131b!important;background:#fff!important;font-family:Inter,Arial,sans-serif}
 #maxess-v21-print-report .v21-pdf-page{break-after:page;page-break-after:always;min-height:9.2in;position:relative;padding:0}
 #maxess-v21-print-report .v21-pdf-page:last-child{break-after:auto;page-break-after:auto}
 #maxess-v21-print-report h1,#maxess-v21-print-report h2,#maxess-v21-print-report h3{color:#111!important;margin-top:0}
 #maxess-v21-print-report p{color:#333!important;line-height:1.62;font-size:12pt}
 #maxess-v21-print-report .v21-pdf-hero{text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center}
 #maxess-v21-print-report .v21-pdf-score{width:250px;height:250px;border-radius:50%;display:grid;place-items:center;border:2px solid #222;background:#f4f1f7;margin:24px auto}
 #maxess-v21-print-report .v21-pdf-score strong{font-size:88px;line-height:.8;color:#111}
 #maxess-v21-print-report .v21-pdf-stage{font-size:11px;font-weight:900;letter-spacing:.16em;text-transform:uppercase}
 #maxess-v21-print-report .v21-pdf-dims{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:30px}
 #maxess-v21-print-report .v21-pdf-dim{padding:12px 6px;text-align:center;border:1px solid #bbb;border-radius:16px;break-inside:avoid}
 #maxess-v21-print-report .v21-pdf-dim strong{display:block;font-size:28px}.v21-pdf-dim span{font-size:9px;color:#555;display:block;margin-top:6px}
 #maxess-v21-print-report .v21-pdf-letter{padding:28px 30px;border:1px solid #bbb;border-radius:18px;break-inside:avoid}
 #maxess-v21-print-report .v21-pdf-letter p{font-family:Georgia,'Times New Roman',serif;font-size:13pt;line-height:1.7}
 #maxess-v21-print-report .v21-pdf-card{border:1px solid #bbb;border-radius:18px;padding:22px;break-inside:avoid;margin-top:20px}
 #maxess-v21-print-report .v21-pdf-footer{position:absolute;bottom:0;left:0;right:0;text-align:center;font-size:8pt;color:#777;border-top:1px solid #ddd;padding-top:8px}
}
`;
    document.head.appendChild(s);
  }

  function getNayaImage(){
    var img=root.querySelector('.v20-avatar,.v18-naya-avatar,img[src*="Naya"]');
    return img&&img.src?img.src:'https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg';
  }

  function buildNaya(){
    var old=root.querySelector('.v20-naya');
    if(old) old.remove();
    var stage=root.querySelector('.v20-stage')||root.querySelector('[data-v20-stage]')||root;
    var n=document.createElement('section');n.className='v21-naya';n.setAttribute('aria-label','Naya introduction');
    n.innerHTML='<img src="'+esc(getNayaImage())+'" alt="Naya, your AI guide"><div><div class="v21-naya-kicker">NAYA · YOUR AI GUIDE</div><h1>Hi. I’ve looked at your results.</h1><p>This isn’t your judgment. <strong>It’s your map.</strong></p></div><button type="button" class="v21-listen">LISTEN TO NAYA <span aria-hidden="true">▶</span></button>';
    var oldListen=root.querySelector('#mx-naya-listen,#v11-naya-listen,#v13-listen,.mx-naya-listen');
    n.querySelector('.v21-listen').addEventListener('click',function(){
      if(oldListen&&oldListen!==this){oldListen.click();return;}
      root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true,detail:{result:R(),narrative:buildNarrative()}}));
      try{if(window.speechSynthesis){window.speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(buildNarrative());u.rate=.96;u.pitch=1;window.speechSynthesis.speak(u);}}catch(e){}
    });
    stage.insertBefore(n,stage.firstChild);
  }

  function buildNarrative(){
    var who=name?name+', ':' ';
    var s=band(score),top=strongest?strongest.name:'your strongest dimension',low=weakest?weakest.name:'your next lever';
    var intro='Your MAXESS score is '+Math.round(score)+', placing you in the '+s+' stage of AI mastery. ';
    var pattern='Your profile shows a current average of '+Math.round(avg)+', with '+top+' standing out as your strongest visible capability and '+low+' representing your clearest improvement opportunity. ';
    var strength=strongest?'Your strongest capability is '+strongest.name+' at '+Math.round(strongest.score)+'. That is something to compound, not overlook. ':'';
    var lever=weakest?'Your biggest lever is '+weakest.name+' at '+Math.round(weakest.score)+'. Improving this area can raise the quality of the system around it rather than simply adding another isolated skill. ':'';
    return 'Hi'+who+'I have looked at your results. '+intro+pattern+strength+lever+'Your next step is not to become perfect. It is to become more deliberate: direct the work, evaluate what comes back, improve it, and repeat. That is how good AI results become exceptional results. Your AI Mastery Key is the next step if you want to keep advancing.';
  }

  function buildMiniOrbs(){
    var old=root.querySelector('.v21-dimensions');if(old)old.remove();
    var stage=root.querySelector('.v20-stage')||root;
    var sec=document.createElement('section');sec.className='v21-dimensions';sec.setAttribute('aria-label','Your five AI dimensions');
    sec.innerHTML='<h2>Your Five Dimensions</h2><p class="v21-sub">One MAXESS score. Five capabilities. Select a dimension to see what it means.</p><div class="v21-orb-grid"></div><div class="v21-detail" aria-live="polite"><strong>Select a dimension.</strong><p>Explore how each part of your AI capability contributes to your overall score.</p></div>';
    var grid=sec.querySelector('.v21-orb-grid'),detail=sec.querySelector('.v21-detail');
    dims.forEach(function(d,i){
      var b=document.createElement('button');b.type='button';b.className='v21-dim-orb';
      var v=Math.round(d.score),nameText=String(d.name);
      b.innerHTML='<span class="v21-mini-ring" style="--v21-p:'+v+'%"><span class="v21-mini-score">'+v+'</span></span><span class="v21-mini-name">'+esc(nameText)+'</span>';
      b.setAttribute('aria-label',nameText+', '+v+' out of 100');
      b.addEventListener('click',function(){
        grid.querySelectorAll('.v21-dim-orb').forEach(function(x){x.classList.remove('is-active');});b.classList.add('is-active');
        var quality=d.score>=85?'a strength you can compound':d.score>=70?'a capable area ready to sharpen':'a high-value area for focused improvement';
        detail.innerHTML='<strong>'+esc(nameText)+' · '+v+'</strong><p>This dimension is '+quality+'. Use the score as a signal, not a judgment, and focus your next improvement cycle here when it supports your larger goal.</p>';
      });
      grid.appendChild(b);
    });
    stage.appendChild(sec);
  }

  function buildReport(){
    var old=root.querySelector('.v21-report');if(old)old.remove();
    var stage=root.querySelector('.v20-stage')||root;
    var sec=document.createElement('section');sec.className='v21-report';sec.setAttribute('aria-label','Your personalized MAXESS report');
    var top=strongest||{name:'Your strongest dimension',score:score},low=weakest||{name:'Your next lever',score:score};
    sec.innerHTML='<div class="v21-report-kicker">YOUR PERSONALIZED REPORT</div><h2>'+esc(name?name+', here is your report.':'Here is your personalized report.')+'</h2><div class="v21-report-meta">MAXESS AI Mastery Assessment · '+Math.round(score)+' / 100 · '+esc(band(score))+'</div><div class="v21-letter-rule"></div><span class="v21-stage">'+esc(band(score))+'</span><h3>What your result means</h3><p>Your MAXESS score of <strong>'+Math.round(score)+'</strong> places you in the <strong>'+esc(band(score))+'</strong> stage. This means your relationship with AI is moving beyond simple experimentation toward a more deliberate ability to direct, evaluate, improve, and apply AI capability.</p><h3>Your pattern</h3><p>Your five dimensions tell a more useful story than the overall score alone. Your current profile averages <strong>'+Math.round(avg)+'</strong>. The pattern shows where your capability is already strong and where improving one specific area could create a larger return across the whole system.</p><h3>Your strength</h3><p><strong>'+esc(top.name)+' — '+Math.round(top.score)+'</strong> is your strongest visible capability. This is something to protect and compound. Use what you already do well as the foundation for more advanced AI work.</p><h3>Your lever</h3><p><strong>'+esc(low.name)+' — '+Math.round(low.score)+'</strong> is your clearest improvement opportunity. This is not a judgment. It is a lever: a focused place where deliberate practice may improve the quality of the work around it.</p><div class="v21-callout"><strong>Protect your strength. Build your lever.</strong><br>Direct the work. Evaluate the result. Improve it. Repeat.</div><h3>Your next move</h3><p>Choose one real AI workflow that matters to you. Define what exceptional looks like before you start. Create the result, score it honestly, identify what is missing, improve it, and repeat until the quality is worthy of your standard.</p><h3>Your invitation</h3><p>MAXESS is built for people who do not want mediocre results from AI. If you want exceptional results and are willing to develop the thinking and evaluation skills required to produce them, keep advancing. Your <strong>AI Mastery Key</strong> is the next step in turning this assessment into capability.</p>';
    stage.appendChild(sec);
  }

  function personalizeMasters(){
    var cards=root.querySelectorAll('.v13-master,.v20-master,.mx-area');
    cards.forEach(function(card){
      if(card.querySelector('.v21-fit'))return;
      var text=(card.textContent||'').toLowerCase();var rel=35;
      if(weakest&&text.indexOf(String(weakest.name).toLowerCase())>=0)rel=96;
      else if(text.indexOf('evaluation')>=0&&weakest&&String(weakest.name).toLowerCase().indexOf('evaluation')>=0)rel=96;
      else if(text.indexOf('systems')>=0&&weakest&&String(weakest.name).toLowerCase().indexOf('system')>=0)rel=96;
      else if(strongest&&text.indexOf(String(strongest.name).toLowerCase())>=0)rel=84;
      if(rel<80)return;
      var el=document.createElement('div');el.className='v21-fit';el.style.cssText='margin-top:10px;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:#cdb4ff;font-weight:900';el.textContent=rel>=90?'RECOMMENDED FOCUS':'STRONG FOUNDATION';card.appendChild(el);
    });
  }

  function buildCta(){
    var old=root.querySelector('.v21-cta-strip');if(old)old.remove();
    var stage=root.querySelector('.v20-stage')||root;
    var sec=document.createElement('section');sec.className='v21-cta-strip';sec.innerHTML='<h3>Ready to go beyond good enough?</h3><p>MAXESS shows you where you are. Your AI Mastery Key shows you how to keep improving.</p><div class="v21-pdf-actions"><button type="button" class="v21-pdf-btn primary" id="v21-print-pdf">Print / Save as PDF</button></div>';
    sec.querySelector('#v21-print-pdf').addEventListener('click',function(){window.print();});
    stage.appendChild(sec);
  }

  function buildPrintReport(){
    var old=document.getElementById('maxess-v21-print-report');if(old)old.remove();
    var top=strongest||{name:'Your strongest dimension',score:score},low=weakest||{name:'Your next lever',score:score};
    var wrap=document.createElement('div');wrap.id='maxess-v21-print-report';
    var dimsHtml=dims.map(function(d){return '<div class="v21-pdf-dim"><strong>'+Math.round(d.score)+'</strong><span>'+esc(d.name)+'</span></div>';}).join('');
    wrap.innerHTML='<div class="v21-pdf-page v21-pdf-hero"><div><div style="font-size:11px;letter-spacing:.22em;font-weight:900">MAXESS</div><h1 style="font-size:42pt;margin:12px 0 0">Your AI Mastery Results</h1><div class="v21-pdf-score"><strong>'+Math.round(score)+'</strong></div><div class="v21-pdf-stage">'+esc(band(score))+'</div><p style="max-width:6.2in;margin:22px auto 0">'+esc(name?name+', ':'')+'Your score is a map of your current AI capability — not a judgment. It shows where you are and where your next gains can come from.</p></div><div class="v21-pdf-footer">MAXESS · Your AI Mastery Results</div></div><div class="v21-pdf-page"><h2>Your Five Dimensions</h2><p>These five capabilities combine to create your overall MAXESS score.</p><div class="v21-pdf-dims">'+dimsHtml+'</div><div class="v21-pdf-card"><h3>Strongest signal</h3><p><strong>'+esc(top.name)+' — '+Math.round(top.score)+'</strong></p><p>This is the capability to protect and compound.</p></div><div class="v21-pdf-card"><h3>Biggest lever</h3><p><strong>'+esc(low.name)+' — '+Math.round(low.score)+'</strong></p><p>This is the focused opportunity most worth exploring next.</p></div><div class="v21-pdf-footer">MAXESS · Five Dimensions</div></div><div class="v21-pdf-page"><h2>Your Personalized Report</h2><div class="v21-pdf-letter"><p>Dear '+esc(name||'MAXESS member')+',</p><p>You achieved a MAXESS score of <strong>'+Math.round(score)+'</strong>, placing you in the <strong>'+esc(band(score))+'</strong> stage of AI mastery.</p><p>Your profile is not simply a collection of scores. It is a pattern. Your strongest visible capability is <strong>'+esc(top.name)+'</strong> at '+Math.round(top.score)+', while <strong>'+esc(low.name)+'</strong> at '+Math.round(low.score)+' represents your clearest improvement lever.</p><p>This means your next level does not require you to improve everything at once. Protect what is already working. Choose the highest-value lever. Practice deliberately. Evaluate honestly. Improve the result. Repeat.</p><p>Exceptional AI results are not accidental. They are built through better thinking, better direction, better evaluation, and continuous improvement.</p><p>That is the path from data to insight, from insight to action, and from action to capability.</p></div><div class="v21-pdf-footer">MAXESS · Personalized Report</div></div><div class="v21-pdf-page"><h2>Your Next Move</h2><div class="v21-pdf-card"><h3>1 · Protect your strength</h3><p>Use '+esc(top.name)+' as a foundation for more advanced AI work.</p></div><div class="v21-pdf-card"><h3>2 · Build your lever</h3><p>Focus deliberate improvement on '+esc(low.name)+'.</p></div><div class="v21-pdf-card"><h3>3 · Create, score, improve, repeat</h3><p>Take one real workflow and raise its quality through deliberate iteration.</p></div><div class="v21-pdf-card"><h3>Your AI Mastery Key</h3><p>If you want exceptional results rather than mediocre ones, continue the journey. MAXESS gives you the map; the AI Mastery Key gives you the operating system for improving.</p></div><div class="v21-pdf-footer">MAXESS · Keep Advancing</div></div>';
    root.appendChild(wrap);
  }

  function centerScore(){
    var orb=root.querySelector('.v20-score-orb .v13-score-orb,.v20-score-orb');
    var num=root.querySelector('.v20-score-orb .v13-score-number');
    if(num){num.textContent=String(Math.round(score));num.setAttribute('aria-label','Your AI Score is '+Math.round(score));}
    if(orb){orb.setAttribute('role','img');orb.setAttribute('aria-label','Your AI Score is '+Math.round(score)+' out of 100');}
    root.querySelectorAll('.v20-score-label').forEach(function(x){x.textContent='YOUR AI SCORE';});
  }

  function run(){
    addStyle();
    buildNaya();
    centerScore();
    buildMiniOrbs();
    buildReport();
    personalizeMasters();
    buildCta();
    buildPrintReport();
    root.setAttribute('data-results-version','21');
    root.setAttribute('data-v21-status','complete-finish-pass');
    root.setAttribute('data-v21-score',String(Math.round(score)));
    console.log('%cMAXESS RESULTS V21 FINISH PASS COMPLETE','color:#cdb4ff;font-weight:900;font-size:16px');
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run,{once:true});else run();
})();
