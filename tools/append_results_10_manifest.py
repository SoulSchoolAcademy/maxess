#!/usr/bin/env python3
"""Append a machine-readable contract for future Naya/agent retrieval.

This is durable product knowledge, not filler: it records the decisions that
must remain true when the real Result Contract replaces the fixture.
"""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
FILES=[ROOT/'MAXESS-RESULTS-FINAL-GROOVE.html',ROOT/'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html',ROOT/'MAXESS-RESULTS-10-GROOVE.html',ROOT/'MAXESS-RESULTS-GROOVE-EMBED.html',ROOT/'MAXESS-RESULTS-GROOVE-EMBED-9.95.html']
MANIFEST={
  'schema':'MAXESS-RESULTS-EXPERIENCE-MANIFEST-1',
  'status':'development-ready',
  'data_mode':'development-fixture',
  'production_rule':'Replace only the fixture payload; never create a second scoring engine in the Results renderer.',
  'system_journey':['MAXESS','Assessment','Result Contract','Results','NayaNET','Zero Cost Start / Free Trial'],
  'experience_job':'Transform assessment measurement into self-understanding, insight, possibility, action, Naya guidance, and continuation.',
  'authoritative_score_bands':[
    {'min':0,'max':50,'label':'Foundation'},
    {'min':51,'max':75,'label':'Developing'},
    {'min':76,'max':90,'label':'Advancing'},
    {'min':91,'max':100,'label':'Mastering'}
  ],
  'five_dimensions':['Direction','Communication','Evaluation','Iteration','Systems Thinking'],
  'eighteen_ai_pathways':[x[0] for x in [
    ('Writing & Communication',''),('Research & Information',''),('Brainstorming & Ideas',''),('Content Creation',''),('Business & Strategy',''),('Marketing & Sales',''),('Learning & Education',''),('Coding & Software',''),('Images & Visual Creation',''),('Video & Media',''),('Documents & Presentations',''),('Data & Analysis',''),('Productivity & Planning',''),('Career & Professional Development',''),('Personal Decision-Making',''),('Creative Work',''),('Automation & Systems',''),('Advanced AI Work','')
  ]],
  'narrative':['Result reveal','Meaning','Five-dimension fingerprint','Score interpretation','Natural advantage','Highest-leverage opportunity','Revelation','Next move','18 AI mastery areas','Naya','Master Key','NayaNET foundation','Conversion'],
  'visual_principles':['Full-width composition','Intelligent editorial reading widths','Controlled density','Darkness plus illumination','Purple/violet depth','High-contrast focal moments','Tactile controls','Purposeful motion','Strong hierarchy','No generic SaaS card wall'],
  'growth_principles':['Value before conversion','Recognition before recommendation','Insight before CTA','Progressive disclosure for complexity','Make the next action feel earned','Optimize for continuation and return, not clicks alone'],
  'naya_integration':{
    'role':'Bridge between knowing the result and doing something with it.',
    'button':'Naya — Listen to Your Report',
    'tiers':['0–50 Foundation','51–75 Developing','76–90 Advancing','91–100 Mastering'],
    'foundation_file':'nayanetpagecode',
    'foundation_rule':'Append the real Page Code as the final chapter; do not recreate weaker button, icon, video, or membership markup.'
  },
  'conversion':{
    'destination':'https://takeyourpowerback.xyz/services',
    'label':'Zero Cost Start / Free Trial',
    'principle':'Commercial action is a natural next chapter, not an interruption.'
  },
  'accessibility':['Keyboard focus','Semantic controls','Readable contrast','Touch-sized controls','Reduced motion','Meaningful chart labels','No interaction required for core understanding'],
  'responsive':['Desktop uses viewport width intelligently','Mobile is intentionally composed','No horizontal overflow','CTA remains obvious','Charts remain understandable','Dense pathway content becomes progressive rather than tiny'],
  'quality_gate':['Correctness','Visual quality','Human experience','Narrative flow','Personalization','Interaction','Brand coherence','Conversion','Mobile','Accessibility','Performance','Memorability'],
  'self_optimization':{
    'lesson':'Growing Lesson 001 — MAXESS Results 4.2',
    'loop':['OUTPUT','SCORE','WHAT WORKED','WHAT FAILED','ROOT CAUSE','CORRECTION','NEW RULE','TEST','VERIFY','REUSE'],
    'permanent_rules':['Technical completion is not product completion.','Do not confuse specification coverage with experience quality.','Design moments and rhythm before components.','Use NayaNET as a system benchmark, not merely a footer.','Ask Why is this not a 10? before release.','Known mistakes must not silently recur.'
  },
  'preservation':['Assessment architecture','Result Contract architecture','Scoring model','Five dimensions','18 AI areas','Naya architecture','Master Key','NayaNET Page Code','Validated CTA and destination wiring'],
  'release_truth':'The live experience is the product. A passing build is evidence of technical viability, not proof of excellence.'
}

blob='<script type="application/json" id="maxess-results-experience-manifest">'+json.dumps(MANIFEST,ensure_ascii=False,indent=2)+'</script>'
for p in FILES:
    text=p.read_text(encoding='utf-8')
    if 'maxess-results-experience-manifest' in text: continue
    text=text.replace('</body>',blob+'\n</body>',1)
    p.write_text(text,encoding='utf-8')
    print(p.name,len(text.splitlines()),len(text.encode()))
