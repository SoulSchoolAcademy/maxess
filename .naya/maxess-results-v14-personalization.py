from pathlib import Path

ARTIFACT = Path('MAXESS-RESULTS-10-GROOVE.html')
MARKER = '<!-- MAXESS-RESULTS-V14-PERSONALIZATION -->'

PATCH = r'''<!-- MAXESS-RESULTS-V14-PERSONALIZATION -->
<style id="maxess-results-v14-personalization-css">
/*
  V14 PERSONALIZATION LAYER
  Purpose: turn Results from a score report into a persistent personal profile.
  Rule: never invent identity or context. Use only authoritative Result Contract data.
*/
#maxess-results-10 .mx-v14-profile{position:relative;width:min(1280px,100%);margin:0 auto;padding:clamp(24px,3.5vw,42px);border:1px solid rgba(150,93,255,.18);border-radius:30px;background:linear-gradient(135deg,rgba(150,93,255,.10),rgba(255,255,255,.035) 55%,rgba(70,229,255,.045));box-shadow:0 28px 90px rgba(0,0,0,.24),inset 0 1px rgba(255,255,255,.10);overflow:hidden}
#maxess-results-10 .mx-v14-profile::before{content:"";position:absolute;width:360px;height:360px;right:-140px;top:-180px;border-radius:50%;background:radial-gradient(circle,rgba(150,93,255,.18),transparent 68%);filter:blur(8px);pointer-events:none}
#maxess-results-10 .mx-v14-profile-head{position:relative;z-index:1;display:flex;align-items:flex-start;justify-content:space-between;gap:24px}
#maxess-results-10 .mx-v14-profile-kicker{display:block;color:#cdb4ff;font-size:10px;font-weight:950;letter-spacing:.2em;text-transform:uppercase}
#maxess-results-10 .mx-v14-profile-title{margin:7px 0 0;font-size:clamp(28px,3.8vw,52px);line-height:.98;letter-spacing:-.05em;font-weight:850}
#maxess-results-10 .mx-v14-profile-sub{max-width:720px;margin:10px 0 0;color:rgba(255,255,255,.62);font-size:14px;line-height:1.55}
#maxess-results-10 .mx-v14-profile-score{display:flex;align-items:baseline;gap:6px;white-space:nowrap}
#maxess-results-10 .mx-v14-profile-score strong{font-size:clamp(46px,6vw,78px);line-height:.8;letter-spacing:-.08em;background:linear-gradient(110deg,#fff,#cdb1ff,#55dfff);-webkit-background-clip:text;background-clip:text;color:transparent}
#maxess-results-10 .mx-v14-profile-score span{color:rgba(255,255,255,.44);font-size:10px;font-weight:900;letter-spacing:.14em}
#maxess-results-10 .mx-v14-profile-grid{position:relative;z-index:1;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin-top:26px}
#maxess-results-10 .mx-v14-profile-cell{min-height:96px;padding:16px;border-radius:18px;border:1px solid rgba(255,255,255,.10);background:rgba(0,0,0,.14)}
#maxess-results-10 .mx-v14-profile-cell span{display:block;color:rgba(255,255,255,.40);font-size:9px;font-weight:950;letter-spacing:.14em;text-transform:uppercase}
#maxess-results-10 .mx-v14-profile-cell b{display:block;margin-top:8px;color:#fff;font-size:15px;line-height:1.25}
#maxess-results-10 .mx-v14-profile-cell small{display:block;margin-top:5px;color:rgba(255,255,255,.48);font-size:10px;line-height:1.4}
#maxess-results-10 .mx-v14-personal-copy{max-width:860px;margin:18px auto 0;color:rgba(255,255,255,.66);font-size:15px;line-height:1.65;text-align:center}
#maxess-results-10 .mx-v14-personal-copy strong{color:#fff}
#maxess-results-10 .mx-v14-personal-badge{display:inline-flex;align-items:center;gap:7px;margin-top:13px;padding:8px 11px;border-radius:999px;border:1px solid rgba(150,93,255,.24);background:rgba(150,93,255,.08);color:#d9c5ff;font-size:9px;font-weight:950;letter-spacing:.13em;text-transform:uppercase}
#maxess-results-10 .mx-v14-personal-dot{width:7px;height:7px;border-radius:50%;background:#55dfff;box-shadow:0 0 12px rgba(85,223,255,.65)}
#maxess-results-10 .mx-v14-profile[data-profile-state="partial"]{border-color:rgba(255,255,255,.12)}
#maxess-results-10 .mx-v14-profile[data-profile-state="minimal"] .mx-v14-profile-cell{opacity:.88}
@media(max-width:900px){#maxess-results-10 .mx-v14-profile-head{display:block}#maxess-results-10 .mx-v14-profile-score{margin-top:22px}#maxess-results-10 .mx-v14-profile-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:560px){#maxess-results-10 .mx-v14-profile{padding:22px 18px;border-radius:24px}#maxess-results-10 .mx-v14-profile-grid{grid-template-columns:1fr}.mx-v14-profile-cell{min-height:82px}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-v14-profile{scroll-behavior:auto}}
@media print{#maxess-results-10 .mx-v14-profile{background:#fff!important;color:#111!important;border:1px solid #bbb!important;box-shadow:none!important;break-inside:avoid}#maxess-results-10 .mx-v14-profile-title,#maxess-results-10 .mx-v14-profile-cell b,#maxess-results-10 .mx-v14-profile-score strong{color:#111!important;-webkit-text-fill-color:#111!important}#maxess-results-10 .mx-v14-profile-sub,#maxess-results-10 .mx-v14-profile-cell small,#maxess-results-10 .mx-v14-personal-copy{color:#333!important}}
</style>
<script id="maxess-results-v14-personalization-js">
(function(){
'use strict';
const root=document.getElementById('maxess-results-10');
if(!root||root.dataset.v14Personalization==='1')return;
root.dataset.v14Personalization='1';
const $=(s,c=root)=>c.querySelector(s);
const $$=(s,c=root)=>Array.from(c.querySelectorAll(s));
const clamp=n=>Math.max(0,Math.min(100,n));
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function result(){return window.MAXESS_RESULT||null}
function first(...vals){return vals.find(v=>v!==undefined&&v!==null&&String(v).trim()!=='')||''}
function score(){const r=result()||{};const n=Number(r.overallScore??r.score??r.masterScore??r.overall);return Number.isFinite(n)?clamp(n):null}
function dimensions(){const r=result()||{};const raw=Array.isArray(r.dimensions)?r.dimensions:[];return raw.slice(0,5).map((d,i)=>({id:d.id||String(i+1),name:d.name||d.label||`Dimension ${i+1}`,score:clamp(Number(d.score??d.value??0)||0),description:d.description||d.insight||''}))}
function profileData(){
 const r=result()||{};
 const p=(r.profile&&typeof r.profile==='object')?r.profile:{};
 const u=(r.user&&typeof r.user==='object')?r.user:{};
 const person=(r.person&&typeof r.person==='object')?r.person:{};
 const identity=(r.identity&&typeof r.identity==='object')?r.identity:{};
 const name=first(p.name,p.displayName,u.name,u.displayName,person.name,identity.name,r.name,r.firstName);
 const role=first(p.role,p.title,p.profession,u.role,person.role,r.role);
 const goal=first(p.goal,p.primaryGoal,p.objective,u.goal,person.goal,r.goal,r.primaryGoal);
 const experience=first(p.experienceLevel,p.level,u.experienceLevel,person.experienceLevel,r.experienceLevel);
 const organization=first(p.organization,p.company,u.organization,person.organization,r.organization);
 const location=first(p.location,u.location,person.location,r.location);
 const bio=first(p.bio,p.about,u.bio,person.bio,r.bio);
 return {name,role,goal,experience,organization,location,bio,hasIdentity:!!(name||role||goal||organization||location||bio),raw:p};
}
function band(s){return s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':'Foundation'}
function buildProfile(){
 const s=score();if(s===null)return;
 const ds=dimensions();const p=profileData();
 const sorted=ds.slice().sort((a,b)=>b.score-a.score);const strongest=sorted[0];const lever=sorted[sorted.length-1];
 const profile=document.createElement('section');profile.id='maxess-personal-profile';profile.className='mx-section';
 profile.setAttribute('aria-label','Your MAXESS personal profile');
 const state=p.hasIdentity?'partial':'minimal';
 profile.innerHTML=`<div class="mx-wide"><div class="mx-v14-profile" data-profile-state="${state}">
   <div class="mx-v14-profile-head">
     <div><span class="mx-v14-profile-kicker">YOUR MAXESS PROFILE</span>
     <h2 class="mx-v14-profile-title">${p.name?esc(p.name)+', here is your AI profile.':'Here is your AI profile.'}</h2>
     <p class="mx-v14-profile-sub">This profile is generated from your authoritative MAXESS result. It changes with your real result data — never with invented assumptions.</p></div>
     <div class="mx-v14-profile-score"><strong>${Math.round(s)}</strong><span>/ 100</span></div>
   </div>
   <div class="mx-v14-profile-grid">
     <div class="mx-v14-profile-cell"><span>LEVEL</span><b>${band(s)}</b><small>Your current MAXESS mastery range.</small></div>
     <div class="mx-v14-profile-cell"><span>STRONGEST SIGNAL</span><b>${strongest?esc(strongest.name):'Building'}</b><small>${strongest?Math.round(strongest.score)+' / 100':'Awaiting dimension data'}</small></div>
     <div class="mx-v14-profile-cell"><span>BIGGEST LEVER</span><b>${lever?esc(lever.name):'Your next opportunity'}</b><small>${lever?Math.round(lever.score)+' / 100':'Awaiting dimension data'}</small></div>
     <div class="mx-v14-profile-cell"><span>PROFILE CONTEXT</span><b>${esc(first(p.role,p.goal,p.experience,p.organization,'Assessment profile'))}</b><small>${p.role||p.goal||p.experience||p.organization?'Personal context supplied by the Result Contract.':'Core score + dimension profile currently available.'}</small></div>
   </div>
   ${p.goal?`<p class="mx-v14-personal-copy"><strong>Your stated goal:</strong> ${esc(p.goal)}. Your report uses that context as a personalization signal without changing your score.</p>`:''}
   <span class="mx-v14-personal-badge"><i class="mx-v14-personal-dot" aria-hidden="true"></i>${p.hasIdentity?'PERSONALIZED FROM RESULT DATA':'PERSONALIZATION-READY RESULT CONTRACT'}</span>
 </div></div>`;
 const anchor=$('#v13-naya-introduction')||$('#v11-naya-report')||$('#naya-report')||$('.mx-hero');
 if(anchor)anchor.insertAdjacentElement('afterend',profile);else root.insertBefore(profile,root.firstElementChild);
}
function personalizeExistingCopy(){
 const s=score();if(s===null)return;const p=profileData();const ds=dimensions();const strongest=ds.slice().sort((a,b)=>b.score-a.score)[0];const lever=ds.slice().sort((a,b)=>a.score-b.score)[0];
 const targetName=p.name?`${esc(p.name)}, `:'';
 const nayaSelectors=['.v13-naya-copy','.v12-naya-copy','.v11-naya-sub','.naya-v6-copy','.naya-presence-copy p'];
 nayaSelectors.forEach(sel=>$$(`${sel}`).forEach(el=>{
   if(el.dataset.v14Personalized==='1')return;
   const original=el.textContent||'';
   if(p.name)el.textContent=`${p.name}, ${original.charAt(0).toLowerCase()+original.slice(1)}`;
   el.dataset.v14Personalized='1';
 }));
 const next=root.querySelector('#your-next-move,#v11-next,#v12-next');
 if(next&&lever){const pEls=$$('p',next);const meaningful=pEls.find(el=>/focused|next|move|leverage/i.test(el.textContent||''));if(meaningful)meaningful.textContent=`Your clearest next opportunity is ${lever.name} at ${Math.round(lever.score)}. Start with one real workflow and improve it deliberately.`}
 if(strongest){root.querySelectorAll('#your-strengths h3,#v11-strengths h3').forEach(h=>{if(!h.dataset.v14Personalized){h.textContent=strongest.name;h.dataset.v14Personalized='1'}})}
}
function exposeProfile(){
 const s=score();if(s===null)return;
 const ds=dimensions(),p=profileData();const sorted=ds.slice().sort((a,b)=>b.score-a.score);
 window.MAXESS_PROFILE={schema:'MAXESS-PERSONAL-PROFILE-1',name:p.name||null,role:p.role||null,goal:p.goal||null,experienceLevel:p.experience||null,organization:p.organization||null,location:p.location||null,overallScore:Math.round(s),band:band(s),dimensions:ds,strongest:sorted[0]||null,biggestLever:sorted[sorted.length-1]||null,personalized:Boolean(p.hasIdentity),source:'window.MAXESS_RESULT',createdAt:new Date().toISOString()};
 root.setAttribute('data-personalization-state',p.hasIdentity?'personalized':'personalization-ready');
 root.dispatchEvent(new CustomEvent('maxess:profile-ready',{detail:window.MAXESS_PROFILE}));
}
function run(){if(score()===null)return;exposeProfile();if(!root.querySelector('#maxess-personal-profile'))buildProfile();personalizeExistingCopy()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,120),{once:true});else setTimeout(run,120);
window.addEventListener('maxess:result-ready',()=>setTimeout(run,40));
})();
</script>
'''

text = ARTIFACT.read_text(encoding='utf-8')
if MARKER in text:
    raise SystemExit('V14 personalization already present; refusing duplicate mutation.')
needle = '</body>'
if needle not in text:
    raise SystemExit('Authoritative Results artifact has no </body>; refusing unsafe mutation.')
updated = text.replace(needle, PATCH + '\n' + needle, 1)
ARTIFACT.write_text(updated, encoding='utf-8')
print(f'V14 personalization appended to {ARTIFACT}; bytes {len(text)} -> {len(updated)}')
