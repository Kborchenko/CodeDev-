import { copyFile, mkdir } from 'node:fs/promises';

const files = [
  'about-ai.webp',
  'about-crm.webp',
  'about-integrations.webp',
  'about-web.webp',
  'code-digital-face.webp',
  'codedev-mark.svg',
  'codedev-favicon.png',
  'codedev-social.jpg',
  'codedev-social-cd-v2.png',
  'codedev-touch.png',
  'process-development.webp',
  'process-discovery.webp',
  'process-launch.webp',
  'process-plan.webp',
  'team-ai-hands.jpg',
];

await mkdir('dist/assets', { recursive: true });
for (const file of files) await copyFile(`assets/${file}`, `dist/assets/${file}`);
await mkdir('dist/assets/fonts', { recursive: true });
for (const file of ['Revolution Gothic Regular.ttf', 'Revolution Gothic Bold.ttf', 'Revolution Gothic ExtraBold.ttf']) {
  await copyFile(`assets/fonts/${file}`, `dist/assets/fonts/${file}`);
}
await copyFile('CNAME', 'dist/CNAME');
await copyFile('agreement.html', 'dist/agreement.html');
