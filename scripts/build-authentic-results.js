const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const towerPath = path.join(root, 'MAXESS-RESULTS-AUTHENTIC-TOWER.html');
const nayaPath = path.join(root, 'nayanetpagecode');
const outPath = path.join(root, 'MAXESS-RESULTS-AUTHENTIC-TOWER-BUILT.html');

const tower = fs.readFileSync(towerPath, 'utf8');
const raw = fs.readFileSync(nayaPath, 'utf8');
let naya = raw;
try { naya = JSON.parse(raw).content || raw; } catch (_) {}

const mount = '<div id="nayanet-source-mount" aria-label="NayaNET ground floor"></div>';
if (!tower.includes(mount)) throw new Error('Expected NayaNET mount was not found in tower source.');

let built = tower.replace(mount, `<!-- NAYANET GROUND FLOOR: canonical source, inlined at build time -->\n${naya}`);

const fetchStart = 'const mount=$(\'nayanet-source-mount\');';
const fetchIndex = built.indexOf(fetchStart);
if (fetchIndex !== -1) {
  const scriptEnd = built.indexOf('\n})();', fetchIndex);
  if (scriptEnd === -1) throw new Error('Could not locate tower runtime boundary.');
  const fetchOnly = built.slice(fetchIndex, scriptEnd);
  const cut = fetchOnly.indexOf("const mount=$('nayanet-source-mount');");
  if (cut !== -1) built = built.slice(0, fetchIndex) + built.slice(fetchIndex, fetchIndex + cut) + built.slice(scriptEnd);
}

fs.writeFileSync(outPath, built, 'utf8');
console.log(`Built ${path.relative(root, outPath)} from MAXESS tower + canonical nayanetpagecode.`);
