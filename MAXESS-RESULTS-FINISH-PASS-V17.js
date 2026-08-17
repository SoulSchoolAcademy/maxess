/*
 MAXESS RESULTS — V17 FINISH PASS
 Preservation-first repair for the existing Groove Results artifact.
 IMPORTANT: This is a patch for the existing MAXESS-RESULTS-10-GROOVE.html.
 It does NOT replace the page, orb, narrative, media, or scoring engine.
 */
(function(){
  'use strict';
  function boot(){
    const root=document.getElementById('maxess-results-10');
    if(!root || root.dataset.v17FinishPass==='1') return;
    root.dataset.v17FinishPass='1';

    /* Remove the competing generated V13 presentation shell.
       The original Groove experience underneath it is preserved. */
    root.querySelectorAll('.v13-shell').forEach(el=>el.remove());

    /* Remove duplicate Naya introductions created by previous presentation passes.
       Keep the existing V11 Naya treatment because it contains the approved avatar/audio hook. */
    root.querySelectorAll('#v12-naya,.v13-naya,.mx-recognition-naya').forEach(el=>el.remove());
    const naya=root.querySelector('.v11-naya-welcome');
    if(naya){
      const title=naya.querySelector('.v11-naya-title');
      const copy=naya.querySelector('.v11-naya-copy');
      const kicker=naya.querySelector('.v11-naya-kicker');
      if(kicker) kicker.textContent='NAYA · YOUR AI GUIDE';
      if(title) title.textContent="Hi. I've looked at your results.";
      if(copy) copy.innerHTML="This isn't your judgment.<br>It's your map.";
      const button=naya.querySelector('button');
      if(button){
        button.innerHTML='Listen to Naya <span aria-hidden="true">▶</span>';
        button.setAttribute('aria-label','Listen to Naya interpret your results');
      }
    }

    const hero=root.querySelector('.mx-hero');
    const grid=hero&&hero.querySelector('.mx-hero-grid');
    const orb=hero&&hero.querySelector('.mx-score-orb');
    if(!hero||!grid||!orb)return;

    /* The existing orb remains the hero. Put the real score back inside it. */
    const result=window.MAXESS_RESULT||{};
    const raw=Number(result.overallScore ?? result.score ?? result.masterScore);
    if(Number.isFinite(raw)){
      const score=orb.querySelector('.mx-score strong');
      const label=orb.querySelector('.mx-score span');
      if(score)score.textContent=String(Math.round(Math.max(0,Math.min(100,raw))));
      if(label)label.textContent='AI SCORE';
      orb.setAttribute('role','img');
      orb.setAttribute('aria-label','Your AI Score is '+Math.round(raw)+' out of 100');
    }

    /* Remove the old competing text stack from the hero, without touching the orb. */
    const oldHeroCopy=grid.querySelector(':scope > div:first-child');
    if(oldHeroCopy && oldHeroCopy!==orb) oldHeroCopy.remove();
    hero.querySelectorAll('.mx-hero-actions,.v12-print,.v15-print,.v13-hero-tools').forEach(el=>el.remove());

    /* Move the best existing Naya card to the top of the hero. */
    if(naya){
      naya.remove();
      grid.insertBefore(naya,orb);
    }

    /* Remove duplicate Listen controls, preserving the first Naya control. */
    const listenButtons=[...root.querySelectorAll('button,a')].filter(el=>/listen\s+to\s+naya|listen\s+to\s+your\s+results|naya\s+—\s+listen/i.test((el.textContent||'').replace(/\s+/g,' ').trim()));
    const keeper=naya&&naya.querySelector('button');
    listenButtons.forEach(el=>{ if(el!==keeper && !el.closest('.v11-naya-welcome')) el.remove(); });

    /* Build exactly five mini-orbs from the authoritative five dimensions.
       These are subordinate to the existing hero orb. */
    let mini=root.querySelector('#v17-five-dim-orbs');
    const dims=Array.isArray(result.dimensions)?result.dimensions.slice(0,5):[];
    if(dims.length===5){
      if(!mini){
        mini=document.createElement('div');
        mini.id='v17-five-dim-orbs';
        mini.setAttribute('aria-label','Your five AI capability dimensions');
        orb.insertAdjacentElement('afterend',mini);
      }
      mini.innerHTML=dims.map((d,i)=>{
        const value=Number(d.score??d.value??0);
        const safe=Number.isFinite(value)?Math.max(0,Math.min(100,value)):0;
        const name=String(d.name||d.label||('Dimension '+(i+1))).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
        return '<button class="v17-mini-orb" type="button" aria-label="'+name+', '+Math.round(safe)+' out of 100"><span class="v17-mini-ring" style="--v17-score:'+safe+'%"><b>'+Math.round(safe)+'</b></span><span class="v17-mini-name">'+name+'</span></button>';
      }).join('');
      mini.querySelectorAll('.v17-mini-orb').forEach((el,i)=>{
        el.addEventListener('click',()=>{
          const dimsSection=root.querySelector('#v11-fingerprint,#v12-dimensions,#v11-dimensions') || [...root.querySelectorAll('section')].find(s=>/five dimensions/i.test(s.textContent||''));
          dimsSection?.scrollIntoView({behavior:'smooth',block:'start'});
        });
      });
    }

    /* Put the existing narrative sections into the intended order without rebuilding them. */
    const findSection=(selectors,terms)=>{
      for(const sel of selectors){const el=root.querySelector(sel);if(el)return el;}
      return [...root.querySelectorAll('section')].find(s=>terms.some(t=>(s.textContent||'').toLowerCase().includes(t)));
    };
    const sections=[
      root.querySelector('.mx-hero'),
      findSection(['#v11-naya-report','#v12-report'],['listen to your results','your report']),
      findSection(['#v11-fingerprint','#v12-pattern'],['see the pattern','your fingerprint']),
      findSection(['#v11-dimensions','#v12-dimensions'],['five dimensions']),
      findSection(['#v11-strengths','#v12-strengths'],['your strengths','your superpowers']),
      findSection(['#v11-lever','#v12-lever'],['your biggest lever','highest-leverage opportunity']),
      findSection(['#v11-next','#v12-next'],['your next move','your next chapter']),
      findSection(['#v11-masters','#v12-masters'],['18 naya masters','18 ai pathways','your naya masters']),
      root.querySelector('#naya-playground'),
      root.querySelector('#v13-video'),
      root.querySelector('#v13-final')
    ].filter(Boolean);
    const unique=[];sections.forEach(s=>{if(!unique.includes(s))unique.push(s)});
    unique.forEach(s=>root.appendChild(s));

    /* Preservation-first CSS. */
    if(!document.getElementById('v17-finish-pass-style')){
      const style=document.createElement('style');
      style.id='v17-finish-pass-style';
      style.textContent=`
#maxess-results-10 .mx-hero{padding-top:clamp(42px,5vw,76px)!important;padding-bottom:clamp(46px,5vw,78px)!important}
#maxess-results-10 .mx-hero-grid{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:22px!important;width:min(1100px,100%)!important;text-align:center!important}
#maxess-results-10 .v11-naya-welcome{order:1!important;width:min(820px,100%)!important;margin:0 auto 2px!important;display:grid!important;grid-template-columns:auto minmax(0,1fr) auto!important;align-items:center!important;gap:18px!important;padding:14px 18px!important;border:1px solid rgba(255,255,255,.14)!important;border-radius:24px!important;background:linear-gradient(135deg,rgba(166,108,255,.10),rgba(255,255,255,.035))!important;box-shadow:0 18px 55px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.08)!important;text-align:left!important}
#maxess-results-10 .v11-naya-welcome .v11-naya-title{margin:2px 0 5px!important;font-size:clamp(20px,2.8vw,30px)!important;line-height:1.05!important}
#maxess-results-10 .v11-naya-welcome .v11-naya-copy{margin:0!important;font-size:15px!important;color:rgba(255,255,255,.72)!important}
#maxess-results-10 .v11-naya-welcome .v11-naya-avatar{width:58px!important;height:58px!important;border-radius:50%!important;object-fit:cover!important}
#maxess-results-10 .mx-score-orb{order:2!important;width:min(570px,74vw)!important;min-width:300px!important}
#maxess-results-10 #v17-five-dim-orbs{order:3!important;display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:12px!important;width:min(930px,100%)!important;margin:4px auto 0!important}
#maxess-results-10 .v17-mini-orb{appearance:none!important;border:0!important;padding:10px 5px!important;background:transparent!important;color:#fff!important;cursor:pointer!important;text-align:center!important;border-radius:18px!important;transition:transform .2s ease,background .2s ease!important}
#maxess-results-10 .v17-mini-orb:hover,#maxess-results-10 .v17-mini-orb:focus-visible{transform:translateY(-3px)!important;background:rgba(255,255,255,.045)!important}
#maxess-results-10 .v17-mini-ring{display:grid!important;place-items:center!important;width:68px!important;height:68px!important;margin:0 auto 8px!important;border-radius:50%!important;background:conic-gradient(#9b61ff var(--v17-score),rgba(255,255,255,.09) 0)!important;position:relative!important;box-shadow:0 0 22px rgba(139,92,255,.16)!important}
#maxess-results-10 .v17-mini-ring:after{content:""!important;position:absolute!important;inset:6px!important;border-radius:50%!important;background:#0b0710!important;box-shadow:inset 0 0 15px rgba(139,92,255,.15)!important}
#maxess-results-10 .v17-mini-ring b{position:relative!important;z-index:1!important;font-size:15px!important}
#maxess-results-10 .v17-mini-name{display:block!important;font-size:10px!important;line-height:1.2!important;color:rgba(255,255,255,.66)!important;max-width:130px!important;margin:auto!important}
@media(max-width:760px){#maxess-results-10 .v11-naya-welcome{grid-template-columns:auto 1fr!important}.v11-naya-welcome button{grid-column:1/-1;width:100%!important}#maxess-results-10 #v17-five-dim-orbs{grid-template-columns:repeat(3,1fr)!important}.v17-mini-orb:nth-child(4){grid-column:2}.v17-mini-orb:nth-child(5){grid-column:3}}
@media(max-width:480px){#maxess-results-10 #v17-five-dim-orbs{grid-template-columns:repeat(2,1fr)!important}.v17-mini-orb:nth-child(4),.v17-mini-orb:nth-child(5){grid-column:auto}}
`;
      document.head.appendChild(style);
    }
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(boot,250),{once:true});else setTimeout(boot,250);
})();
