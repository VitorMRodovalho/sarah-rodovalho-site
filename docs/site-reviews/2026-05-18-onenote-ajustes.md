# Site Review · Sarah · OneNote "Ajustes do site"

**Source**: `~/Downloads/A/My Notebook.pdf` — exported from OneNote notebook **AIA2025**, seção **Ajustes do site**, dated Monday, May 18, 2026, 3:41 PM
**Author of review**: Sarah Faria Alcantara Macedo Rodovalho
**Transcribed/mapped by**: Vitor + Claude (Anthropic), 2026-05-18
**Status**: **v2** — todos os 28 CLARIFYs resolvidos por Vitor; 3 re-análises arquiteturais inline (2.5 / 11.x / 13.x); PR plan re-organizado em 7 PRs (PR-S07a/b separados).

> **v1** focou em transcrição + dúvidas. **v2** consolida decisões e está pronto pra começar a implementar.

---

## Cor-code legend (used by Sarah)

| Marca | Significado | Where |
|---|---|---|
| 🔴 **Vermelho** (riscado/contorno) | Retirar | Body copy + callout labels + months on dates |
| 🟡 **Amarelo** (highlight) | Trocar / mudar para — | Numbers, dates, locations, section names |
| 🔵 **Azul** (highlight) | Adicionar | New items (e.g., PhD bullet) |
| 🟢 **Verde** | Categoria de callout (slot 1) | Scope card callouts |
| 🩷 **Rosa/Pink** | Categoria de callout (slot 3) | Scope card callouts |
| 🟠 **Laranja/Orange** | Categoria de callout (slot 4) | Scope card callouts |
| 🟣 **Roxo/Purple** | Corrigir | Punctual fixes (HTML entity leaks like `&amp;`) |
| ➡️ **Seta rosa** | Realocar | Move block/photo |
| ➡️ **Seta marrom (brown)** | Trocar tag/label | Section header ("Beyond the case studies" → "Beyond the selection") |
| ➡️ **Seta lavanda** | Incluir | Add specific item (e.g., "Assistant" before "Teaching") |

**Callout slot convention** (confirmed Vitor 4.5): each case study card has 4 callout pills mapped to color slots in `src/content/projects/*.mdx` `scope` array:
- 🟢 Green = slot 1
- 🔵 Blue = slot 2
- 🩷 Pink = slot 3
- 🟠 Orange = slot 4

Per `content.config.ts` `projects.scope` schema: `array({label, value})`. Color rendering is per-position in the array, not stored in MDX.

---

## Index — pages reviewed + status

| # | OneNote section | PDF pgs | Repo target | Status |
|---|---|---|---|---|
| 1 | PAGINA DE ENTRADA | 1 | `src/pages/index.astro` | ✅ Resolved |
| 2 | PAGINA ABOUT | 2–4 | `src/pages/about.astro` | ✅ Resolved |
| 3 | PAGINA WORK → merge in EXPERIENCE | 3 | `src/pages/experience.astro` (kept) + `src/pages/work.astro` (deprecated) | ✅ Resolved |
| 4 | Case 01 Aligned hyperscale | 3–4 | `src/content/projects/aligned-multi-building-campus.mdx` | ✅ Resolved |
| 5 | Case 02 Microsoft CO+I CLT | 5 | `src/content/projects/microsoft-coi-hyperscale-program.mdx` | ✅ Resolved |
| 6 | Case 03 Tesla Lathrop | 5 | `src/content/projects/tesla-industrial-rd-portfolio.mdx` | ✅ Resolved |
| 7 | Case 04 Passeio das Águas | 5 | `src/content/projects/passeio-das-aguas-shopping.mdx` | ✅ Resolved |
| 8 | Case 05 Goiânia BRT | 5 | `src/content/projects/goiania-brt-network.mdx` | ✅ Resolved |
| 9 | Case 06 Virtua Healthcare | 5–6 | `src/content/projects/array-architects-healthcare.mdx` | ✅ Resolved |
| 10 | PAGINA RESEARCH | 6 | `src/pages/research.astro` | ✅ No-op ("Não alterar por hoje") |
| 11 | PAGINA SPEAKING | 6 | `src/pages/speaking.astro` + slide assets | ✅ Resolved (watermark scope = slide images) |
| 12 | **NOVA**: Academic | 7 | NEW `src/pages/academic.astro` | ✅ Resolved (re-analysis confirmed clean cut) |
| 13 | PAGINA PRESS KIT | 7 | `src/pages/press-kit.astro` + NEW `src/pages/admin/*` | ✅ Resolved (admin = logged-in layer per CF Access) |
| 14 | **NOVA**: Contact | 3 | NEW `src/pages/contact.astro` | ✅ Resolved |

---

## 1 · PAGINA DE ENTRADA (home) — `src/pages/index.astro`

### 1.1 Hero copy — replace ending [RESOLVED]
- **Decisão Vitor**: substituir "on a multi-building, ~264 MW campus" → **"on a multi-hundred-megawatt campus"**
- **Ação**: `copy-edit`
- **Alvo**: hero text em `src/pages/index.astro`

### 1.2 Big numbers — swap 264 MW + $279 M+ for PMI deck values [RESOLVED]
- **Source**: PMI Follow the Sun deck (`~/Downloads/A/PMI Women In Construction Follow the Sun 2026 Presentation SR_final.pptx`, slide 29 "Project scale and Impact / Big Numbers")
- **Decisão**: trocar para os 2 mais hero-iconic da slide 29:
  - `264 MW` → **`7M+`** label `Square feet delivered`
  - `$279 M+` → **`~$1.5B+`** label `Total program value`
- **Demais slots já existentes mantém**: `16+` (Years in delivery) e `3` (Peer-reviewed papers)
- **Por que estes 2**:
  - Career-aggregate, não employer-specific (alinhado com concern Sarah sobre exposição interna)
  - Magnitude maior, mais impactante
  - Source oficial da apresentação dela (PMI Follow the Sun)
  - Frame coerente com "16+ years" (já no quadro): toda a stat strip vira career-spanning
- **Alternativas inferiores consideradas** (do mesmo slide): `60+` Stakeholders, `5` Countries (Brazil, Portugal, Italy, China, US) — bons mas menos hero. Podem ser mencionados em texto narrativo posterior.

---

## 2 · PAGINA ABOUT — `src/pages/about.astro`

### 2.1 Bio narrative — remove "on a multi-building campus" [RESOLVED]
- **Decisão Vitor**: substituir frase paralela ao 1.1 → bio termina com **"on a multi-hundred-megawatt campus"** (consistência hero ↔ about)
- **Alvo**: `about.astro` linha 63 — `I currently work at Aligned Data Centers as Integrated Design Manager on a multi-building, ~264 MW campus.`
- **Trocar para**: `I currently work at Aligned Data Centers as Integrated Design Manager on a multi-hundred-megawatt campus.`

### 2.2 Section "Now" → "Current Engagements" [RESOLVED]
- **Decisão Vitor**: ✅ confirmado
- **Alvo**: `about.astro` linha 117 — `<h2>Now</h2>` → `<h2>Current Engagements</h2>`

### 2.3 First bullet "Aligned" — replace stat phrase [RESOLVED]
- **Decisão Vitor**: ✅ implícito em 1.1/2.1
- **Alvo**: `about.astro` linhas 122–124 — `Leading integrated design management across a ~264 MW multi-building campus.`
- **Trocar para**: `Leading integrated design management on a multi-hundred-megawatt campus.`

### 2.4 PhD bullet — reposition [RESOLVED]
- **Decisão Vitor**: "está na sessão abaixo de educação, mas como estamos fazendo ajustes é algo que faz sentido estar no contexto da sessão"
- **Estado atual**: PhD aparece em DUAS sections:
  1. `about.astro` linhas 125–130 — section Now → mantém como Current Engagement
  2. `about.astro` linhas 259–262 — section Education
- **Ação consolidada**:
  - **Now / Current Engagements**: PhD bullet STAYS (já lá)
  - **Education section**: vai TODA pra `/academic` (per 2.5) — o PhD bullet vem junto, com status "in progress" badge
  - **Resultado net**: Sarah aparece com PhD em DOIS lugares — `/about` (como current engagement) E `/academic` (como educação em progresso). Both contexts são honestos e não-duplicativos (current activity vs formal academic record).

### 2.5 Remove CV-style blocks — restructure [RESOLVED via re-analysis]
- **Decisão Vitor**: "esta decisão é mais tua que nossa, caso queira fazer uma re análise e voltar com dúvidas pendentes de decisão de negócio com opção a b c e recomendação eu topo em o fazermos"
- **Re-análise (resultado decisivo, sem dúvidas pendentes)**:

  **Estado atual em `about.astro`**:
  - Header / bio (linhas 39–95)
  - Section Now / Current Engagements (linhas 117–200)
  - Section Selected past roles (linhas 202–251) — Microsoft + Tesla + TJU + Array + Aliansce
  - Section Education (linhas 253–353) — PhD + MSc + MBA + Bachelor + photos
  - Section Certifications & affiliations (linhas 355–399) — PMP, LEED GA, OSHA 30, AIA Assoc, CAU, Sigma Lambda Chi, NCARB
  - Section Languages (linhas 401–408) — Portuguese + English

  **Pages existentes na repo onde isto já mora (ou pode morar)**:
  - `src/pages/experience.astro` — JÁ renderiza Past Roles via `experience/*.mdx` collection (7 MDXs)
  - `src/pages/credentials.astro` — JÁ renderiza Certifications via `credentials/*.mdx` collection (6 MDXs)
  - `src/pages/awards.astro` — separa awards (não-overlap)

  **Análise de overlap**:
  | Section em about.astro | Already covered? | Action |
  |---|---|---|
  | Bio header + Now | Não | KEEP em /about |
  | Selected past roles | **SIM** — `/experience` | REMOVE de /about (already at /experience) |
  | Education | **NÃO** — orphan | MOVE pra NEW /academic |
  | Certifications & affiliations | **SIM** — `/credentials` | REMOVE de /about (already at /credentials) |
  | Languages | **NÃO** — orphan | MOVE pra NEW /academic |

  **Decisão final (sem opção a/b/c — data dictates the answer)**:
  - `/about` fica: bio + Current Engagements (clean, sem CV)
  - REMOVE de `/about`: Past Roles (já em /experience), Certs (já em /credentials), Education (mudou pra /academic), Languages (mudou pra /academic)
  - NEW `/academic` contém: **Education** (PhD em progresso + MSc + MBA + Bachelor + photos) + **Languages**

- **Risk flagged**: Section Education em about.astro tem 4 fotos (thesis defense, commencement TJU, UEG CBA 2006, UEG formatura 2009). Ao mover pra /academic, preservar todos os caminhos de Picture + alt text + figcaptions atuais.

### 2.6 (was: investigação) — auto-resolved acima

---

## 3 · PAGINA WORK / EXPERIENCE merge — kept page: `/experience`

### 3.1 Merge — keep `/experience` slug [RESOLVED]
- **Decisão Vitor**: "expirence" → kept page é **`/experience`**, `/work` é deprecada com 301 redirect
- **Implementação**:
  - Copy content de `work.astro` (rich case study layout w/ `projects/*.mdx`) → REPLACE content atual de `experience.astro`
  - DELETE `src/pages/work.astro`
  - ADD 301 redirect `/work` → `/experience` em `worker.js`
- **Camada de dados**:
  - Manter `projects/*.mdx` collection (6 case studies) — fonte das cards
  - Manter `experience/*.mdx` collection (7 past roles c/ heroImage) — segunda fonte de foto/link se quiser cruzar
  - **Por projeto / case study**: foto + link de cada experiência together (Sarah's intent)
  - Schema atual já suporta — só precisa renderizar
- **CLARIFY-resolved-12 (intro paragraph)**: Vitor → "sarah removeu tudo pós o primeiro statement"
  - Atual: `work.astro` linhas 49–66: `Six selected programs from a 16+ year delivery career in the U.S. and Brazil. Each entry pairs scope numbers with the role I held and the project's delivery context. The full chronology — including earlier roles in architecture practice and public-sector work — is on LinkedIn; broader role overview lives on the experience page.`
  - **Trocar para**: `Six selected programs from a 16+ year delivery career in the U.S. and Brazil.` (somente primeira sentença; remove o resto)

### 3.2 NOT exposing CV-style content publicly [RESOLVED]
- **Decisão Vitor**: "ela falou que estava ficando repetitivo e ela riscou toda parte que é mais descritiva pq tem nos bullet points muita informação sensível de negócio das funções"
- **Pattern identificado**: `experience/*.mdx` `highlights[]` array contém bullets com:
  - Internal financial metrics (e.g., `$4.2M+ verified savings`, `20% reduction in design-consultant fees`)
  - Specific function detail (e.g., `Mechyard tool installation conflict resolution`, `RFP cycles under 72 hours`)
  - Internal organizational detail (e.g., `divide ownership with a peer Design Manager`)
- **Decisão de implementação**:
  - `highlights: []` (empty array) em todos 7 `experience/*.mdx`
  - Bullets sensíveis MOVE pra novo arquivo gitignored `_private/experience-detailed.md` (single source preservado pra interviews/CV uso pessoal Sarah)
  - Add `_private/` ao `.gitignore` se ainda não estiver
- **Net effect público**: `experience.astro` mostra `summary` + heroImage por role, sem bullets. Detalhes ficam em arquivo privado.

### 3.3 NEW page Contact [RESOLVED]
- **Decisão Vitor**: "contact" (English-first per CLAUDE.md)
- **Alvo**: NEW `src/pages/contact.astro`
- **Escopo "simples"** (Sarah's word):
  - Headline (e.g., "Get in touch")
  - Email único `sarah@sarahrodovalho.com` (mailto link)
  - LinkedIn link
  - Press inquiries → link pra `/press-kit`
  - Localização: "Based in Leesburg, Virginia · Washington DC – Baltimore region"
  - NO form (per content-discipline + Sarah's "simples")

---

## 4 · Case 01 · Aligned hyperscale campus — `src/content/projects/aligned-multi-building-campus.mdx`

### 4.1 Date format — only years [RESOLVED]
- **Decisão Vitor**: `2025` (sem mês)
- **Convention (per 4.1+)**: `<year> — present · USA` (or country) aplicado a TODOS os cards
- **Alvo MDX**:
  - `period: "Oct 2025 — present"` → `period: "2025 — present · USA"`
  - `location: "Virginia & Maryland, U.S."` → `location: "USA"`

### 4.2 Intro paragraph — keep first sentence only [RESOLVED]
- Ver item 3.1 acima (este é o footer prose do /work, vai pra /experience após merge)

### 4.3 Strikethrough callout tags — superseded by new callouts (4.5)

### 4.4 Body text — abstract + body split per recommendation [RESOLVED]
- **Decisão Vitor**: "em acordo com a recomendação" → 1º parágrafo → `abstract`, 2º parágrafo → MDX body markdown
- **`abstract` (frontmatter)**:
  > Hyperscale campuses don't get strained because any one workflow is hard. They get strained because design, permitting, underground systems, and field execution all move in parallel — and the toughest problems live in the gaps between them.
- **Body markdown (abaixo do frontmatter)**:
  > That's the work at Aligned. I lead owner-side integrated design on a multi-building campus, coordinating trade workstreams across mixed delivery models. A few frameworks have crystallized along the way — for permitting, underground coordination, and handoff.

### 4.5 Callouts (4 slots) — inference confirmed [RESOLVED]
- **Decisão Vitor**: "confirmado a inferência"
- **MDX `scope` array final** (ordem = display slot):
  ```yaml
  scope:
    - { label: "CONTEXT", value: "Dual-track delivery" }       # green
    - { label: "INTEGRATION", value: "Disciplines · trades · Vendors" }  # blue
    - { label: "REGION", value: "NoVA / Maryland corridor" }   # pink
    - { label: "METHODOLOGY", value: "Field-tested governance frameworks" }  # orange
  ```

---

## 5 · Case 02 · Microsoft CO+I CLT — `src/content/projects/microsoft-coi-hyperscale-program.mdx`

### 5.1–5.2 Location + date [RESOLVED]
- Per convention `<year> — <year> · USA`

### 5.3 Body — abstract + body split [RESOLVED]
- **`abstract`**:
  > Hyperscale data centers are some of the most carbon-intensive structures in modern construction. Microsoft's mass-timber pilot in Northern Virginia is the industry's first serious attempt to change that — a hybrid cross-laminated timber, steel, and concrete design targeting 35% less embodied carbon than steel and 65% less than precast concrete.
- **Body markdown**:
  > I was on the first team. The visible work was construction contracts and change-order management across several concurrent builds. Development of change-order framework that ended up used across projects — and a CO+I team award.

### 5.4 Callouts (4 slots) — corrigir typo [RESOLVED]
- **Decisão Vitor**: "sim corrigir" → `CONTRIBUITION` → **`CONTRIBUTION`**
- **MDX `scope` final**:
  ```yaml
  scope:
    - { label: "INITIATIVE", value: "First-team CLT data centers (FOK)" }  # green
    - { label: "SCOPE", value: "Concurrent hyperscale portfolio" }          # blue
    - { label: "CONTRIBUTION", value: "Change-order framework" }            # pink
    - { label: "RECOGNITION", value: "CO+I Team Award · FY25" }             # orange
  ```

---

## 6 · Case 03 · Tesla Lathrop — `src/content/projects/tesla-industrial-rd-portfolio.mdx`

### 6.1–6.2 Location + date [RESOLVED]

### 6.3 Body — abstract + body split
- **`abstract`**:
  > The Lathrop Megafactory is the world's first dedicated facility for mass-producing Tesla Megapacks and North America's largest utility-scale battery plant. My time at Tesla overlapped its publicly announced doubling — from 20 to 40 GWh of annual production capacity.
- **Body markdown**:
  > The work was a multi-facility portfolio of industrial and workplace projects across Tesla's U.S. operations, coordinated across engineering, facilities, and construction through scope discipline and vendor consolidation.

### 6.4 Callouts (4 slots) — explícitos [RESOLVED]
```yaml
scope:
  - { label: "SCALE-UP", value: "20 → 40 GWh" }                              # green
  - { label: "SCOPE", value: "Multi-facility industrial portfolio" }         # blue
  - { label: "CATEGORY", value: "First-of-kind energy storage facility" }    # pink
  - { label: "DOMAIN", value: "Energy storage manufacturing" }               # orange
```

---

## 7 · Case 04 · Passeio das Águas — `src/content/projects/passeio-das-aguas-shopping.mdx`

### 7.1 Purple — HTML entity leak fix [RESOLVED]
- **Decisão Vitor**: "está em roxo o `&` que está modulando como `&amp;` tem outros locais da página com esta falha de renderização do símbolo"
- **Root cause**: ampersand HTML entity leak — algum lugar tem `&amp;` literal no MDX/Astro source onde devia ser `&` (Astro/JSX auto-escapes); ou um double-escape pattern.
- **Locais para grep (todos os arquivos do repo)**:
  - `pages/*.astro` — `&amp;` literal (CORRETO em JSX/Astro template, ESCAPADO já)
  - `content/**/*.mdx` — `&amp;` literal (INCORRETO no MDX frontmatter strings — escape leak)
  - MDX body — `&amp;` em prose também pode ser leak dependendo do parser
- **Diagnóstico Vitor flagged "outros locais com mesma falha"** — não-único ao card 04; sweep general aplica
- **Action**: PR-S10 inclui sweep de `&amp;` em MDX frontmatter strings → trocar por `&` literal (Astro renderiza correctly desde que não venha duplo-escapado)

### 7.2 Vermelho — months elimination [RESOLVED]
- **Decisão Vitor**: "meses que ela está eliminando e deixando só anos" — alinhado com 4.1 convention

### 7.3 Yellow — date format [RESOLVED]
- Per convention: Passeio é Brasil → `2013 · Brazil`

### 7.4 Body — abstract + body split
- **`abstract`**:
  > Passeio das Águas is one of the largest shopping centers in Brazil's center-west region — a ground-up project I delivered from construction through commissioning and into ongoing tenant operations. It opened on its original target date of 30 October 2013.
- **Body markdown**:
  > The visible work was design and construction management at scale. The deeper work was building a tenant-improvement operational framework that was later adopted across Aliansce Sonae's national portfolio — a methodology born on one project that ended up shaping how the company ran the rest.

### 7.5 Callouts (4 slots) — auto-fill suggested by me [RESOLVED via my recommendation]
- **Decisão Vitor**: "auto-fill a sugerir por ti"
- **Sugestão (4 slots completos)**:
  ```yaml
  scope:
    - { label: "SCHEDULE", value: "Delivery on-time" }              # green (explicit Sarah)
    - { label: "TENANTS MANAGED", value: "300+" }                   # blue (explicit Sarah)
    - { label: "BUDGET", value: "$232M" }                           # pink (auto, from PMI slide 20)
    - { label: "IMPACT", value: "Framework adopted nationally" }    # orange (auto, from Sarah's body para 2)
  ```
- **Justificativa auto-fill**:
  - Pink BUDGET / $232M — number já público em press-kit + PMI deck slide 20; coerente magnitude
  - Orange IMPACT / Framework adopted nationally — captura o "deeper work" do parágrafo 2 da Sarah ("tenant-improvement framework adopted across Aliansce Sonae's national portfolio"); transforma a história em um callout dimensional

---

## 8 · Case 05 · Goiânia BRT — `src/content/projects/goiania-brt-network.mdx`

### 8.1 Yellow — date [RESOLVED]
- Per convention: Brazil → `2017 · Brazil`

### 8.2 Body — abstract + body split
- **`abstract`**:
  > The Bus Rapid Transit corridor runs through the dense center of Goiânia, Brazil's tenth-largest city — a public-infrastructure program that had to reach functional opening while threading construction through active urban fabric.
- **Body markdown**:
  > The visible work was design management across the full corridor — terminals, stations, and ground-up infrastructure. The defining moment was a two-month critical-criteria window: targeted design revisions that bypassed eminent-domain constraints without triggering land disputes, and R$1.5M in design-change savings absorbed before they reached construction.

### 8.3 Photo position — below text, ALL cards [RESOLVED]
- **Decisão Vitor**: "todos, sarah informou que a foto em cima confunde ela pq a descrição do que está abaixo entao por isto ela solicitou a inversao da ordem"
- **Reasoning**: foto em cima sem contexto deixa ambíguo qual é o projeto; texto primeiro orienta o leitor antes da imagem confirmar
- **Implementação**: refactor `work.astro` (que virará `experience.astro` per 3.1) — mover `<figure>` heroImage de ANTES do título para DEPOIS do body+scope grid
- **Aplicação**: TODOS os 6 case study cards (uniformidade visual)
- **Note**: card 05 não tem callouts adicionais especificados — manter atual `scope` array

---

## 9 · Case 06 · Virtua Healthcare — `src/content/projects/array-architects-healthcare.mdx`

### 9.1 Yellow #1 — title trim [RESOLVED]
- **Decisão Vitor**: "substituir 'clinical planning & design' por 'planning & design'"
- **Title atual** (no card screenshot): "Healthcare clinical planning & design"
- **Title novo**: "Healthcare planning & design" (drop "clinical")
- **Alvo MDX**: `title:` field
- **OBS**: também há possível leak `&amp;` (per 7.1 sweep)

### 9.2 Yellow #2 — location → USA [RESOLVED]
- **Alvo MDX**: `location: "USA"`

### 9.3 Yellow #3 — date [RESOLVED]
- Per convention: `2022 · USA`

### 9.4 Body — abstract + body split
- **`abstract`**:
  > Virtua Our Lady of Lourdes in Camden is the anchor project of Virtua Health's $500M "Advancing Well" reinvestment — a 254,000 sq ft new tower and 458,000 sq ft renovation consolidating cardiac, neuroscience, and transplant services for South Jersey.
- **Body markdown**:
  > I contributed during design development and construction documentation as an Architectural Designer at Array Architects, the project's architect of record. The visible work was life-safety detailing and RFI workflow through Autodesk Build, delivered ahead of phased-handoff deadlines. The deeper work was clinical-planning practice in its most demanding form — bed-tower programming where adjacencies, infection-control, patient experience, and operational continuity drive every plan decision.

### 9.5 Callouts (4 slots) — explícitos [RESOLVED]
```yaml
scope:
  - { label: "SCOPE", value: "Tower Addition & Renovation" }    # green
  - { label: "TOWER", value: "254K sq ft" }                     # blue
  - { label: "RENOVATION", value: "458K sq ft" }                # pink
  - { label: "PROGRAM", value: "$500M" }                        # orange
```

### 9.6 Brown arrow — section header rename [RESOLVED]
- **Decisão Vitor**: "trocar 'Beyond the case studies' para 'Beyond the selection'"
- **Alvo**: `work.astro` linha 184 — `<p class="eyebrow">Beyond the case studies</p>` → `<p class="eyebrow">Beyond the selection</p>`
- **Note**: após o merge per 3.1, este pedaço fica em `experience.astro`

### 9.7 Lavender arrow — add "Assistant" to teaching [RESOLVED]
- **Decisão Vitor**: "sarah era professora assistente durante o mestrado, então por isto ela solicitou adicionar assistente a frente de teaching para nao gerar uma inferência errada"
- **Context CPT**: Sarah era aluna do MSc em TJU e atuou como **Teaching Assistant** dos professores de Construction Management como parte do CPT (Curricular Practical Training, F-1 visa work authorization).
- **Alvos**:
  - `work.astro` linhas 186–188 (Beyond the selection prose) — "teaching at Thomas Jefferson University's Department of Construction Management" → **"teaching assistant at Thomas Jefferson University's Department of Construction Management"** (ou "as a teaching assistant" se ficar melhor gramaticalmente)
  - Verificar TODOS os outros locais que mencionam TJU + "teaching" — sweep similar ao `&amp;`
  - `about.astro` linha 222–224 — JÁ tem "Teaching Assistant" → no-op
  - `experience/tju-teaching-assistant.mdx` — verificar role + summary; provavelmente já correto

---

## 10 · PAGINA RESEARCH — `src/pages/research.astro`

### 10.1 No-op
- **Decisão Vitor**: ✅ "Não alterar por hoje"

---

## 11 · PAGINA SPEAKING + UPCOMING EVENTS PLACEHOLDER

### 11.1 Upcoming events block — build NOW (re-analysis confirmed) [RESOLVED]
- **Decisão Vitor**: "eu prefiro do ponto de vista técnico em já criar a página, e colocar em breve next events ou algo do tipo, pq aí temos o placeholder já diagramado e fica fácil de lembrar em atualizar quando tiver novos e futuros eventos a colocar lá, o que inclusive nutre o Orenu com informações valiosas, e Sarah tem já upcoming events (ela só está sem tempo em nos trazer a lista)"
- **Re-análise — design do placeholder**:
  - Top da `speaking.astro` ganha uma nova `<section>` ANTES da listagem de past engagements
  - Use existing `engagements` content collection (schema já tem `date: string`)
  - Filter dynamically: `upcoming = engagements.filter(e => new Date(e.data.date) >= today)` e `past = engagements.filter(e => new Date(e.data.date) < today)`
  - Section "Upcoming engagements":
    - Se `upcoming.length > 0`: render cards iguais aos past, com badge "Upcoming"
    - Se `upcoming.length === 0`: render empty state — "Sarah is currently scheduling 2026 events. Reach out via [contact](/contact) to invite her."
- **Implementation notes**:
  - `speaking.astro` atual já carrega `getCollection("engagements")` (linha 37) — só precisa split por date
  - HERO_IMAGES + DECK_IMAGES dict (linhas 41–86) precisa cobrir upcoming events também — ok como pattern
  - Schema engagements suporta `date` — nada a mudar em `content.config.ts`
- **Tie-in Orenu (per Vitor's intent)**: quando Sarah preencher upcoming events em `engagements/*.mdx`, o mesmo content pode alimentar o Orenu dim_engagement table via auto-PR pattern descrito em ADR-024 phase 1b (fact_speaker_engagement). Continuidade entre o site da Sarah + Orenu data layer.

### 11.2 Watermark slide images — embedded diagonal [RESOLVED]
- **Decisão Vitor**: "as imagens da apresentação dela do PMI ela pediu que tenha uma watermark em cima da imagem para evitar de outros usarem imagem de apresentação dela sem o consent entao é uma proteção que ela está pedindo"
- **Scope clarification**: watermark **embedida no asset** (binary modification), NÃO page-level ambient (que já existe via `WatermarkLayer.astro`)
- **Assets alvo** (per `speaking.astro` HERO_IMAGES + DECK_IMAGES dicts):
  - `src/assets/speaking/24-hours-women-construction-event-banner.png` (event banner)
  - `src/assets/speaking/ai-compute-demand-growth.png` (slide deck thumbnail)
  - `src/assets/speaking/anatomy-of-a-data-center.png`
  - `src/assets/speaking/arcc-2025-sarah-presenting.jpg` (ARCC; este é foto da Sarah, watermark com cuidado pra não cobrir o rosto)
  - `src/assets/speaking/how-i-ended-up-in-data-centers-timeline.png`
  - `src/assets/speaking/physical-backbone-digital-world.png`
- **Watermark text** (default per minha recomendação CLARIFY-25, Vitor não overrode): **"© Sarah Rodovalho · sarahrodovalho.com"**
- **Pattern**: diagonal, semi-transparente (~25% opacity), repetido em grid (3-4 instances por imagem para dificultar crop-out)
- **Implementação**: novo script `scripts/watermark-images.py` usando Pillow:
  - Input: pasta `src/assets/speaking/_originals/` (originais sem watermark, ADD to `.gitignore`)
  - Output: `src/assets/speaking/*.png/jpg` (watermarked, committed)
  - Idempotente: skip se output já existe e tem mtime > input
- **OBS sobre PR #43/#45**: ambient `WatermarkLayer.astro` continua útil pra page-level. Os dois sistemas convivem — Layer cobre página inteira, embedded protege imagens individuais que podem ser baixadas/screenshot/extraídas isoladamente.

### 11.3 PMI talk description rewrite [RESOLVED]
- **Alvo**: `src/content/engagements/pmi-women-construction-follow-the-sun-2026.mdx` — campo `abstract:`
- **Body novo**:
  > An invited session at PMI's annual global women-in-construction-leadership conference. The talk is for construction project managers thinking about a pivot into mission-critical infrastructure — what a data center actually is in the AI era, what transfers from architecture and large-scale construction, and what you have to stop assuming you can't do.

### 11.4 Outros engagements [RESOLVED]
- **Decisão Vitor (Sarah implicit)**: "Outro items ok por agora"
- **No-op** para `arcc-2025-wellbeing-net-zero-healthcare.mdx`, `ia-na-construcao-autodesk-forma-2026.mdx`, `startse-construtech-summit-2024.mdx`

---

## 12 · NOVA PÁGINA · Academic — NEW `src/pages/academic.astro`

### 12.1 Page slug + scope [RESOLVED]
- **Decisão Vitor**: `academic` (English, conciso)
- **URL final**: `/academic`
- **Conteúdo** (movido de `about.astro` per 2.5):
  - **Section: Education**
    - PhD in Information Systems Engineering & Management · Harrisburg University, PA · 2026 – 2030 (in progress, badge)
    - M.Sc. in Sustainable Design & Construction Management · Thomas Jefferson University, PA · 2021 – 2023 + 2 photos (thesis defense + commencement)
    - MBA in Real Estate & Construction Business Management · FGV, Brazil · 2012 – 2016
    - Bachelor of Architecture and Urban Planning · UEG, Brazil · 2004 – 2009 + 2 photos (UEG CBA 2006 + formatura 2009)
  - **Section: Languages**
    - Portuguese (native or bilingual)
    - English (full professional)
- **Cross-links** (rodapé):
  - "Active credentials with verification IDs on [credentials](/credentials)"
  - "Awards & honors on [awards](/awards)"
- **Layout**: mirror `/credentials.astro` aesthetic (max-w-4xl, eyebrow + h1 + sections)
- **Assets**: reaproveitar imports de `about.astro` linhas 3–8 (thesisDefenseImg, commencementImg, uegCbaImg, uegFormaturaImg)
- **Navigation**: adicionar link "Academic" no `SiteHeader.astro` (provavelmente entre About e Experience)

---

## 13 · PAGINA PRESS KIT + ADMIN LAYER (security restructure + future newsletter)

### 13.1 Public press-kit — minimal restructure [RESOLVED]
- **Decisão Vitor sintetizada**: estrutura literal da Sarah confirmada
- **Novo conteúdo público** de `src/pages/press-kit.astro`:
  - Headshot (lower-res, watermarked com "Sarah Rodovalho · sarahrodovalho.com" no canto)
  - One short bio (~280 chars):
    > Sarah Rodovalho is an Integrated Design Manager at Aligned Data Centers and a doctoral researcher at Harrisburg University, with 16+ years delivering capital programs across hyperscale data centers, advanced manufacturing, and large-scale infrastructure in the U.S. and Brazil. She serves on the AIA Construction Contract Administration Knowledge Community Leadership Board (2026–2030).
  - Pronunciation guide (display name + IPA somente; **remove** legal name completo "Sarah Faria Alcantara Macedo Rodovalho")
  - Contact email `sarah@sarahrodovalho.com`
  - CTA: "For high-resolution images, extended bios, or quick-fact sheets, email me directly."
- **REMOVED do público**: BIO_MEDIUM (~810 chars), BIO_LONG (~1850 chars), QUICK_FACTS array, hi-res photo downloads, legal name

### 13.2 Gate type — Lighter (direct email) [RESOLVED]
- **Decisão Vitor**: ✅ Opção A — Lighter gate / direct email
- **Implementação**: copy-only no `press-kit.astro` público; sem form/captcha/backend

### 13.3 Admin layer — re-analysis [RESOLVED → architecture decision]
- **Decisão Vitor**: "sarah está sugerindo de a página ter uma camada logada, ou seja que ela possa entrar no site como admin e ter uma sessao visivel somente a ela"
- **Casos de uso**:
  1. Sarah usa o site durante apresentações — admin-view expõe info não-pública sem precisar abrir outros tabs/files
  2. Future: Substack-style newsletter archive (como [dfolloni.substack.com/archive](https://dfolloni.substack.com/archive)) — onde subscribers leem newsletters da Sarah
  3. Gated press-kit assets (BIOs longas, hi-res photos, quick-facts, employer-specific refs) ficam acessíveis a Sarah logada
- **Re-análise — opções de auth provider**:

  | Provider | Custo | Effort | Pattern já no household | Recomendação |
  |---|---|---|---|---|
  | **Cloudflare Access** (Zero Trust) | Free (até 50 users) | Baixo (config wrangler.toml + Access policy) | ✅ orenu.vitormr.dev usa Email OTP | ⭐ **Recomendado** |
  | Clerk | Free (até 10k MAU) | Médio (React/JS SDK) | ❌ | Overkill p/ 1 user |
  | Auth.js (NextAuth) | Free | Médio-alto (requer DB) | ❌ | Não cabe — site é Astro static |
  | Supabase Auth | Free tier ok | Alto (novo projeto Supabase) | ❌ | Custo cognitivo desnecessário |

- **Decisão final (single source of truth)**:
  - **Auth**: Cloudflare Access (Email OTP, free tier, Sarah's email allowlist)
  - **Routes**: `/admin/*` protegido por Access policy em `wrangler.toml`
  - **Páginas admin (initial)**:
    - `src/pages/admin/index.astro` — dashboard placeholder com links pra outras admin pages
    - `src/pages/admin/press-kit-full.astro` — conteúdo full do press-kit original (BIO_MEDIUM, BIO_LONG, QUICK_FACTS, hi-res photo downloads, legal name)
    - `src/pages/admin/newsletter.astro` — placeholder com external link to Substack archive (quando Sarah criar)
  - **Wrangler config (delta to add)**:
    ```toml
    # wrangler.toml
    [[env.production.access]]
    name = "Sarah admin"
    type = "self_hosted"
    domain = "sarahrodovalho.com"
    paths = ["/admin/*"]
    require_email = ["sarah@sarahrodovalho.com"]
    ```
- **Justificativa Cloudflare Access pick**:
  - Já tem em casa (orenu.vitormr.dev gate descrito em `decisions/ADR-013-security.md` e `docs/runbooks/cloudflare-access-gate-orenu.md`) — runbook + experiência operacional já existem
  - Zero código de auth (no JWT handling, no session management) — Cloudflare cuida; assets server-side normais
  - Email OTP UX já validado para Sarah (mesmo padrão Vitor + Sarah usam em Orenu)
  - Custo $0 até 50 users (Sarah só precisa de 1 user)

### 13.4 Substack newsletter — placeholder now, integration later [RESOLVED]
- **Decisão Vitor**: "placeholder para futuro, dando voz a tudo que ela tem a dizer via newsletter no substrack"
- **Phase 1 (PR-S07b)**: `/admin/newsletter.astro` placeholder text — "Sarah's newsletter archive will appear here. External link → [substack URL when published]"
- **Phase 2 (FUTURE PR-S13)**: quando Sarah publicar Substack:
  - Pull RSS feed via build-time script (`scripts/sync_substack.py`)
  - Render archive em `/newsletter` (público!) — newsletter content é PARA ser lido pelo público (não admin-gated)
  - Cron rebuild (Cloudflare Pages auto-deploy on schedule)
  - Pattern espelha o `dfolloni.substack.com/archive` referência citada por Vitor
- **OPSEC note**: Substack URL pública por design — não-PII. Tags como "AI · construction · women in tech" alinham com personal branding pattern Sarah já tem.

---

## 14 · NOVA PÁGINA · Contact — NEW `src/pages/contact.astro`

Detalhado em 3.3 acima.

---

## 🔍 CLARIFY resolutions summary

| ID | Item | Resolution |
|---|---|---|
| 01 | Hero ending | "multi-hundred-megawatt campus" |
| 02 | Big numbers | 7M+ sq ft + ~$1.5B+ total program value (PMI slide 29) |
| 03 | Bio ending | Same as 01 — "multi-hundred-megawatt campus" |
| 04 | "Current Engagements" | ✅ confirmed |
| 05 | PhD bullet | Keep in Now (already there); ALSO appears in /academic Education |
| 06 | Academic page | NEW `/academic` w/ Education + Languages (data-driven decision) |
| 07 | Kept slug | `/experience` (work.astro deprecated, 301 to /experience) |
| 08 | CV content audit | `highlights: []` empty in MDX; sensitive bullets → gitignored `_private/` |
| 09 | Contact slug | `/contact` (English) |
| 10 | Date format | Year only (no month) |
| 11 | USA convention | All cards apply same pattern |
| 12 | Intro paragraph | Keep first sentence only |
| 13 | abstract+body split | 1st para → frontmatter abstract; 2nd para → MDX body |
| 14 | Card 01 callouts | Inference confirmed (CONTEXT / INTEGRATION / REGION / METHODOLOGY) |
| 15 | CONTRIBUITION | → CONTRIBUTION (typo fix) |
| 16 | Purple card 04 | `&amp;` HTML entity leak; sweep needed |
| 17 | Red card 04 | Month elimination (per 4.1 convention) |
| 18 | Card 04 callouts | Auto-fill: BUDGET / $232M + IMPACT / Framework adopted nationally |
| 19 | Photo position | All cards photo BELOW text |
| 20 | Card 06 title | "Healthcare planning & design" (drop "clinical") |
| 21 | Brown arrow | "Beyond the case studies" → "Beyond the selection" |
| 22 | Lavender "assistant" | "teaching at TJU" → "teaching assistant at TJU" in Beyond prose |
| 23 | Upcoming events | Build placeholder NOW with empty-state pattern + dynamic engagement filter |
| 24 | Watermark scope | Embedded-in-image (binary modification), NOT just page-level overlay |
| 25 | Watermark text | "© Sarah Rodovalho · sarahrodovalho.com" diagonal repeated |
| 26 | Academic slug | `/academic` ✅ |
| 27 | Press-kit gate | Lighter gate (direct email) ✅ |
| 28 | Admin storage | Logged-in admin layer via Cloudflare Access Email OTP |

**All 28 resolved. Ready to implement.**

---

## 📋 Updated PR sequencing (7 PRs)

### PR-S07a · Press Kit minimal public restructure ⚠️ URGENT SECURITY
- **Scope**:
  - `src/pages/press-kit.astro` → minimal public layer per 13.1
  - Generate low-res watermarked headshot (`scripts/watermark-headshot.py` new) → `public/press/sarah-rodovalho-headshot-public.jpg`
  - Keep `mailto:` CTA only (no form)
  - Remove BIO_MEDIUM, BIO_LONG, QUICK_FACTS, hi-res photo downloads, legal name from public view
- **Files**: `src/pages/press-kit.astro`, `public/press/*.jpg` (regen), `scripts/watermark-headshot.py` (new), `.gitignore` (add `public/press/_originals/`)
- **Done criterion**: opened `/press-kit` shows minimal layer; legal name + hi-res not on public DOM

### PR-S07b · Admin layer skeleton (Cloudflare Access)
- **Scope**:
  - Add Cloudflare Access policy in `wrangler.toml` for `/admin/*` (Sarah's email allowlist)
  - NEW `src/pages/admin/index.astro` (dashboard placeholder w/ navigation to sub-pages)
  - NEW `src/pages/admin/press-kit-full.astro` (BIO_SHORT + BIO_MEDIUM + BIO_LONG + QUICK_FACTS + hi-res photo downloads + legal name — content moved here from press-kit.astro)
  - NEW `src/pages/admin/newsletter.astro` (placeholder + external Substack link slot)
  - Update `worker.js` if needed to coordinate with Access (typically not — Access intercepts at edge)
  - Cloudflare Pages settings UI: enable Access policy
- **Depends on**: PR-S07a (press-kit.astro must be already cleaned before content moves to admin)
- **Done criterion**: `/admin/*` requires email-OTP login; Sarah logs in successfully; press-kit-full content visible in admin

### PR-S08 · Home + About copy edits (safe parallel)
- **Scope**:
  - `src/pages/index.astro`:
    - Hero text: remove "on a multi-building, ~264 MW campus" (1.1)
    - Stats swap: `264 MW` → `7M+` / `Square feet delivered`; `$279 M+` → `~$1.5B+` / `Total program value` (1.2)
  - `src/pages/about.astro`:
    - Bio: replace "multi-building campus" → "multi-hundred-megawatt campus" (2.1)
    - Rename "Now" → "Current Engagements" (2.2)
    - First bullet: "~264 MW multi-building" → "multi-hundred-megawatt" (2.3)
- **Files**: `src/pages/index.astro`, `src/pages/about.astro`
- **Independent of PR-S07a/b** — can run in parallel

### PR-S09 · About CV-block removal + NEW Academic + NEW Contact
- **Scope**:
  - REMOVE from `src/pages/about.astro`: section Selected past roles, section Education, section Certifications & affiliations, section Languages (2.5)
  - NEW `src/pages/academic.astro` w/ Education + Languages (12.1) — moves assets imports from about.astro
  - NEW `src/pages/contact.astro` simples (3.3)
  - Update `src/components/SiteHeader.astro` navigation: add "Academic" + "Contact" links
- **Files**: `src/pages/about.astro`, NEW `src/pages/academic.astro`, NEW `src/pages/contact.astro`, `src/components/SiteHeader.astro`
- **Depends on**: PR-S08 (about content stabilized first)

### PR-S10 · Work → Experience merge + photo position + entity sweep
- **Scope**:
  - Move `work.astro` rich case-study layout INTO `experience.astro` (3.1)
  - DELETE `src/pages/work.astro`
  - Add 301 redirect `/work` → `/experience` in `worker.js`
  - Photo position: ALL 6 cards photo BELOW text instead of above (8.3, 19)
  - Rename "Beyond the case studies" → "Beyond the selection" (9.6, 21)
  - Add "Assistant" to teaching mention in Beyond prose (9.7, 22)
  - Audit `experience/*.mdx` × 7: empty `highlights: []`, move sensitive bullets to NEW `_private/experience-detailed.md` (3.2, 8)
  - Add `_private/` to `.gitignore`
  - Intro paragraph: keep first sentence only (3.1, 12)
  - **Sweep `&amp;` HTML entity leaks** (7.1, 16, 20) — grep all MDX + Astro files for double-encoded ampersands
- **Files**: `src/pages/experience.astro` (replaced), `src/pages/work.astro` (deleted), `worker.js`, `src/content/experience/*.mdx` (×7), NEW `_private/experience-detailed.md`, `.gitignore`, MDX/Astro sweep
- **Depends on**: PR-S09 (academic page exists so /experience doesn't need to host past-roles overlap)

### PR-S11 · Case studies batch (cards 01–06)
- **Scope**: 6 MDX file updates per items 4–9:
  - All 6: location `USA`/`Brazil`, period year-only convention, abstract+body split
  - Card 01 Aligned (4.4, 4.5)
  - Card 02 Microsoft CO+I (5.3, 5.4 + CONTRIBUTION typo fix)
  - Card 03 Tesla (6.3, 6.4)
  - Card 04 Passeio (7.4, 7.5 + auto-fill pink/orange)
  - Card 05 BRT (8.2)
  - Card 06 Virtua (9.1 title trim + 9.4 body + 9.5 callouts)
- **Files**: `src/content/projects/*.mdx` (×6)
- **Depends on**: PR-S10 (experience page layout stable)

### PR-S12 · Speaking watermarks + PMI talk rewrite + upcoming events placeholder
- **Scope**:
  - NEW `scripts/watermark-images.py` (Pillow, diagonal multi-instance pattern)
  - Watermark all PMI deck slide assets in `src/assets/speaking/*` (11.2, 24, 25)
  - Move originals to `src/assets/speaking/_originals/` (`.gitignore` add)
  - Rewrite `pmi-women-construction-follow-the-sun-2026.mdx` `abstract:` (11.3)
  - ADD upcoming-events section at top of `speaking.astro` (11.1, 23):
    - Split `engagements` by `date >= today` vs `< today`
    - Render "Upcoming engagements" section with cards (if any) or empty state
  - Optional: add Schema.org `Event` JSON-LD for upcoming events too (consistency)
- **Files**: `src/pages/speaking.astro`, `src/content/engagements/pmi-women-construction-follow-the-sun-2026.mdx`, `src/assets/speaking/*` (regen), NEW `scripts/watermark-images.py`, `.gitignore`
- **Depends on**: PR-S11 (work/experience merge stable; speaking page can be touched independently but ordering keeps cognitive load low)

---

## Implementation order summary

```
PR-S07a (Press Kit minimal public — security urgent)
 │
 ├─► PR-S07b (Admin layer skeleton + content move)
 │
PR-S08 (parallel-safe copy edits — Home + About)
 │
 └─► PR-S09 (About CV removal + new Academic + new Contact)
      │
      └─► PR-S10 (Work → Experience merge + photo position + entity sweep)
           │
           └─► PR-S11 (case studies batch)
                │
                └─► PR-S12 (speaking watermarks + PMI rewrite + upcoming events)
```

Estimated effort:
- PR-S07a: 0.5 session (asset gen + page rewrite)
- PR-S07b: 1 session (Cloudflare Access config + 3 admin pages skeleton)
- PR-S08: 0.5 session
- PR-S09: 1 session (3 page touches + nav)
- PR-S10: 1.5 sessions (merge + photo refactor + sweep + audit)
- PR-S11: 1 session (6 MDX files)
- PR-S12: 1 session (script + 6 assets + page + abstract)
- **Total**: ~6.5 sessions to ship Sarah's full review

---

## Future (post-Sarah-review-PRs)

- **PR-S13**: Substack newsletter integration when Sarah publishes (13.4 phase 2) — RSS feed pull + build-time render at `/newsletter`
- **PR-S14**: Orenu ADR-024 phase 1b `fact_speaker_engagement` — auto-PR from engagement MDX into Orenu data layer

---

## Next step

1. **Vitor reviews this v2 doc** — sanity check my interpretations of all CLARIFYs + the 3 architectural decisions (2.5 / 11.1 / 13.4)
2. **Confirm PR-S07a starts now** OR identify any blocker I missed
3. **Start implementing**

> Sarah's clarifications were exhaustive — there are no open blockers. We're ready to start at PR-S07a.

---

**Document maintained**: living doc until all 7 PRs ship. Each PR closes its corresponding items here; update status column from "Resolved" → "Shipped" as PRs merge.
