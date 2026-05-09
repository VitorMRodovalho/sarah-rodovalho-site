// @ts-check
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "astro/config";

// Astro 6.3 config — pure-static site for sarahrodovalho.com on Cloudflare Pages.
//
// NO @astrojs/cloudflare adapter: with `output: 'static'`, the adapter would
// emit a server bundle that triggers `npx wrangler deploy` on Pages, which
// fails because wrangler isn't in the deploy image. Pure-static + dist/ output
// = Cloudflare Pages auto-detects and uploads as static assets.
//
// MDX enables rich content authoring without CMS lock-in.
// Sitemap auto-generated for SEO (Schema.org Person + ScholarlyArticle markup
// added per page).

export default defineConfig({
  site: "https://sarahrodovalho.com",
  output: "static",
  integrations: [mdx(), sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
