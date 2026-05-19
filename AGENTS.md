# sarah-rodovalho-site — Agent Context

Loaded automatically by Claude/Cursor/Cline/Aider (2025-2026 convention). **Read this before making changes.**

This file holds the **operating principles** for any AI agent working in this repo. For project state, stack, commands, and the "where to look first" map, read [`CLAUDE.md`](./CLAUDE.md) — that's the dense source of truth.

## Two-layer doc structure

- **Root `AGENTS.md` (this file):** harness engineering principles, operating rules, guardrails.
- **Root `CLAUDE.md`:** project state, stack, content discipline, PII boundary, file structure.
- **`docs/site-reviews/*.md`:** session-by-session implementation plans (e.g., `2026-05-18-onenote-ajustes.md` v2).
- **`docs/runbooks/*.md`** (when added): operational recipes (Cloudflare Access setup, watermark regen, etc.).

If anything here conflicts with `CLAUDE.md`, follow `CLAUDE.md` — it's closer to the code.

## What this is

Personal/professional site for **Sarah F. Rodovalho** — Integrated Design Manager at Aligned Data Centers + doctoral researcher at Harrisburg University. Strategic frame per ADR-023 in the `rodovalho-finance` parent repo: independently-citable surface that amplifies the discoverability of her published work + recognition. Live at https://sarahrodovalho.com/ behind Cloudflare. A gated `/admin/*` layer behind Cloudflare Zero Trust Access (Email OTP, single-email allowlist) hosts back-of-house content.

**Stack:** Astro 6.3 + Tailwind v4 + MDX + TypeScript 6 + Biome 2.4 + Cloudflare Workers Static Assets (`wrangler.toml` `[assets]` + `worker.js`). pnpm package manager (locked). No backend, no database, no analytics — static-only.

**Sibling sites:** `vitormr.dev` (Vitor's site) shares stack + many patterns. Both sit behind separate Cloudflare configurations. `orenu.vitormr.dev` is the family fintech (Next.js, separate repo). Architectural conventions are coordinated across the 3 repos.

## Harness engineering principles (adopted 2026-05-19)

Anchored on Anthropic's three engineering posts:
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) (2024)
- [Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Nov 2025)
- [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (Mar 2026)

**1. Workflow first, agent second.** Most edits in this repo are deterministic (copy edit, MDX update, callout swap, photo replace). Reserve agentic flow for design-language calls (logo wording, voice review, layout tradeoff) — and even those should be framed as "recommendation + tradeoffs", not "A or B?".

**2. Context is finite.** Don't load the entire 688-line `docs/site-reviews/2026-05-18-onenote-ajustes.md` v2 wholesale into context. Index it by section (the TOC + Index table at the top), then read the specific section being touched. Same for long MDX bodies — read frontmatter first, then the prose block being edited.

**3. Persist outside the model.** State lives in: git commits (single source of truth), `docs/site-reviews/*.md` (session-specific implementation plans), and the user-level memory dir referenced from `rodovalho-finance`. Old session detail → handoff docs under `docs/site-reviews/`. Don't re-derive — read.

**4. Validate, don't trust.** Every completion claim must be proven:
```bash
pnpm exec astro check    # typecheck — 0 errors, 0 warnings, 0 hints
pnpm exec biome check    # lint + format
pnpm build               # builds 15 pages currently — verify count if a page is added/removed
```
- The pre-commit PII scan (`scripts/pii-scan.sh` via husky hook) blocks USCIS receipt numbers, SSN/CPF, etc. WARN-level patterns (currency) are allowed.
- CI runs the same 3 commands plus the PII scan + dependency audit. All 5 must be green to merge.

**5. Defense-in-depth markers ≠ enforcement.** *Critical operational lesson, 2026-05-19.* The PR-S07b admin layer shipped with `noIndex` BaseLayout prop, sitemap exclusion, `robots.txt Disallow: /admin/`. None of those gate the URL — they're crawler guidelines. The real gate is the Cloudflare Zero Trust Access app configured in the dashboard. For any "gated" route claim, **verify with `curl -I <url>` from an anonymous shell** (no cookies, no `CF_Authorization`). Expected: HTTP 302 → `https://orenu.cloudflareaccess.com/cdn-cgi/access/login/...`. Anything else (200 with content) = not gated. PR description claims and code comments are not evidence; curl is.

**6. Workers Static Assets bypass the Worker by default.** When `main = worker.js` co-exists with `[assets] directory = dist/`, matched asset paths skip the Worker handler unless `run_worker_first = true` is set in `wrangler.toml`. The `www → apex` 301 (and any other Worker-side logic like `/work → /experience`) requires this flag. Test post-deploy with anonymous curl on both `www.` and apex.

**7. Plan for context reset.** Session-end ritual:
1. Update or close any open PR / branch.
2. Add a session-close annotation to the active `docs/site-reviews/*-handoff.md` if substantial work happened.
3. Refresh `project_open_actions.md` (in the `rodovalho-finance` memory dir) to reflect cross-repo state.

The next session reads the handoff doc + project_open_actions and picks up cold.

**8. The ACI is the design.** Aesthetic discipline:
- Marina Mogilko-inspired typography (serif logo, anchor nav, social-icon row)
- Warm-stone palette in `src/styles/global.css` (distinct from Vitor's vitormr-site cool-blue)
- Double-bezel containers, eyebrow tags, generous whitespace
- HTML-native interactions (no client JS unless absolutely required — e.g., theme toggle uses vanilla details/summary)
- Watermark layer (`WatermarkLayer.astro`) + embedded watermarks on slide assets (`scripts/watermark-images.py`, idempotent)

**9. Guardrails in layers:**
- **PII boundary** (per CLAUDE.md): pre-commit regex blocks receipt numbers, SSN/CPF, home address, phone, salary, family detail. Allowed: name, role, employer, public talks, professional email.
- **OPSEC discipline:** legal name "Sarah Faria Alcantara Macedo Rodovalho" lives only behind CF Access (`/admin/press-kit-full`). Public surface uses "Sarah Rodovalho" only.
- **Sarah voice gating:** every public-facing copy edit goes through Sarah review (test plan item, not optional). Voice ownership is non-negotiable — bias toward "draft, then ask" rather than "ship, then iterate".
- **Audit:** material decisions become ADRs in the `rodovalho-finance/decisions/` directory (the parent repo), not here.

## Conventions (enforced)

1. **Commit trailer:** `Assisted-By: Claude (Anthropic) <noreply@anthropic.com>` on every commit. **NEVER `Co-Authored-By: Claude…`** — same convention as `rodovalho-finance` (ADR-010).
2. **Decision framing:** "recommendation + why + tradeoffs", not "A or B?". User makes the call after seeing the framing.
3. **Content discipline:** every public claim must be independently verifiable (DOI link, Scholar URL, Harrisburg `.edu` page, conference recording). No marketing puffery.
4. **Language:** English primary. PT secondary deferred to v2.

## Validation gates (mandatory before merge to `main`)

```bash
pnpm exec astro check    # typecheck
pnpm exec biome check    # lint + format
pnpm build               # 15 pages — verify count if pages added/removed
# Pre-commit hook also runs scripts/pii-scan.sh
```

After merge, `Cloudflare Workers Builds` auto-deploys `main` → `https://sarahrodovalho.com/`. The integration status check on PR is sticky on the merge commit and may not update — verify production with `curl -I` instead of waiting for the GitHub check to flip.

## When to consult external sources

- Plan v2 `docs/site-reviews/2026-05-18-onenote-ajustes.md` — canonical source for the current Sarah-review batch
- `CLAUDE.md` — stack details, PII regex, file structure
- ADR-023 in `rodovalho-finance/decisions/` — strategic frame
- ADR-024 / ADR-024.1 — Orenu source-of-truth for publications / engagements / awards (auto-PR build-time pattern)
- Astro 6 docs (`https://docs.astro.build`) when touching Content Layer, Image Service, or new integration
- Cloudflare Workers Static Assets docs when touching `wrangler.toml` `[assets]` or `worker.js`
- Cloudflare Access docs when touching `/admin/*` gate
- **Do not search "how to fix [error]" before checking the current branch's site-review doc + git log first.**

---

*Initial adoption: 2026-05-19. Complements `CLAUDE.md` (project state) and the parent repo's `rodovalho-finance/AGENTS.md`.*
