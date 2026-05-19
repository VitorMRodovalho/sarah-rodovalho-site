# Site Review · Sarah · OneNote "Ajustes do site"

**Source**: `~/Downloads/A/My Notebook.pdf` — exported from OneNote notebook **AIA2025**, seção **Ajustes do site**, dated Monday, May 18, 2026, 3:41 PM
**Author of review**: Sarah Faria Alcantara Macedo Rodovalho
**Transcribed/mapped by**: Vitor + Claude (Anthropic), 2026-05-18
**Mapping discipline**: every action item below cites the OneNote PDF page number where the comment + screenshot appears. Items flagged `CLARIFY` require Sarah/Vitor input before implementation.

---

## Cor-code legend (used by Sarah)

| Marca | Significado | Where |
|---|---|---|
| 🔴 **Vermelho** (riscado/contorno) | Retirar | Body copy + callout labels |
| 🟡 **Amarelo** (highlight) | Trocar / mudar para — | Numbers, dates, locations |
| 🔵 **Azul** (highlight) | Adicionar | New items to add |
| 🟢 **Verde** | Categoria de callout (slot 1) | Scope card callouts |
| 🩷 **Rosa/Pink** | Categoria de callout (slot 3) | Scope card callouts |
| 🟠 **Laranja/Orange** | Categoria de callout (slot 4) | Scope card callouts |
| 🟣 **Roxo/Purple** | Corrigir | Punctual fixes (typos, formatting) |
| ➡️ **Seta rosa** | Realocar | Move block/photo |
| ➡️ **Seta marrom (brown)** | Trocar tag/label | Source/credit tag |
| ➡️ **Seta lavanda** | Incluir | Add specific item nearby |

**Callout slot convention** (inferred from cards 02–06 explicit labels): each case study card has 4 callout pills. Sarah's color code maps to **slots**:
- 🟢 Green = slot 1 (Context / Initiative / Scale-up / Schedule / Scope)
- 🔵 Blue = slot 2 (Integration / Scope / Tower / Tenants managed)
- 🩷 Pink = slot 3 (Contribution / Category / Renovation)
- 🟠 Orange = slot 4 (Methodology / Recognition / Domain / Program)

> Today's MDX schema has a single `scope: [{label, value}]` array — slot order in the array maps to display position. Color is rendered by the component (not stored in MDX).

---

## Index — pages reviewed

| # | OneNote section | PDF pgs | Repo target | Density | Type |
|---|---|---|---|---|---|
| 1 | PAGINA DE ENTRADA | 1 | `src/pages/index.astro` | Média | Copy + stats replace |
| 2 | PAGINA ABOUT | 2–4 | `src/pages/about.astro` | **Alta** | Restructure + copy edits |
| 3 | PAGINA WORK / EXPERIENCE merge | 3 | `src/pages/work.astro` + `src/pages/experience.astro` | **Alta — estrutural** | Merge pages + remove CV exposure |
| 4 | Case 01 Aligned hyperscale | 3–4 | `src/content/projects/aligned-multi-building-campus.mdx` | Alta | Body + callouts + date format |
| 5 | Case 02 Microsoft CO+I CLT | 5 | `src/content/projects/microsoft-coi-hyperscale-program.mdx` | Alta | Body + callouts |
| 6 | Case 03 Tesla Lathrop | 5 | `src/content/projects/tesla-industrial-rd-portfolio.mdx` | Alta | Body + callouts |
| 7 | Case 04 Passeio das Águas | 5 | `src/content/projects/passeio-das-aguas-shopping.mdx` | Média | Body + 2 callouts (verde/azul); restantes CLARIFY |
| 8 | Case 05 Goiânia BRT | 5 | `src/content/projects/goiania-brt-network.mdx` | Média | Body + photo position + Experience link |
| 9 | Case 06 Virtua Healthcare | 5–6 | `src/content/projects/array-architects-healthcare.mdx` | Alta | Body + callouts + 2 arrows |
| 10 | PAGINA RESEARCH | 6 | `src/pages/research.astro` | **Zero** | "Não alterar por hoje" |
| 11 | PAGINA SPEAKING | 6 | `src/pages/speaking.astro` + `src/content/engagements/*` | Média | Watermark slide assets + rewrite talk description |
| 12 | **NOVA**: Academic / Past Studies | 7 | NEW `src/pages/academic.astro` (or reuse `experience.astro`) | Criar | Receive content removed from About |
| 13 | PAGINA PRESS KIT | 7 | `src/pages/press-kit.astro` | **CRÍTICA** | Security restructure: admin-only + public/gated layers |
| 14 | **NOVA**: Contate-me | 3 | NEW `src/pages/contact.astro` | Criar | Simple contact page |

**14 estruturas tocadas + ~30 itens granulares de copy edit dentro delas.**

---

## 1 · PAGINA DE ENTRADA (home) — `src/pages/index.astro`

> **PDF p. 1.** Section header "PAGINA DE ENTRADA".

### 1.1 Hero copy — remove "multi-building, ~264 MW campus"
- **Comentário OneNote**: tag `REMOVER` abaixo do screenshot do hero
- **Strikethrough vermelho**: "on a multi-building, ~264 MW campus" dentro do parágrafo intro do hero
- **Ação**: `copy-edit` — remover essa frase específica do hero copy (provavelmente está no body do `index.astro` ou em props passados ao componente Hero)
- **Alvo**: `src/pages/index.astro` — texto hero atual: "I am Sarah Rodovalho — a senior design and project leader, architect by training, with 16+ years delivering capital programs across hyperscale data centers, advanced manufacturing, healthcare, and large-scale retail in the U.S. and Brazil. Currently **Integrated Design Manager at Aligned Data Centers** on a multi-building, ~264 MW campus, while pursuing a PhD in Information Systems Engineering at Harrisburg University."
- **CLARIFY-01**: deixar "Currently Integrated Design Manager at Aligned Data Centers" terminando aí, ou substituir por "on a multi-hundred-megawatt campus" (consistência com substituição equivalente no About — ver item 2.3)?

### 1.2 Big numbers — trocar 264 MW + $279 M+
- **Comentário OneNote**: "Remover e pegar os outros big numbers que tenho na apresentaçao do PMI follow the Sun"
- **Yellow highlight**: stats "264 MW" e "$279 M+" no bloco "By the numbers / Scale, scope, and a research record"
- **Stats atuais visíveis**: `16+` (Years in delivery — Brazil), `264 MW` (Current campus scope), `$279 M+` (Microsoft change orders), `3` (UAC · Sustainability · MDPI papers)
- **Ação**: `asset-replace` — trocar `264 MW` e `$279 M+` por outros big numbers da apresentação **PMI Women in Construction · Follow the Sun · 2026**
- **Alvo**: `src/pages/index.astro` (stats block, likely defined as array near top of frontmatter)
- **CLARIFY-02**: quais 2 big numbers da PMI Follow the Sun? Precisa da Sarah indicar. Candidatos lógicos olhando o conteúdo dela (publicações, projetos): números do paper IJAC 2026 / Sustainability 2025 / case studies ARCC. Pedir a Sarah listar os 2 que ela quer ver na home.
  - Source possível: `src/content/engagements/pmi-women-construction-follow-the-sun-2026.mdx` (já existe no repo) — verificar se já temos os números.

---

## 2 · PAGINA ABOUT — `src/pages/about.astro`

> **PDF pp. 2–4.** Section header "PAGINA ABOUT".

### 2.1 Bio narrative — remove "on a multi-building campus"
- **Comentário OneNote**: tag `REMOVER`
- **Strikethrough vermelho**: "on a multi-building campus" no parágrafo "I currently work at Aligned Data Centers as Integrated Design Manager **on a multi-building campus**"
- **Ação**: `copy-edit`
- **Alvo**: `src/pages/about.astro` linha ~63 — `<p>I am a senior design and project leader and architect with 16+ years delivering complex capital programs ... I currently work at Aligned Data Centers as Integrated Design Manager on a multi-building, ~264 MW campus.</p>`
- **Trocar para**: `I currently work at Aligned Data Centers as Integrated Design Manager.` (sem frase de localização/scope)
- **CLARIFY-03**: ou substituir por "on a multi-hundred-megawatt campus" pra manter o framing de scale sem precisar mexer toda vez que o campus crescer? Linkado com CLARIFY-01.

### 2.2 Section "Now" — rename to "Current Engagements"
- **Comentário OneNote**: "AMARELO HIGHLIGHT #1 - MUDAR PARA : Current Engadements (ou algo do tipo que mostre onde estou engajada ou envolvida atualmente)"
- **Yellow highlight**: o título "Now" e o subtítulo da section
- **Ação**: `copy-edit`
- **Alvo**: `src/pages/about.astro` linha 117 — `<h2 class="font-display text-2xl sm:text-3xl tracking-tight">Now</h2>`
- **Trocar para**: `Current Engagements`
- **CLARIFY-04**: Sarah escreveu "Engadements" (typo) — confirmar "Current Engagements" é a versão final.

### 2.3 First bullet — "across a ~264 MW multi-building campus"
- **Comentário OneNote**: "AMARELO HIGHLITGH #2 - Mudar para -- on a multi-hundred-megawatt campus"
- **Yellow highlight**: "across a ~264 MW multi-building campus" no primeiro `<li>` da section Now
- **Ação**: `copy-edit`
- **Alvo**: `src/pages/about.astro` linhas 122–124 — `Leading integrated design management across a ~264 MW multi-building campus.`
- **Trocar para**: `Leading integrated design management on a multi-hundred-megawatt campus.`

### 2.4 Add PhD as current engagement (já existe? confirmar position)
- **Comentário OneNote**: "AZUL HIGHLITGH - addicionar meu PHS aqui como algo que estou engajada nesse momento tb."
- **Blue highlight**: trecho onde o PhS [PhD] deveria entrar como item da section "Now"
- **Status atual**: já existe na about.astro linhas 125–130 como segundo `<li>` (`PhD candidate ... Harrisburg University ... in progress, expected Dec 2030`)
- **CLARIFY-05**: Sarah escreveu "addicionar" mas o item **já existe** na página. Ela quer:
  - (a) Confirmar que está OK (no-op para 2.4)?
  - (b) Reposicionar (talvez mover pra primeiro ou destacar)?
  - (c) Reformular o texto?
  - **Recomendação default** se Sarah não responder: no-op + reportar "já presente — confirmar se está como você quer".

### 2.5 Remover bloco CV completo da About — mover pra nova página
- **Comentário OneNote**: "REMOVEER TODA ESSA PARTE DA PAGINA INICIAL DO SITE / Ta muito curriculo, o ideal eh separar - o principal chamariz ja esta na parte principal que eh o textinho e no que to trabalhando atualmente / Fora que algumas coisas duplica nas outras abas entao eh desnecessario estar aqui"
- **Tag**: `REMOVER` aplicado a (do que vejo no PDF):
  - section "Selected past roles" (about.astro linhas 202–251)
  - section "Education" (about.astro linhas 253–353)
  - section "Certifications & affiliations" (about.astro linhas 355–399)
  - section "Languages" (about.astro linhas 401–408)
- **Reasoning da Sarah**: a página está muito CV, o "chamariz" principal já está no bio header + section Now; duplica conteúdo de `/credentials` e `/experience`
- **Ação**: `restructure` — remover essas 4 sections do `about.astro`; mover conteúdo para nova página **Academic/Past Studies** (ver item 12) ou consolidar com pages existentes (`/experience` e `/credentials`)
- **CLARIFY-06**: a Sarah pede "criar uma página dedicada para experiências acadêmicas/passado de estudos" (PDF p.7). Já existem `experience.astro` + `credentials.astro` + `awards.astro`. Três opções:
  - (a) Criar `src/pages/academic.astro` consolidando Education + Past roles + Certs + Languages (single new page conforme literal da Sarah). Risk: dup com pages existentes.
  - (b) Mover Education + Languages para `experience.astro` (que já tem Past roles?), Certs ficam em `credentials.astro` (já existem lá).
  - (c) Manter `experience.astro` como "Past roles" + criar novo `academic.astro` só pra Education + Languages.
  - **Recomendação default**: (a) — mais fiel à fala literal da Sarah "criar uma página dedicada", e mais simples de implementar. **Verificar primeiro se `experience.astro` e `credentials.astro` já têm o conteúdo equivalente — se sim, remover duplicação na hora de criar o academic.astro.**

### 2.6 Páginas Education/Certs/Past roles podem já estar duplicadas
- **Comentário OneNote** (inferido): "Fora que algumas coisas duplica nas outras abas entao eh desnecessario estar aqui"
- **Ação investigativa**: ler `src/pages/experience.astro` + `credentials.astro` + `awards.astro` antes de implementar 2.5/12, identificar dups, decidir merge vs new.
- **TODO (Vitor)**: tarefa de implementação — read pre-implementation.

---

## 3 · PAGINA WORK / EXPERIENCE merge — `src/pages/work.astro` + `src/pages/experience.astro`

> **PDF p. 3.** Section header "PAGINA WORK".

### 3.1 Merge das duas páginas Work + Experience
- **Comentário OneNote**: "Fazer o merge com a pagina Experience - trazer a foto e o link para junto de cada experiencia"
- **Ação**: `restructure` — fundir `work.astro` + `experience.astro` em uma única página (provavelmente `work.astro` permanece e `experience.astro` é removida via redirect, ou vice-versa)
- **Critério**: cada experiência (item do `src/content/experience/*.mdx`) deve aparecer junto com sua foto + link pro case study correspondente em `src/content/projects/*.mdx`
- **CLARIFY-07**: qual page name fica? `/work` ou `/experience`? Recomendação: `/work` (mais curto, foco no portfolio) + 301 redirect de `/experience` → `/work`.

### 3.2 NÃO expor currículo aberto
- **Comentário OneNote**: "nao usar nada dos items do meu currrulo descrito na pagina experiencia (isso eh dado somente para curriculo nao pode ser divulgado abertamente) caso precise posso mandar para alguem separado"
- **Ação**: `security` / `content-discipline` — auditar `experience.astro` + `src/content/experience/*.mdx` removendo qualquer item que seja CV-style com detalhamento extenso (números internos, employer-specific metrics não-públicos, etc.)
- **CLARIFY-08**: o que constitui "items do currículo descrito"? Sarah precisa indicar especificamente o que retirar. Recomendação default: comparar conteúdo `experience/*.mdx` com o **bio public** da press-kit BIO_SHORT (~280 chars) — tudo além desse nível de detalhe pra cada experiência deve ser revisto.
- **TODO (Sarah)**: passar checklist do que retirar específico, OU passar o CV em PDF separado pra Vitor anexar à pasta admin gated (não-public).

### 3.3 Criar página Contate-me
- **Comentário OneNote**: "Criar uma pagina contate-me simples"
- **Ação**: `new-page`
- **Alvo**: NEW `src/pages/contact.astro`
- **Escopo "simples"**:
  - Headline "Get in touch" (ou "Contact" / "Contate-me" — CLARIFY-09 abaixo)
  - Email único `sarah@sarahrodovalho.com` (mailto link)
  - LinkedIn link
  - Press inquiries → link pra `/press-kit` (já existe)
  - Localização: "Based in Leesburg, Virginia · Washington DC – Baltimore region"
  - **NÃO** incluir form (per content-discipline atual + Sarah pediu "simples")
- **CLARIFY-09**: page slug e nome? `/contact` (English-first, alinhado com restante do site) ou `/contato` (PT)?
- **Recomendação default**: `/contact` (English-first per CLAUDE.md "Language: English primary").

---

## 4 · Case 01 · Aligned hyperscale campus — `src/content/projects/aligned-multi-building-campus.mdx`

> **PDF pp. 3–4.** First case study card screenshot.

### 4.1 Datas — só anos, USA
- **Comentário OneNote**: "Data colocar somente anos 2025/2026 - USA"
- **Yellow highlight**: período atual "Oct 2025 - present | Virginia & Maryland, U.S."
- **Ação**: `copy-edit`
- **Alvo MDX**:
  - `period: "Oct 2025 — present"` → **trocar para** `period: "2025 — present · USA"` (ou similar)
  - `location: "Virginia & Maryland, U.S."` → simplificar pra `location: "USA"`
- **CLARIFY-10**: manter o formato `Oct 2025` ou somente `2025`? Sarah disse "somente anos" → `2025 — present`.
- **CLARIFY-11**: outros cards seguem o mesmo padrão? Cards 02, 03, 06 também têm `#1 yellow — trocar para USA` — ver itens 5.1, 6.1, 9.2.

### 4.2 Strikethrough vermelho — bloco intro narrative do /work
- **Comentário OneNote**: implícito no risco vermelho do screenshot principal — o parágrafo "Six selected programs from a 16+ year career in the U.S. and Brazil. Each entry pairs scope-numbers with the role I held..."
- **Ação**: `copy-edit` — remover esse intro paragraph (parece estar no `work.astro` como header da page, não no MDX do case 01)
- **Alvo**: `src/pages/work.astro` (verificar header text antes de implementar)
- **CLARIFY-12**: confirmar com Sarah que esse texto inteiro vai ser removido (não só editado). Alternativa: trocar por algo mais conciso/menos CV-style.

### 4.3 Strikethrough vermelho — callout tags "Multi-building" + "Design management"
- **Comentário OneNote**: risco vermelho nas tags
- **Status MDX atual**:
  ```
  scope:
    - { label: "Campus capacity", value: "~264 MW" }
    - { label: "Buildings", value: "Multi-building" }
    - { label: "Region", value: "DC-Baltimore" }
    - { label: "Discipline", value: "Design management" }
  ```
- **Ação**: `copy-edit` — substituir os 4 callouts pelos novos abaixo (4.5)

### 4.4 Body text — rewrite
- **Comentário OneNote**: texto completo escrito pela Sarah na p. 4
- **Novo abstract/body**:
  > Hyperscale campuses don't get strained because any one workflow is hard. They get strained because design, permitting, underground systems, and field execution all move in parallel — and the toughest problems live in the gaps between them.
  >
  > That's the work at Aligned. I lead owner-side integrated design on a multi-building campus, coordinating trade workstreams across mixed delivery models. A few frameworks have crystallized along the way — for permitting, underground coordination, and handoff.
- **Ação**: `copy-edit`
- **Alvo MDX**: `abstract:` (linhas 13–18 do .mdx) + body markdown abaixo do frontmatter
- **CLARIFY-13**: split entre `abstract` (frontmatter, mostrado no card) e `body markdown` (mostrado no detail page)? Recomendação: 1º parágrafo vai no `abstract`, 2º parágrafo vai no body markdown.

### 4.5 Novos callouts (4 slots — VERDE/BLUE/PINK/ORANGE)
- **Comentário OneNote** (p.4 transcript literal):
  - "VERDE / Context"
  - "BLUE / DUAL-TRACK DELIVERY / Integration / Disciplines/trades/Vendors"
  - "PINK / NoVA/Maryland corridor"
  - "ORANGE / Methodology / Field-tested governance frameworks"
- **Inferência (split label/content per pattern dos cards 02–06)**:
  - **Slot 1 (Green)**: label `CONTEXT` · value `Dual-track delivery` *(inferido — "Dual-track delivery" parece ser o highlight do conceito; alternativa: value="Integration")*
  - **Slot 2 (Blue)**: label `INTEGRATION` · value `Disciplines / trades / Vendors`
  - **Slot 3 (Pink)**: label `REGION` *(inferido, sem label explícito do Sarah)* · value `NoVA / Maryland corridor`
  - **Slot 4 (Orange)**: label `METHODOLOGY` · value `Field-tested governance frameworks`
- **CLARIFY-14** ⚠️ **AMBIGUIDADE PRINCIPAL DESTE CARD**: o parse acima é a melhor leitura possível, mas o card 01 é o único onde Sarah não escreveu explicitamente o split entre LABEL e VALUE. Os outros cards (02–06) seguem o padrão `COR / LABEL / VALUE` ou `COR / LABEL / linha1 / linha2`. Para 01 ela escreveu:
  - `VERDE / Context` → 1 token só (label? value?)
  - `BLUE / DUAL-TRACK DELIVERY / Integration / Disciplines/trades/Vendors` → 3 tokens
  - `PINK / NoVA/Maryland corridor` → 1 token só
  - `ORANGE / Methodology / Field-tested governance frameworks` → 2 tokens
  - **Pedir clarificação direta da Sarah** — alternativa: ela define cada par {label, value} explicitamente, ou confirma a inferência acima.

---

## 5 · Case 02 · Microsoft CO+I CLT — `src/content/projects/microsoft-coi-hyperscale-program.mdx`

> **PDF p. 5.** Second case study card screenshot.

### 5.1 Yellow #1 — location → USA
- **Comentário**: "#1 amarelo trocar para USA"
- **Ação**: `copy-edit` — trocar location para `USA`

### 5.2 Yellow #2 — período (formato simplificado)
- **Comentário**: "#2 amarelo - trocar para -"
- **Ação**: `copy-edit` — formato simplificado de período (anos, USA), consistente com 4.1

### 5.3 Body text — rewrite
- **Novo abstract/body**:
  > Hyperscale data centers are some of the most carbon-intensive structures in modern construction. Microsoft's mass-timber pilot in Northern Virginia is the industry's first serious attempt to change that — a hybrid cross-laminated timber, steel, and concrete design targeting 35% less embodied carbon than steel and 65% less than precast concrete.
  >
  > I was on the first team. The visible work was construction contracts and change-order management across several concurrent builds. Development of change-order framework that ended up used across projects — and a CO+I team award.

### 5.4 Callouts (4 slots — explícitos pela Sarah)
- **GREEN** · label `INITIATIVE` · value `First-team CLT data centers (FOK)`
- **BLUE** · label `SCOPE` · value `Concurrent hyperscale portfolio`
- **PINK** · label `CONTRIBUITION` *(Sarah escreveu com este spelling — keep ou normalize para `CONTRIBUTION`?)* · value `Change-order framework`
- **ORANGE** · label `RECOGNITION` · value `CO+I Team Award · FY25`
- **CLARIFY-15**: spelling `CONTRIBUITION` → `CONTRIBUTION` (typo fix)? Recomendação default: corrigir.

---

## 6 · Case 03 · Tesla Lathrop — `src/content/projects/tesla-industrial-rd-portfolio.mdx`

> **PDF p. 5.** Third case study card screenshot.

### 6.1 Yellow #1 — location → USA
- **Ação**: `copy-edit` — location `USA`

### 6.2 Yellow #2 — período (formato simplificado)
- **Ação**: `copy-edit` — consistent com 4.1/5.2

### 6.3 Body text — rewrite
- **Novo abstract/body**:
  > The Lathrop Megafactory is the world's first dedicated facility for mass-producing Tesla Megapacks and North America's largest utility-scale battery plant. My time at Tesla overlapped its publicly announced doubling — from 20 to 40 GWh of annual production capacity.
  >
  > The work was a multi-facility portfolio of industrial and workplace projects across Tesla's U.S. operations, coordinated across engineering, facilities, and construction through scope discipline and vendor consolidation.

### 6.4 Callouts (4 slots — explícitos)
- **GREEN** · label `SCALE-UP` · value `20 → 40 GWh`
- **BLUE** · label `SCOPE` · value `Multi-facility industrial portfolio`
- **PINK** · label `CATEGORY` · value `First-of-kind energy storage facility`
- **ORANGE** · label `DOMAIN` · value `Energy storage manufacturing`

---

## 7 · Case 04 · Passeio das Águas — `src/content/projects/passeio-das-aguas-shopping.mdx`

> **PDF p. 5.** Fourth case study card screenshot (transição entre p.5).

### 7.1 Purple — corrigir (item não-identificado)
- **Comentário**: "Purple - corrigir"
- **Status**: highlight roxo visível no screenshot, mas o **alvo do corrigir não está claro** na transcrição do PDF.
- **CLARIFY-16** ⚠️: pedir Sarah indicar especificamente o que está em roxo (provavelmente um typo, data ou nome no card). Sem isso, este item fica blocked.

### 7.2 Vermelho — retirar (item não-identificado)
- **Comentário**: "Vermelho - retirar"
- **CLARIFY-17** ⚠️: igual ao 7.1 — alvo do risco vermelho não está claro. Pedir Sarah indicar.

### 7.3 Yellow — mudar para —
- **Ação**: `copy-edit` — consistente com 4.1/5.2/6.2 (formato anos + USA, mas Passeio é Brasil então provavelmente `2013 · Brazil`)

### 7.4 Body text — rewrite
- **Novo abstract/body**:
  > Passeio das Águas is one of the largest shopping centers in Brazil's center-west region — a ground-up project I delivered from construction through commissioning and into ongoing tenant operations. It opened on its original target date of 30 October 2013.
  >
  > The visible work was design and construction management at scale. The deeper work was building a tenant-improvement operational framework that was later adopted across Aliansce Sonae's national portfolio — a methodology born on one project that ended up shaping how the company ran the rest.

### 7.5 Callouts (somente 2 explícitos no PDF — verde/azul)
- **GREEN** · label `SCHEDULE` · value `Delivery on-time`
- **BLUE** · label `TENANTS MANAGED` · value `300+`
- **PINK + ORANGE** — não-explicitados no PDF
- **CLARIFY-18** ⚠️: para 4 slots completos, Sarah precisa indicar PINK e ORANGE. Recomendação default: deixar 2 slots em vez de 4 (cards com slot count variável é OK se o componente suportar), OU sugerir auto-fill:
  - Pink possível: `BUDGET` / `$232M` (já em MDX hoje)
  - Orange possível: `IMPACT` / `Framework adopted nationally`

---

## 8 · Case 05 · Goiânia BRT — `src/content/projects/goiania-brt-network.mdx`

> **PDF p. 5.** Fifth case study card screenshot.

### 8.1 Yellow — período mudar
- **Ação**: `copy-edit` — formato consistente, mas Brazil

### 8.2 Body text — rewrite
- **Novo abstract/body**:
  > The Bus Rapid Transit corridor runs through the dense center of Goiânia, Brazil's tenth-largest city — a public-infrastructure program that had to reach functional opening while threading construction through active urban fabric.
  >
  > The visible work was design management across the full corridor — terminals, stations, and ground-up infrastructure. The defining moment was a two-month critical-criteria window: targeted design revisions that bypassed eminent-domain constraints without triggering land disputes, and R$1.5M in design-change savings absorbed before they reached construction.

### 8.3 Foto position + Experience link (seta rosa)
- **Comentário**: "SETA ROSA / Trocar a foto para apos/abaixo do texto - incluir o link da pagina Experience (se houver um link para a foto)"
- **Ação**: `restructure` (layout) + `copy-edit` (link)
- **Alvo**: provavelmente está no template `work.astro` ou no componente que renderiza cada card; pode estar como prop `imagePosition: 'top' | 'bottom'` no MDX frontmatter
- **CLARIFY-19**: este re-layout aplica APENAS ao card 05, ou seria mais consistente aplicar a todos os 6 cards? Recomendação default: aplicar a TODOS pra mantenção da uniformidade visual. Confirmar com Sarah.

---

## 9 · Case 06 · Virtua Healthcare (Array Architects) — `src/content/projects/array-architects-healthcare.mdx`

> **PDF p. 5–6.** Sixth case study card screenshot.

### 9.1 Yellow #1 — title trimming
- **Comentário**: "#1 amarelo trocar para - planning & design"
- **Status**: title atual no card screenshot é "Healthcare clinical planning &amp; design"
- **CLARIFY-20**: o que Sarah quer é:
  - (a) Manter "Healthcare clinical planning & design" (a frase já contém "planning & design")?
  - (b) Trocar pra somente "planning & design" (drop "Healthcare clinical")?
  - (c) Trocar pra "Clinical planning & design" (drop "Healthcare")?
- **Recomendação default**: pedir Sarah indicar.

### 9.2 Yellow #2 — location → USA
- **Comentário**: "#2 amarelo - incluir USA"
- **Ação**: `copy-edit` — incluir/trocar location para `USA`

### 9.3 Yellow #3 — período
- **Comentário**: "#3 amarelo - trocar para -"
- **Ação**: `copy-edit` — formato consistente (provavelmente `2022 · USA`)

### 9.4 Body text — rewrite
- **Novo abstract/body**:
  > Virtua Our Lady of Lourdes in Camden is the anchor project of Virtua Health's $500M "Advancing Well" reinvestment — a 254,000 sq ft new tower and 458,000 sq ft renovation consolidating cardiac, neuroscience, and transplant services for South Jersey.
  >
  > I contributed during design development and construction documentation as an Architectural Designer at Array Architects, the project's architect of record. The visible work was life-safety detailing and RFI workflow through Autodesk Build, delivered ahead of phased-handoff deadlines. The deeper work was clinical-planning practice in its most demanding form — bed-tower programming where adjacencies, infection-control, patient experience, and operational continuity drive every plan decision.

### 9.5 Callouts (4 slots — explícitos)
- **GREEN** · label `SCOPE` · value `Tower Addition & Renovation`
- **BLUE** · label `TOWER` · value `254K sq ft`
- **PINK** · label `RENOVATION` · value `458K sq ft`
- **ORANGE** · label `PROGRAM` · value `$500M`

### 9.6 Brown arrow — trocar tag de origem
- **Comentário**: "Brow arrow - TROCAR PARA - THE SELECTION"
- **Status**: flecha marrom aponta de uma tag/source label existente para "THE SELECTION"
- **CLARIFY-21** ⚠️: qual tag exatamente trocar para "THE SELECTION"? Inferência: a tag "By yore - Array Architects" / "Earlier work includes..." parte inferior do card pode estar virando "The selection" (ou seja, uma section divider no /work)? Pedir Sarah indicar.

### 9.7 Lavender arrow — incluir "assistant"
- **Comentário**: "Seta lavanda * - inlciur **assistent**"
- **Status**: flecha lavanda aponta para um ponto específico onde adicionar "assistant"
- **Inferência possível**: role label muda de "Architectural Designer" → "Architectural Designer (Assistant)" / "Assistant Architectural Designer" — pra refletir senioridade na época
- **CLARIFY-22** ⚠️: confirmar onde e como adicionar "assistant" — provavelmente role title ou mention no body.

---

## 10 · PAGINA RESEARCH — `src/pages/research.astro`

> **PDF p. 6.**

### 10.1 No action
- **Comentário OneNote**: "Nao alterar nada por hoje"
- **Ação**: `no-op`

---

## 11 · PAGINA SPEAKING — `src/pages/speaking.astro` + `src/content/engagements/*.mdx`

> **PDF p. 6.**

### 11.1 Future: upcoming events block
- **Comentário OneNote**: "Mais pra frente a gente pode colocar proximos eventos confirmados ou algo do tipo no topo da pagina ou criar uma pagina (upcoming events) mas por agora acho melhor deixar sem"
- **Ação**: **deferred / no-op now** — anotar para roadmap futuro
- **CLARIFY-23**: anotar onde? Sugestão: criar issue no GitHub do repo OU adicionar TODO no `src/pages/speaking.astro`.

### 11.2 Watermark slide images (anti-cópia)
- **Comentário OneNote**: "colocar marca dagua - varias na diagonal - para que ninguem possa copiar - em todas as images dos slides"
- **Status atual**: PR #43 + #45 já adicionaram **ambient watermarks** (page-level Astro component `WatermarkLayer.astro`). Sarah pediu watermark **nas imagens dos slides** especificamente.
- **CLARIFY-24** ⚠️: distinção importante:
  - (a) WatermarkLayer atual (overlay no page background) — já existe
  - (b) Watermarks **embedidos nas imagens dos slides** (multiple diagonal stripes within image asset) — NOT yet, requer image processing
- **Ação se confirmada (b)**: `asset-replace` + script — adicionar watermarks diagonais multiple ao asset .jpg/.png dos slides (provavelmente em `src/assets/speaking/` ou `public/speaking/`). Recomendação técnica:
  - Usar Python script (Pillow) ou ImageMagick para regenerar assets com diagonal watermark "© Sarah Rodovalho · sarahrodovalho.com"
  - Manter originals em pasta `_originals/` (gitignored) e versão watermarked em `src/assets/speaking/`
- **CLARIFY-25**: texto exato do watermark? Sugestão default: `© Sarah Rodovalho · sarahrodovalho.com · Do not redistribute`.

### 11.3 Talk PMI — descrição rewrite
- **Comentário OneNote**: "Na descricao do talk trocar para - An invited session at PMI's annual global women-in-construction-leadership conference. The talk is for construction project managers thinking about a pivot into mission-critical infrastructure — what a data center actually is in the AI era, what transfers from architecture and large-scale construction, and what you have to stop assuming you can't do."
- **Ação**: `copy-edit`
- **Alvo**: `src/content/engagements/pmi-women-construction-follow-the-sun-2026.mdx` — campo `abstract:` ou `description:`
- **Body**:
  > An invited session at PMI's annual global women-in-construction-leadership conference. The talk is for construction project managers thinking about a pivot into mission-critical infrastructure — what a data center actually is in the AI era, what transfers from architecture and large-scale construction, and what you have to stop assuming you can't do.

### 11.4 Outros items
- **Comentário**: "Outro items ok por agora"
- **Ação**: `no-op` para os outros engagements (4 engagements MDX no repo: ARCC 2025, IA na Construção Autodesk Forma 2026, PMI Follow the Sun 2026, StartSE Construtech Summit 2024)

---

## 12 · NOVA PÁGINA · Academic / Past Studies — NEW `src/pages/academic.astro`

> **PDF p. 7.**

### 12.1 Criar página dedicada
- **Comentário OneNote**: "Criar uma pagina dedicada para as experiencias academicas/passado de estudos e colocar os items que estavam na pagina ABOUT"
- **Ação**: `new-page`
- **Alvo**: NEW `src/pages/academic.astro`
- **Conteúdo** (vindo do about.astro, sections 2.5 retiradas):
  - **Education** (PhD Harrisburg, MSc TJU, MBA FGV, Bachelor UEG) + photos thesis defense + commencement + UEG group + UEG formatura
  - **Past roles** (Microsoft, Tesla, TJU, Array, Aliansce Sonae) — **SUJEITO A REVISÃO** do item 3.2 (não expor CV detalhado)
  - **Certifications & affiliations** (PMP, LEED GA, OSHA 30, AIA Associate, CAU, Sigma Lambda Chi, NCARB)
  - **Languages** (Portuguese, English)
- **CLARIFY-26**: nome do page slug — `/academic` (mais conciso) vs `/background` (mais inclusivo de past roles)? Recomendação default: `/academic` se foco for education-heavy, `/background` se incluir past roles também. Como Sarah disse "academicas/passado de estudos", `/academic` é mais fiel literal. Mas se 12.1 inclui Past roles, `/background` é mais honesto.
- **Recomendação técnica**: `/background` cobre tudo. Confirmar com Sarah.

### 12.2 Cross-link com `/credentials` existente
- **Status atual**: `src/pages/credentials.astro` já existe + 6 MDX em `src/content/credentials/*`
- **Ação**: `restructure` — decidir se `/academic` tem section "Certifications" linkando pra `/credentials`, ou se duplica (não recomendado), ou se remove `/credentials` (não recomendado — já indexado pelo Google?).
- **Recomendação**: `/academic` tem section "Certifications" como **lista compacta** com link **"See full credentials with verification IDs →"** para `/credentials`.

### 12.3 Cross-link com `/experience` (se persistir)
- **Status**: dependente do item 3.1 (merge work + experience)
- **Recomendação**: se Past roles vai pra `/academic`, então `/experience` (se permanecer como page) seria sobrepor — melhor: ou `/experience` vira `/work` (merge), ou `/experience` é deprecada com 301 → `/academic`.

---

## 13 · PAGINA PRESS KIT — `src/pages/press-kit.astro` — **RESTRUCTURE CRÍTICA (SEGURANÇA)**

> **PDF p. 7.** Section header em CAPS LOCK pela Sarah.

### 13.1 Remover tudo do PUBLIC layer para ADMIN-only
- **Comentário OneNote** (transcrito literal):
  > "PAGINA PRESS KIT - REMOVER TUDO PARA UMA AREA ADMIN (TEM VARIAS COISAS PARA COORIGIR) E RODEI MEUS CONCERNS E O CLAU CONDORDOU COMIGO QUE EH UM RISO MUITO GRANDE DEIXAR ISSO DISPONIVEL. ENTAO ELE SUGERIU:"
- **Status atual**: `press-kit.astro` expõe **publicamente** (sem gate):
  - 3 bios completas (SHORT 280 chars, MEDIUM 810 chars, LONG 1850 chars)
  - Pronunciação completa (nome legal completo "Sarah Faria Alcantara Macedo Rodovalho" + IPA + soft "h" explanation)
  - Quick facts numbers ($232M, $279M+, 264 MW, AIA board 2026-2030, CAU A978191, etc.)
  - High-res photo downloads (jpg + png, sem watermark, com filename sugerindo redistribution)
  - Email direto `sarah@sarahrodovalho.com`
- **Risk concern da Sarah**: exposição de identifying info + employer-specific metrics + hi-res photos sem gate = enables scraping/misuse
- **Validation extern**: "CLAU" (terceiro, provavelmente colega de confiança) concordou com a concern e sugeriu a estrutura abaixo.

### 13.2 Nova estrutura PUBLIC layer (no gate)
- **Sarah's design literal**:
  > **Public layer (no gate)**
  > - Headshot (lower resolution, watermarked or with a small "Sarah Rodovalho · sarahrodovalho.com" mark in the corner — discourages reuse without breadcrumb)
  > - One short bio (~280 chars), written tightly -- (Sarah Rodovalho is an Integrated Design Manager at Aligned Data Centers and a doctoral researcher at Harrisburg University, with 16+ years delivering capital programs across hyperscale data centers, advanced manufacturing, and large-scale infrastructure in the U.S. and Brazil. She serves on the AIA Construction Contract Administration Knowledge Community Leadership Board (2026–2030).)
  > - Pronunciation guide
  > - Contact email for press inquiries
  > - Brief mention that medium/long bios, high-res photos, and quick-fact sheets are *available on request*
- **Ação**: `restructure` — reescrever `press-kit.astro` removendo tudo além desses 5 items, com asset pipeline:
  - Headshot watermarked low-res: NEW `public/press/sarah-rodovalho-headshot-watermarked-lowres.jpg` (gerar via script)
  - Pronunciation: manter parcial (nome de display + IPA simples; remover nome legal completo "Sarah Faria Alcantara Macedo Rodovalho" pro gated layer)
  - Email: manter `sarah@sarahrodovalho.com`
  - CTA "for medium/long bios + hi-res photos + quick-facts — available on request" → link para form/email

### 13.3 Nova estrutura GATED layer (request only)
- **Sarah's design literal**:
  > **Gated layer (request only)**
  > - Medium and long bios
  > - High-resolution print-quality headshot
  > - Quick-facts sheet with verifiable claims (publications, board appointments, certifications)
  > - Anything with specific employer/program references
- **Gate options literal**:
  > **Light gate — form-based request.** A short form: name, organization, event/publication, intended use, deadline. Auto-replies are fine. This catches 95% of legitimate requesters (event programmers, podcast bookers, journalists) without friction, while filtering out the casual scrapers.
  > **Lighter gate — direct email.** "For high-resolution images, extended bios, or quick-fact sheets, email sarah@sarahrodovalho.com." This is what most senior consultants and academics use. Easier to set up, slightly higher friction for legitimate users, but creates a paper trail of who has your assets.
- **CLARIFY-27** ⚠️ **DECISÃO ARQUITETURAL**: qual gate?
  - **Opção A (Lighter gate / direct email)**: zero infrastructure, só copy. Recomendado para MVP.
  - **Opção B (Light gate / form)**: requer form backend (Cloudflare Pages Function? Formspree? Web3Forms?), captcha (Cloudflare Turnstile), email forwarding setup.
  - **Recomendação default**: começar com (A) — direct email com paper trail; migrar pra (B) quando volume justificar.
- **Ação**: `restructure` + `new-page` (se gate-B) — depende da decisão acima.

### 13.4 Admin-only area
- **Comentário literal Sarah**: "REMOVER TUDO PARA UMA AREA ADMIN"
- **CLARIFY-28** ⚠️ **DECISÃO ARQUITETURAL**: como armazenar os assets full (hi-res, long bios, quick-facts)?
  - **Opção A**: gitignored folder `_admin/press-kit/` no repo (assets nunca commitam; servidos manualmente quando request chega)
  - **Opção B**: Cloudflare R2 bucket gated com signed URLs (mais infra mas escala)
  - **Opção C**: existing private GitHub repo / Notion private page / Sarah's own OneDrive (zero infra)
  - **Recomendação default**: (C) — Sarah envia manualmente cada requisição da inbox; zero infra, máxima discrição, paper trail orgânico via email.

### 13.5 Watermark headshot público
- **Implementação**: script Python/Pillow ou ImageMagick para regenerar headshot atual em versão lower-res + watermark esquina inferior direita
- **Asset target**: `public/press/sarah-rodovalho-headshot-public.jpg` (substituir atual `sarah-rodovalho-headshot.jpg`)
- **Watermark text**: `Sarah Rodovalho · sarahrodovalho.com`
- **Resolution**: target ~600×600 (web-display only, defeating print-quality reuse)

---

## 14 · NOVA PÁGINA · Contate-me — NEW `src/pages/contact.astro`

> **PDF p. 3.** (Comentário no contexto de "PAGINA WORK".)

Ver item 3.3 acima.

---

## 🔍 Consolidated CLARIFY list (24 items)

Items abaixo precisam de input Sarah/Vitor **antes** ou **durante** implementação:

| ID | Item | Página/Item | Pergunta |
|---|---|---|---|
| CLARIFY-01 | Hero ending | 1.1 | Stop em "Aligned Data Centers" ou substituir por "multi-hundred-megawatt campus"? |
| CLARIFY-02 | Big numbers | 1.2 | Quais 2 stats do PMI Follow the Sun pra trocar 264MW + $279M+? |
| CLARIFY-03 | Bio ending | 2.1 | Idem CLARIFY-01 (paralelo no About) |
| CLARIFY-04 | "Current Engagements" | 2.2 | Confirmar typo fix |
| CLARIFY-05 | PhD bullet | 2.4 | Já existe — no-op, reposition, ou rewrite? |
| CLARIFY-06 | Página academic | 2.5 | (a) novo `/academic`, (b) merge em existing `experience.astro` + `credentials.astro`, ou (c) split? |
| CLARIFY-07 | Work vs Experience name | 3.1 | Qual slug mantém? `/work` ou `/experience`? |
| CLARIFY-08 | CV-style content audit | 3.2 | Sarah lista o que retirar do `experience/*.mdx` |
| CLARIFY-09 | Contact slug | 3.3 | `/contact` ou `/contato`? |
| CLARIFY-10 | Date format | 4.1 | `Oct 2025` ou só `2025`? |
| CLARIFY-11 | USA convention | 4.1+ | Todos os cards aplicam mesmo padrão `2025 — present · USA`? |
| CLARIFY-12 | Intro paragraph remove | 4.2 | Remover inteiro ou editar? |
| CLARIFY-13 | abstract vs body split | 4.4 | Como dividir 2 parágrafos novos entre frontmatter+body? |
| CLARIFY-14 | ⚠️ Case 01 callouts | 4.5 | Sarah confirma split label/value das 4 cores |
| CLARIFY-15 | CONTRIBUITION typo | 5.4 | Corrigir spelling? |
| CLARIFY-16 | ⚠️ Purple item card 04 | 7.1 | Qual elemento está em roxo? |
| CLARIFY-17 | ⚠️ Red item card 04 | 7.2 | Qual elemento está riscado em vermelho? |
| CLARIFY-18 | ⚠️ Card 04 pink+orange | 7.5 | 2 callouts faltam — Sarah indica ou cards podem ter 2 só? |
| CLARIFY-19 | Photo position scope | 8.3 | Aplica só ao card 05 ou todos? |
| CLARIFY-20 | Card 06 title | 9.1 | Manter title atual ou trim? |
| CLARIFY-21 | ⚠️ Brown arrow target | 9.6 | Qual tag exatamente troca pra "THE SELECTION"? |
| CLARIFY-22 | ⚠️ Lavender "assistant" | 9.7 | Onde + como adicionar "assistant"? |
| CLARIFY-23 | Future upcoming events | 11.1 | TODO em código ou GitHub issue? |
| CLARIFY-24 | ⚠️ Watermark scope | 11.2 | Page-level (already done) ou embedded-in-image (new work)? |
| CLARIFY-25 | Watermark text | 11.2 | Texto exato do watermark? |
| CLARIFY-26 | Academic slug | 12.1 | `/academic` ou `/background`? |
| CLARIFY-27 | ⚠️ Press-kit gate type | 13.3 | Light gate (form) ou Lighter gate (email)? |
| CLARIFY-28 | ⚠️ Admin-only storage | 13.4 | gitignore folder / R2 / external (OneDrive/Notion)? |

**Items com ⚠️ são blockers para implementação** — sem resposta da Sarah, ficamos parados em pontos específicos.

---

## 📋 Proposed PR sequencing (6 PRs)

Ordem por **risco/dependência/urgência**:

### PR-S07 · Press Kit security restructure ⚠️ URGENT
- **Why first**: exposição de PII + employer-specific data + hi-res photos sem gate é o item de maior risco identificado. Sarah + Clau concordaram que é "risco muito grande".
- **Scope**:
  - `src/pages/press-kit.astro` → minimal public layer (headshot watermarked + bio 280 chars + pronunciation parcial + email + "available on request" CTA)
  - Watermark headshot público (script + new asset)
  - Gated layer copy (depending on CLARIFY-27: form OR email-only)
  - Move long bios + quick-facts + hi-res photos to admin-only storage (CLARIFY-28)
- **Blockers**: CLARIFY-27 (gate type), CLARIFY-28 (storage)
- **Files**: `src/pages/press-kit.astro`, `public/press/sarah-rodovalho-headshot.jpg` (regen), `scripts/watermark-headshot.py` (new), conditionally new form page
- **Done criterion**: opened `/press-kit` shows minimal public layer only; full-detail assets inaccessible without explicit request

### PR-S08 · Home + About copy edits (small, safe)
- **Why second**: low-risk copy edits; visible improvement; warm-up for the bigger restructures
- **Scope**:
  - `src/pages/index.astro` — remove "on a multi-building, ~264 MW campus" from hero (1.1); swap big numbers (1.2, blocked on CLARIFY-02)
  - `src/pages/about.astro` — remove "on a multi-building campus" from bio (2.1); rename "Now" → "Current Engagements" (2.2); replace "~264 MW multi-building" → "multi-hundred-megawatt" (2.3); confirm PhD bullet (2.5)
- **Blockers (partial)**: CLARIFY-01, CLARIFY-02, CLARIFY-03, CLARIFY-04, CLARIFY-05 — most can be inferred/default
- **Files**: `src/pages/index.astro`, `src/pages/about.astro`
- **Done criterion**: home + about read clean per Sarah's intent; no CV-block removal yet (that's PR-S09)

### PR-S09 · About CV-block removal + new Academic page + new Contact page
- **Why third**: depends on PR-S08 (about copy stable); creates 1–2 new pages
- **Scope**:
  - Remove sections "Selected past roles", "Education", "Certifications & affiliations", "Languages" from `src/pages/about.astro` (2.5)
  - Audit `experience.astro` + `credentials.astro` for duplication (2.6)
  - Create new `src/pages/academic.astro` (or `/background` — CLARIFY-26) with education + past roles + certs + languages
  - Create new `src/pages/contact.astro` (3.3)
  - Update SiteHeader navigation to include new pages
  - 301 redirects in `worker.js` for any deprecated paths
- **Blockers**: CLARIFY-06, CLARIFY-08, CLARIFY-09, CLARIFY-26
- **Files**: `src/pages/about.astro`, NEW `src/pages/academic.astro`, NEW `src/pages/contact.astro`, `src/components/SiteHeader.astro`, `worker.js` (if redirects)
- **Done criterion**: about page is bio-only; academic page is complete CV-style page; contact page is minimal & functional

### PR-S10 · Work/Experience merge
- **Why fourth**: structural change to navigation; depends on PR-S09 academic page existing (so /experience can be deprecated cleanly)
- **Scope**:
  - Merge `src/pages/work.astro` + `src/pages/experience.astro` into single page (3.1)
  - Bring photo + Experience-page link junto de cada case study card (3.1)
  - Apply photo-position adjustment from card 05 (Goiânia BRT) → all cards uniformly (8.3, CLARIFY-19)
  - Audit `src/content/experience/*.mdx` for CV-style content; remove items per 3.2 (blocked on CLARIFY-08)
  - 301 redirect `/experience` → `/work` in `worker.js`
- **Blockers**: CLARIFY-07, CLARIFY-08, CLARIFY-19
- **Files**: `src/pages/work.astro`, `src/pages/experience.astro` (delete), `src/content/experience/*.mdx` (audit), `worker.js`
- **Done criterion**: `/work` is single source of truth for portfolio; `/experience` redirects; no CV-detailed content public

### PR-S11 · Case studies batch (cards 01–06)
- **Why fifth**: depends on Work page structure (PR-S10) being stable; many small focused changes
- **Scope**: 6 MDX file edits + body rewrites + callout updates per cards 01–06:
  - Card 01 Aligned (4.x) — body + callouts (CLARIFY-13, CLARIFY-14 blocker)
  - Card 02 Microsoft CO+I (5.x) — body + callouts + spelling fix
  - Card 03 Tesla (6.x) — body + callouts
  - Card 04 Passeio (7.x) — body + 2 callouts + Purple/Red items (CLARIFY-16, 17, 18 blockers)
  - Card 05 Goiânia BRT (8.x) — body + photo position
  - Card 06 Virtua (9.x) — body + callouts + arrow items (CLARIFY-20, 21, 22 blockers)
- **Blockers**: many (see column 3)
- **Files**: `src/content/projects/*.mdx` (6 files)
- **Done criterion**: each case study card reads per Sarah's new body + has consistent callouts + date format

### PR-S12 · Speaking watermarks + PMI talk rewrite
- **Why last**: depends on watermark architecture decision (might reuse asset from PR-S07)
- **Scope**:
  - Rewrite talk PMI description in `src/content/engagements/pmi-women-construction-follow-the-sun-2026.mdx` (11.3)
  - Image-embedded watermarks on slide images (CLARIFY-24, 25 blockers); decision: do this OR confirm current ambient layer is enough
  - GitHub issue or TODO comment for future upcoming-events block (11.1, CLARIFY-23)
- **Blockers**: CLARIFY-24, CLARIFY-25, CLARIFY-23
- **Files**: `src/content/engagements/pmi-women-construction-follow-the-sun-2026.mdx`, conditionally `src/assets/speaking/*` (regen), conditionally `scripts/watermark-images.py` (new)
- **Done criterion**: PMI talk reads per Sarah's copy; slide assets watermarked per Sarah's anti-cópia intent

---

## Implementation order summary

```
PR-S07 (urgent, security)
 └─► PR-S08 (parallel-safe copy edits)
      └─► PR-S09 (CV restructure → new pages)
           └─► PR-S10 (Work/Experience merge)
                └─► PR-S11 (case studies batch)
                     └─► PR-S12 (speaking watermarks)
```

Estimated effort:
- PR-S07: 1–2 sessions (depends on gate decision)
- PR-S08: 0.5 session
- PR-S09: 1–2 sessions
- PR-S10: 1 session
- PR-S11: 1–2 sessions
- PR-S12: 0.5–1 session
- **Total**: ~5–8 working sessions to ship Sarah's full review

---

## Next step

1. **Sarah responds CLARIFY-01 → CLARIFY-28** (preferably as a list in OneNote or chat; minimum: blockers marked ⚠️)
2. **Vitor reviews this doc, adjusts mappings if I misread something** (especially the CLARIFY items)
3. **Start with PR-S07** (Press Kit security restructure) — highest urgency

---

**Document maintained**: this is a living doc until all 6 PRs ship. Update CLARIFY status as Sarah answers; mark items as DONE as PRs merge.
