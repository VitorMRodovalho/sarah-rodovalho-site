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

/**
 * `awards` — recognition, honors, scholarships, judging-relevant memberships.
 *
 * Schema design notes:
 *  - `period` is free text (exact when known: "2024", "2026-2030"; or
 *    contextual when not: "During M.Sc. at TJU 2021-2023") to avoid
 *    inventing year precision the source data doesn't carry.
 *  - `scope` groups awards visually on the page; not all 6 buckets
 *    will always be populated.
 *  - `kazarianCriterion` is metadata for internal EB-1A mapping; NOT
 *    displayed on the public site (avoids leaking immigration framing
 *    into a professional context). Used at most by Vitor + counsel
 *    when extracting evidence rows for case work.
 */
const awards = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/awards" }),
  schema: z.object({
    title: z.string(),
    organization: z.string(),
    period: z.string(),
    scope: z.enum([
      "international",
      "professional-leadership",
      "honor-society",
      "team-award",
      "academic-honor",
      "competitive-scholarship",
    ]),
    kazarianCriterion: z.array(z.number().int().min(1).max(10)).optional(),
    description: z.string(),
    externalUrl: z.url().optional(),
    order: z.number().int().default(100),
  }),
});

/**
 * `experience` — curated employment timeline.
 *
 * Source-of-truth: CV + LinkedIn (cross-validated). 5-7 highlighted
 * projects per ADR-023 §D4.1 §Experience (deferred from initial PRs;
 * shipped as PR-S07 once Sarah's MVP content was settled). Full
 * 17-role chronology lives in LinkedIn for completeness.
 *
 * Schema design notes:
 *  - `period` free text, same convention as `awards` collection
 *  - `industry` enum supports visual badges + filtering at scale (only
 *    one industry value per entry — pick the most representative)
 *  - `highlights` = bulleted impact statements with quantitative
 *    detail when public-disclosed (e.g., $279M change-orders is on
 *    Sarah's public LinkedIn)
 *  - `isCurrent` flips a "Current role" badge on the listing page
 */
const experience = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/experience" }),
  schema: z.object({
    role: z.string(),
    organization: z.string(),
    organizationUrl: z.url().optional(),
    period: z.string(),
    location: z.string(),
    industry: z.enum([
      "data-center",
      "manufacturing",
      "healthcare",
      "retail-mall",
      "transit",
      "academia",
    ]),
    summary: z.string(),
    highlights: z.array(z.string()).default([]),
    isCurrent: z.boolean().default(false),
    order: z.number().int().default(100),
  }),
});

/**
 * `projects` — featured case studies (selected work).
 *
 * Curated subset of Sarah's portfolio, surfaced on /work with scope
 * numbers + project narrative in the foreground. Distinct from
 * `experience` (which is the broader career-timeline view): a project
 * here is a single body of work with quantitative scope, not a role.
 *
 * Schema design notes:
 *  - `scope` is an ordered list of {label, value} pairs rendered as a
 *    stat strip on the card and the detail page. Cap visually at 4
 *    on cards; detail pages may show more.
 *  - `category` controls a small tonal accent + badge label, not a
 *    full filter UI (kept simple while the catalog is < 10 items).
 *  - All fact sources MUST be public (CV / LinkedIn / Scholar / public
 *    press) — see `feedback_role_title_verify_against_offer_letter.md`
 *    + ADR-023 §D8.
 *  - `hasDetailPage` toggles whether `/work/[slug]` is rendered; the
 *    card always links to `#anchor` on /work otherwise.
 */
const projects = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/projects" }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    role: z.string(),
    employer: z.string(),
    employerUrl: z.url().optional(),
    period: z.string(),
    yearStart: z.number().int(),
    yearEnd: z.number().int().nullable().default(null),
    isCurrent: z.boolean().default(false),
    location: z.string(),
    category: z.enum([
      "data-center",
      "retail-mall",
      "transit",
      "healthcare",
      "manufacturing",
      "academia",
      "hospitality",
    ]),
    abstract: z.string(),
    scope: z.array(z.object({ label: z.string(), value: z.string() })).default([]),
    order: z.number().int().default(100),
    hasDetailPage: z.boolean().default(false),
  }),
});

export const collections = { publications, awards, experience, projects };
