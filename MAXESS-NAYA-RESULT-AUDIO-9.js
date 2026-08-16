/*
  MAXESS — NAYA RESULT AUDIO
  10.0 integration pass.

  Score bands:
    0–50   Foundation
    51–75  Developing
    76–90  Advancing
    91–100 Mastering

  The production audio URLs remain intentionally empty until real Naya assets
  are supplied. Browser speech synthesis remains a functional preview fallback.

  10.0 integration:
  - Loads the MAXESS Living Signature visual engine.
  - Emits public Naya visual events while the report is playing.
  - Positive-result moments can trigger stronger visual resonance.
*/
(function(){
  'use strict';

  const AUDIO_URLS = {
    foundation: '',
    developing: '',
    advancing: '',
    mastering: ''
  };

  const LIVING_SIGNATURE_URL = 'https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/feat/maxess-living-signature-10/MAXESS-LIVING-SIGNATURE-10-PATCH.js';

  const result = window.MAXESS_RESULT || {};
  const score = Math.max(0, Math.min(100, Number(result.overallScore) || 0));
  const dims = Array.isArray(result.dimensions) ? result.dimensions : [];

  function esc(v){return String(v ?? '').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c]));}

  function bandFor(n){
    if(n<=50)return {key:'foundation',label:'FOUNDATION',range:'0–50',intro:'You are building your foundation with AI.'};
    if(n<=75)return {key:'developing',label:'DEVELOPING',range:'51–75',intro:'You are developing your AI capability.'};
    if(n<=90)return {key:'advancing',label:'ADVANCING',range:'76–90',intro:'You are advancing into confident AI mastery.'};
    return {key:'mastering',label:'MASTERING',range:'91–100',intro:'You are operating at a mastering level with AI.'};
  }

  const band=bandFor(score);
  const sorted=dims.slice().sort((a,b)=>(Number(b.score)||0)-(Number(a.score)||0));
  const strongest=sorted[0];
  const opportunity=sorted[sorted.length-1];

  function emit(name,detail){
    try{window.dispatchEvent(new CustomEvent(name,{detail:detail||{}}));}catch(e){}
  }

  function reportText(){
    const parts=[
      `Hello. I'm Naya. This is your MAXESS AI Mastery Report.`,
      `Your overall MAXESS score is ${Math.round(score)} out of 100. Your current level is ${band.label.toLowerCase()}. ${band.intro}`
    ];
    if(strongest)parts.push(`Your strongest signal is ${strongest.name}, with a score of ${Math.round(Number(strongest.score)||0)} out of 100. This is a capability you can use as leverage.`);
    if(opportunity && strongest && opportunity.id!==strongest.id)parts.push(`Your biggest growth opportunity is ${opportunity.name}, currently at ${Math.round(Number(opportunity.score)||0)} out of 100. Strengthening this area can help close the gap between what you already do well and what you can do next.`);
    if(dims.length)parts.push(`Your five-dimensional profile is ${dims.map(d=>`${d.name} ${Math.round(Number(d.score)||0)}`).join(', ')}.`);
    parts.push(`Your MAXESS result is not a label. It is a starting point. The goal is to understand how you work with AI, build the skills that matter most, and turn those skills into repeatable advantage.`);
    parts.push(`Thank you for completing MAXESS. I'm Naya, and I'm here to help you take your next step.`);
    return parts.join(' ');
  }

  function addStyles(){
    if(document.getElementById('maxessNayaAudioStyles'))return;
    const s=document.createElement('style');s.id='maxessNayaAudioStyles';s.textContent=`
      #maxessNayaAudio{position:relative;padding:clamp(60px,8vw,105px) 0 40px;background:radial-gradient(ellipse 75% 65% at 50% 35%,rgba(168,76,255,.18),transparent 72%);overflow:hidden}
      #maxessNayaAudio .mna-wrap{width:min(1050px,calc(100% - 30px));margin:auto}
      #maxessNayaAudio .mna-card{position:relative;border:1px solid rgba(201,145,255,.34);border-radius:34px;padding:clamp(28px,5vw,68px);background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.018));box-shadow:0 30px 100px rgba(0,0,0,.48),0 0 90px rgba(132,51,227,.13);overflow:hidden}
      #maxessNayaAudio .mna-card:before{content:"";position:absolute;width:620px;height:420px;left:50%;top:-220px;transform:translateX(-50%);background:radial-gradient(circle,rgba(194,92,255,.25),transparent 68%);filter:blur(14px);pointer-events:none}
      #maxessNayaAudio .mna-content{position:relative;z-index:1;text-align:center}
      #maxessNayaAudio .mna-eyebrow{color:#d8a9ff;font-size:10px;font-weight:950;letter-spacing:.2em;text-transform:uppercase}
      #maxessNayaAudio h2{font-size:clamp(38px,5.8vw,76px);line-height:.94;letter-spacing:-.06em;margin:12px 0 16px}
      #maxessNayaAudio .mna-intro{max-width:720px;margin:auto;color:rgba(255,255,255,.68);font-size:17px;line-height:1.65}
      #maxessNayaAudio .mna-band{display:inline-flex;align-items:center;gap:9px;margin-top:24px;padding:10px 15px;border-radius:999px;border:1px solid rgba(202,153,255,.35);background:rgba(169,92,255,.10);color:#ead5ff;font-size:11px;font-weight:900;letter-spacing:.15em}
      #maxessNayaAudio .mna-dot{width:8px;height:8px;border-radius:50%;background:#c07aff;box-shadow:0 0 14px #b764ff}
      #maxessNayaAudio .mna-player{margin:32px auto 0;max-width:760px;padding:18px;border-radius:23px;border:1px solid rgba(255,255,255,.11);background:rgba(0,0,0,.27)}
      #maxessNayaAudio audio{display:none;width:100%}
      #maxessNayaAudio .mna-play{width:78px;height:78px;margin:auto;border-radius:50%;border:1px solid rgba(255,255,255,.75);background:radial-gradient(circle at 30% 20%,#fff,#dfb3ff 22%,#9a45ff 53%,#35106f 100%);color:#fff;font-size:25px;font-weight:900;box-shadow:inset 0 2px 4px rgba(255,255,255,.9),0 0 34px rgba(170,80,255,.42);cursor:pointer;transition:transform .2s ease,filter .2s ease}
      #maxessNayaAudio .mna-play:hover{transform:scale(1.05);filter:brightness(1.08)}
      #maxessNayaAudio .mna-play:focus-visible{outline:3px solid #fff;outline-offset:5px}
      #maxessNayaAudio .mna-label{margin-top:14px;font-weight:850;font-size:18px}
      #maxessNayaAudio .mna-sub{margin-top:6px;color:rgba(255,255,255,.46);font-size:12px;line-height:1.5}
      #maxessNayaAudio .mna-progress{height:5px;margin:22px auto 0;max-width:620px;border-radius:999px;background:rgba(255,255,255,.08);overflow:hidden}
      #maxessNayaAudio .mna-progress i{display:block;width:0;height:100%;border-radius:inherit;background:linear-gradient(90deg,#7c2be0,#f0d5ff,#8d43ff);transition:width .25s linear}
      #maxessNayaAudio .mna-note{margin-top:18px;color:rgba(255,255,255,.38);font-size:10px;line-height:1.5}
      @media(max-width:600px){#maxessNayaAudio{padding-top:50px}.mna-card{border-radius:26px!important}.mna-play{width:70px!important;height:70px!important}}
      @media(prefers-reduced-motion:reduce){#maxessNayaAudio .mna-play{transition:none}}
    `;document.head.appendChild(s);
  }

  function loadLivingSignature(){
    if(document.getElementById('maxessLivingSignatureScript'))return;
    const script=document.createElement('script');
    script.id='maxessLivingSignatureScript';
    script.src=LIVING_SIGNATURE_URL;
    script.async=true;
    script.onerror=function(){console.warn('MAXESS Living Signature: visual engine could not be loaded.');};
    document.head.appendChild(script);
  }

  function insert(){
    if(document.getElementById('maxessNayaAudio'))return;
    const endpoint=document.querySelector('.naya-end')||document.querySelector('.naya-section')||document.getElementById('nayaEnd');
    if(!endpoint)return;
    const theater=endpoint.querySelector('.ny-theater')||endpoint.querySelector('.ny-screen-frame')||endpoint.firstElementChild;
    const section=document.createElement('section');section.id='maxessNayaAudio';section.setAttribute('aria-label','Naya MAXESS audio report');
    section.innerHTML=`<div class="mna-wrap"><div class="mna-card"><div class="mna-content"><div class="mna-eyebrow">NAYA · YOUR PERSONAL REPORT</div><h2>Listen to your result.</h2><p class="mna-intro">Naya has your MAXESS result. Press play and listen to the report for your level.</p><div class="mna-band"><span class="mna-dot"></span>${band.label} · ${band.range}</div><div class="mna-player"><audio id="maxessNayaAudioElement" preload="none"></audio><button class="mna-play" id="maxessNayaPlay" type="button" aria-label="Play your Naya MAXESS report">▶</button><div class="mna-label" id="maxessNayaPlayLabel">Play your Naya report</div><div class="mna-sub" id="maxessNayaStatus">${AUDIO_URLS[band.key]?'Your personalized Naya audio is ready.':'Preview mode: the four Naya audio URLs have not yet been added to the repository.'}</div><div class="mna-progress"><i id="maxessNayaProgress"></i></div><div class="mna-note">Your report is selected automatically from your MAXESS score.</div></div></div></div></div>`;
    if(theater)theater.parentNode.insertBefore(section,theater);else endpoint.insertBefore(section,endpoint.firstChild);

    const audio=document.getElementById('maxessNayaAudioElement');
    const play=document.getElementById('maxessNayaPlay');
    const label=document.getElementById('maxessNayaPlayLabel');
    const status=document.getElementById('maxessNayaStatus');
    const progress=document.getElementById('maxessNayaProgress');
    const url=AUDIO_URLS[band.key];
    if(url)audio.src=url;

    let speaking=false;
    let wordTimer=null;

    function startVisual(){emit('maxess:naya:start',{score,band:band.key});}
    function stopVisual(){emit('maxess:naya:stop',{score,band:band.key});if(wordTimer)clearInterval(wordTimer);wordTimer=null;}
    function simulateSpeech(){
      if(wordTimer)clearInterval(wordTimer);
      let t=0;
      wordTimer=setInterval(()=>{
        t++;
        const energy=.48 + .44*((Math.sin(t*1.7)+1)/2);
        emit('maxess:naya:word',{energy,step:t});
        if(t%7===0)emit('maxess:naya:positive',{energy:.94});
      },260);
    }

    play.addEventListener('click',async()=>{
      if(url){
        if(audio.paused){
          try{await audio.play();label.textContent='Pause your Naya report';play.textContent='❚❚';status.textContent='Naya is speaking your personalized report.';startVisual();}
          catch(e){status.textContent='Audio could not start. Press play again.';}
        }else{audio.pause();label.textContent='Resume your Naya report';play.textContent='▶';stopVisual();}
        return;
      }
      if(!('speechSynthesis' in window)){status.textContent='No Naya audio asset is configured and this browser has no speech preview support.';return;}
      if(speaking){speechSynthesis.cancel();speaking=false;play.textContent='▶';label.textContent='Play your Naya report';status.textContent='Preview stopped.';stopVisual();return;}
      speechSynthesis.cancel();
      const u=new SpeechSynthesisUtterance(reportText());
      u.rate=.94;u.pitch=1.0;u.volume=1;
      speaking=true;play.textContent='❚❚';label.textContent='Stop your Naya report';status.textContent='Preview mode: your browser is speaking the generated report. Replace the four URLs with Naya recordings for production.';
      startVisual();simulateSpeech();speechSynthesis.speak(u);
      u.onend=()=>{speaking=false;play.textContent='▶';label.textContent='Play your Naya report';status.textContent='Preview complete.';stopVisual();};
      u.onerror=()=>{speaking=false;play.textContent='▶';label.textContent='Play your Naya report';status.textContent='Speech preview stopped.';stopVisual();};
    });
    audio.addEventListener('timeupdate',()=>{const p=audio.duration?audio.currentTime/audio.duration*100:0;progress.style.width=p+'%';});
    audio.addEventListener('play',()=>{startVisual();});
    audio.addEventListener('pause',()=>{if(!audio.ended)stopVisual();});
    audio.addEventListener('ended',()=>{play.textContent='▶';label.textContent='Replay your Naya report';status.textContent='Naya has finished your report.';progress.style.width='100%';stopVisual();});
  }

  function run(){addStyles();loadLivingSignature();insert();}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,50));else setTimeout(run,50);
})();
