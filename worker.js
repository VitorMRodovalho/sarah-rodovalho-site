// Thin Worker wrapping the static-asset bundle in dist/.
//
// Sole responsibility: 301-redirect www.sarahrodovalho.com to the apex.
// Both hostnames are bound to this Worker via Custom Domains, so without
// an explicit redirect they serve identical content under different URLs
// — Google flagged this pattern on vitormr.dev as "Duplicate without
// user-selected canonical" (GSC alert WNC-20237597 2026-05-14); this
// is the preventive symmetry port before the same alert hits here. All
// other requests fall through to env.ASSETS, which serves dist/ exactly
// as the prior static-only deployment did.

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.hostname === "www.sarahrodovalho.com") {
      url.hostname = "sarahrodovalho.com";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(req);
  },
};
