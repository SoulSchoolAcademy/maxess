#!/usr/bin/env python3
"""Deterministically upgrades the existing MAXESS Groove artifact in-place.

This is an enhancement layer, not a replacement renderer. It downloads the
current artifact from the current Git ref, verifies it is the expected
MAXESS-RESULTS-AAA-GROOVE-EMBED.html, injects one versioned CSS/JS layer, and
writes the complete resulting artifact back to the same path.
"""
from __future__ import annotations

import base64
import json
import os
import re
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "SoulSchoolAcademy/maxess")
REF = os.environ.get("GITHUB_REF_NAME", "maxess-results-v22-aaa-execution")
PATH = "MAXESS-RESULTS-AAA-GROOVE-EMBED.html"
MARKER = "MAXESS_AAA_V22_EXECUTION_LAYER"
API = f"https://api.github.com/repos/{REPO}/contents/{PATH}?ref={REF}"
TOKEN = os.environ["GITHUB_TOKEN"]


def request(url: str, method: str = "GET", payload: bytes | None = None):
    req = urllib.request.Request(url, data=payload, method=method)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    data = request(API)
    if data.get("name") != PATH:
        raise RuntimeError(f"Wrong target returned: {data.get('name')!r}")
    raw = base64.b64decode(data["content"].replace("\n", "")).decode("utf-8")
    if "MAXESS_RESULT_10_10_BOOTSTRAP" not in raw or "window.MAXESS_RESULT" not in raw:
        raise RuntimeError("Target does not look like the real MAXESS Results artifact.")
    if MARKER in raw:
        print("V22 layer already present; no-op.")
        return

    css = r'''\n<style id="MAXESS_AAA_V22_EXECUTION_LAYER">
/* MAXESS V22 — AAA EXPERIENCE LAYER. Existing functionality remains underneath. */
#maxess-results-10{
  --aaa-radius:42px;
  --aaa-soft:rgba(255,255,255,.78);
  --aaa-line:rgba(255,255,255,.14);
  --aaa-hue:278;
  --aaa-accent:hsl(var(--aaa-hue) 92% 68%);
  --aaa-accent2:hsl(calc(var(--aaa-hue) + 28) 94% 72%);
  --aaa-shadow:0 28px 90px rgba(0,0,0,.32);
}
#maxess-results-10 .mx-section{
  isolation:isolate;
  border-top:1px solid rgba(255,255,255,.055);
  background:
    radial-gradient(ellipse 60% 45% at 12% 12%,rgba(166,108,255,.11),transparent 70%),
    radial-gradient(ellipse 55% 45% at 88% 78%,rgba(40,170,255,.065),transparent 70%),
    linear-gradient(180deg,rgba(255,255,255,.012),rgba(255,255,255,0));
}
#maxess-results-10 .mx-section:nth-of-type(even){
  background:
    radial-gradient(ellipse 65% 50% at 86% 12%,rgba(70,190,255,.10),transparent 70%),
    radial-gradient(ellipse 55% 45% at 14% 88%,rgba(198,74,255,.075),transparent 70%),
    linear-gradient(180deg,rgba(255,255,255,.028),rgba(255,255,255,.006));
}
#maxess-results-10 .mx-section.aaa-light-chapter{
  color:#101018;
  background:
    radial-gradient(ellipse 55% 55% at 15% 15%,rgba(166,108,255,.12),transparent 72%),
    radial-gradient(ellipse 45% 50% at 88% 85%,rgba(30,170,255,.10),transparent 72%),
    #fbf9ff;
}
#maxess-results-10 .aaa-section-inner{position:relative;z-index:2}
#maxess-results-10 .aaa-naya-whisper{
  display:flex;
  align-items:center;
  gap:12px;
  width:max-content;
  max-width:min(430px,100%);
  margin:0 0 24px auto;
  padding:8px 14px 8px 8px;
  border:1px solid rgba(255,255,255,.14);
  border-radius:999px 999px 999px 24px;
  background:rgba(12,8,20,.52);
  box-shadow:0 12px 34px rgba(0,0,0,.22),inset 0 1px rgba(255,255,255,.14);
  backdrop-filter:blur(16px);
}
#maxess-results-10 .aaa-naya-whisper img{
  width:42px;height:42px;flex:0 0 42px;border-radius:50%;object-fit:cover;
  border:2px solid rgba(255,255,255,.6);box-shadow:0 5px 18px rgba(0,0,0,.28)
}
#maxess-results-10 .aaa-naya-whisper b{display:block;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:#fff}
#maxess-results-10 .aaa-naya-whisper span{display:block;margin-top:2px;color:rgba(255,255,255,.72);font-size:12px;line-height:1.35}
#maxess-results-10 .aaa-light-chapter .aaa-naya-whisper{background:rgba(255,255,255,.78);border-color:rgba(30,20,50,.10);box-shadow:0 12px 34px rgba(80,50,120,.12)}
#maxess-results-10 .aaa-light-chapter .aaa-naya-whisper b{color:#17121e}
#maxess-results-10 .aaa-light-chapter .aaa-naya-whisper span{color:rgba(23,18,30,.68)}
#maxess-results-10 .mx-dim-grid{align-items:stretch}
#maxess-results-10 .mx-dim{
  position:relative;overflow:hidden;border-radius:42px 58px 46px 64px / 54px 44px 64px 50px;
  background:linear-gradient(145deg,rgba(255,255,255,.085),rgba(255,255,255,.018));
  box-shadow:inset 0 1px rgba(255,255,255,.10),0 18px 55px rgba(0,0,0,.18);
  transform:translateZ(0);
}
#maxess-results-10 .mx-dim:nth-child(2n){border-radius:58px 42px 64px 46px / 48px 60px 44px 64px}
#maxess-results-10 .mx-dim:nth-child(3n){border-radius:48px 68px 40px 58px / 66px 42px 60px 46px}
#maxess-results-10 .mx-dim::before{
  content:"";position:absolute;inset:12px;border-radius:inherit;padding:1px;
  background:conic-gradient(from -90deg,var(--aaa-dim-color,#b36cff) var(--aaa-dim-pct,50%),rgba(255,255,255,.035) 0);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;opacity:.75;pointer-events:none;
}
#maxess-results-10 .mx-dim::after{
  content:"";position:absolute;width:180px;height:180px;right:-80px;bottom:-90px;border-radius:50%;
  background:radial-gradient(circle,var(--aaa-dim-color,#b36cff),transparent 68%);opacity:.12;filter:blur(6px);pointer-events:none
}
#maxess-results-10 .mx-dim-head strong{font-size:34px}
#maxess-results-10 .mx-dim-head h3{font-size:18px}
#maxess-results-10 .mx-score-orb{
  background:
    radial-gradient(circle at 31% 23%,rgba(255,255,255,.34),transparent 9%),
    radial-gradient(circle at 50% 48%,hsla(var(--aaa-hue),85%,34%,.78),#13091e 48%,#05030a 76%,#020104 100%);
  box-shadow:0 0 0 1px rgba(255,255,255,.18),inset 0 0 90px hsla(var(--aaa-hue),90%,65%,.20),0 36px 110px rgba(0,0,0,.66),0 0 130px hsla(var(--aaa-hue),90%,62%,.28);
  animation:aaa-orb-breathe 5.5s ease-in-out infinite;
}
#maxess-results-10 .mx-score-orb::before{border-color:hsla(var(--aaa-hue),90%,78%,.36);box-shadow:0 0 55px hsla(var(--aaa-hue),90%,65%,.24);animation:aaa-ring 9s linear infinite}
#maxess-results-10 .mx-score-orb::after{border-color:hsla(calc(var(--aaa-hue) + 40),90%,80%,.12)}
@keyframes aaa-orb-breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.018)}}
@keyframes aaa-ring{to{transform:rotate(360deg)}}
#maxess-results-10 .mx-cta{border-radius:999px;box-shadow:0 12px 30px rgba(0,0,0,.22),inset 0 1px rgba(255,255,255,.55)}
#maxess-results-10 .mx-cta-primary{background:linear-gradient(135deg,hsl(var(--aaa-hue) 95% 80%),hsl(var(--aaa-hue) 70% 54%) 48%,hsl(calc(var(--aaa-hue) - 18) 72% 34%))}
#maxess-results-10 .mx-cta:hover{transform:translateY(-4px) scale(1.01)}
#maxess-results-10 .aaa-chapter-number{display:inline-flex;align-items:center;justify-content:center;width:42px;height:42px;border-radius:50%;margin-right:10px;color:#fff;font-size:11px;font-weight:900;letter-spacing:.08em;background:linear-gradient(145deg,hsl(var(--aaa-hue) 85% 66%),hsl(calc(var(--aaa-hue) + 35) 85% 58%));box-shadow:0 8px 24px hsla(var(--aaa-hue),80%,55%,.25)}
#maxess-results-10 .aaa-signal{display:inline-flex;align-items:center;gap:7px;margin-top:12px;padding:7px 11px;border-radius:999px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.10);font-size:10px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
#maxess-results-10 .aaa-signal i{width:7px;height:7px;border-radius:50%;background:var(--aaa-accent);box-shadow:0 0 12px var(--aaa-accent)}
#maxess-results-10 .mx-title,#maxess-results-10 .mx-section-head h2{ text-wrap:balance }
#maxess-results-10 .mx-copy,#maxess-results-10 .mx-section-head p{ text-wrap:pretty }
@media(max-width:900px){
  #maxess-results-10 .mx-hero-grid,#maxess-results-10 .mx-fingerprint{grid-template-columns:1fr}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  #maxess-results-10 .aaa-naya-whisper{margin-left:0}
}
@media(max-width:560px){
  #maxess-results-10 .mx-dim-grid{grid-template-columns:1fr}
  #maxess-results-10 .mx-score-orb{width:min(360px,88vw)}
  #maxess-results-10 .aaa-naya-whisper{width:100%;max-width:none}
  #maxess-results-10 .mx-proof{grid-template-columns:1fr}
}
@media(prefers-reduced-motion:reduce){
  #maxess-results-10 .mx-score-orb,#maxess-results-10 .mx-score-orb::before{animation:none}
}
@media print{
  #maxess-results-10 .aaa-naya-whisper{break-inside:avoid}
  #maxess-results-10 .mx-score-orb{animation:none;box-shadow:none}
}
</style>\n'''

    js = r'''\n<script id="MAXESS_AAA_V22_EXECUTION_SCRIPT">
(function(){
  "use strict";
  var root=document.getElementById("maxess-results-10");
  if(!root || root.getAttribute("data-maxess-aaa-v22")==="1") return;
  root.setAttribute("data-maxess-aaa-v22","1");
  var data=window.MAXESS_RESULT || {};
  var score=Number(data.overallScore ?? data.score ?? 0);
  if(Number.isFinite(score)){
    var hue;
    if(score<50) hue=18 + score/50*22;
    else if(score<65) hue=40 + (score-50)/15*18;
    else if(score<75) hue=58 + (score-65)/10*42;
    else if(score<85) hue=100 + (score-75)*5;
    else if(score<90) hue=150 + (score-85)*4;
    else if(score<95) hue=170 + (score-90)*13;
    else hue=235 + (score-95)*8;
    root.style.setProperty("--aaa-hue",String(Math.max(0,Math.min(315,hue))));
  }

  var nayaBlack="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg";
  var nayaWhite="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20white.jpg";
  var whispers=[
    "I'm here to help you see what your score is really telling you.",
    "Let's turn the number into something useful — something you can actually use.",
    "These are your strengths. Notice what you already do exceptionally well.",
    "Now let's look at the one area where a little growth can create a lot of leverage.",
    "This is your capability fingerprint — five parts of one system, working together.",
    "Your pattern matters because strengths become more powerful when they connect.",
    "Here's the part I'd pay attention to next. Small improvements can compound.",
    "You don't need to become perfect. You need to know your next best move.",
    "These are doors you can open with AI. Start where your strengths give you momentum.",
    "I'm with you. The goal isn't more AI — it's better results from the AI you already have."
  ];

  var sections=Array.prototype.slice.call(root.querySelectorAll(".mx-section"));
  sections.forEach(function(section,i){
    if(section.querySelector(".aaa-naya-whisper")) return;
    var head=section.querySelector("h2,h1,h3");
    var text=(head?head.textContent:"section").trim().toLowerCase();
    var light=(i%4===1 || /means|strength|advantage|next move/i.test(text));
    if(light) section.classList.add("aaa-light-chapter");
    var wrap=section.querySelector(":scope > .mx-wide, :scope > .mx-wrap, :scope > .mx-reading") || section.firstElementChild;
    if(!wrap) return;
    var note=whispers[Math.min(i,whispers.length-1)];
    if(/dimension/i.test(text)) note=whispers[4];
    if(/pattern/i.test(text)) note=whispers[5];
    if(/lever|opportunity/i.test(text)) note=whispers[6];
    if(/next/i.test(text)) note=whispers[7];
    if(/master|pathway/i.test(text)) note=whispers[8];
    if(/playground|naya/i.test(text)) note=whispers[9];
    var el=document.createElement("div");
    el.className="aaa-naya-whisper";
    el.innerHTML='<img src="'+(light?nayaWhite:nayaBlack)+'" alt="Naya" loading="lazy" width="42" height="42"><div><b>Naya</b><span>'+note+'</span></div>';
    wrap.insertBefore(el,wrap.firstChild);
    var num=document.createElement("span");
    num.className="aaa-chapter-number";
    num.textContent=String(i+1).padStart(2,"0");
    if(head && !head.querySelector(".aaa-chapter-number")) head.insertBefore(num,head.firstChild);
  });

  var dims=Array.prototype.slice.call(root.querySelectorAll(".mx-dim"));
  dims.forEach(function(card,i){
    var strong=card.querySelector(".mx-dim-head strong");
    var n=strong?parseFloat((strong.textContent||"").replace(/[^0-9.]/g,"")):NaN;
    if(Number.isFinite(n)){
      card.style.setProperty("--aaa-dim-pct",Math.max(0,Math.min(100,n))+"%");
      var colors=["#ff6048","#ffd54a","#4de39b","#48cfff","#9f70ff"];
      card.style.setProperty("--aaa-dim-color",colors[i%colors.length]);
    }
  });

  var orb=root.querySelector(".mx-score-orb");
  if(orb) orb.setAttribute("aria-label","MAXESS AI Score: "+(Number.isFinite(score)?score:"not available"));

  // Never silently invent a production score. The enhancement layer only reads the existing contract.
  if(!window.MAXESS_RESULT){ root.setAttribute("data-maxess-v22-no-result","1"); }
})();
</script>\n'''

    if "</head>" not in raw or "</body>" not in raw:
        raise RuntimeError("Target HTML is structurally incomplete: missing head/body close tags.")
    updated = raw.replace("</head>", css + "</head>", 1)
    updated = updated.replace("</body>", js + "</body>", 1)
    if len(updated) <= len(raw) + 1000:
        raise RuntimeError("AAA patch unexpectedly produced a tiny change.")

    encoded = base64.b64encode(updated.encode("utf-8")).decode("ascii")
    payload = json.dumps({
        "message": "MAXESS V22: execute AAA visual/personalization upgrade",
        "content": encoded,
        "sha": data["sha"],
        "branch": REF,
    }).encode("utf-8")
    result=request(f"https://api.github.com/repos/{REPO}/contents/{PATH}","PUT",payload)
    print(json.dumps({
        "path":PATH,"ref":REF,"old_sha":data["sha"],
        "new_sha":result.get("content",{}).get("sha"),
        "commit":result.get("commit",{}).get("sha"),
        "bytes_before":len(raw.encode()),"bytes_after":len(updated.encode()),
        "delta_bytes":len(updated.encode())-len(raw.encode()),
        "marker":MARKER
    },indent=2))

if __name__=="__main__":
    main()
