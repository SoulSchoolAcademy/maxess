import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';

const html = await readFile('MAXESS-RESULTS-PRIME-NAYA-10.html', 'utf8');
const server = createServer((req, res) => {
  if (req.url === '/results' || req.url?.startsWith('/results?')) {
    res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
    res.end(html);
    return;
  }
  res.writeHead(404); res.end('not found');
});
await new Promise(resolve => server.listen(4173, '127.0.0.1', resolve));

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
const errors = [];
page.on('console', msg => { if (msg.type() === 'error') errors.push(`console: ${msg.text()}`); });
page.on('pageerror', err => errors.push(`pageerror: ${err.message}`));

await page.goto('http://127.0.0.1:4173/results?demo=1', { waitUntil: 'load' });
await page.waitForSelector('#mx-radar');

const checks = await page.evaluate(() => ({
  title: document.title,
  score: document.querySelector('.mx-score')?.textContent?.trim(),
  dimensions: document.querySelectorAll('.mx-dim').length,
  areas: document.querySelectorAll('.mx-area').length,
  masters: document.querySelectorAll('.mx-master').length,
  canvas: !!document.querySelector('#mx-radar'),
  videoSlot: !!document.querySelector('#mx-video-slot'),
  membershipCards: document.querySelectorAll('.mx-offer').length,
  primaryMembershipLinks: [...document.querySelectorAll('.mx-action.primary')].length,
  iframes: document.querySelectorAll('iframe').length,
  legacyRoyal: !!document.querySelector('#royal-results-995'),
  legacyM9: !!document.querySelector('#m9-results'),
  resultContract: !!window.MAXESS_NAYA_CONTEXT,
  overall: window.MAXESS_RESULTS_DATA?.overall,
  strongest: window.MAXESS_NAYA_CONTEXT?.strongest,
  opportunity: window.MAXESS_NAYA_CONTEXT?.opportunity
}));

const failures = [];
if (checks.title !== 'MAXESS — Your AI Mastery Results') failures.push('wrong document title');
if (checks.score !== '82/100') failures.push(`unexpected demo score: ${checks.score}`);
if (checks.dimensions !== 5) failures.push(`expected 5 dimensions, got ${checks.dimensions}`);
if (checks.areas !== 18) failures.push(`expected 18 AI areas, got ${checks.areas}`);
if (checks.masters !== 3) failures.push(`expected 3 Naya master roles, got ${checks.masters}`);
if (!checks.canvas) failures.push('radar canvas missing');
if (!checks.videoSlot) failures.push('video slot missing');
if (checks.membershipCards !== 1) failures.push(`expected one membership card, got ${checks.membershipCards}`);
if (checks.primaryMembershipLinks !== 1) failures.push(`expected one primary membership action, got ${checks.primaryMembershipLinks}`);
if (checks.iframes !== 0) failures.push('iframe detected');
if (checks.legacyRoyal || checks.legacyM9) failures.push('legacy Results layer detected');
if (!checks.resultContract) failures.push('MAXESS_NAYA_CONTEXT was not created');
if (checks.overall !== 82) failures.push(`Result Contract overall mismatch: ${checks.overall}`);
if (checks.strongest !== 'communication') failures.push(`strongest mismatch: ${checks.strongest}`);
if (checks.opportunity !== 'systems') failures.push(`opportunity mismatch: ${checks.opportunity}`);
if (errors.length) failures.push(...errors);

await browser.close();
server.close();

console.log(JSON.stringify({ checks, failures }, null, 2));
if (failures.length) process.exit(1);
console.log('PRIME NAYA RESULTS SMOKE TEST: PASS');
