from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
original = s
MARKER = 'MAXESS NAYA MASTERS BRAND SYSTEM'

CSS = r'''
/* =========================================================
   MAXESS NAYA MASTERS BRAND SYSTEM
   Naya is the brand. The specialist is the mastery.
========================================================= */
.maxess-treasure{
  background:
    radial-gradient(circle at 50% -8%,rgba(138,92,255,.17),transparent 34%),
    radial-gradient(circle at 12% 80%,rgba(84,36,181,.10),transparent 30%),
    linear-gradient(145deg,#09070d,#030306 72%);
  border-color:rgba(184,149,255,.27);
  box-shadow:0 34px 100px rgba(0,0,0,.62),0 0 90px rgba(138,92,255,.10),inset 0 1px 0 rgba(255,255,255,.08);
}
.maxess-treasure::before{opacity:.45;}
.maxess-treasure-kicker{color:#b895ff;}
.maxess-treasure-title span{
  background:linear-gradient(90deg,#fff,#d9c7ff,#8a5cff,#fff);
  background-size:220% auto;
}
.maxess-value-line{margin-bottom:34px;}
.maxess-value-chip{
  border-color:rgba(184,149,255,.18);
  background:rgba(138,92,255,.045);
  color:#dcd4eb;
}
.maxess-expert-header{margin:46px 0 22px;text-align:center;}
.maxess-expert-header h4{font-size:clamp(24px,3vw,34px);color:#fff;}
.maxess-expert-header p{max-width:760px;margin:0 auto;color:#aaa5b3;font-size:14px;}
.maxess-expert-grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:14px;
  text-align:left;
}
.maxess-expert-card{
  position:relative;
  min-height:178px;
  padding:19px 18px 18px;
  border:1px solid rgba(255,255,255,.09);
  border-radius:26px;
  overflow:hidden;
  background:
    radial-gradient(circle at 20% 10%,rgba(138,92,255,.12),transparent 46%),
    linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.012) 58%,rgba(52,24,104,.08));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.055),0 15px 34px rgba(0,0,0,.30);
  transition:transform .22s var(--ease),border-color .22s ease,box-shadow .22s ease;
}
.maxess-expert-card::after{
  content:"NAYA";
  position:absolute;
  right:15px;
  top:13px;
  color:rgba(184,149,255,.20);
  font-size:8px;
  letter-spacing:.18em;
  font-weight:1000;
}
.maxess-expert-card:hover{
  transform:translateY(-4px);
  border-color:rgba(184,149,255,.34);
  box-shadow:0 18px 40px rgba(0,0,0,.38),0 0 28px rgba(138,92,255,.11);
}
.maxess-expert-icon{
  width:58px;
  height:58px;
  margin:0 0 17px;
  display:grid;
  place-items:center;
  border-radius:18px;
  background:
    radial-gradient(circle at 30% 18%,#fff 0%,#d8c6ff 11%,#9b74ff 36%,#4a2298 68%,#0d0718 100%);
  border:1px solid rgba(255,255,255,.72);
  box-shadow:inset 0 2px 5px rgba(255,255,255,.72),0 0 26px rgba(138,92,255,.22),0 10px 18px rgba(0,0,0,.45);
  color:#fff;
  font-size:19px;
  font-weight:1000;
  letter-spacing:.02em;
}
.maxess-expert-name{
  max-width:86%;
  color:#fff;
  font-size:16px;
  line-height:1.12;
  font-weight:950;
  letter-spacing:-.015em;
}
.maxess-expert-type{
  margin-top:9px;
  color:#a99fb7;
  font-size:10px;
  line-height:1.4;
  letter-spacing:.08em;
  text-transform:uppercase;
  font-weight:850;
}
.maxess-expert-card .naya-master-label{
  display:block;
  margin-top:7px;
  color:#b895ff;
  font-size:10px;
  font-weight:900;
}
.maxess-three-step{grid-template-columns:repeat(3,1fr);gap:15px;}
.maxess-step-card{
  padding:24px;
  border-color:rgba(184,149,255,.16);
  background:linear-gradient(145deg,rgba(138,92,255,.065),rgba(255,255,255,.012));
}
.maxess-step-no{color:#b895ff;}
.maxess-offer{
  border-color:rgba(184,149,255,.28);
  background:linear-gradient(145deg,rgba(138,92,255,.10),rgba(70,37,130,.07) 58%,rgba(0,0,0,.18));
  box-shadow:0 0 55px rgba(138,92,255,.09),inset 0 1px 0 rgba(255,255,255,.08);
}
.maxess-offer-badge{background:rgba(138,92,255,.10);border-color:rgba(184,149,255,.24);color:#d8c7ff;}
.maxess-cta-primary{color:#fff;background:linear-gradient(180deg,#7f55ea,#5a2cb8);box-shadow:0 15px 38px rgba(92,47,190,.24),0 0 28px rgba(138,92,255,.13);}
.maxess-cta-secondary{border-color:rgba(184,149,255,.42)!important;}
.maxess-ecosystem img{opacity:.95;filter:drop-shadow(0 0 18px rgba(138,92,255,.20));}
@media(max-width:900px){.maxess-expert-grid{grid-template-columns:repeat(2,minmax(0,1fr));}}
@media(max-width:620px){.maxess-expert-grid{grid-template-columns:1fr;gap:10px}.maxess-expert-card{min-height:150px;padding:17px}.maxess-expert-icon{width:52px;height:52px;margin-bottom:14px}.maxess-expert-name{font-size:15px}.maxess-expert-header{margin-top:38px}}
'''

if MARKER not in s:
    s = s.replace('</style>', CSS + '\n</style>', 1)

JS_ANCHOR = 'const specialized=areas.slice(0,18).map((area,i)=>({name:area&&area.name?area.name:`AI Expert ${i+1}`,type:"Specialized Naya"}));'
JS_REPLACEMENT = '''const masterNames={
      "Writing & Communication":"Naya Master Writer",
      "Research & Information":"Naya Master Researcher",
      "Brainstorming & Ideas":"Naya Master Idea Strategist",
      "Content Creation":"Naya Master Content Creator",
      "Business & Strategy":"Naya Master Business Strategist",
      "Marketing & Sales":"Naya Master Marketing Strategist",
      "Learning & Education":"Naya Master Learning Designer",
      "Coding & Software":"Naya Master Developer",
      "Images & Visual Creation":"Naya Master Visual Creator",
      "Video & Media":"Naya Master Video Creator",
      "Audio & Voice":"Naya Master Audio Creator",
      "Data & Analysis":"Naya Master Data Analyst",
      "Productivity & Automation":"Naya Master Automation Architect",
      "Personal Growth & Reflection":"Naya Master Reflection Guide",
      "Career & Work":"Naya Master Career Strategist",
      "Creativity & Design":"Naya Master Creative Director",
      "AI Agents & Systems":"Naya Master AI Systems Architect",
      "Something Else":"Naya Master Explorer"
    };
    const specialized=areas.slice(0,18).map((area,i)=>({
      name:(area&&masterNames[area.name])||`Naya Master ${area&&area.name?area.name:`Specialist ${i+1}`}`,
      type:"Master Naya · Specialized Intelligence",
      original:area&&area.name?area.name:"Specialist"
    }));'''
if JS_ANCHOR in s:
    s=s.replace(JS_ANCHOR,JS_REPLACEMENT,1)

s=s.replace(
    'const core=[{name:"Naya Prime",type:"Master intelligence"},{name:"Naya Orchestrator",type:"Coordinates the experts"},{name:"Naya Oscar",type:"Elite quality judge"}];',
    'const core=[{name:"Naya Prime",type:"Naya Master · Core Intelligence"},{name:"Naya Orchestrator",type:"Naya Master · Expert Coordination"},{name:"Naya Oscar",type:"Naya Master · Quality & Excellence"}];'
)

s=s.replace(
    'const iconFor=(name)=>{const letters=String(name).replace(/^Naya\\s*/i,"").trim().split(/\\s+/).filter(Boolean).slice(0,2).map(x=>x[0]).join("").toUpperCase();return letters||"N";};',
    'const iconFor=(name)=>{const words=String(name).replace(/^Naya\\s*/i,"").split(/\\s+/).filter(w=>w.length>2 && !/^Master$/i.test(w));const letters=words.slice(0,2).map(x=>x[0]).join("").toUpperCase();return letters||"NY";};'
)
s=s.replace(
    '<div class="maxess-expert-name">${escapeHtmlSafe(e.name)}</div><div class="maxess-expert-type">${escapeHtmlSafe(e.type)}</div>',
    '<div class="maxess-expert-name">${escapeHtmlSafe(e.name)}</div><div class="naya-master-label">NAYA · MASTER SPECIALIST</div><div class="maxess-expert-type">${escapeHtmlSafe(e.type)}</div>'
)
if s==original:
    print('Naya Masters transform already applied; continuing safely')
else:
    p.write_text(s,encoding='utf-8')
    print('Naya Masters brand presentation applied')
