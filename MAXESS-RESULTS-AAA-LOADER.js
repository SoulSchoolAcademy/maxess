/* =====================================================================
   MAXESS RESULTS AAA — LIVE GROOVE BRIDGE
   Load this script AFTER the existing MAXESS assessment code.

   It does NOT duplicate assessment scoring. It waits for the existing
   Results state to appear, captures the rendered real result, loads the
   complete flagship Results artifact, and mounts the captured data.
   ===================================================================== */
(function(){
  'use strict';

  const SOURCE='https://cdn.jsdelivr.net/gh/SoulSchoolAcademy/maxess@main/MAXESS-RESULTS-AAA-FULL.html';
  let launched=false;

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

    return {
      overallScore:overall,
      profile:{
        name:text('#resultLevelText')||text('#resultLevel'),
        description:text('#resultSubtitle')
      },
      dimensions,
      strengths:text('#strongestName')?[{name:text('#strongestName'),score:number('#strongestScore'),description:text('#strongestText')}]:[],
      opportunities:text('#opportunityName')?[{name:text('#opportunityName'),score:number('#opportunityScore'),description:text('#opportunityText')}]:[],
      personalizedAnalysis:text('#analysisCloud'),
      insight:{text:text('#analysisCloud')},
      metadata:{source:'MAXESS assessment result boundary',capturedAt:new Date().toISOString()}
    };
  }

  async function load(){
    if(launched)return;
    launched=true;
    const realResult=readCurrentResult();

    const response=await fetch(SOURCE,{cache:'no-store'});
    if(!response.ok)throw new Error(`MAXESS Results source failed: ${response.status}`);

    const html=await response.text();
    const doc=new DOMParser().parseFromString(html,'text/html');

    document.title='MAXESS — Your AI Mastery Results';
    document.head.innerHTML=doc.head.innerHTML;
    document.body.innerHTML=doc.body.innerHTML;

    doc.body.querySelectorAll('script').forEach(oldScript=>{
      const script=document.createElement('script');
      if(oldScript.src)script.src=oldScript.src;
      else script.textContent=oldScript.textContent;
      document.body.appendChild(script);
    });

    let tries=0;
    const mount=()=>{
      tries++;
      if(window.MAXESS_RESULTS&&typeof window.MAXESS_RESULTS.mount==='function'){
        window.MAXESS_RESULTS.mount(realResult);
        return;
      }
      if(tries<50)setTimeout(mount,50);
      else console.error('MAXESS Results mount API was not found.');
    };
    mount();
  }

  function ready(){
    const results=document.getElementById('resultsView');
    if(!results)return false;
    return results.classList.contains('visible')&&number('#overallScore')>0&&document.querySelectorAll('#dimensionConstellation .dimension-orb').length>=5;
  }

  function watch(){
    if(ready()){load().catch(reportError);return;}
    const observer=new MutationObserver(()=>{
      if(ready()){
        observer.disconnect();
        load().catch(reportError);
      }
    });
    observer.observe(document.body,{subtree:true,childList:true,attributes:true,attributeFilter:['class','style']});
    setTimeout(()=>observer.disconnect(),30*60*1000);
  }

  function reportError(error){
    console.error('MAXESS AAA Results bridge failed:',error);
    const box=document.createElement('div');
    box.style.cssText='min-height:70vh;display:grid;place-items:center;background:#030305;color:#fff;font-family:Inter,system-ui,sans-serif;padding:40px;text-align:center';
    box.innerHTML='<div style="max-width:620px"><div style="font-size:11px;letter-spacing:.18em;color:#d4adff;font-weight:900">MAXESS RESULTS</div><h1 style="font-size:42px;margin:12px 0">Your result is ready, but the presentation could not be loaded.</h1><p style="color:#aaa;line-height:1.6">Please refresh once. Your assessment data has not been changed.</p></div>';
    document.body.replaceChildren(box);
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',watch);else watch();
})();
