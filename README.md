# broisinvesting

**Multi-agent AI system for Instagram investing card-news.** Drop a topic in, and a team of 13+1 agents researches the market, drafts the narrative, designs the visuals, and ships a 6–9 slide carousel ready for `@broisinvesting` — captions, charts, memes, and a 1-page CTA PDF included.

> Instagram · [@broisinvesting](https://instagram.com/broisinvesting) *(replace with handle)*

---

## Overview

broisinvesting turns a one-line topic into a polished Instagram carousel before you write a single caption. The orchestrator coordinates research, script approval, visual direction, and auto-posting — each phase gated by a human-in-the-loop checkpoint so you stay in control.

```
Topic   → research  → script draft   → slide JSON + images → caption → IG publish
Creator   (Phase 1-2)  (CP2.5 gate)    (Phase 4 batches)    (Phase 5) (Phase 6)
```

---

## Features

- **13+1 agent pipeline** — Orchestrator + 13 specialists (economy / politics / market / chart analysts, validator, body & title writers, visual curator, background designer, layout composer, final assembler, CTA report builder, meme curator, caption writer)
- **Human-in-the-loop checkpoints** — CP1 (research) → CP2 (arc) → CP2.5 (script) → CP3 (batch images) → CP4 (final)
- **Polaroid corkboard design DNA** — Funko Pop mascot, kraft brown + burnt sienna palette, rubber-stamp accents, hand-drawn sepia annotations
- **Topic mascot per post** — CEO/founder for company posts, Buffett for value, Powell for macro — one mascot per post, never center, always in a corner
- **Local meme library** — 13 reusable meme assets auto-matched to slide intent (distracted_boyfriend, to-the-moon, etc.)
- **1-page CTA PDF report** — auto-generated alongside the carousel as the lead-magnet reward
- **Auto-posting pipeline** — Cloudinary upload + Instagram Graph API publish via `ig_skill/` scripts
- **Per-topic folder output** — every post saved to `{topic_slug}/` with `slide_NN.json`, `cta_report.pdf`, and `manifest.json`

---

## Repository Structure

```
broisinvesting.md/
├── 00_orchestrator.md          # workflow control + HITL + batch pacing
├── 01_ARCHITECTURE.md          # 13+1 agent architecture
├── 01_us_economy_analyst.md    # Phase 1 research agents
├── 02_us_politics_analyst.md
├── 03_us_stock_market_analyst.md
├── 04_chart_data_analyst.md
├── 05_validator.md             # Reflection + fact-check
├── 06_body_writer.md           # Slide copy
├── 07_title_writer.md
├── 08_visual_curator.md        # Visual direction + mascot rules
├── 09_background_designer.md
├── 10_layout_composer.md
├── 11_final_assembler.md       # Gemini JSON prompt builder
├── 12_cta_report_builder.md    # 1-page PDF
├── 13_meme_curator.md
├── 14_caption_writer.md        # Phase 6 caption
├── 02_DESIGN_DNA.json          # design tokens
├── 03_MASTER_PROMPT.md         # system prompt
├── 04_AGENT_SCHEMAS.json
├── 05_FEWSHOT_EXAMPLES.json
├── 06_GEMINI_JSON_TEMPLATE.json
├── 07_USAGE_GUIDE.md
├── 08_CTA_PDF_TEMPLATE.md
├── ig_skill/                   # Instagram posting automation
│   ├── ig_api.py               # Graph API client
│   ├── upload_cloudinary.py    # image host
│   ├── post_workflow.py        # end-to-end publish
│   └── refresh_token.py        # long-lived token rotation
└── meme/                       # reusable meme library
```

---

## Quick Start

1. **Load the master prompt** — paste `03_MASTER_PROMPT.md` into Claude's system area.
2. **Submit a topic** —
   ```
   Topic: "Will Private Credit be the 2008 of 2026?"
   Slides: 8
   Tone: standard
   CTA reward: 1-page PDF
   ```
3. **Respond to HITL checkpoints** — approve research → narrative arc → script → image batches → final.
4. **Trigger posting** — `포스팅 시작 {topic_slug}` to run Cloudinary upload + Instagram publish.

See `broisinvesting.md/07_USAGE_GUIDE.md` for the full walkthrough.

---

## Versions

| Version | Highlight |
|--------|-----------|
| v4.7 | HOOK center = real-photo polaroid · mascot from S2, always corner, 12–15% slide height |
| v4.6 | Phase 3.5 script approval gate · polaroid corkboard Design DNA v1 |
| v4.3 | Phase 6 Instagram auto-posting (Cloudinary + Graph API) |
| v4.2 | 4-Beat narrative arc · prev_carryover · ≥3 visual asset types per post |
| v4.1 | Meme Curator (Agent 13) · per-topic folder output |
| v4.0 | Batch pacing · CTA PDF builder · Buffett ~40% frequency rule |

---

## License

[MIT](LICENSE) © 2026 Dohyun Ryu
