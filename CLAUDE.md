# Project: sarah-rodovalho-site

**Mission**: Personal/professional site for Sarah F. Rodovalho, sustainable design + construction management researcher at Harrisburg University. Strategic frame: independently-citable surface that amplifies the discoverability of her published work + recognition. Per ADR-023 in the `rodovalho-finance` parent repo (private).

## Stack

- Astro 6.3 + Tailwind v4 + MDX + TypeScript 6.0 + Biome 2.4
- Cloudflare Pages deployment (PR-S05+ ties domain `sarahrodovalho.com`)
- pnpm package manager (locked)

## Conventions

- **Commit trailer**: `Assisted-By: Claude (Anthropic) <noreply@anthropic.com>` on every assisted commit. **NEVER** `Co-Authored-By: Claude…`. (Same convention as Orenu / `rodovalho-finance`.)
- **Author of record**: Vitor Maia Rodovalho (technical maintainer) + Sarah Faria Alcantara Macedo Rodovalho (content authority).
- **Content discipline**: every claim on the site must be independently verifiable (DOI link, Scholar URL, Harrisburg `.edu` page, conference recording, etc.). No marketing puffery, no recommendation framing.
- **PII boundary** (enforced via pre-commit hook in PR-S02):
  - **Allowed**: name, professional headshot, role, employers (when public), affiliations, public talks/papers, LinkedIn URL, Scholar URL, professional email
  - **Blocked**: USCIS receipt numbers (`[A-Z]{3}\d{10}`), case status/details, attorney communications, home address, phone, salary, SSN/ITIN/CPF, bank/brokerage details, health info
- **Language**: English primary. PT secondary deferred to v2 if BR network engagement justifies.

## File structure

- `src/pages/` — Astro routes (`index.astro`, `about.astro`, etc.)
- `src/layouts/BaseLayout.astro` — site-wide HTML wrapper with Schema.org markup
- `src/content/` — MDX content collections (schemas in `src/content.config.ts`)
- `src/styles/global.css` — Tailwind v4 config + design tokens
- `public/` — static assets (favicon, images, downloads)
- `astro.config.mjs` — Astro + adapters config
- `biome.json` — lint + format config

## Sources of truth (read these for content drops)

- Sarah's Scholar profile: https://scholar.google.com/citations?user=3s1M4TIAAAAJ
- Affiliation: Harrisburg University of Science and Technology (verified `.edu`)
- Published byline: `S Rodovalho` (encoded in BaseLayout `Person.alternateName`)
- ADR-023 in `rodovalho-finance/decisions/` for strategic context, content architecture, section list, integration patterns

## CI gates (GitHub Actions)

- `pnpm install --frozen-lockfile`
- `pnpm typecheck` (astro check)
- `pnpm check:ci` (biome check, no fixes)
- `pnpm build` (astro build to ./dist)

## Out of scope

- Vitor's own site (`vitormr.dev`) — separate repo, separate decisions, deferred until Sarah MVP ships.
- Orenu integration — eventual publish-gated feed pattern (per ADR-023 §D5); v1 = manual MDX content drops only.
