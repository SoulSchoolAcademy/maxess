/* =====================================================================
   MAXESS RESULTS — LIVE GROOVE BRIDGE · AAA RELEASE
   Source of truth: completed MAXESS assessment result boundary.
   The Results experience is built BEFORE the existing NayaNET endpoint.
   The NayaNET video/buttons/membership remain the final destination.
   ===================================================================== */
(function(){
  'use strict';

  const SOURCE='https://cdn.jsdelivr.net/gh/SoulSchoolAcademy/maxess@main/MAXESS-RESULTS-NAYANET-FINAL.html';
  const ENHANCER='https://cdn.jsdelivr.net/gh/SoulSchoolAcademy/maxess@main/MAXESS-RESULTS-AAA-ENHANCER.js';
  const RESULT_KEY='MAXESS_RESULT_V1';
  let launched=false;

  function text(selector){
    const el=document.querySelector(selector);
    return el?el.textContent.trim():'';
  }

  function number(selector){
    const raw=text(selector).replace(/[^0-9.\-]/g,'');
    const n=parseFloat(raw);
    return Number.isFinite(n)?n:0;
  }

  function dimensionScore(row){
    const score=row.querySelector('.dimension-score');
    const raw=(score?.textContent||'').replace(/[^0-9.\-]/g,'');
    const n=parseFloat(raw);
    return Number.isFinite(n)?Math.max(0,Math.min(100,n)):0;
  }

  function readCurrentResult(){
    const rows=[...document.querySelectorAll('#dimensionConstellation .dimension-orb')];
    const dimensions=rows.map((row,i)=>({
      id:row.dataset.dimension||`dimension-${i+1}`,
      name:(row.querySelector('.dimension-name')||{}).textContent?.trim()||`Dimension ${i+1}`,
      score:dimensionScore(row),
      description:(row.querySelector('.dimension-description')||{}).textContent?.trim()||'',
      color:getComputedStyle(row).getPropertyValue('--dimensionColor').trim()
    }));

    const result={
      version:'1.0',
      overallScore:number('#overallScore'),
      profile:{
        name:text('#resultLevelText')||text('#resultLevel')||'Your AI Capability Profile',
        description:text('#resultSubtitle')
      },
      dimensions,
      strengths:text('#strongestName')?[{name:text('#strongestName'),score:number('#strongestScore'),description:text('#strongestText')}]:[],
      opportunities:text('#opportunityName')?[{name:text('#opportunityName'),score:number('#opportunityScore'),description:text('#opportunityText')}]:[],
      personalizedAnalysis:text('#analysisCloud'),
      insight:{text:text('#analysisCloud')},
      metadata:{source:'MAXESS assessment result boundary',capturedAt:new Date().toISOString()}
    };

    return result;
  }

  function persist(result){
    try{sessionStorage.setItem(RESULT_KEY,JSON.stringify(result));}catch(e){console.warn('[MAXESS] sessionStorage unavailable',e);}
    window.MAXESS_RESULT=result;
  }

  function injectScript(src){
    return new Promise((resolve,reject)=>{
      const script=document.createElement('script');
      script.src=src;script.async=false;
      script.onload=resolve;script.onerror=()=>reject(new Error(`Enhancer failed: ${src}`));
      document.body.appendChild(script);
    });
  }

  async function load(){
    if(launched)return;
    launched=true;
    const realResult=readCurrentResult();
    persist(realResult);

    let html='';
    try{
      const response=await fetch(SOURCE,{cache:'no-store',credentials:'omit'});
      if(!response.ok)throw new Error(`MAXESS Results source failed: ${response.status}`);
      html=await response.text();
    }catch(error){
      reportError(error,realResult);
      return;
    }

    const doc=new DOMParser().parseFromString(html,'text/html');
    if(!doc.body||!doc.body.children.length){reportError(new Error('Results document was empty'),realResult);return;}

    document.title='MAXESS — Your AI Mastery Results';
    document.head.innerHTML=doc.head.innerHTML;
    document.body.innerHTML=doc.body.innerHTML;

    // Restore the structured result before any Results code runs.
    window.MAXESS_RESULT=realResult;
    try{sessionStorage.setItem(RESULT_KEY,JSON.stringify(realResult));}catch(e){}

    const scripts=[...doc.body.querySelectorAll('script')];
    for(const oldScript of scripts){
      const script=document.createElement('script');
      if(oldScript.src)script.src=oldScript.src;
      else script.textContent=oldScript.textContent;
      document.body.appendChild(script);
    }

    // Enhancement is intentionally loaded after the base Results page so it
    // can improve the experience without replacing the working NayaNET endpoint.
    try{await injectScript(ENHANCER);}catch(error){console.error('[MAXESS AAA] enhancer load failed',error);}
  }

  function ready(){
    const results=document.getElementById('resultsView');
    if(!results)return false;
    return results.classList.contains('visible')&&number('#overallScore')>0&&document.querySelectorAll('#dimensionConstellation .dimension-orb').length>=5;
  }

  function watch(){
    if(ready()){load();return;}
    const observer=new MutationObserver(()=>{
      if(ready()){
        observer.disconnect();
        load();
      }
    });
    observer.observe(document.body,{subtree:true,childList:true,attributes:true,attributeFilter:['class','style']});
    setTimeout(()=>observer.disconnect(),30*60*1000);
  }

  function reportError(error,result){
    console.error('MAXESS Results bridge failed:',error,result);
    const box=document.createElement('div');
    box.style.cssText='min-height:100vh;display:grid;place-items:center;background:#030305;color:#fff;font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;padding:40px;text-align:center';
    box.innerHTML='<div style="max-width:680px"><div style="font-size:11px;letter-spacing:.18em;color:#d4adff;font-weight:900">MAXESS RESULTS</div><h1 style="font-size:clamp(36px,6vw,62px);line-height:.95;margin:14px 0">Your result is safe.</h1><p style="color:#aaa;line-height:1.65;font-size:16px">The Results presentation could not be loaded. Your completed assessment was preserved. Please refresh once to retry.</p><button id="maxessRetry" style="margin-top:24px;min-height:52px;padding:0 22px;border-radius:15px;border:1px solid #c79bff;background:#0b0810;color:#fff;font-weight:900;cursor:pointer">Retry Results</button></div>';
    document.body.replaceChildren(box);
    document.getElementById('maxessRetry')?.addEventListener('click',()=>location.reload());
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',watch);else watch();
})();
