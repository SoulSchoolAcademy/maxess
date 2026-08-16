from pathlib import Path

ARTIFACT = Path('MAXESS-RESULTS-10-GROOVE.html')
MARKER = '<!-- MAXESS-RESULTS-V15-POLISH -->'
PATCH = r'''<!-- MAXESS-RESULTS-V15-POLISH -->
<style id="maxess-results-v15-polish-css">
#maxess-results-10.v15-results #v13-masters .v13-master-grid{position:relative}
#maxess-results-10.v15-results #v13-masters .v13-master{padding:24px 20px 20px 92px!important;min-height:158px!important;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.012))!important}
#maxess-results-10.v15-results .v15-master-icon{position:absolute;left:20px;top:22px;display:grid;place-items:center;width:52px;height:52px;border-radius:18px;background:radial-gradient(circle at 30% 25%,rgba(255,255,255,.28),rgba(150,93,255,.16) 48%,rgba(0,0,0,.20));border:1px solid color-mix(in srgb,var(--g) 48%,white 8%);box-shadow:inset 0 1px rgba(255,255,255,.18),0 12px 32px rgba(0,0,0,.24);color:#fff;font-size:21px;font-weight:900}
#maxess-results-10.v15-results .v15-master-icon::after{content:"";position:absolute;width:70px;height:70px;border-radius:50%;background:radial-gradient(circle,color-mix(in srgb,var(--g) 20%,transparent),transparent 70%);filter:blur(5px);z-index:-1}
#maxess-results-10.v15-results #v13-masters .v13-master>b{position:absolute;right:16px;top:15px;color:rgba(255,255,255,.28)!important;font-size:9px!important;letter-spacing:.12em}
#maxess-results-10.v15-results .v15-profile-cell{display:grid;grid-template-columns:32px 1fr;column-gap:10px;align-content:center}
#maxess-results-10.v15-results .v15-profile-cell::before{content:"✦";display:grid;place-items:center;width:32px;height:32px;border-radius:11px;background:rgba(150,93,255,.10);border:1px solid rgba(150,93,255,.20);color:#d9c5ff;font-size:12px;grid-row:1/4}
#maxess-results-10.v15-results .v15-profile-cell:nth-child(2)::before{content:"↗";color:#55dfff}
#maxess-results-10.v15-results .v15-profile-cell:nth-child(3)::before{content:"◎";color:#ef4bc8}
#maxess-results-10.v15-results .v15-profile-cell:nth-child(4)::before{content:"◈";color:#ffd84a}
#maxess-results-10.v15-results .v15-profile-cell span,#maxess-results-10.v15-results .v15-profile-cell b,#maxess-results-10.v15-results .v15-profile-cell small{grid-column:2}
#maxess-results-10.v15-results #v15-pattern .v15-pattern-stage{box-shadow:0 35px 100px rgba(0,0,0,.30),0 0 90px rgba(150,93,255,.08)}
@media(max-width:720px){#maxess-results-10.v15-results #v13-masters .v13-master{padding-left:82px!important}.v15-results .v15-master-icon{left:16px;top:18px;width:48px;height:48px}.v15-results .v15-profile-cell{grid-template-columns:30px 1fr}}
@media print{#maxess-results-10.v15-results .v15-master-icon,#maxess-results-10.v15-results .v15-profile-cell::before{background:#eee!important;color:#111!important;box-shadow:none!important;border:1px solid #aaa!important}}
</style>
<script id="maxess-results-v15-polish-js">
(function(){
'use strict';
const root=document.getElementById('maxess-results-10');if(!root)return;
const icons=['✎','◌','✦','▣','◈','↗','⌘','</>','◉','▶','∿','◫','≡','◎','◇','✧','∞','✺'];
function polish(){
 if(root.dataset.v15Polished==='1')return;
 const masters=root.querySelectorAll('#v13-masters .v13-master');
 masters.forEach((card,i)=>{if(card.querySelector('.v15-master-icon'))return;const icon=document.createElement('span');icon.className='v15-master-icon';icon.textContent=icons[i]||'✦';icon.setAttribute('aria-hidden','true');card.appendChild(icon)});
 root.dataset.v15Polished='1';
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(polish,180),{once:true});else setTimeout(polish,180);
window.addEventListener('maxess:profile-ready',polish);
})();
</script>
'''
text = ARTIFACT.read_text(encoding='utf-8')
if MARKER in text:
    raise SystemExit('V15 polish already present; refusing duplicate mutation.')
if '</body>' not in text:
    raise SystemExit('No </body>; refusing unsafe mutation.')
ARTIFACT.write_text(text.replace('</body>', PATCH + '\n</body>', 1), encoding='utf-8')
print('V15 visual polish appended')
