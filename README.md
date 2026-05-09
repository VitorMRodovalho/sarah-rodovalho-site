# sarahrodovalho.com

Personal site of Sarah F. Rodovalho — sustainable design and construction management researcher at Harrisburg University of Science and Technology.

## Stack

- **Astro 6.3** (static site generator; zero JS by default)
- **Tailwind CSS v4** (CSS-first config)
- **MDX** for rich content authoring (research papers, future essays)
- **TypeScript 6.0** strict mode
- **Biome 2.4** for lint + format
- **Cloudflare Pages** for deployment via `@astrojs/cloudflare` adapter

## Local development

Requires Node 22+ and pnpm 10+.

```bash
pnpm install
pnpm dev          # local dev server on :4321
pnpm build        # produces ./dist
pnpm preview      # serves ./dist locally
pnpm typecheck    # astro check
pnpm check:ci     # biome check (no fixes)
```

## Decisions

Strategic frame and stack rationale: see `decisions/ADR-023` in the parent project repository (`rodovalho-finance`, private). Site is a public independently-citable surface; not standalone immigration evidence.

## Maintenance

- Dependencies: pnpm + lockfile + Dependabot (alerts via GitHub for public repo)
- Content updates: edit MDX in `src/content/` (collections schema in `src/content.config.ts` once added in PR-S04)
- Deploy: auto via Cloudflare Pages on push to `main`

## License

Content (text, photos, research summaries) © Sarah F. Rodovalho. All rights reserved.
Code (Astro components, build configuration) is incidental to the content; no separate license file. Reuse with attribution welcome via direct contact.
