// Usage: node save-plan.mjs <plan.md>
// Parses markdown with the tracker's own importer and writes data/plans/<id>.json (never overwrites).
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const TRACKER = process.env.PLAN_TRACKER || path.join(os.homedir(), 'selfhost/plan-tracker');
const { parseMarkdown } = await import(path.join(TRACKER, 'server/markdownImport.js'));

const src = process.argv[2];
if (!src) { console.error('usage: node save-plan.mjs <plan.md>'); process.exit(1); }

const plan = parseMarkdown(fs.readFileSync(src, 'utf8'));
const dir = path.join(TRACKER, 'data/plans');
fs.mkdirSync(dir, { recursive: true });

const base = plan.id.slice(0, 60);
let id = plan.id;
for (let n = 2; fs.existsSync(path.join(dir, `${id}.json`)); n++) id = `${base}-${n}`;
plan.id = id;

const file = path.join(dir, `${id}.json`);
fs.writeFileSync(file, JSON.stringify(plan, null, 2) + '\n');

let items = 0;
for (const p of plan.phases) for (const m of p.modules) items += m.items.length;
console.log(`Saved ${file}\n${plan.phases.length} sections, ${items} items. Open http://localhost:4321`);
