# UTM + QR attribution conventions

> **Audience:** Sarah (divulgation), Vitor + Claude (consistency).
> **Why:** every link Sarah shares — LinkedIn post, conference QR code, email
> blast, WhatsApp DM — should be tagged so `/admin/metrics` shows clean
> per-channel attribution. Untagged links collapse into "direct" and
> become invisible.
> **Last updated:** 2026-05-19.

---

## TL;DR — the 3 params Sarah uses

Every shared URL gets these three query parameters:

```
?utm_source=<channel>&utm_medium=<format>&utm_campaign=<context>
```

| Param | What it answers | Examples |
|---|---|---|
| `utm_source` | **Where did the click come from?** | `linkedin`, `qr`, `email`, `whatsapp`, `arcc`, `pmi` |
| `utm_medium` | **What kind of placement?** | `post`, `bio`, `talk-slide`, `talk-handout`, `newsletter`, `dm` |
| `utm_campaign` | **What event / push / context?** | `launch-2026-05`, `arcc-2026-talk`, `pmi-women-2026`, `general` |

Two more params exist (`utm_term`, `utm_content`) — ignore unless we need to
A/B test two variants of the same link. Not needed in v1.

---

## Naming convention — opinionated picks

So attribution stays clean, **stick to these vocabularies** (lowercase,
hyphens, no spaces).

### `utm_source` — channel of origin

| Source | Use when |
|---|---|
| `linkedin` | Anything Sarah posts on LinkedIn (feed post, comment, article, profile bio link). |
| `qr` | Any printed or projected QR code (talk slides, business card, handouts, posters). |
| `email` | Personal email signature, or one-off intro emails. |
| `newsletter` | Substack issues (when live). |
| `whatsapp` | WhatsApp shares (close network, professional groups). |
| `arcc` | ARCC.com (Architectural Research Centers Consortium) — site or any ARCC channel. |
| `pmi` | PMI Brazilian Chapter channels (Slack, WhatsApp group, event posts). |
| `aia` | AIA Knowledge Community Board channels. |
| `direct` | Auto-filled by CF for visits with no referrer / no UTM. **Never set manually.** |

### `utm_medium` — format / placement

| Medium | Use when |
|---|---|
| `post` | Social media post (LinkedIn feed, etc.). |
| `bio` | Profile bio link (LinkedIn "Featured" or summary). |
| `talk-slide` | QR code shown on a presentation slide. |
| `talk-handout` | QR on a printed/digital handout at a talk. |
| `newsletter` | Substack issue body / footer link. |
| `dm` | Direct message (WhatsApp, LinkedIn InMail). |
| `signature` | Email signature. |
| `poster` | Physical poster at an event. |

### `utm_campaign` — context / event

Format: `<event-or-context>-<YYYY-MM>` (kebab-case + year-month).

| Campaign | Use when |
|---|---|
| `launch-2026-05` | The initial site divulgation push. |
| `arcc-2026-talk` | ARCC 2026 paper presentation. |
| `pmi-women-2026` | PMI Women in Construction "Follow the Sun" talk. |
| `general` | Default for ongoing channels (LinkedIn bio link, email signature) where there's no specific event. |

**Rule of thumb:** if you can't predict the campaign 6 months from now, use
`general`. Don't invent campaign names mid-flight unless there's a real
event tied to it.

---

## QR code recipe — per-event template

When Sarah presents at a talk, the closing slide should have a QR code
pointing to the site with attribution baked in. Two acceptable shapes:

### Option A — homepage with UTM (simplest)

```
https://sarahrodovalho.com/?utm_source=qr&utm_medium=talk-slide&utm_campaign=arcc-2026-talk
```

QR generator: any. Recommended: [qr-code-generator.com](https://www.qr-code-generator.com/)
(no account needed for static QR; color override available so it can match
the deck's Soft-Structuralism aesthetic).

### Option B — deep-link to a specific page (when the talk is about that page)

```
https://sarahrodovalho.com/research/?utm_source=qr&utm_medium=talk-slide&utm_campaign=arcc-2026-talk
```

Use Option B when the talk is on a topic where the audience benefits from
landing directly on `/research` or `/experience` instead of the homepage.

### What `/admin/metrics` will show after the talk

- **Top pages** row for `/?utm_source=qr&utm_medium=talk-slide&utm_campaign=arcc-2026-talk`
  → exact count of QR scans during/after the talk window.
- **Top referrers** row for `qr / talk-slide / arcc-2026-talk` → same number, summarized.
- **30-day sparkline** → a visible spike on the day of the talk.
- **Top countries** for that campaign → who actually scanned (international audience signal).

---

## LinkedIn divulgation — template

When Sarah publishes the launch post on LinkedIn (or any future post linking
to the site), use this URL structure in the post body:

```
https://sarahrodovalho.com/?utm_source=linkedin&utm_medium=post&utm_campaign=launch-2026-05
```

For the LinkedIn **profile bio link** (the one Sarah keeps in her summary
section, doesn't change often):

```
https://sarahrodovalho.com/?utm_source=linkedin&utm_medium=bio&utm_campaign=general
```

The two will appear as distinct rows in `/admin/metrics` referrer
breakdown, so Sarah can tell which channel her post is pulling from vs the
always-on bio link.

---

## Email signature — template

```
Sarah Rodovalho · sarahrodovalho.com/?utm_source=email&utm_medium=signature&utm_campaign=general
```

Hide the query string visually by hyperlinking the URL text. Recipients
still get attribution but the rendered link is clean.

---

## Anti-patterns (don't do these)

- ❌ **Manually setting `utm_source=direct`** — that's an artifact of "no UTM
  + no referrer," not a value Sarah should set. CF logs untagged + no-
  referrer visits as direct by default.
- ❌ **Inventing new sources/mediums per post** (`linkedin-may-2026`,
  `linkedin-talk-promo`, `linkedin-launch`). Use the vocab above; vary
  `utm_campaign` instead.
- ❌ **Spaces or special characters** in any param. CF GraphQL aggregates
  by literal string match; `?utm_campaign=PMI Talk` and
  `?utm_campaign=pmi-talk` count as different rows.
- ❌ **UTMs inside internal links** between pages of the site. UTMs are for
  inbound traffic only; cross-page navigation pollutes the data.
- ❌ **Shortened URLs that hide the UTM** (`bit.ly/sarah-talk`). The
  shortener captures attribution upstream and the destination URL Sarah
  controls just sees the shortener as referrer. If you must use a
  shortener (e.g., for a QR code that's too dense), make sure it preserves
  the UTM params on the redirect — Bitly and similar do this by default.

---

## How to test a tagged link before sharing

```bash
curl -sI "https://sarahrodovalho.com/?utm_source=qr&utm_medium=talk-slide&utm_campaign=arcc-2026-talk" \
  | head -5
```

Expected: `HTTP/2 200`. The visit will show up in `/admin/metrics` after
the CF Web Analytics pipeline catches up (~2-10 minutes typically).

---

## Adding new vocabulary

If a new channel/event comes up that doesn't fit the table above:

1. Add a row in the appropriate section of this doc (PR with `docs(utm):` prefix).
2. Use the new value in the first link that goes out — don't backfill old links.
3. Mention it in the next Sarah-confirm script so the convention stays shared.

This keeps the vocabulary stable + auditable.
