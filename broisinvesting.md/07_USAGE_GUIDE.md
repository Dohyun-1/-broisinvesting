# 📖 USAGE GUIDE v4.0 — 카드뉴스 AI 생성 시스템 사용 설명서

> **대상 독자**: Claude에 이 시스템을 적용하여 카드뉴스를 생성하려는 사용자 / 시스템 관리자

---

## 🎯 이 시스템이 하는 일

사용자가 주제를 입력하면, **12+1 에이전트**가 순차적·병렬적으로 협업하여:

1. 주제 관련 리서치 (경제·정치·시장·차트 데이터) 수행
2. Reflection 기반 팩트체크
3. Instagram 4:5 (1080×1350) 카드뉴스 N장 (6-9장) 제작용 **Gemini JSON 프롬프트** 생성
4. **🆕 v4.0**: CTA 슬라이드에 약속된 보상 자료를 **1페이지 PDF 리포트**로 동시 제작
5. 커버(1) + 본문(2장씩) + CTA(1장+PDF) 구조의 배치로 사용자에게 순차 전달

각 배치에서 사용자 승인(HITL)을 받아 진행하므로 품질과 통제력 모두 확보 가능.

---

## 🚀 빠른 시작

### Step 1: 시스템 프롬프트 활성화

Claude에게 다음과 같이 요청:

```
/home/claude/v4.0/03_MASTER_PROMPT.md 내용을 시스템 프롬프트로 로드해줘.
그리고 필요할 때마다 agents/ 폴더의 개별 에이전트 MD를 참조해서 
각 에이전트의 역할을 수행해줘.
```

또는 Master Prompt의 내용을 직접 복사하여 새 대화의 system 영역에 붙여넣기.

### Step 2: 주제 입력

예시:
```
주제: "Private Credit이 2026년판 2008년이 될까?"
슬라이드 수: 8
톤: standard
CTA 보상: 1-page PDF report
```

### Step 3: HITL 체크포인트 응답

Orchestrator가 Phase별로 다음과 같이 질문:

- **CP1** (리서치 후): "리서치 품질 승인? 재검색? 특정 finding 제외?"
- **CP2** (아크 후): "내러티브 아크 승인? CTA PDF 개요 OK?"
- **CP3a~CP3-final** (배치별): "배치 {X} 승인? 수정? 재생성?"
- **CP4** (완료 후): "전체 최종 승인?"

각 체크포인트에서 `✅ OK` / `✏️ 수정` / `🔄 재생성` 중 선택.

### Step 4: 결과물 수령

최종 출력:
- `slide_01.json` ~ `slide_N.json` (각 슬라이드의 Gemini JSON)
- `cta_report.pdf` (1페이지 PDF 리포트)
- `manifest.json` (메타데이터 + 약자 레지스트리 + data freshness audit)

각 `slide_N.json`의 `gemini_prompt` 필드를 **Gemini 2.5 Flash Image**에 직접 투입하여 이미지 생성.

---

## 🆕 v4.0 5대 변경 사항

| # | 변경 내용 | 영향 |
|---|-----------|------|
| 1 | **버핏 30% 크기 규칙** | 코너/모서리 마스코트 배치 시 주인공 인물의 ~30% 크기로 축소 (자연어 묘사) |
| 2 | **T-1 데이터 강제** | 수치·지표는 T-1 영업일 종가/최근 발표분 강제 / 뉴스·분석은 공신력 기준 |
| 3 | **CTA PDF 자동 제작** | 새 Agent 12가 카드뉴스와 동시에 1페이지 PDF 리포트 생성 |
| 4 | **에이전트 MD 완전 분리** | Orchestrator + 12 에이전트 = 13개 독립 MD 파일 |
| 5 | **배치 페이싱** | 커버(1) + 본문(2씩) + CTA(1+PDF) 구조로 순차 전달 / HITL CP3도 배치별 |

추가: v3.3 acronym gloss가 v4.0에 공식 흡수 — Orchestrator가 포스트 전체 약자 레지스트리 관리.

---

## 📁 파일 구조

```
v4.0/
├── 01_ARCHITECTURE.md         # 아키텍처 개요
├── 02_DESIGN_DNA.json         # 디자인 규칙 (테마·폰트·색상·크기)
├── 03_MASTER_PROMPT.md        # Orchestrator 활성화 프롬프트 ⭐
├── 04_AGENT_SCHEMAS.json      # 에이전트 간 인터페이스 요약
├── 05_FEWSHOT_EXAMPLES.json   # 18 원본 슬라이드 역설계 참조
├── 06_GEMINI_JSON_TEMPLATE.json  # 슬라이드 JSON 템플릿
├── 07_USAGE_GUIDE.md          # 이 문서
├── 08_CTA_PDF_TEMPLATE.md     # CTA PDF 리포트 구조 가이드 🆕
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
    └── 12_cta_report_builder.md   🆕
```

**읽는 순서 권장**:
1. `01_ARCHITECTURE.md` — 전체 구조 파악
2. `03_MASTER_PROMPT.md` — 관제탑 규칙
3. `02_DESIGN_DNA.json` — 디자인 DNA 이해
4. 필요한 에이전트의 MD 파일 — 상세 규칙

---

## 🧭 사용 시나리오별 가이드

### 시나리오 A: 처음부터 카드뉴스 제작

1. Claude에게 `03_MASTER_PROMPT.md`를 시스템 프롬프트로 로드
2. 주제 입력: "미국 상업용 부동산 위기"
3. 슬라이드 수 선택 (default 8)
4. Phase 1-4 진행 중 각 CP에서 응답
5. Phase 5 (완료) 시 JSON 파일들 + PDF 수령
6. JSON의 `gemini_prompt`를 Gemini 2.5 Flash Image에 투입

### 시나리오 B: 기존 포스트 수정

1. 이전에 생성된 `slide_N.json` 파일 로드
2. Claude에게 "이 슬라이드의 [특정 요소]를 수정해줘" 요청
3. 적절한 에이전트 (보통 Agent 6/7/8/10) 재호출
4. Agent 11에서 재조립
5. 수정된 JSON 재생성

### 시나리오 C: CTA PDF만 재생성

1. 이전 `verified_research.json` 로드
2. Agent 12 (`agents/12_cta_report_builder.md` 규칙 적용) 재호출
3. 새로운 `cta_report.pdf` 생성

### 시나리오 D: 약자 풀이 정책 변경

1. `02_DESIGN_DNA.json`의 `acronym_gloss_rules_v4.common_whitelist_no_gloss_needed` 수정
2. 이후 생성되는 포스트에 새 화이트리스트 적용

---

## 🛠 커스터마이징 가이드

### 톤 강도 조절

Phase 0 인테이크에서:
- `tone_intensity: "mild"` — 슬랭 최소, 차분한 분석
- `tone_intensity: "standard"` (default) — 원본 스타일
- `tone_intensity: "aggressive"` — 최대 밈/슬랭/선정성

### 슬라이드 수 조절

- 6장: 짧은 팩트 요약
- 8장 (default): 일반 포스트
- 9장: 대형 이벤트 (macro_event_9 arc)

### 버핏 마스코트 비율 조절

`02_DESIGN_DNA.json`의 `character_system.warren_buffett_mascot.frequency_target` 수정:
- `"~40%"` (default v4.0 — HOOK + CTA + 선택 본문 1-2장, 권장)
- `"~25%"` — 최소 등장 (HOOK + CTA만, 마스코트 절제 시)
- `"~50%"` — 강조 등장 (마스코트 캐릭터를 더 부각하고 싶을 때)
- 50% 초과는 임팩트 희석 위험 — 비권장

### 테마 분포 조절

`02_DESIGN_DNA.json`의 `theme_system.{theme}.usage_ratio` 수정. 단, 합계는 100% 유지.

---

## 🐛 트러블슈팅

### 문제: "Gemini가 JSON/hex 코드를 텍스트로 그려넣음"
→ Agent 11의 누출 스캔이 실패한 것. `11_final_assembler.md`의 체크리스트 재확인. `gemini_prompt` 필드에 `{`, `}`, `#`, `px` 등이 있으면 제거.

### 문제: "버핏 마스코트가 너무 큼 (30% 규칙 무시)"
→ Agent 8에서 `buffett_size_rule_v4: "mascot_corner_30pct"` 설정 확인. Agent 10의 `buffett_placement_v4.size_directive_for_prompt`에 "approximately 30% of {primary_subject}'s rendered size" 자연어 포함 확인. Agent 11이 gemini_prompt에 이 자연어를 전달했는지 확인.

### 문제: "오래된 주가/지수가 들어감"
→ Agent 5 Validator가 `t1_rule_passed: false`를 잡아냈어야 함. Phase 1에서 `MANDATORY_DATA_FRESHNESS_RULE_v4.0`이 명시적으로 전달됐는지, 리서치 에이전트가 웹 검색을 실제로 수행했는지 확인.

### 문제: "CTA PDF가 생성 안 됨"
→ Orchestrator가 CTA 슬라이드 생성 후 Agent 12를 호출했는지 확인. Agent 4의 `cta_pdf_chart_candidates_v4`가 CP2에서 확정됐는지 확인.

### 문제: "같은 약자가 여러 슬라이드에 반복 풀이됨"
→ Orchestrator의 acronym_registry가 제대로 업데이트되지 않은 것. Agent 6/7가 `acronym_report`를 Orchestrator에 제출하고, Orchestrator가 Agent 10에 "이번 슬라이드에서 풀이할 약자 목록"을 전달하는 흐름 확인.

### 문제: "배치가 3장으로 묶여서 전달됨"
→ Orchestrator의 배치 페이싱 위반. `03_MASTER_PROMPT.md`의 "배치 페이싱" 섹션의 pseudo-code 참조. 커버는 1장, CTA는 1장+PDF, 나머지 본문만 2장씩.

### 문제: "HOOK 슬라이드가 아닌데 스프링+연필이 나옴"
→ Agent 9/10/11의 `cover_exclusive_tokens_correctly_applied` 체크 실패. slide_role이 HOOK일 때만 허용되는 토큰임을 강제.

### 문제: "light 테마에 격자(grid)가 그려짐"
→ `light_lined` 테마는 **가로줄만**. Agent 9의 `ruling_style: "horizontal_only"`를 확인하고, gemini_prompt에 "NO vertical lines, NO grid pattern" 명시 여부 확인.

---

## 📊 데이터 최신성 예외 사례 (v4.0)

| 시나리오 | 분류 | T-1 적용? |
|---------|------|-----------|
| "어제 S&P500 종가 얼마?" | numerical (index_close) | YES, T-1 종가 |
| "최근 CPI 얼마?" | latest_release (CPI) | YES, 최근 발표분 |
| "지난주 FOMC 회의 내용" | latest_release (FOMC) | YES, 최신 회의 |
| "Dot-com 버블은 언제 터졌나?" | historical context | NO, 무제한 |
| "Michael Burry의 Big Short 전략은?" | analysis / history | NO, 무제한 |
| "Fed가 작년에 했던 발언" | policy analysis | NO, 단 여전히 유효한지 체크 |
| "2001년 연준 금리 인하 사례" | historical context | NO, 무제한 |
| "JP Morgan CEO의 최신 인터뷰 요지" | news (credible source) | NO, 기간 제한 없음 but credible |

---

## 🎨 v4.0 버핏 크기 규칙 예시

### 예 1: 본문 EVIDENCE 슬라이드
- 중앙: 40% 빅스탯 (primary subject)
- 버핏 배치: `mascot_corner_30pct` → bottom_left, 40% 스탯의 ~30% 크기
- gemini_prompt: "... Render him at approximately 30% of the size of the central 40% big stat hero element..."

### 예 2: HOOK 슬라이드 (주인공 = 인물)
- 중앙: Larry Fink 컷아웃 (primary subject)
- 버핏 배치: `mascot_corner_30pct` → bottom_left, Fink의 ~30% 크기
- gemini_prompt: "... Render him at approximately 30% of the size of Larry Fink's cutout..."

### 예 3: 주제가 버핏 본인
- 중앙: 버핏 본인 (central_protagonist)
- 버핏 배치: `central_protagonist_full` → middle_center, 큰 크기 (30% 규칙 예외)
- gemini_prompt: "... place a large photorealistic cutout of Warren Buffett..."

### 예 4: CTA 슬라이드
- 버핏 배치: `cta_podium_medium` → middle_center, 중간 크기 (30% 규칙 예외)
- gemini_prompt: "... place a photorealistic cutout of Warren Buffett at the Berkshire Hathaway annual meeting podium..."

---

## 🚫 절대 금지사항 (요약)

1. HITL 체크포인트 스킵 금지
2. 배치당 이미지 JSON 3장 이상 전달 금지
3. CTA 슬라이드만 전달하고 PDF 누락 금지
4. T-1 규정 위반 수치 통과 금지
5. 영어 이외 언어로 슬라이드 콘텐츠 생성 금지
6. `gemini_prompt`에 JSON/hex/px/폰트명 리터럴 포함 금지
7. 비-HOOK에 스프링+연필 배치 금지
8. HOOK에 마스킹테이프/압정 대신 스프링+연필 누락 금지
9. 같은 약자를 한 포스트에서 2회 이상 풀이 금지
10. 버핏 mascot_corner 케이스에서 30% 규칙 누락 금지
11. `binder_clip` 사용 금지 (deprecated since v3.2)
12. `light_grid` 테마명 사용 금지 (`light_lined`로 통일)

---

## 📚 참고 문서 연결

| 주제 | 참조 문서 |
|------|-----------|
| 아키텍처 전체 | `01_ARCHITECTURE.md` |
| 디자인 DNA (테마·폰트) | `02_DESIGN_DNA.json` |
| Orchestrator 활성화 | `03_MASTER_PROMPT.md` |
| 에이전트 간 인터페이스 | `04_AGENT_SCHEMAS.json` |
| 원본 슬라이드 역설계 | `05_FEWSHOT_EXAMPLES.json` |
| Gemini JSON 구조 | `06_GEMINI_JSON_TEMPLATE.json` |
| CTA PDF 구조 | `08_CTA_PDF_TEMPLATE.md` |
| 개별 에이전트 상세 | `agents/{agent}.md` |

---

## 📬 질문·피드백

이 시스템의 사용 중 문제 발생 시:
1. Reflection 라운드가 제대로 수행됐는지 확인
2. 각 에이전트 MD 파일의 "절대 금지사항" 섹션 재확인
3. Agent 11의 `quality_checklist_passed` 필드에서 실패한 체크 항목 확인
4. 누락된 HITL 응답이 있는지 체크

---

**v4.0 — 최종 승인 후 배포.**
