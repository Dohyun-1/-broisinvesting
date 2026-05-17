# 📄 Agent 12 — CTA Report Builder ⭐ NEW v4.0

> **역할**: CTA에서 약속한 보상 자료(1페이지 PDF 리포트)를 카드뉴스와 동시 제작

---

## 📌 기본 정보

| 항목 | 값 |
|------|-----|
| Agent ID | `agent_12_cta_report_builder` |
| Layer | Layer 5 — Deliverable (🆕 v4.0 신설) |
| Reflection 라운드 | 1라운드 |
| 신설 버전 | **v4.0** |
| 출력 형식 | 1-페이지 PDF 파일 |

---

## 🎯 존재 이유

v3.x까지: CTA 슬라이드에서 "Comment 'BAGS'를 남기면 리포트를 보내드립니다"라고 약속만 하고, **실제 리포트는 제작 안 됨**. → 사용자가 나중에 직접 만들어야 했음.

v4.0: **카드뉴스 제작과 동시에** 보상 리포트를 생성하여 즉시 공유 가능.

---

## 🎯 주요 책무

1. 최종 검증된 리서치 번들(Agent 5의 verified_findings)을 1페이지로 요약
2. Agent 4가 선정한 **CTA PDF 차트 후보 2개** 중 1-2개 활용
3. Morning Brew/The Hustle 스타일 짧은 요약
4. Fed 정책·정치 맥락 배경 (공신력 소스 기반, 기간 제한 없음)
5. T-1 수치 반드시 포함 (카드뉴스와 최신성 일치)
6. PDF 파일 생성 (`cta_report.pdf`)

---

## 📄 1-페이지 PDF 리포트 구조

| 영역 | 내용 | 길이 |
|------|------|------|
| **Header** | 포스트 주제 한 줄 헤드라인 (뉴스페이퍼 세리프 느낌) | 1줄 |
| **Hook Paragraph** | "Why this matters right now" 3-4문장 | ~60단어 |
| **Key Data Points** | T-1 수치 3-5개 (불릿) | 각 1줄 |
| **Primary Chart** | Agent 4의 `cta_pdf_chart_candidates_v4.primary` | 페이지 1/2 점유 |
| **The Mechanism** | 메커니즘 설명 2-3문장 | ~50단어 |
| **Secondary Chart (optional)** | Agent 4의 `secondary` | 소형 |
| **What To Watch** | 향후 체크포인트 3개 (불릿) | 각 1줄 |
| **Sources** | 출처 박스 (소형 footer) | 3-5개 |
| **Disclaimer** | 투자 권유 아님 고지 | 1줄 footer |

**총 분량**: A4 또는 Letter 1페이지 (여백 포함)

---

## 🎨 PDF 디자인 스펙

| 요소 | 스펙 |
|------|------|
| 페이지 크기 | Letter (8.5 × 11 인치) 또는 A4 |
| 마진 | 상하좌우 0.75 인치 |
| 헤드라인 폰트 | Serif (Old Standard TT-like) 또는 시스템 serif |
| 본문 폰트 | Sans-serif (Roboto 또는 시스템 sans) |
| 색상 팔레트 | 본문 흑색 / 키워드 crimson (#C8302C) / 포지티브 green (#1A8F50) |
| 배경 | 순수 흰색 (카드뉴스와 달리 깔끔한 리포트 느낌) |
| 차트 배치 | 원본 스크린샷 스타일 OR 재생성 차트 |
| 브랜딩 푸터 | 발행자 이름 / 날짜 / 페이지 1/1 |

---

## 🆕 v4.0 데이터 최신성 규칙

**카드뉴스와 동일 규칙**:
- 수치 데이터: **T-1 영업일 종가** (주가·지수·금리)
- 경제 지표: 최근 발표분
- 배경 설명·정책 맥락: 공신력 소스면 기간 제한 없음

**attestation 필수**:
```json
"data_freshness_attestation": {
  "t1_reference_date": "2026-04-20",
  "generation_date": "2026-04-21",
  "numbers_verified_via_agent_5": true
}
```

---

## 🪞 Reflection 1R 체크리스트

- [ ] 헤드라인 카드뉴스 전체 메시지 요약?
- [ ] Hook paragraph 60단어 이내?
- [ ] Key data points 3-5개?
- [ ] Primary chart 존재 + Agent 4에서 지정된 것?
- [ ] 모든 수치가 Agent 5 verified_findings에서 온 것?
- [ ] T-1 규칙 준수 (수치 카테고리)?
- [ ] Sources 박스에 3개 이상 출처?
- [ ] Disclaimer 포함?
- [ ] 분량이 1페이지에 들어가는가? (2페이지 초과 시 축소)
- [ ] 영어로만 작성?

---

## 📤 입력

```json
{
  "verified_research": "Agent 5의 출력",
  "cta_pdf_chart_candidates": "Agent 4의 cta_pdf_chart_candidates_v4",
  "narrative_arc": "Orchestrator의 arc blueprint",
  "cta_keyword": "Comment 'XXX' (카드뉴스 CTA 슬라이드의 단어)",
  "post_topic": "string"
}
```

---

## 📤 출력

```json
{
  "agent": "cta_report_builder",
  "v": "4.0",
  "pdf_filepath": "cta_report.pdf",
  "pdf_content_manifest": {
    "headline": "string",
    "hook_paragraph": "string (60 words max)",
    "key_data_points": [
      {"label": "string", "value": "string", "date": "YYYY-MM-DD", "source": "string"}
    ],
    "primary_chart": {
      "viz_id_from_agent_4": "string",
      "caption": "string",
      "source_url": "string"
    },
    "mechanism_paragraph": "string (50 words max)",
    "secondary_chart": {
      "viz_id_from_agent_4": "string or null",
      "caption": "string or null"
    },
    "what_to_watch": ["string", "string", "string"],
    "sources": [{"title": "string", "url": "string", "date": "YYYY-MM-DD"}],
    "disclaimer": "string"
  },
  "data_freshness_attestation": {
    "t1_reference_date": "YYYY-MM-DD",
    "generation_date": "YYYY-MM-DD",
    "numbers_verified_via_agent_5": true,
    "numbers_count": "int"
  },
  "page_count": 1,
  "reflection_passed": true
}
```

---

## 🛠 구현 가이드 (Claude가 실행 시)

PDF 생성은 `reportlab` 또는 `weasyprint` (Python) 권장:

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table

# 또는 HTML → PDF로 weasyprint 사용 (더 유연한 레이아웃)
```

**권장**: HTML/CSS 템플릿을 작성한 뒤 weasyprint로 PDF 변환. CSS 제어가 쉬워 1페이지 레이아웃 맞추기 수월.

---

## ⚠️ 절대 금지사항

1. 2페이지 초과 금지 (1-페이지 리포트 제약)
2. Agent 5 rejected_findings의 수치 사용 금지
3. T-1 규정 위반 수치 사용 금지
4. 카드뉴스 CTA 슬라이드와 다른 "약속 키워드" 사용 금지 (일관성)
5. 투자 권유로 읽힐 수 있는 단정적 표현 금지 ("반드시 팔아라" 등)
6. Disclaimer 누락 금지
7. 출처 3개 미만 금지

---

## 💡 좋은 출력 예시 (content manifest)

```json
{
  "pdf_content_manifest": {
    "headline": "The Private Credit Bubble: Why 2026 Might Be 2008 All Over Again",
    "hook_paragraph": "Private credit AUM has ballooned to $2.1 trillion. 40% of loans now go to companies with negative free cash flow — up from 21% in 2021. Major banks are quietly starting to pull back. Here's what retail investors need to know — before the headlines hit.",
    "key_data_points": [
      {"label": "Private Credit AUM", "value": "$2.1T", "date": "2026-03-31", "source": "IMF GFSR"},
      {"label": "Loans to Negative-FCF firms", "value": "40% (vs 21% in 2021)", "date": "2026-03-31", "source": "IMF"},
      {"label": "10Y Treasury Yield (T-1)", "value": "4.32%", "date": "2026-04-20", "source": "US Treasury"},
      {"label": "S&P 500 (T-1 close)", "value": "5,842 (-0.3%)", "date": "2026-04-20", "source": "NYSE"},
      {"label": "JPMorgan PC Lending (YoY)", "value": "-18%", "date": "2026-Q1", "source": "10-Q filing"}
    ],
    "primary_chart": {
      "viz_id_from_agent_4": "viz_03",
      "caption": "From 21% to 40%: The Silent Shift in Private Credit Risk",
      "source_url": "https://www.imf.org/en/Publications/GFSR/..."
    },
    "mechanism_paragraph": "Private credit funds promise high yields by lending to riskier companies that banks avoid. When AI disrupts software revenue (25% of PC lending), loans sour. Funds freeze withdrawals to prevent a run. Sound familiar?",
    "secondary_chart": {
      "viz_id_from_agent_4": "viz_07",
      "caption": "Withdrawal Freezes: March-April 2026"
    },
    "what_to_watch": [
      "JPMorgan Q2 earnings (July 2026) — private credit exposure disclosure",
      "SEC final rule on PC fund concentration (expected Q3 2026)",
      "Additional withdrawal freezes at Apollo, Ares, Blue Owl"
    ],
    "sources": [
      {"title": "IMF Global Financial Stability Report", "url": "https://www.imf.org/...", "date": "2026-04"},
      {"title": "JPMorgan 10-Q Q1 2026", "url": "https://www.sec.gov/...", "date": "2026-04-15"},
      {"title": "Reuters: JPM reins in PC lending", "url": "https://www.reuters.com/...", "date": "2026-03-22"},
      {"title": "SEC Proposed Rule Release", "url": "https://www.sec.gov/rules/...", "date": "2026-02-14"}
    ],
    "disclaimer": "This report is for educational purposes only. Not financial advice. All data as of 2026-04-20 close."
  }
}
```
