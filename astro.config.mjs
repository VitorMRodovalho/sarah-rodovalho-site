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
  // Astro v7 mudou o padrao de compressHTML de true para 'jsx', o que colapsa
  // whitespace entre elementos inline. Fixado em true para preservar a
  // renderizacao da v6 — a troca de regra e decisao separada, nao efeito
  // colateral de um bump de major.
  compressHTML: true,
  site: "https://sarahrodovalho.com",
  output: "static",
  integrations: [
    mdx(),
    sitemap({
      // Exclude admin-gated routes from sitemap. CF Access blocks
      // crawlers at the edge, but excluding here is defense-in-depth
      // — pairs with BaseLayout `noIndex` meta on /admin/* pages and
      // robots.txt Disallow.
      filter: (page) => !page.includes("/admin/"),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
