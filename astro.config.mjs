// @ts-check
import cloudflare from "@astrojs/cloudflare";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "astro/config";

// Astro 6.3 config — static site for sarahrodovalho.com.
// Cloudflare adapter included for Pages deployment (PR-S05).
// MDX enables rich content authoring without CMS lock-in.
// Sitemap auto-generated for SEO (Schema.org Person + ScholarlyArticle markup added per page).

export default defineConfig({
  site: "https://sarahrodovalho.com",
  output: "static",
  adapter: cloudflare(),
  integrations: [mdx(), sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
