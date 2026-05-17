# 🏗 카드뉴스 AI 생성 시스템 v4.0 — 계층형 12+1 에이전트 아키텍처

## 🆕 v4.2 추가 변경 (다음 신규 포스트부터 활성화)

> 🔍 **회고 기반 개선**: Google v4.0 포스트의 5가지 약점(텍스트 짧음, 시각 단조, 슬라이드 연결성 약함, meme 과다, 배경 단조) 보완.

1. **텍스트 풍부화**: 불릿 2-5 → **2-8 단어** + 서브라인. 문단 ≤12 → **≤18 단어**. 슬라이드당 블록 2 → 3.
2. **시각 다양성 의무화**: 신규 asset_type 5종 (`stat_card`, `chart_annotated`, `speech_bubble`, `before_after_split`, `stamp_overlay`). 8장 포스트 기준 의무 포함 ≥3종.
3. **내러티브 연결성 강화**: 기승전결 4-Beat Arc + 슬라이드별 `prev_carryover` 키워드 캐리오버.
4. **Meme ~40% 빈도 강제**: 8장 기준 3-4개 슬라이드만 (HOOK + IRONY + 본문 1-2개), CTA·DEFINITION 단독·THE_MACHINE·CONCLUSION 단독은 제외.
5. **배경 테마 다양화**: 추가 5종 (`dark_grid_neon_green`, `bright_cream_minimal`, `tan_paper_aged`, `red_alert_overlay`, `split_then_now`). 8장 포스트 기준 ≥3개 다른 테마.

---

## 🆕 v4.1 추가 변경 (다음 신규 포스트부터 활성화)

1. **🆕 Agent 13 (Meme Curator) 신설**: Agent 8 (Visual Curator)에서 meme 책무 분리 → 전담 에이전트. `/broisinvesting/meme/` 폴더 자동 인덱싱 + 슬라이드 의미 매칭.
2. **🆕 JSON 자동 로컬 저장 규칙**: 모든 산출물은 `/broisinvesting/{topic_slug}/` 주제별 폴더에 자동 저장 (slide_NN.json, cta_report.pdf, manifest.json).
3. **에이전트 카운트**: 12+1 → **13+1** (Orchestrator + 13 working agents).
4. **Phase 4 흐름**: Agent 6 → 7 → **13 (Meme)** → 8 (Visual) → 9 → 10 → 11.

> ⚠️ 진행 중인 포스트(예: `Google`)는 v4.0으로 유지. v4.1은 다음 신규 포스트(topic) 입력 시 활성화.

---

## 🆕 v4.0 핵심 변경 (from v3.2 + v3.3 흡수)

1. **워렌 버핏 마스코트 크기 규칙 신설**: 코너/모서리 배치 시 **주인공 인물의 30% 크기**로 축소. 중앙 주인공이거나 CTA 연단 케이스는 예외.
2. **🆕 워렌 버핏 등장 빈도 규칙 신설**: 전체 포스트의 **~40% 슬라이드에만** 등장 (HOOK + CTA 필수, 본문 1-2개). 매 슬라이드 등장 금지 — 임팩트 희석 방지.
3. **🆕 슬라이드 간 내러티브 연결자 의무화**: 비-HOOK 슬라이드의 헤드라인 또는 본문 첫 줄에 전환어/연결구 (But, However, And, Plus, Therefore, This is why, Why? 등) 필수.
4. **🆕 의미 전달 우선 원칙 (Meaning-First)**: 텍스트 단어 수 한도는 목표(target). 의미 보존 위해 헤드라인·불릿 ≤7, 문단 ≤14까지 허용. 정확한 의미 > 간결성.
5. **데이터 최신성 규칙 강화**: 수치·지표(주가·지수·금리·CPI·NFP)는 **T-1 영업일 종가 / 최근 발표분** 강제. 뉴스·분석·정책 맥락은 공신력 소스면 기간 제한 없음.
6. **CTA 보상 리포트 제작 자동화**: **새 Agent 12 (CTA Report Builder)** 신설. 1페이지 PDF 리포트(요약 + 차트 1-2개)를 카드뉴스와 동시 제작.
7. **에이전트 MD 완전 분리**: Orchestrator + 12 에이전트 각각 독립 MD 파일 (총 13개). 통합 `04_AGENT_SCHEMAS.json`은 스키마 참조용으로 간소화.
8. **배치 페이싱 도입**: 이미지 프롬프트 JSON을 **커버(1장) + 본문(2장씩) + CTA(1장)** 구조로 묶어 Orchestrator가 사용자에게 전달. HITL CP3이 배치 단위로 작동.
9. **v3.3 약자 풀이 정식 흡수**: Orchestrator가 포스트 전체 약자 레지스트리 관리. Agent 10이 비어있는 모서리에 배치.

## 🆕 v3.2 계승 (여전히 유효)

- **커버 독점성**: 커버 전용 토큰(spring+pencil, oversized headline, 40%+ whitespace, sole focal subject)은 HOOK에만 허용
- **소제목 +10% 크기**: body의 1.1×
- **본문 폰트 = Roboto-like** 모던 sans-serif
- **배경 light_lined**: 밝은 크림 + 가로줄만 (격자 X)
- **binder_clip deprecated**: HOOK = 스프링+연필, 비-HOOK = 마스킹테이프/압정/찢긴 스티커

## 🆕 v3.1 계승

- 워렌 버핏 사진 컷아웃 마스코트 (9가지 포즈)
- 헤드라인 세리프 유지 (Old Standard TT 느낌)
- 텍스트 타이트화: 불릿 2-5단어, 문단 1단문(≤12단어), 슬라이드당 최대 2개 블록
- text_to_render ↔ styling_spec 분리
- 메타 문자열 누출 방지 스캐너

---

## 🧠 전체 아키텍처 (계층형, v4.0)

```
                    ┌─────────────────────────────────┐
                    │  [0] ORCHESTRATOR (관제탑)       │
                    │  워크플로우 + HITL + 배치 페이싱  │
                    └─────────────────────────────────┘
                                   │
          ┌────────────────────────┴────────────────────────┐
          │                                                 │
          ▼                                                 ▼
╔═════════════════════════════════════╗    ╔══════════════════════════════╗
║  LAYER 1: RESEARCH                  ║    ║  LAYER 2: VERIFICATION       ║
║  ─ 병렬 + T-1 게이트 ─              ║───▶║                              ║
║                                      ║    ║  [5] Fact-Check Validator    ║
║  [1] US Economy Analyst              ║    ║  + Reflection 2R             ║
║  [2] US Politics Analyst             ║    ║  + 🆕 T-1 규정 검증          ║
║  [3] US Stock/Market Analyst         ║    ║                              ║
║  [4] Chart/Data Analyst              ║    ║                              ║
║    └─ 🆕 CTA PDF 차트 후보 2개      ║    ║                              ║
╚═════════════════════════════════════╝    ╚══════════════════════════════╝
                                                        │
                                            (검증 통과한 자료만 아래로)
                                                        │
                                                        ▼
                        ╔══════════════════════════════════════╗
                        ║  LAYER 3: CONTENT (슬라이드별 순차)  ║
                        ║                                       ║
                        ║  [6] Body Text Writer                 ║
                        ║      + Unifier + 🆕 acronym 감지      ║
                        ║                                       ║
                        ║  [7] Title & Subtitle Writer          ║
                        ║                                       ║
                        ║  [8] Visual Asset Curator             ║
                        ║      + 🆕 버핏 30% 분기 판정          ║
                        ╚══════════════════════════════════════╝
                                        │
                                        ▼
                        ╔══════════════════════════════════════╗
                        ║  LAYER 4: DESIGN                      ║
                        ║                                       ║
                        ║  [9]  Background Designer              ║
                        ║       (테마·배경·커버 독점성)          ║
                        ║                                       ║
                        ║  [10] Layout Composer                 ║
                        ║       (9-zone + 🆕 버핏 30% 배치      ║
                        ║        + 🆕 약자 풀이 배치)            ║
                        ║                                       ║
                        ║  [11] Final JSON Assembler            ║
                        ║       (Gemini JSON + 🆕 v4.0 감사)    ║
                        ╚══════════════════════════════════════╝
                                        │
                                        ▼
                              📦 slide_N.json (배치별)
                                        │
                                        ▼
                ╔══════════════════════════════════════╗
                ║  LAYER 5: DELIVERABLE 🆕 v4.0         ║
                ║                                       ║
                ║  [12] CTA Report Builder              ║
                ║       1-페이지 PDF (요약+차트 1-2개)    ║
                ║       Orchestrator가 CTA 배치 시 호출  ║
                ╚══════════════════════════════════════╝
                                        │
                                        ▼
                          📦 cta_report.pdf
```

---

## 🎯 v4.0 변경 영향이 있는 에이전트

### 🎛 [0] Orchestrator (v4.0 주요 역할 추가)

- **배치 페이싱**: 슬라이드 완성물을 `[HOOK 1장]`, `[본문 2장]`, `[본문 2장]`, ..., `[CTA 1장 + PDF 1개]` 구조로 묶어 전달
- **Agent 12 호출**: CTA 슬라이드 생성 시 부수적으로 `cta_report_builder` 호출
- **약자 레지스트리 관리**: 포스트 전체 약자 풀이 상태 추적
- **T-1 규칙 명시적 전달**: Phase 1 시작 시 리서치 에이전트에 data_freshness_rule 주입

### 🔍 [1][2][3][4] Research Layer (v4.0 규칙 수용)

- Agent 1, 3: **T-1 규칙 강제** + `data_freshness_attestation` 필드 출력
- Agent 2: 뉴스·정책은 공신력 소스면 기간 제한 없음, 단 "still_in_effect_as_of_today" 체크
- Agent 4: **CTA PDF 차트 후보 2개 선정** (primary + secondary) → Agent 12에 공급

### ✅ [5] Validator (v4.0 감사 강화)

- Round 1에 `data_freshness_compliance` 체크 추가
- T-1 규정 위반 수치는 자동 `rejected_findings`
- `data_freshness_audit` 객체 출력

### ✍️ [6] Body Writer (v4.0 약자 감지)

- 약자(2-5자 대문자) 등장 시 `acronym_report` 필드 작성
- 내부 화이트리스트(IPO, ETF, CEO, CPI 등) 외의 약자만 풀이 대상
- Orchestrator 레지스트리에 제출

### 🎭 [8] Visual Curator (v4.0 핵심 변경)

- 버핏 역할 분류: `mascot_corner_30pct | central_protagonist_full | cta_podium_medium`
- `mascot_corner_30pct` 케이스에서 `primary_subject_reference_for_sizing` 명시
- description_for_gemini에 "approximately 30% of {주인공}'s rendered size" 자연어 포함

### 🧩 [10] Layout Composer (v4.0 중요 확장)

- `buffett_placement_v4` 객체 출력 (case + zone + size_directive)
- `acronym_gloss_placements` 배열 (비어있는 모서리 선택)
- z-index 스택에 `acronym_gloss_footnotes` 최상단 추가

### 🧾 [11] Final Assembler (v4.0 감사 확장)

- 기본 체크리스트 (v3.2) + v4.0 추가 4개 체크:
  1. 버핏 30% 규칙 프롬프트 반영
  2. T-1 attestation 필드 존재
  3. 약자 풀이 별표 prefix
  4. batch_metadata 설정

### 📄 [12] CTA Report Builder 🆕 NEW

- Layer 5에 단독 존재
- Agent 4의 CTA PDF 차트 후보 활용
- 1페이지 PDF 생성 (reportlab 또는 weasyprint)
- T-1 데이터 attestation 포함
- Disclaimer + Sources 박스 필수

---

## 🔁 Reflection Loop 분포 (v4.0)

| Agent | Reflection 라운드 |
|-------|-------------------|
| 0. Orchestrator | — (제어만) |
| 1-4. Research Agents | 1라운드 |
| **5. Validator** | **2라운드** (핵심) |
| 6. Body Writer | 2라운드 |
| 7. Title Writer | 1라운드 |
| 8. Visual Curator | 1라운드 |
| 9. Background | 1라운드 |
| 10. Layout | 1라운드 |
| 11. Assembler | 0라운드 (검증만) |
| **12. CTA Report Builder** 🆕 | **1라운드** |

---

## 🙋 HITL 체크포인트 (v4.0 확장)

| CP | 시점 | 사용자 검토 대상 |
|----|------|-------------------|
| **CP1** | Layer 2 완료 후 | 리서치 품질 + 검증 결과 + **T-1 attestation** |
| **CP2** | 내러티브 아크 확정 후 | 슬라이드 구성안 + 텍스트 예산 + **CTA PDF 리포트 개요** |
| **CP3** | **각 배치 완료 후** (슬라이드별 → 배치별로 변경) | 배치 단위 승인 / 특정 슬라이드 수정 |
| └ CP3a | 커버 배치 (1장) | HOOK 슬라이드 승인 |
| └ CP3b~z | 본문 배치 (2장씩) | 2장 동시 승인 |
| └ CP3-final | CTA 배치 (슬라이드 1 + PDF 1) | CTA 슬라이드 + PDF 리포트 동시 승인 |
| **CP4** | 전체 완료 후 | 최종 통합 (모든 슬라이드 + PDF + 약자 레지스트리) |

---

## 📊 데이터 흐름 (v4.0)

```
User Topic
   ↓
[0] Orchestrator → T-1 rule 명시 전달 → 병렬 리서치 트리거
   ↓
[1][2][3][4] 4개 리서치 (동시, v4.0 freshness 준수)
   ↓ (research_bundle.json + CTA chart candidates)
[5] Validator (Reflection 2R) → HITL CP1 (T-1 감사 포함)
   ↓ (verified_research.json)
[0] Orchestrator → 내러티브 아크 결정 + Agent 12 pre-brief → HITL CP2
   ↓ (arc_blueprint.json + cta_pdf_outline)
[루프 시작: n = 1 → N]
   ↓
[6] Body Writer (R2R)  → 본문 + acronym_report
   ↓ (body_n.json)
[7] Title Writer (R1R) → 제목 + subtitle +10%
   ↓ (titles_n.json)
[8] Visual Curator (R1R) → 버핏 30% 분기 판정
   ↓ (visuals_n.json)
[9] Background Designer (R1R) → 테마 + 커버 독점성
   ↓ (background_n.json)
[10] Layout Composer (R1R) → 9-zone + 버핏 배치 + 약자 풀이
   ↓ (layout_n.json)
[11] Final Assembler → Gemini JSON + 6개 체크 + 배치 메타
   ↓ (slide_n.json)
[루프 종료]
   ↓
[Orchestrator 배치 페이싱]
  [배치 1: HOOK 단독] → HITL CP3a
  [배치 2: S2+S3] → HITL CP3b
  [배치 3: S4+S5] → HITL CP3c
  ...
  [마지막 배치 직전 - CTA 슬라이드]
   ↓
[12] CTA Report Builder (R1R) → 1페이지 PDF
   ↓ (cta_report.pdf)
  [마지막 배치: CTA 슬라이드 + PDF] → HITL CP3-final
   ↓
[0] Orchestrator → 최종 통합 → HITL CP4
   ↓
📦 최종 slide_01.json ~ slide_N.json + cta_report.pdf
```

---

## 🌏 언어 & 페르소나 (고정)

- **출력 언어**: English 100%
- **타겟**: US residents, age 18-30, retail finance enthusiasts
- **리서치 기준 (v4.0)**:
  - 수치 → T-1 영업일 종가 / 최근 발표분 (강제)
  - 분석·뉴스 → 공신력 소스 (tier 1-2), 기간 제한 없음, 단 현재 상황 반영
- **톤**: Morning Brew + The Hustle + finance Twitter/TikTok 밈 톤

---

## 📁 파일 구조 (v4.0)

```
프로젝트 루트/
├── 01_ARCHITECTURE.md              # 이 문서
├── 02_DESIGN_DNA.json              # 디자인 규칙 (v4.0 갱신)
├── 03_MASTER_PROMPT.md             # Orchestrator 활성화 프롬프트 (v4.0)
├── 04_AGENT_SCHEMAS.json           # 스키마 요약 (v4.0, 간소화)
├── 05_FEWSHOT_EXAMPLES.json        # 18 원본 역설계 (v4.0 주석 추가)
├── 06_GEMINI_JSON_TEMPLATE.json    # Gemini 템플릿 (v4.0)
├── 07_USAGE_GUIDE.md               # 사용 설명서 (v4.0)
├── 08_CTA_PDF_TEMPLATE.md          # 🆕 CTA PDF 구조 가이드
└── agents/
    ├── 00_orchestrator.md
    ├── 01_us_economy_analyst.md
    ├── 02_us_politics_analyst.md
    ├── 03_us_stock_market_analyst.md
    ├── 04_chart_data_analyst.md
    ├── 05_validator.md
    ├── 06_body_writer.md
    ├── 07_title_writer.md
    ├── 08_visual_curator.md
    ├── 09_background_designer.md
    ├── 10_layout_composer.md
    ├── 11_final_assembler.md
    └── 12_cta_report_builder.md     # 🆕 NEW v4.0
```
