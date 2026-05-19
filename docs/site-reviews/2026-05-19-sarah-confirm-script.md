# Sarah confirmation script — site review S07–S12 final pass

**Tempo estimado:** ~10 minutos.
**O que aconteceu:** Sua revisão do OneNote ("Ajustes do site") foi implementada em 9 PRs entre 2026-05-18 e 2026-05-19. **Tudo que era determinístico já foi para produção.** Restam só decisões de voz / brand / escolhas de produto que precisam do seu olho.

---

## 📋 O que precisa do seu input (8 perguntas)

### 1 · 🎙️ Voz dos textos · abre `/experience`

Eu reescrevi os 6 abstracts dos case studies seguindo seu OneNote. Lê os 6 cards e me diz:

- [ ] **Aligned** — abstract "Hyperscale campuses don't get strained..."
- [ ] **Microsoft CO+I** — "Hyperscale data centers are some of the most carbon-intensive..."
- [ ] **Tesla** — "The Lathrop Megafactory is the world's first..."
- [ ] **Passeio das Águas** — "Passeio das Águas is one of the largest shopping centers..."
- [ ] **Goiânia BRT** — "The Bus Rapid Transit corridor runs through..."
- [ ] **Virtua Healthcare** — "Virtua Our Lady of Lourdes in Camden is the anchor project..."

**Pergunta:** soa como você? Algum tom estranho / parágrafo que precisa ajustar?
**Como responder:** "tudo OK" / ou cita qual card + o trecho que quer mudar.

---

### 2 · 🖼️ Watermark nas fotos · abre `/speaking`

As 6 imagens da apresentação PMI agora têm watermark diagonal "© Sarah Rodovalho · sarahrodovalho.com" (~22% opacity, -30°).

**Olha especificamente a foto ARCC** (você apresentando) — o watermark cruza a região do seu rosto/ombro.

**Perguntas:**
- [ ] Opacidade está OK ou prefere mais sutil (ex.: 15%)?
- [ ] Posição cruzando o rosto incomoda? Se sim, prefere watermark só nos cantos / só em diagonal evitando o centro?

**Como responder:** "deixa como está" / ou "muda pra X opacity" / ou "tira do centro".

---

### 3 · 📅 Goiânia BRT · ano

No seu OneNote você escreveu `2017 · Brazil` pra Goiânia BRT.
A gente tem dados internos dizendo que o seu envolvimento foi **Nov 2019 – Jul 2021**.

Foi por isto que mostramos `2019 — 2021 · Brazil` no site, contudo possa ter um equivoco no levantamento de fatos da implementacao, ou um equivoco na descricao da Sarah no OneNote.

**Pergunta:** confirma se o que está deployado está certo ou se deveria estar como 2017?
**Como responder:** "2017" / "2019-2021 está certo" / "foi 2017 design phase + 2019-2021 entrega — quer mostrar ambos?".

---

### 4 · 🏥 Virtua Healthcare · "Clinical" no role

Você pediu pra tirar "clinical" do **título** do card → feito ("Healthcare planning & design").

**Mas o campo `role:` (subtitulo do card)** ainda mostra:
`"Architectural Designer (Clinical Planning & Healthcare Design)"`

**Pergunta:** tira "Clinical" do role também? Ou role pode manter já que é a descrição técnica do que você fazia no Array Architects?
**Como responder:** "tira do role também" / "role pode manter".

---

### 5 · 🌐 Crédito "Vitor M. Rodovalho → vitormr.dev" no rodapé

Todo o rodapé do site tem um link "Vitor M. Rodovalho" → https://vitormr.dev (crédito de quem fez o desenvolvimento).

**Perguntas:**
- [ ] Pode manter assim (cross-link entre os dois sites)?
- [ ] Ou prefere crédito mais genérico ("Site by Vitor Rodovalho" sem link)?
- [ ] Ou prefere remover totalmente?

**Como responder:** "mantém" / "genérico sem link" / "remove".

---

### 6 · 🔐 Link discreto pro /admin no rodapé?

Hoje `/admin/` não tem nenhum link público no site — você digita a URL na barra de endereço. Funciona, mas é fácil esquecer.

**Opção:** adicionar um link super-discreto no rodapé `Admin →` (qualquer pessoa que clicar sem ter sua sessão CF Access ativa cai no challenge de email OTP — você é a única na allowlist, então é zero risco de OPSEC).

**Pergunta:** quer esse link no rodapé?
**Como responder:** "sim, adiciona" / "não, deixa só URL manual" / "outra ideia: ___".

---

### 7 · 📄 AGENTS.md no root do site

PR aberto para mim adicionar um arquivo `AGENTS.md` no root do seu repo (`sarah-rodovalho-site`). É só uma ferramenta interna — instruções pra IA quando trabalhar no seu site (regras OPSEC, voice gating, etc). Não tem nada user-facing.

**Pergunta (joint-owner check):** OK com a adição?
**Como responder:** "OK" / "olha o que escreveu antes (link do PR)".
**Link do PR:** https://github.com/VitorMRodovalho/sarah-rodovalho-site/pull/56

---

### 8 · ⚠️ FYI · Incidente OPSEC do dia 18 — fechado

Por ~28h depois do PR-S07b (admin layer), as 3 páginas `/admin/*` ficaram **publicamente acessíveis** (sem login). Continham: nome legal completo + 2 fotos hi-res + bios longas. O gate Cloudflare Access que devia estar ativado não estava.

Resolvido: a gente selou via Worker até reconfigurar o CF Access. Hoje está corretamente gated (verifiquei).

**Bonus check:** Wayback Machine (Internet Archive) — **zero snapshots foram tirados durante a janela**. Não foi indexado. Exposição real foi limitada a quem fez fetch direto naquelas 28h (provavelmente ninguém ou bots casuais).

**Não precisa fazer nada.** Só pra você saber.

---

## ✅ O que já está feito e foi shipped (sem ação tua)

- ✅ Home: hero "multi-hundred-megawatt campus" + stats 7M+ / $1.5B+ do seu deck PMI
- ✅ About: "Current Engagements" + slim CV (Past roles / Education / Certs / Languages saíram daqui)
- ✅ Work → Experience merge, fotos abaixo do texto em todos os 6 cards
- ✅ 6 case studies: period year-only, country simplificado (USA/Brazil), abstract + body split, 4 callouts coloridos por card
- ✅ NEW `/academic` — Education + Languages
- ✅ NEW `/contact` — minimal
- ✅ `/speaking` — Upcoming + Past sections, watermark embutida nos slides, PMI abstract reescrito
- ✅ `/press-kit` — minimal público (curta bio + headshot watermarked + email CTA)
- ✅ `/admin/*` (gated por CF Access Email OTP) — full press kit + newsletter placeholder
- ✅ Logo no header agora "Sarah Rodovalho" (sem F. A. M.) — em todas as páginas
- ✅ Logout real no admin (botão CF Access logout)
- ✅ Privacy page atualizada — disclose CF Access flow

---

## 🎯 Próximos passos depois que você responder

Para cada item que precisar de ajuste → 1-PR pequeno fix-forward. Vitor + Claude executam.

Se TUDO estiver OK → projeto Sarah-site review fechado. Próxima onda quando você marcar um evento upcoming (preenche um MDX em `engagements/*` → mostra na seção Upcoming + automaticamente alimenta Orenu via ADR-024 sync).
