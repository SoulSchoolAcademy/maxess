const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const towerPath = path.join(root, 'MAXESS-RESULTS-AUTHENTIC-TOWER.html');
const nayaPath = path.join(root, 'nayanetpagecode');
const enhancementCssPath = path.join(root, 'knowledge', 'results-experience-aaa-enhancements.css');
const enhancementJsPath = path.join(root, 'knowledge', 'results-experience-aaa-enhancements.js');
const outDir = path.join(root, 'current-ui');
const outPath = path.join(outDir, 'MAXESS-RESULTS.html');

const tower = fs.readFileSync(towerPath, 'utf8');
const raw = fs.readFileSync(nayaPath, 'utf8');
const enhancementCss = fs.readFileSync(enhancementCssPath, 'utf8');
const enhancementJs = fs.readFileSync(enhancementJsPath, 'utf8');
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

if (!built.includes('results-experience-aaa-enhancements')) {
  built = built.replace('</style>', `\n/* results-experience-aaa-enhancements */\n${enhancementCss}\n</style>`);
  built = built.replace('</body>', `\n<!-- MAXESS AAA enhancement runtime -->\n<script>${enhancementJs}</script>\n</body>`);
}

fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(outPath, built, 'utf8');
console.log(`Built ${path.relative(root, outPath)} from MAXESS tower + canonical nayanetpagecode + AAA enhancement layer.`);
