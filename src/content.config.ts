import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

/**
 * Astro Content Collections — type-safe MDX schemas.
 *
 * `publications` — peer-reviewed papers + conference panels. Each entry
 * is validated at build time against the schema below; missing required
 * fields fail the build (caught by `astro check` in CI).
 *
 * Schema design notes:
 *  - `kind` discriminates "journal-article" (DOI required) vs
 *    "conference-panel" (DOI optional; conference URL required).
 *  - `coAuthors` accepts an ordered list — order matches the published
 *    byline (e.g., G Ozcan-Deniz first, S Rodovalho second).
 *  - `citationsAt` is a frozen-in-time count + the date observed; we
 *    don't pretend to track live citations (Scholar API is unreliable).
 *  - `abstract` is plain string (1-3 paragraphs); the MDX body can hold
 *    extended notes if needed.
 */

const publications = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/publications" }),
  schema: z.object({
    title: z.string(),
    kind: z.enum(["journal-article", "conference-panel"]),
    venue: z.string(),
    venueShort: z.string().optional(),
    publisher: z.string().optional(),
    year: z.number().int().min(2000).max(2100),
    volume: z.string().optional(),
    issue: z.string().optional(),
    pages: z.string().optional(),
    article: z.string().optional(),
    doi: z.string().optional(),
    venueUrl: z.url().optional(),
    paperUrl: z.url().optional(),
    abstract: z.string(),
    coAuthors: z.array(z.string()).min(1),
    citationsAt: z
      .object({
        count: z.number().int().min(0),
        observedOn: z.string(),
      })
      .optional(),
    order: z.number().int().default(100),
  }),
});

export const collections = { publications };
