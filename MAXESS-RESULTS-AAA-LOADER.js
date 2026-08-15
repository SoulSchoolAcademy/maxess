/* =====================================================================
   MAXESS RESULTS AAA — LIVE GROOVE BRIDGE
   Load this script AFTER the existing MAXESS assessment code.

   It deliberately does NOT duplicate scoring.
   It reads the already-rendered MAXESS result at the assessment boundary,
   loads the full flagship Results artifact, and mounts the real values.
   ===================================================================== */
(function(){
  'use strict';

  const SOURCE='https://cdn.jsdelivr.net/gh/SoulSchoolAcademy/maxess@main/MAXESS-RESULTS-AAA-FULL.html';

  function text(selector){
    const el=document.querySelector(selector);
    return el?el.textContent.trim():'';
  }

  function number(selector){
    const n=parseFloat(text(selector).replace(/[^0-9.\-]/g,''));
    return Number.isFinite(n)?n:0;
  }

  function readCurrentResult(){
    const overall=number('#overallScore');
    const rows=[...document.querySelectorAll('#dimensionConstellation .dimension-orb')];
    const dimensions=rows.map((row,i)=>({
      id:`dimension-${i+1}`,
      name:(row.querySelector('.dimension-name')||{}).textContent?.trim()||`Dimension ${i+1}`,
      score:parseFloat((row.querySelector('.dimension-score')||{}).textContent||'0')||0,
      color:getComputedStyle(row).getPropertyValue('--dimensionColor').trim()||['#ffd45a','#43dfa0','#5ca8ff','#a95cff','#ef62d2'][i]
    }));

    const profile=text('#resultLevelText')||text('#resultLevel');
    const subtitle=text('#resultSubtitle');
    const strongestName=text('#strongestName');
    const strongestScore=number('#strongestScore');
    const opportunityName=text('#opportunityName');
    const opportunityScore=number('#opportunityScore');

    return {
      overallScore:overall,
      profile:{name:profile,description:subtitle},
      dimensions,
      strengths:strongestName?[{name:strongestName,score:strongestScore,description:text('#strongestText')}]:[],
      opportunities:opportunityName?[{name:opportunityName,score:opportunityScore,description:text('#opportunityText')}]:[],
      personalizedAnalysis:text('#analysisCloud'),
      insight:{text:text('#analysisCloud')},
      metadata:{source:'MAXESS assessment result boundary',capturedAt:new Date().toISOString()}
    };
  }

  async function load(){
    const realResult=readCurrentResult();

    const response=await fetch(SOURCE,{cache:'no-store'});
    if(!response.ok) throw new Error(`MAXESS Results source failed: ${response.status}`);

    const html=await response.text();
    const doc=new DOMParser().parseFromString(html,'text/html');

    document.title='MAXESS — Your AI Mastery Results';
    document.head.innerHTML=doc.head.innerHTML;
    document.body.innerHTML=doc.body.innerHTML;

    /* Re-execute the full Results application script because scripts inserted
       through innerHTML are intentionally inert in browsers. */
    doc.body.querySelectorAll('script').forEach(oldScript=>{
      const script=document.createElement('script');
      if(oldScript.src) script.src=oldScript.src;
      else script.textContent=oldScript.textContent;
      document.body.appendChild(script);
    });

    /* The flagship page exposes a clean mount API. Give it the actual
       assessment result captured BEFORE the old Results DOM disappeared. */
    let tries=0;
    const mount=()=>{
      tries++;
      if(window.MAXESS_RESULTS && typeof window.MAXESS_RESULTS.mount==='function'){
        window.MAXESS_RESULTS.mount(realResult);
        return;
      }
      if(tries<50) setTimeout(mount,50);
      else console.error('MAXESS Results mount API was not found.');
    };
    mount();
  }

  load().catch(error=>{
    console.error('MAXESS AAA Results bridge failed:',error);
    const box=document.createElement('div');
    box.style.cssText='min-height:70vh;display:grid;place-items:center;background:#030305;color:#fff;font-family:Inter,system-ui,sans-serif;padding:40px;text-align:center';
    box.innerHTML='<div style="max-width:620px"><div style="font-size:11px;letter-spacing:.18em;color:#d4adff;font-weight:900">MAXESS RESULTS</div><h1 style="font-size:42px;margin:12px 0">Your result is ready, but the presentation could not be loaded.</h1><p style="color:#aaa;line-height:1.6">Please refresh once. Your assessment data has not been changed.</p></div>';
    document.body.replaceChildren(box);
  });
})();
