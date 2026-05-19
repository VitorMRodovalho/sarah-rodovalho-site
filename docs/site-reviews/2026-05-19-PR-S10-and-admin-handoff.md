# Session handoff — 2026-05-19 close (PR-S10 + admin emergency seal)

> Continues `2026-05-18-PR-S10-handoff.md`. This handoff doc closes the 2026-05-19 session and seeds the next one.

## What landed today

| PR | Commit on main | Status |
|---|---|---|
| **PR #50 — hotfix(worker): seal /admin/* with 403** | `58ea918` (squash from `f0bf554`) | ✅ Merged + auto-deploy presumed; worker version `16881aee` confirmed live |
| **PR-S10** — Work→Experience merge + photo flip + entity sweep | `86d5f22` on `feat/s10-work-experience-merge` (pushed) | 🚧 **Branch only — PR not yet opened.** Conflicts with main `worker.js` (admin gate). Rebase before opening. |

## Emergency context (read first)

At ~04:40 UTC during PR-S10 verification, Vitor opened an incognito tab and reported `/admin/` loaded without a CF Access challenge. Anonymous `curl -I` from this terminal confirmed:

```
HTTP/2 200
cf-cache-status: HIT
```

…on all of:

- `https://sarahrodovalho.com/admin/`
- `https://sarahrodovalho.com/admin/press-kit-full/` (legal name + bios long + hi-res URLs in body)
- `https://sarahrodovalho.com/admin/newsletter/`
- `https://sarahrodovalho.com/admin/press/sarah-rodovalho-headshot.jpg` (1493×1506, 272KB)
- `https://sarahrodovalho.com/admin/press/sarah-rodovalho-full-body.png` (1.45MB)

**Root cause hypothesis** (not yet confirmed by Zero Trust dashboard inspection): PR-S07b shipped admin Astro pages with defense-in-depth markers (`noIndex` meta, sitemap exclusion, `robots.txt` Disallow), but the Cloudflare Access application that was supposed to gate `/admin/*` at the edge was either never created, was disabled, or its policy/host/path matcher did not include `sarahrodovalho.com/admin/*`. `wrangler.toml` carries no Access binding (Access is dashboard-only, never wrangler-side).

The line in `project_open_actions.md` saying "Vitor configurou CF Access policy `sarahrodovalho.com/admin/*` Email OTP" was either premature or the policy was misconfigured — either way, anonymous browsing succeeded against production for ~28 hours after PR-S07b merge.

## What the seal does

`worker.js` post-merge:

```js
if (url.pathname === "/admin" || url.pathname.startsWith("/admin/")) {
  return new Response(
    "Restricted area.\n\nThis space is being reconfigured. Contact sarah@sarahrodovalho.com for access.\n",
    {
      status: 403,
      headers: {
        "content-type": "text/plain; charset=utf-8",
        "cache-control": "no-store, max-age=0, must-revalidate",
        "x-robots-tag": "noindex,nofollow",
      },
    },
  );
}
```

Pairs with `run_worker_first = true` in `wrangler.toml` (load-bearing — without it, matched static assets bypass the Worker entirely).

Post-deploy verified (5 URLs above + sanity on `/` and `/about/`):
- All 5 `/admin/*` paths → **HTTP 403** with `cache-control: no-store`
- Home `/` + `/about/` → **HTTP 200** (non-admin traffic unaffected)

## Pending — user action required

1. **Cloudflare cache purge of `/admin/*` URLs** (defense-in-depth — the worker already intercepts via `run_worker_first`, but purge clears any stale 200s in edge cache). Path: CF dashboard → `sarahrodovalho.com` zone → Caching → Configuration → Purge Cache → Custom URLs. Paste these 5:
   ```
   https://sarahrodovalho.com/admin/
   https://sarahrodovalho.com/admin/press-kit-full/
   https://sarahrodovalho.com/admin/newsletter/
   https://sarahrodovalho.com/admin/press/sarah-rodovalho-headshot.jpg
   https://sarahrodovalho.com/admin/press/sarah-rodovalho-full-body.png
   ```

2. **Cloudflare Zero Trust Access application** (proper long-term gate):
   - Hostname: `sarahrodovalho.com`
   - Path: `/admin/*`
   - Policy: Allow, identity → Email OTP, email allowlist `sarah@sarahrodovalho.com`
   - Pattern detailed in `docs/runbooks/cloudflare-access-gate-orenu.md` (Orenu uses the same edge-gate model).
   - After config, verify with `curl -I https://sarahrodovalho.com/admin/`:
     - Expected: **HTTP 302** redirect to `https://sarahrodovalho.com/cdn-cgi/access/...`
     - That confirms CF Access is intercepting before the Worker is reached.

3. **When (2) is verified, revert the worker gate**:
   - Remove the `/admin*` 403 block from `worker.js`
   - Worker reverts to www→apex redirect + ASSETS passthrough
   - CF Access then becomes the sole gate (the right architecture)

## PR-S10 — open queue

`feat/s10-work-experience-merge` (commit `86d5f22`) is pushed but not yet a PR. Contents:

- `experience.astro` replaced with merged layout (rich case-study cards · fuzzy-join `experience/*.mdx` for heroImage · photo position BELOW grid)
- `work.astro` deleted
- `worker.js` → `/work` → `/experience` 301 redirect (will conflict with main's admin gate — rebase will need both)
- `SiteHeader.astro` nav: `/work` entry removed
- `SiteFooter.astro`: stale "Selected work" row removed
- `index.astro` home CTA href: `/work` → `/experience`
- 4 experience MDX: `highlights: []` (bullets preserved in gitignored `_private/experience-detailed.md`)
- 3 project MDX: `&amp;` entity leaks unescaped
- `array-architects-healthcare.mdx` title: `"Healthcare planning & design"` (dropped "clinical")
- Footer prose: "Beyond the case studies" → "Beyond the selection"; "teaching at TJU" → "teaching assistant at TJU"; intro trimmed to first sentence

Build verified pre-push: astro check 0/0/0, biome check 0, build 15 pages.

### How to ship PR-S10 next session

```bash
cd ~/Documents/sarah-rodovalho-site
git fetch origin
git checkout feat/s10-work-experience-merge
git rebase origin/main
# conflict in worker.js — keep BOTH the admin gate (from main 58ea918)
# AND the /work → /experience 301 redirect (from feat/s10 86d5f22).
# Order: admin gate FIRST (security before SEO), then www redirect, then /work redirect, then ASSETS.
git push --force-with-lease
gh pr create --base main --head feat/s10-work-experience-merge \
  --title "feat(experience,nav): Work→Experience merge + photo flip + entity sweep (PR-S10)" \
  --body-file <(git log -1 --format=%B)
```

Resolution sketch for the worker.js conflict — final shape should be:

```js
export default {
  async fetch(req, env) {
    const url = new URL(req.url);

    // (1) Admin gate — from hotfix 58ea918
    if (url.pathname === "/admin" || url.pathname.startsWith("/admin/")) {
      return new Response(
        "Restricted area.\n\nThis space is being reconfigured. Contact sarah@sarahrodovalho.com for access.\n",
        { status: 403, headers: { /* same as today */ } },
      );
    }

    // (2) www → apex
    if (url.hostname === "www.sarahrodovalho.com") {
      url.hostname = "sarahrodovalho.com";
      return Response.redirect(url.toString(), 301);
    }

    // (3) /work → /experience (PR-S10)
    if (url.pathname === "/work" || url.pathname === "/work/") {
      url.pathname = "/experience/";
      return Response.redirect(url.toString(), 301);
    }

    return env.ASSETS.fetch(req);
  },
};
```

## Followups (PR-S11 + PR-S12 unchanged)

- **PR-S11** case studies batch (6 MDXs per items 4–9 of `2026-05-18-onenote-ajustes.md` v2) — depends on PR-S10
- **PR-S12** speaking watermarks + PMI talk rewrite + upcoming-events placeholder — depends on PR-S11

## Initial prompt for next session

> Continuing Sarah-site review.
>
> Today (2026-05-19) shipped: **PR #50 hotfix** (worker.js 403 gate on `/admin/*`, commit `58ea918` on main, worker version `16881aee` live). PR-S10 work committed on `feat/s10-work-experience-merge` (pushed, not yet a PR — needs rebase on top of admin gate hotfix first).
>
> Read first:
>   `~/Documents/sarah-rodovalho-site/docs/site-reviews/2026-05-19-PR-S10-and-admin-handoff.md`
>
> Source plan (unchanged, v2, 688 lines, all 28 CLARIFYs resolved):
>   `~/Documents/sarah-rodovalho-site/docs/site-reviews/2026-05-18-onenote-ajustes.md`
>
> First-action options:
> 1. **If user confirms CF Access app is configured + verified** (`curl -I /admin/` returns 302 to `cdn-cgi/access`): create a `revert/admin-worker-gate` branch, delete the `/admin/*` 403 block in worker.js, deploy, verify, PR + merge.
> 2. **If CF Access still pending**: rebase `feat/s10-work-experience-merge` on top of new main (preserve both admin gate AND /work redirect per the conflict sketch in the handoff doc), force-push, open PR-S10.
>
> Ask which path the user wants before executing.
