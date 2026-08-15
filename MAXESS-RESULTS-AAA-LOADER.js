/*
 MAXESS 9.5 — PRODUCTION RESULTS BRIDGE
 Purpose: read the real completed assessment boundary, persist the result,
 and hand the user to the complete Results experience. The Results page
 owns the entire journey above the original NayaNET destination.
*/
(function(){
  'use strict';
  const RESULT_KEY='MAXESS_RESULT_V1';
  const RESULTS_URL='https://cdn.jsdelivr.net/gh/SoulSchoolAcademy/maxess@maxess-9-5-production-results/MAXESS-RESULTS-9-5-PRODUCTION.html';
  let launched=false;

  const clamp=v=>Math.max(0,Math.min(100,Math.round(Number(v)||0)));
  const text=el=>el?el.textContent.trim():'';
  const numberFrom=el=>{const n=parseFloat(text(el).replace(/[^0-9.\-]/g,''));return Number.isFinite(n)?clamp(n):0};

  function readJSON(key){
    for(const store of [sessionStorage,localStorage]){
      try{const raw=store.getItem(key);if(raw)return JSON.parse(raw)}catch(e){}
    }
    return null;
  }

  function extract(){
    if(window.MAXESS_RESULT && typeof window.MAXESS_RESULT==='object')return window.MAXESS_RESULT;
    for(const key of ['MAXESS_RESULT_V1','MAXESS_RESULT','MAXESS_RESULTS','maxessResult','assessmentResult']){
      const r=readJSON(key);if(r)return r;
    }

    const root=document.querySelector('[data-maxess-result],.maxess-results,.results-screen,.result-screen,[data-results]')||document.body;
    const scoreEl=root.querySelector('[data-overall-score],.overall-score,.max-score,.score-value,.score,[class*="overall"]');
    const dims={};
    const rows=root.querySelectorAll('[data-dimension],.dimension-row,.dimension,.dimension-card');
    rows.forEach(row=>{
      const name=(row.getAttribute('data-dimension')||row.querySelector('.dimension-name,.dimension-title,h3,h4,strong')?.textContent||'').trim();
      const value=row.querySelector('[data-score],.dimension-score,.score,.value');
      if(name&&value)dims[name]=numberFrom(value);
    });
    const score=scoreEl?numberFrom(scoreEl):0;
    if(score||Object.keys(dims).length)return {overall:score,dimensions:dims};
    return null;
  }

  function persist(result){
    try{sessionStorage.setItem(RESULT_KEY,JSON.stringify(result));localStorage.setItem(RESULT_KEY,JSON.stringify(result))}catch(e){}
    window.MAXESS_RESULT=result;
  }

  function launch(result){
    if(launched)return;
    if(!result)return;
    launched=true;
    persist(result);
    const url=new URL(RESULTS_URL);
    url.searchParams.set('score',String(clamp(result.overall??result.score??0)));
    window.location.assign(url.toString());
  }

  /* Explicit API: the assessment can call this immediately when it knows it
     has completed. This is the preferred integration path. */
  window.MAXESS_OPEN_RESULTS=function(result){launch(result||extract())};

  /* Compatibility path for existing assessment builds: watch for the real
     result boundary without inventing a result before completion. */
  function check(){const r=extract();if(r&&((r.overall||0)>0||Object.keys(r.dimensions||{}).length))launch(r)}
  check();
  const observer=new MutationObserver(()=>check());
  observer.observe(document.documentElement,{subtree:true,childList:true,characterData:true});
  let ticks=0;const timer=setInterval(()=>{check();if(++ticks>360){clearInterval(timer);observer.disconnect()}},500);
})();
