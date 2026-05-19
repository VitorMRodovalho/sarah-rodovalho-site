// Thin Worker wrapping the static-asset bundle in dist/.
//
// Responsibilities:
//   1. Hard 403 gate on /admin/* — emergency seal applied 2026-05-19 after
//      production verification showed the prior Cloudflare Access policy
//      (PR-S07b) was NOT enforcing: anonymous browsers were receiving
//      HTTP 200 with the full admin HTML (legal name + hi-res photo
//      links) served from cf-cache HIT. Until the Zero Trust Access
//      application is correctly configured + verified, this worker
//      returns a plain-text 403 with `cache-control: no-store` for any
//      /admin path. When the Access policy is verified working, this
//      block can be removed and traffic again falls through to ASSETS
//      (which is fronted by CF Access at the edge).
//   2. 301-redirect www.sarahrodovalho.com to the apex (prevents the
//      "Duplicate without user-selected canonical" GSC alert that fired
//      on vitormr.dev — WNC-20237597 2026-05-14).
//
// All other requests fall through to env.ASSETS, which serves dist/
// exactly as the prior static-only deployment did.
//
// `run_worker_first = true` in wrangler.toml is load-bearing — without
// it, matched static assets bypass the Worker entirely and the gate
// above never fires.

export default {
  async fetch(req, env) {
    const url = new URL(req.url);

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

    if (url.hostname === "www.sarahrodovalho.com") {
      url.hostname = "sarahrodovalho.com";
      return Response.redirect(url.toString(), 301);
    }

    return env.ASSETS.fetch(req);
  },
};
