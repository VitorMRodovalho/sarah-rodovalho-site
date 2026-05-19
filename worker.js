// Thin Worker wrapping the static-asset bundle in dist/.
//
// Responsibilities:
//   1. 301-redirect www.sarahrodovalho.com to the apex (prevents the
//      "Duplicate without user-selected canonical" GSC alert that fired
//      on vitormr.dev — WNC-20237597 2026-05-14).
//   2. 301-redirect the legacy /work route to /experience (the two
//      pages were merged in PR-S10, 2026-05-19). Preserves any
//      external links to /work that pre-date the merge.
//
// All other requests fall through to env.ASSETS, which serves dist/
// exactly as the prior static-only deployment did.

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.hostname === "www.sarahrodovalho.com") {
      url.hostname = "sarahrodovalho.com";
      return Response.redirect(url.toString(), 301);
    }
    if (url.pathname === "/work" || url.pathname === "/work/") {
      url.pathname = "/experience/";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(req);
  },
};
