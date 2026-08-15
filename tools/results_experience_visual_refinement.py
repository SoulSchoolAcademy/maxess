from pathlib import Path

PATH = Path('code')
s = PATH.read_text(encoding='utf-8')
original = s
MARKER = 'MAXESS RESULTS EXPERIENCE VISUAL REFINEMENT'

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE VISUAL REFINEMENT
   Black + purple first. Naya is the brand. Reduce UI noise.
========================================================= */
.results-v4-card,
.results-master-v2,
.results-v4-naya,
.results-master-v2-card,
.maxess-signal-item{
  background:linear-gradient(145deg,rgba(255,255,255,.035),rgba(138,92,255,.028) 58%,rgba(0,0,0,.22));
  border-color:rgba(184,149,255,.16);
}

.results-v4-strength strong,
.maxess-signal-keep span,
.results-master-v2-next strong{
  color:#b895ff;
}

.results-v4-opportunity strong,
.maxess-signal-build span{
  color:#b895ff;
}

.results-v4-card h4,
.results-master-v2-kicker,
.maxess-signal-kicker,
.results-v4-naya h4{
  color:#b895ff;
}

.results-v4-truth strong,
.results-master-v2-title,
.maxess-signal h3{
  color:#fff;
}

.results-v4-card p,
.results-master-v2-card p,
.results-master-v2-intro,
.maxess-signal-lead,
.results-v4-truth>span{
  color:#bdb7c5;
}

/* The personal analysis section is meant to feel human, not clinical. */
.analysis-cloud{
  padding:clamp(26px,4vw,38px);
  border-color:rgba(184,149,255,.20);
  background:
    radial-gradient(circle at 22% 0,rgba(138,92,255,.11),transparent 42%),
    linear-gradient(145deg,#0c0a11,#050507);
  box-shadow:0 22px 58px rgba(0,0,0,.38),inset 0 1px 0 rgba(255,255,255,.07);
}
.analysis-cloud::before{
  content:"NAYA'S READING";
  display:block;
  margin-bottom:13px;
  color:#b895ff;
  font-size:10px;
  font-weight:950;
  letter-spacing:.19em;
}
.analysis-cloud p{
  max-width:850px;
  color:#e5e0ea;
  font-size:clamp(15px,1.7vw,18px);
  line-height:1.68;
}

/* Naya is the identity, not a decorative orb. */
.results-v4-naya{
  padding:clamp(24px,4vw,36px);
  grid-template-columns:auto minmax(0,1fr);
  background:radial-gradient(circle at 8% 0,rgba(138,92,255,.13),transparent 45%),linear-gradient(145deg,#0b0910,#050507);
}
.results-v4-naya-orb{
  width:58px;
  height:58px;
  background:#050507;
  border:1px solid rgba(184,149,255,.65);
  box-shadow:0 0 26px rgba(138,92,255,.22),inset 0 1px 0 rgba(255,255,255,.12);
  display:grid;
  place-items:center;
}
.results-v4-naya-orb::before{
  content:"N";
  color:#fff;
  font-weight:1000;
  font-size:18px;
  letter-spacing:-.04em;
}
.results-v4-naya h4::before{
  content:"NAYA · ";
  color:#fff;
}

/* Replace the blocky expert grid with a quiet Naya command-center feel. */
.maxess-treasure{
  border-color:rgba(184,149,255,.24);
  background:
    radial-gradient(circle at 50% -12%,rgba(138,92,255,.15),transparent 34%),
    radial-gradient(circle at 10% 88%,rgba(90,50,190,.10),transparent 34%),
    linear-gradient(145deg,#09070d,#020204 70%);
  box-shadow:0 34px 100px rgba(0,0,0,.62),0 0 80px rgba(138,92,255,.08),inset 0 1px 0 rgba(255,255,255,.08);
}
.maxess-treasure::before{display:none}
.maxess-treasure-kicker{color:#b895ff}
.maxess-treasure-title span{
  background:linear-gradient(90deg,#fff,#d6c4ff,#b895ff,#fff);
  background-size:220% auto;
}
.maxess-value-chip{
  border-color:rgba(184,149,255,.16);
  background:rgba(138,92,255,.045);
  color:#d9d1e5;
}

.maxess-expert-header{
  margin-top:42px;
  text-align:center;
}
.maxess-expert-header h4{
  color:#fff;
  font-size:clamp(24px,3.5vw,36px);
  letter-spacing:-.03em;
}
.maxess-expert-header h4::before{
  content:"NAYA · ";
  color:#b895ff;
}
.maxess-expert-header p{
  max-width:730px;
  margin:10px auto 0;
  color:#9f98aa;
  font-size:13px;
}
.maxess-expert-grid{
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:11px;
  margin-top:22px;
}
.maxess-expert-card{
  min-height:0;
  padding:19px 18px;
  border-color:rgba(184,149,255,.15);
  border-radius:20px;
  background:linear-gradient(145deg,rgba(255,255,255,.035),rgba(138,92,255,.045) 60%,rgba(0,0,0,.22));
}
.maxess-expert-card:hover{
  border-color:rgba(184,149,255,.34);
  box-shadow:0 14px 30px rgba(0,0,0,.38),0 0 25px rgba(138,92,255,.10);
}
.maxess-expert-icon{
  width:36px;
  height:36px;
  margin-bottom:11px;
  border-radius:12px;
  border:1px solid rgba(184,149,255,.34);
  background:linear-gradient(145deg,#17121f,#07060a);
  color:#b895ff;
  box-shadow:0 0 18px rgba(138,92,255,.12);
}
.maxess-expert-icon::before{
  content:"N";
  font-size:13px;
  font-weight:1000;
}
.maxess-expert-icon{font-size:0}
.maxess-expert-name{
  color:#fff;
  font-size:14px;
  line-height:1.25;
  font-weight:950;
}
.maxess-expert-type{
  margin-top:5px;
  color:#8f879b;
  font-size:9px;
  letter-spacing:.07em;
}

.maxess-three-step{
  gap:12px;
}
.maxess-step-card{
  border-color:rgba(184,149,255,.13);
  background:rgba(255,255,255,.018);
}
.maxess-step-no{color:#b895ff}
.maxess-step-card p{font-size:13px;color:#aba5b4}

.maxess-offer{
  border-color:rgba(184,149,255,.30);
  background:linear-gradient(145deg,rgba(138,92,255,.10),rgba(255,255,255,.02) 55%,rgba(0,0,0,.18));
  box-shadow:0 0 55px rgba(138,92,255,.08),inset 0 1px 0 rgba(255,255,255,.09);
}
.maxess-offer-badge{
  background:rgba(138,92,255,.10);
  border-color:rgba(184,149,255,.25);
  color:#d7c7f4;
}
.maxess-cta-primary{
  color:#fff;
  background:linear-gradient(180deg,#17121f,#08070b);
  border-color:rgba(184,149,255,.68)!important;
  box-shadow:0 15px 38px rgba(0,0,0,.32),0 0 28px rgba(138,92,255,.12);
}
.maxess-cta-secondary{
  background:linear-gradient(180deg,#0f0d14,#050507);
  border-color:rgba(184,149,255,.42)!important;
}
.maxess-cta-primary:hover,
.maxess-cta-secondary:hover{
  border-color:#cbb5ff!important;
  box-shadow:0 18px 40px rgba(0,0,0,.42),0 0 30px rgba(138,92,255,.18);
}
.maxess-cta-fine{color:#81798f!important}
.maxess-ecosystem{border-top-color:rgba(184,149,255,.10);color:#8f8898}

@media(max-width:900px){
  .maxess-expert-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media(max-width:620px){
  .maxess-expert-grid{grid-template-columns:1fr;gap:9px}
  .maxess-expert-card{padding:17px}
  .maxess-expert-name{font-size:15px}
  .maxess-treasure-title{font-size:32px}
}
'''

if MARKER not in s:
    s = s.replace('</style>', CSS + '\n</style>', 1)

# Make the expert cards explicitly Naya-branded and role-led.
CARD_OLD = 'const specialized=areas.slice(0,18).map((area,i)=>({name:area&&area.name?area.name:`AI Expert ${i+1}`,type:"Specialized Naya"}));'
CARD_NEW = 'const specialized=areas.slice(0,18).map((area,i)=>({name:`Naya Elite ${area&&area.name?area.name.replace(/\\s*&\\s*/g," & "): `Expert ${i+1}`}`,type:"Elite Naya Expert"}));'
if CARD_OLD in s:
    s = s.replace(CARD_OLD, CARD_NEW, 1)

s = s.replace(
    'const core=[{name:"Naya Prime",type:"Master intelligence"},{name:"Naya Orchestrator",type:"Coordinates the experts"},{name:"Naya Oscar",type:"Elite quality judge"}];',
    'const core=[{name:"Naya Prime",type:"Master Intelligence"},{name:"Naya Orchestrator",type:"Expert Coordination"},{name:"Naya Oscar",type:"Elite Quality Judge"}];',
    1
)

# Remove the old yellow-forward wording where it is purely decorative.
s = s.replace('✦ YOUR INVITATION · START FREE','✦ YOUR NAYA INVITATION · START FREE',1)

PATH.write_text(s,encoding='utf-8')
print('MAXESS visual system refinement applied' if s != original else 'no changes required')
