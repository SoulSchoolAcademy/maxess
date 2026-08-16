from pathlib import Path
import re

path = Path('code')
source = path.read_text(encoding='utf-8')
marker = 'MAXESS_9_5_CROSS_DOMAIN_HANDOFF'

if marker in source:
    print('Assessment handoff already installed.')
    raise SystemExit(0)

pattern = re.compile(r'function finishInterestSelection\(\)\{.*?\n\}', re.S)
replacement = r'''/* MAXESS_9_5_CROSS_DOMAIN_HANDOFF */
function finishInterestSelection(){

  DOM.interestsView.classList.remove(
    "visible"
  );

  /* Naya Law: the assessment remains the scoring authority.
     Results receives the completed result through an explicit
     cross-domain contract rather than shared browser storage. */
  const results = calculateResults();
  const payload = {
    version: "MAXESS-RESULTS-CONTRACT-1",
    assessmentId: "ai-max",
    assessmentVersion: "MAXESS-1.0",
    completed: true,
    overall: results.overall,
    dimensions: Object.fromEntries(
      results.dimensions.map(
        dimension => [dimension.id, dimension.score]
      )
    ),
    strongest: [...results.dimensions]
      .sort((a,b)=>b.score-a.score)[0]?.id || null,
    opportunity: [...results.dimensions]
      .sort((a,b)=>a.score-b.score)[0]?.id || null,
    responses: state.responses,
    selectedInterests: [...state.selectedInterests],
    completedAt: new Date().toISOString()
  };

  const bytes = new TextEncoder().encode(JSON.stringify(payload));
  let binary = "";
  bytes.forEach(byte => binary += String.fromCharCode(byte));

  const encoded = btoa(binary)
    .replace(/\+/g,"-")
    .replace(/\//g,"_")
    .replace(/=+$/g,"");

  window.location.assign(
    "https://results.nayanet.xyz/?result=" +
    encodeURIComponent(encoded)
  );
}'''

patched, count = pattern.subn(replacement, source, count=1)
if count != 1:
    raise SystemExit('Could not locate finishInterestSelection() for the controlled handoff patch.')

path.write_text(patched, encoding='utf-8')
print('Installed MAXESS cross-domain Results handoff.')
