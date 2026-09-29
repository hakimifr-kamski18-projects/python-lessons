// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { readdirSync, readFileSync } from 'node:fs';
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

/**
 * The unit folders are read from the content directory rather than listed
 * here, so the sidebar cannot drift out of step with the course. Each unit's
 * display name comes from the title in its own lesson.md.
 */
const CONTENT = './src/content/docs';

/**
 * Short forms for the sidebar, where the full lesson title would wrap. Units
 * missing from this map fall back to their lesson.md title, so adding a unit
 * still works without touching this file.
 */
const SHORT_NAMES = {
  '00-setup': 'Setup',
  '01-values-and-variables': 'Values and variables',
  '02-text-and-input': 'Text and input',
  '03-decisions': 'Making decisions',
  '04-repetition': 'Repetition',
  '05-lists': 'Lists',
  '06-functions': 'Functions',
  '07-dicts-and-tuples': 'Dictionaries',
  '08-files-and-errors': 'Files and errors',
  '09-modules-and-beyond': 'Modules',
};

function unitName(dir) {
  if (SHORT_NAMES[dir]) {
    return SHORT_NAMES[dir];
  }
  try {
    const lesson = readFileSync(`${CONTENT}/${dir}/lesson.md`, 'utf8');
    const match = lesson.match(/^title:\s*(.+)$/m);
    if (match) {
      return match[1].trim().replace(/^Unit \d+\s*[—-]\s*/, '');
    }
  } catch {
    // No lesson.md, fall back to the folder name.
  }
  return dir;
}

const units = readdirSync(CONTENT, { withFileTypes: true })
  .filter((entry) => entry.isDirectory() && /^\d\d-/.test(entry.name))
  .map((entry) => entry.name)
  .sort();

/**
 * GitHub Pages deploys a project site under a path, so both of these are set
 * by the deploy workflow. Locally they are left unset, which means the dev
 * server serves from / and you do not have to remember a prefix.
 */
const site = process.env.SITE_URL || undefined;
const base = process.env.BASE_PATH || undefined;

/**
 * Put the base path in front of every internal link in the built HTML.
 *
 * Astro applies `base` to the assets it generates and Starlight does the same
 * for its navigation, but a link written by hand as `/cheat-sheets/glossary/`
 * is left exactly as written. On a project site served from
 * `/repository-name/` that means it 404s, which is what happened here.
 *
 * Doing it to the finished HTML rather than to the markdown has two advantages.
 * It catches everything, including links in frontmatter such as the hero
 * buttons on the home page and links inside .astro pages, and it does not
 * depend on the markdown processor's plugin API.
 *
 * Links left alone: external ones, protocol-relative ones, in-page anchors, and
 * anything already carrying the base path.
 */
function applyBaseToLinks() {
  const prefix = !base || base === '/' ? '' : `/${base.replace(/^\/+|\/+$/g, '')}`;

  return {
    name: 'apply-base-to-links',
    hooks: {
      'astro:build:done': async ({ dir }) => {
        if (!prefix) return;

        // Only root-relative URLs are touched, and only once: Astro has
        // already prefixed its own assets, so anything that already starts
        // with the prefix has to be left alone.
        const rewrite = (html) =>
          html.replace(/(href|src)="(\/[^"]*)"/g, (whole, attr, url) => {
            if (url.startsWith('//')) return whole; // protocol-relative
            if (url === prefix || url.startsWith(`${prefix}/`)) return whole;
            return `${attr}="${prefix}${url}"`;
          });

        let pages = 0;
        const walk = async (folder) => {
          for (const entry of await readdir(folder, { withFileTypes: true })) {
            const full = join(folder, entry.name);
            if (entry.isDirectory()) {
              await walk(full);
            } else if (entry.name.endsWith('.html')) {
              const before = await readFile(full, 'utf8');
              const after = rewrite(before);
              if (after !== before) {
                await writeFile(full, after);
                pages += 1;
              }
            }
          }
        };

        await walk(fileURLToPath(dir));
        console.log(`[apply-base-to-links] prefixed internal links in ${pages} pages with ${prefix}/`);
      },
    },
  };
}

export default defineConfig({
  site,
  base,

  // Nothing to configure here, and the floating toolbar is just noise when you
  // are showing the site to someone.
  devToolbar: { enabled: false },

  integrations: [
    applyBaseToLinks(),
    starlight({
      title: 'Python from Zero',
      description:
        'A beginner course in Python, for people who have never written a line of code.',

      sidebar: [
        {
          label: 'Units',
          items: units.map((dir) => ({
            label: `${dir.slice(0, 2)} · ${unitName(dir)}`,
            items: [{ autogenerate: { directory: dir } }],
          })),
        },
        {
          label: 'Reference',
          items: [{ autogenerate: { directory: 'cheat-sheets' } }],
        },
      ],
    }),
  ],
});
