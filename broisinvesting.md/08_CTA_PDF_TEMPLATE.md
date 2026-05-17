# 📄 CTA PDF TEMPLATE v4.0 — 1-페이지 보상 리포트 구조 가이드

> Agent 12 (CTA Report Builder)가 제작하는 `cta_report.pdf`의 상세 디자인 스펙. v4.0에서 새로 도입.

---

## 🎯 목적

CTA 슬라이드에서 "Comment 'BAGS' for the free report"라고 약속한 보상 자료를 **카드뉴스 제작과 동시에** 생성. 사용자가 나중에 직접 만들 필요 없이 즉시 공유 가능.

---

## 📐 페이지 스펙

| 항목 | 값 |
|------|-----|
| 페이지 크기 | Letter (8.5 × 11 in) 또는 A4 (210 × 297 mm) |
| 마진 | 상하좌우 각 0.75 in (19 mm) |
| 분량 | **정확히 1페이지** (2페이지 초과 시 축소) |
| 색상 모드 | RGB (디지털 배포) |
| 해상도 | 300 DPI (인쇄 가능 품질) |
| 파일 형식 | PDF (권장: `weasyprint` 또는 `reportlab` 사용) |
| 파일명 | `cta_report.pdf` |

---

## 🎨 비주얼 DNA

카드뉴스의 scrapbook 느낌과 달리, PDF는 **깔끔한 "Morning Brew / The Hustle" 스타일 리포트** 느낌:

| 요소 | 스펙 |
|------|-----|
| 배경 | 순수 흰색 (#FFFFFF) |
| 헤드라인 폰트 | Serif (Old Standard TT, Merriweather, 또는 시스템 serif) |
| 본문 폰트 | Sans-serif (Roboto, Inter, 또는 시스템 sans) |
| 본문 색상 | 진한 블랙 (#1A1A1A) |
| 키워드 강조 | 크림슨 (#C8302C) |
| 포지티브 강조 | 에메랄드 그린 (#1A8F50) |
| 차트 강조색 | 크림슨 또는 네이비 (#1F3A5F) |
| 구분선 | 얇은 회색 (#CCCCCC, 0.5pt) |

---

## 📋 1-페이지 구조 (상단부터 순서)

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  🏷️ HEADER                                                │
│  ──────────────────────────────────────────              │
│  Serif headline (24-28pt)                                │
│                                                          │
│  📖 HOOK PARAGRAPH                                        │
│  3-4 sentences, ~60 words                                │
│  (Sans-serif body, 11pt)                                 │
│                                                          │
│  🔢 KEY DATA POINTS                                       │
│  • Label: Value (date) — Source                          │
│  • Label: Value (date) — Source                          │
│  • Label: Value (date) — Source                          │
│                                                          │
│  📊 PRIMARY CHART (1/2 page width or full width)          │
│  ┌──────────────────────────────┐                        │
│  │                              │                        │
│  │        [Chart Image]         │                        │
│  │                              │                        │
│  └──────────────────────────────┘                        │
│  Caption (9pt italic)                                    │
│                                                          │
│  ⚙️ THE MECHANISM                                          │
│  2-3 sentences, ~50 words                                │
│                                                          │
│  📊 SECONDARY CHART (optional, small)                     │
│  ┌──────────┐                                            │
│  │ [Chart]  │                                            │
│  └──────────┘                                            │
│                                                          │
│  👀 WHAT TO WATCH                                         │
│  • Milestone 1 (expected timing)                         │
│  • Milestone 2                                           │
│  • Milestone 3                                           │
│                                                          │
│  ───────────────────────────────────                     │
│  📚 SOURCES                                               │
│  [1] Title — URL — Date                                  │
│  [2] Title — URL — Date                                  │
│  [3] Title — URL — Date                                  │
│                                                          │
│  ⚠️ Disclaimer: Educational purposes only. Not advice.    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 📝 각 섹션 상세

### 1. HEADER (헤드라인)

- **폰트**: Serif, 24-28pt, bold
- **길이**: 1줄 (8-14단어 권장)
- **내용**: 카드뉴스 전체 메시지를 한 문장으로 요약
- **예시**: "The Private Credit Bubble: Why 2026 Might Be 2008 All Over Again"

### 2. HOOK PARAGRAPH

- **폰트**: Sans-serif, 11pt
- **길이**: **60단어 이하** (3-4 문장)
- **목적**: 왜 지금 이 이슈가 중요한지 요약
- **키워드 강조**: 1-2개 단어에 크림슨
- **예시**:
  > "Private credit AUM has ballooned to $2.1 trillion. **40% of loans** now go to companies with negative free cash flow — up from 21% in 2021. Major banks are quietly pulling back. Here's what retail investors need to know — before the headlines hit."

### 3. KEY DATA POINTS (핵심 수치 불릿)

- **개수**: 3-5개
- **형식**: `• Label: Value (as of YYYY-MM-DD) — Source`
- **필수**: T-1 수치 최소 1개 + 최근 발표분 지표 최소 1개 포함
- **예시**:
  - Private Credit AUM: $2.1T (2026-03-31) — IMF GFSR
  - Loans to Negative-FCF firms: 40% vs 21% in 2021 (2026-03-31) — IMF
  - 10Y Treasury Yield (T-1): 4.32% (2026-04-20) — US Treasury
  - S&P 500 (T-1 close): 5,842 (-0.3%) (2026-04-20) — NYSE
  - JPMorgan PC Lending (YoY): -18% (2026-Q1) — 10-Q filing

### 4. PRIMARY CHART (핵심 차트)

- **출처**: Agent 4의 `cta_pdf_chart_candidates_v4.primary`
- **크기**: 페이지 너비의 약 50-100% (시각 임팩트 기준)
- **캡션**: 9pt italic, 차트 아래 배치
- **주석 허용**: 핵심 데이터 포인트에 화살표·원·빨간 박스 오버레이 OK
- **예시 캡션**: "From 21% to 40%: The Silent Shift in Private Credit Risk (IMF GFSR April 2026)"

### 5. THE MECHANISM (메커니즘 설명)

- **폰트**: Sans-serif, 11pt
- **길이**: **50단어 이하** (2-3 문장)
- **목적**: 이 문제가 왜 발생하는지 (인과 구조)
- **예시**:
  > "Private credit funds promise high yields by lending to riskier companies banks avoid. When AI disrupts software revenue (25% of PC lending), loans sour. Funds freeze withdrawals to prevent a run. Sound familiar?"

### 6. SECONDARY CHART (선택적 보조 차트)

- **출처**: Agent 4의 `cta_pdf_chart_candidates_v4.secondary` (있을 경우만)
- **크기**: 작게 (페이지 너비의 30-40%)
- **캡션**: 9pt italic
- **생략 가능**: primary chart만으로 충분하면 secondary 생략 OK

### 7. WHAT TO WATCH (향후 체크포인트)

- **개수**: **정확히 3개**
- **형식**: `• Event or milestone (expected timing)`
- **목적**: 독자가 이후 추적할 구체적 사건
- **예시**:
  - JPMorgan Q2 earnings (July 2026) — private credit exposure disclosure
  - SEC final rule on PC fund concentration (expected Q3 2026)
  - Additional withdrawal freezes at Apollo, Ares, Blue Owl (ongoing)

### 8. SOURCES (출처 박스)

- **개수**: **최소 3개, 최대 7개**
- **형식**: `[번호] 제목 — URL — Date`
- **우선순위**: primary_gov > major_media > analysis_thinktank
- **폰트**: Sans-serif, 9pt
- **예시**:
  - [1] IMF Global Financial Stability Report (April 2026) — imf.org — 2026-04
  - [2] JPMorgan 10-Q Q1 2026 — sec.gov — 2026-04-15
  - [3] Reuters: JPM reins in PC lending — reuters.com — 2026-03-22
  - [4] SEC Proposed Rule Release — sec.gov — 2026-02-14

### 9. DISCLAIMER (고지)

- **폰트**: Sans-serif, 8pt, italic
- **색상**: 연한 회색 (#666666)
- **내용 예시**:
  > "This report is for educational purposes only and does not constitute financial advice. All numerical data is as of 2026-04-20 market close. Past performance does not indicate future results. Always consult a licensed financial advisor."

---

## 🛠 구현 예시 (Python)

### 옵션 1: weasyprint (HTML/CSS 기반 — 권장)

```python
from weasyprint import HTML, CSS

html_content = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    @page {{ size: Letter; margin: 0.75in; }}
    body {{ font-family: 'Roboto', 'Helvetica', sans-serif; color: #1A1A1A; font-size: 11pt; line-height: 1.4; }}
    h1 {{ font-family: 'Merriweather', 'Georgia', serif; font-size: 24pt; margin: 0 0 12pt 0; }}
    .hook {{ font-size: 11pt; margin-bottom: 14pt; }}
    .key-data {{ list-style: none; padding: 0; margin: 0 0 14pt 0; }}
    .key-data li {{ padding: 4pt 0; border-bottom: 0.5pt solid #CCCCCC; }}
    .chart-primary {{ width: 100%; margin: 12pt 0; }}
    .chart-caption {{ font-size: 9pt; font-style: italic; color: #666; margin-top: 4pt; }}
    .mechanism {{ margin: 14pt 0; }}
    .watch {{ list-style-type: disc; margin: 0 0 14pt 20pt; }}
    .sources {{ font-size: 9pt; border-top: 0.5pt solid #CCCCCC; padding-top: 8pt; margin-top: 14pt; }}
    .disclaimer {{ font-size: 8pt; font-style: italic; color: #666; margin-top: 10pt; }}
    strong.key {{ color: #C8302C; }}
  </style>
</head>
<body>
  <h1>{manifest['headline']}</h1>
  <p class="hook">{manifest['hook_paragraph']}</p>
  <ul class="key-data">
    {"".join([f"<li><strong>{d['label']}</strong>: {d['value']} ({d['date']}) — {d['source']}</li>" for d in manifest['key_data_points']])}
  </ul>
  <img src="{primary_chart_path}" class="chart-primary" />
  <p class="chart-caption">{manifest['primary_chart']['caption']}</p>
  <p class="mechanism">{manifest['mechanism_paragraph']}</p>
  <h3>What To Watch</h3>
  <ul class="watch">
    {"".join([f"<li>{w}</li>" for w in manifest['what_to_watch']])}
  </ul>
  <div class="sources">
    <strong>Sources</strong>
    {"<br/>".join([f"[{i+1}] {s['title']} — {s['url']} — {s['date']}" for i, s in enumerate(manifest['sources'])])}
  </div>
  <p class="disclaimer">{manifest['disclaimer']}</p>
</body>
</html>
"""

HTML(string=html_content).write_pdf("cta_report.pdf")
```

### 옵션 2: reportlab (프로그래매틱 제어 — 복잡)

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, ListFlowable, ListItem

doc = SimpleDocTemplate("cta_report.pdf", pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)
styles = getSampleStyleSheet()
# ... build story with Paragraph, Image, ListFlowable
doc.build(story)
```

---

## ✅ Agent 12 최종 체크리스트

제작 완료 전 확인:

- [ ] 정확히 1페이지?
- [ ] 헤드라인 serif 24-28pt?
- [ ] Hook paragraph 60단어 이하?
- [ ] Key data points 3-5개?
- [ ] 모든 수치 `source` + `date` 포함?
- [ ] T-1 수치 최소 1개 포함 (수치 중요 포스트)?
- [ ] Primary chart 포함?
- [ ] Primary chart 캡션 포함?
- [ ] Mechanism paragraph 50단어 이하?
- [ ] What to watch 정확히 3개?
- [ ] Sources 3-7개?
- [ ] 모든 source URL 유효?
- [ ] Disclaimer 포함?
- [ ] 영어 100%?
- [ ] 파일명 `cta_report.pdf`?
- [ ] 크림슨 키워드 강조 1-3개?

---

## 🎁 좋은 리포트 예시 (요약)

```
HEADLINE: The Private Credit Bubble: Why 2026 Might Be 2008 All Over Again

HOOK: Private credit AUM has ballooned to $2.1 trillion. 40% of loans 
now go to companies with negative free cash flow — up from 21% in 2021. 
Major banks are quietly starting to pull back. Here's what retail 
investors need to know — before the headlines hit.

KEY DATA:
• Private Credit AUM: $2.1T (2026-03-31) — IMF GFSR
• Loans to Negative-FCF firms: 40% vs 21% in 2021 (2026-03-31) — IMF
• 10Y Treasury Yield (T-1): 4.32% (2026-04-20) — US Treasury
• S&P 500 (T-1 close): 5,842 (-0.3%) (2026-04-20) — NYSE
• JPMorgan PC Lending (YoY): -18% (2026-Q1) — 10-Q filing

[PRIMARY CHART: Bar chart showing 21% → 40% over 2021-2026]
Caption: From 21% to 40% — The Silent Shift in Private Credit Risk

MECHANISM: Private credit funds promise high yields by lending to 
riskier companies banks avoid. When AI disrupts software revenue 
(25% of PC lending), loans sour. Funds freeze withdrawals to prevent 
a run. Sound familiar?

[SECONDARY CHART: Line chart of withdrawal freezes Mar-Apr 2026]
Caption: Withdrawal Freezes, March-April 2026

WHAT TO WATCH:
• JPMorgan Q2 earnings (July 2026) — PC exposure disclosure
• SEC final rule on PC fund concentration (Q3 2026)
• Additional withdrawal freezes at Apollo, Ares, Blue Owl

SOURCES:
[1] IMF Global Financial Stability Report — imf.org — April 2026
[2] JPMorgan 10-Q Q1 2026 — sec.gov — 2026-04-15
[3] Reuters: JPM reins in PC lending — reuters.com — 2026-03-22
[4] SEC Proposed Rule Release — sec.gov — 2026-02-14

DISCLAIMER: This report is for educational purposes only and does not 
constitute financial advice. Data as of 2026-04-20 market close. 
Always consult a licensed financial advisor.
```

---

## 🚫 절대 금지사항

1. 2페이지 초과 금지
2. Agent 5 `rejected_findings` 수치 사용 금지
3. T-1 규정 위반 수치 사용 금지
4. 투자 권유 단정형 표현 금지 ("반드시 팔아라", "무조건 사라")
5. Disclaimer 누락 금지
6. 출처 3개 미만 금지
7. 카드뉴스의 `cta_keyword`와 다른 단어 사용 금지 (CTA 슬라이드와 PDF의 키워드 일치)
8. 영어 이외 언어 사용 금지
9. 차트 없이 텍스트만으로 구성 금지 (최소 primary chart 필요)

---

**끝.** Agent 12는 이 가이드를 완전히 내부화하여 PDF를 제작합니다.
