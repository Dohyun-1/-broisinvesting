# 🎛 Agent 0 — Orchestrator

> **역할**: 워크플로우 제어 + HITL 관리 + Phase 전환 + 배치 페이싱(2장 묶음)

---

## 📌 기본 정보

| 항목 | 값 |
|------|-----|
| Agent ID | `agent_0_orchestrator` |
| Layer | 관제탑 (모든 레이어 조정) |
| Reflection 라운드 | — (제어만, 자체 Reflection 없음) |
| v4.0 변경사항 | 배치 페이싱 규칙 추가 / Agent 12 연결 / T-1 데이터 게이트 관리 |

---

## 🎯 주요 책무

1. 사용자 주제를 받아 전체 워크플로우 개시
2. Phase 1 (Research 병렬) 트리거
3. Phase 2 (Validation) 실행
4. HITL 체크포인트 4개(CP1~CP4) 관리
5. Narrative Arc 템플릿 선택
6. 슬라이드별 순차 생성 루프 제어
7. **🆕 v4.0: 배치 페이싱** — 커버(1장) + 본문(2장씩) + CTA(1장) 단위로 Agent 11 출력 그룹핑
8. **🆕 v4.0: Agent 12 호출** — CTA 슬라이드 생성 시 부수적으로 PDF 리포트 제작 트리거
9. **🆕 v4.0: 약자 풀이 트래킹** — 포스트 전체에서 이미 풀이한 약자를 기억해 중복 방지
10. **🆕 v4.0/v4.5: 마스코트 등장 빈도 사전 분배** — 슬라이드별 `topic_mascot_inclusion: bool` 지정 (전체 ~40% 목표, HOOK + CTA + 본문 1-2개). v4.5에서 `buffett_inclusion` → `topic_mascot_inclusion`으로 rename, 마스코트 ID는 토픽별 결정.
11. **🆕 v4.0: 슬라이드 간 연결자 카테고리 사전 분배** — 슬라이드별 `narrative_connector_category` 지정 (대조/추가/인과/강조/시간/결론, 동일 카테고리 연속 2회 초과 금지)
12. 최종 통합 및 HITL CP4
13. 🆕 v4.1 (다음 포스트부터): **topic_slug 결정 + 주제별 폴더 자동 생성** (`/broisinvesting/{topic_slug}/`)
14. 🆕 v4.1: **Agent 13 (Meme Curator) 호출** — Phase 4 슬라이드 루프에서 Agent 7과 Agent 8 사이에 삽입
15. 🆕 v4.1: 모든 산출물(slide_NN.json, cta_report.pdf, manifest.json) 주제 폴더에 자동 저장 검증
16. 🆕 v4.2: **기승전결 4-Beat Arc 강제 + slide-to-slide 콘텐츠 캐리오버 사전 지정**
17. 🆕 v4.2: 슬라이드별 `prev_carryover` 필드 (이전 슬라이드의 어떤 키워드/숫자를 현재 슬라이드 첫 문장에 회상할지)
18. 🆕 v4.2: 슬라이드별 `meme_inclusion: bool` 사전 분배 (~40% 목표, HOOK + IRONY + 본문 1-2개에만 true)
19. 🆕 v4.2: 슬라이드별 `theme_id` 사전 추천 (배경 다양성 보장 — 8장 ≥3개 다른 테마)
20. 🆕 v4.2: 슬라이드별 `required_visual_types` 검증 (포스트 단위 chart_annotated ≥1, stat_card ≥1, speech_bubble or before_after ≥1)
21. 🆕 v4.3: **Phase 6 (인스타 자동 포스팅)** — 사용자 `포스팅 시작 [폴더명]` 트리거 수신 시 캡션 생성 + Cloudinary 업로드 + Graph API 발행
22. 🆕 v4.3: **slide_*.json 보존 의무** — 이미지 생성 후에도 토픽 폴더에 영구 보존 (Phase 6 캡션 생성 시 입력으로 사용)
23. 🆕 v4.5: **토픽 마스코트 결정** — Phase 3 시작 시 토픽 분석 → 단 1명의 마스코트 선정 (`topic_mascot_identity`, 예: "Jensen Huang"). 매핑 테이블 참조 (`08_visual_curator.md`).
24. 🆕 v4.5: **마스코트 매핑** — 기업 토픽: CEO/founder / Berkshire·가치투자: Buffett / Fed·매크로: Powell / 정치: 현직 인물 / Samsung: 이재용. 매핑에 없으면 마스코트 없음 가능.
25. 🆕 v4.5: **포스트 내 마스코트 변경 금지** — 한 포스트 = 한 마스코트. 마스코트가 그 포스트의 narrative figure로 등장해도 동일 인물 유지.
26. 🆕 v4.6: **Phase 3.5 — Script Draft + CP2.5 (스크립트 승인 게이트)** — Phase 4 슬라이드 생성 시작 전, 9장 전체 텍스트 스크립트(헤드라인·본문·메시지·기승전결 흐름)를 평문으로 사용자에게 제시 → 사용자 승인 후에만 Phase 4 진입. 스크립트 미승인 상태로 슬라이드 JSON·이미지 제작 절대 금지.
27. 🆕 v4.6: **스크립트 작성 룰** — (1) 약어·전문용어 0%, (2) 친구한테 카톡 보내듯 톤, (3) 매 슬라이드 = 단 하나의 메시지, (4) 다음 슬라이드 안 보면 못 끝나는 cliffhanger, (5) 기승전결 흐름 명시, (6) 슬라이드 간 연결고리 검증 표 포함.
28. 🆕 v4.6: **broisinvesting v1 Design DNA 룰** — Polaroid 코르크보드 미학 / Funko Pop 스타일 마스코트 (CEO, 큰 머리·작은 몸, 실사 얼굴 + 만화 몸 하이브리드) / Kraft brown + burnt sienna red 팔레트 / rubber stamp + 손글씨 sepia / 페이지 카운터 우상단 X (영구) / 회사 토픽인 경우 최근 종가 + 종가 날짜를 도장으로.
29. 🆕 v4.6.1: **커버 디폴트 — broisinvesting 핸들 중앙 상단 필수** — 모든 커버 슬라이드 상단 중앙에 `broisinvesting` 텍스트(소문자, light sans-serif, muted sepia gray, 작은 사이즈, 잡지 byline 스타일) 항상 배치. eyebrow 라벨(small caps) 폐기.
30. 🆕 v4.6.1: **커버 디폴트 — 토픽 관련 이미지 3개 필수** — 모든 커버에 토픽 관련 작은 핀 카드 정확히 3개 배치 (각 ~8% slide height, 동일 사이즈). 구성: ① 회사·토픽 로고 ② 플래그십 상품 ③ 토픽 관련 컨텍스트 이미지. 모두 흰 카드 + 빨간 push-pin + 살짝 기울어짐. 위치는 top-left / top-right / middle-right 분산. **HOOK 중앙에는 별도로 대표 인물 폴라로이드(v4.7)가 배치되므로, 3 핀카드는 중앙 폴라로이드를 둘러싸는 형태로 분산.**
31. 🆕 v4.7: **HOOK 슬라이드 중앙 = 대표 인물 실제 사진 폴라로이드 (필수)** — 모든 HOOK은 중앙 (`middle_center`) 에 대표 인물 (CEO 또는 토픽 representative)의 **실제 사진**을 폴라로이드 프레임(두꺼운 흰 테두리, 빨간 푸시핀 1개)으로 배치. 인물은 photoreal — 실제 그 인물의 얼굴이어야 함. 일러스트·3D Memoji·랜덤 AI 생성 인물 금지. 폴라로이드 하단 흰 테두리에 손글씨 sepia로 한 줄 메타데이터 (예: `Market Cap — $330B`). 폴라로이드 우상단 모서리에 종가 도장 겹치게.
32. 🆕 v4.7: **마스코트는 슬라이드 2부터 등장** — HOOK은 마스코트 금지. S2부터 CTA까지 분배. CTA에는 마스코트 필수.
33. 🆕 v4.7.1 (**v4.9.4에서 정정**): **마스코트 = 머리만 실사, 몸은 자유, 사방 4코너 중 하나에 작게** — 머리(얼굴 영역, 헤어/안경/표정 포함)는 무조건 대표 인물의 **실제 photoreal cut-out**. 몸은 Funko Pop·일러스트·단순 cartoon·막대 인형 어떤 스타일이든 OK. **얼굴은 절대 일러스트·3D Memoji·만화·랜덤 인물 금지.** 위치는 **4코너 중 하나** (`top-left` / `top-right` / `bottom-left` / `bottom-right`). 중앙 배치 금지. 사이즈는 슬라이드 높이의 **12-15%**, 슬라이드 메인 요소의 30% 이하. 마스코트는 절대 중앙 주인공이 되지 않음. negative_prompt에 다음 문구 명시 강제: `"no 3D Memoji, no chibi cartoon, no illustrated face — the mascot's head must be a real photograph of [topic_mascot_identity]'s face. mascot is always small (12-15% slide height) and in one of the four corners, never center."`.

> ⚠️ **v4.1 + v4.2 적용 시점**: 다음 신규 포스트부터. 진행 중인 `Google` 포스트는 v4.0 워크플로우 그대로 유지.
> ⚠️ **v4.3 적용 시점**: `사용중/ig_skill/SETUP_GUIDE.md` 셋업 완료 후 즉시.
> ⚠️ **v4.6 적용 시점**: NVDA 포스트부터 즉시. Phase 3.5 (스크립트 승인) 미통과 시 Phase 4 진입 금지.
> ⚠️ **v4.7 적용 시점**: PLTR 포스트(2026-05-11)부터 즉시. HOOK 마스코트 등장 절대 금지, 중앙 대표 인물 실사 폴라로이드 강제.

---

## 🆕 v4.9.5 룰 — 로컬 meme 폴더 활용 (NEW, 강제)

**경로**: `/Users/dohyun/Desktop/개인 인스타/broisinvesting/broisinvesting.md/meme/`
**현재 자산** (13개): distracted_boyfriend / 0x0 / Willem_Dafoe_Looking_Up / 7ptqxy / images / interesting_man / stock-market-meme-elon-musk / ToTheMoonStockMarketMeme01 / 기타 webp·jpg.

### 강제 룰
1. `meme_inclusion = true` 슬라이드는 **반드시** 위 폴더에서 1개 자산 선택해 사용.
2. JSON에 `meme_source_file_reference` 필드 명시 (절대 경로) — 작업 추적용.
3. `visual_elements`의 해당 자산 `source_image_url` 에 동일 경로.
4. `gemini_prompt` 안 meme description은 그 밈의 **시각 패턴을 자연어로 묘사** (Gemini가 실제 파일을 fetch하지 못하므로). 예: distracted_boyfriend → "a young man in a checkered shirt walking with a young woman but turning his head to look at another woman in a red dress".
5. 밈 위에 라벨을 붙여 슬라이드 메시지에 맞게 narrative 입힘. 예: distracted boyfriend의 세 인물 위에 각각 'PALANTIR' / 'GOVERNMENT' / 'COMPANIES' 라벨.

### 슬라이드별 추천 매핑 가이드
- **수익 분리·전환** (예: 회사 → 신규 시장 끌림) → `distracted_boyfriend`
- **상승·폭발 성장** → `ToTheMoonStockMarketMeme01`
- **놀라움·충격** → `Willem_Dafoe_Looking_Up`
- **분석·자신감** → `interesting_man`
- **밈 자체로 시장 풍자** → `stock-market-meme-elon-musk`

### 자가 검증
- [ ] `meme_inclusion: true`면 폴더 자산 1개 사용했는가?
- [ ] `meme_source_file_reference` 절대 경로 명시?
- [ ] 밈 위 라벨이 슬라이드 메시지와 직접 연결?

---

## 🆕 v4.8 룰 (newmoney.blog 레퍼런스 흡수, 정체성 유지)

**적용 시점**: PLTR 포스트(2026-05-11)부터 즉시. 코르크보드 배경·페이지 카운터 금지·broisinvesting handle·Funko Pop 좌측 코너 마스코트·burnt sienna 팔레트·종가 도장은 **모두 유지** (정체성).

### A. 헤드라인 톤 강화 — 질문형 + 3-4줄 분할
- 헤드라인은 **질문형** 또는 **도발적 단언** 중 하나 (Title Case)
- 단어 수 6-10개, **3-4줄로 분할 렌더링** 권장 (큰 신문 serif 활용)
- 톤 예시: "Is This Airline Stock The Real AI Winner?" / "Can We Just Ignore The Effects Of The Iran War?" / "Allbirds Was All-Dead." / "The Company That Helped Catch Bin Laden."
- 모든 본문 슬라이드가 질문일 필요는 없음 — 도발적 단언도 OK. 단 톤은 호기심·텐션 유발.

### B. 노란 형광펜 하이라이트 — 키워드 1개 (NEW STYLE)
- 헤드라인 안 **가장 임팩트 큰 키워드 1개에만** 노란 형광펜 하이라이트 (highlighter marker effect, 부드러운 노란~머스타드 색)
- 빨간 밑줄과 **함께 쓰지 않음** — 슬라이드당 노란 하이라이트 OR 빨간 밑줄 중 **하나만** 선택
- 노란 하이라이트가 단일 키워드의 "충격" 강조 / 빨간 밑줄은 "결론/단정" 강조 — 슬라이드 역할에 맞춰 선택
- 노란 색감: 머스타드 노랑 (#F4D03F 같은 영역), 형광펜 박스 형태 (살짝 비뚤어진 직사각형, 손으로 그은 듯)

### D. 콜라주 시각 밀도 — 본문에도 매거진 콜라주
- 본문 슬라이드 중앙은 단일 폴라로이드 단독 ❌ → **콜라주 구성** ✅
- 콜라주 요소: ① 인물/제품 cutout(가슴샷, 폴라로이드 프레임 없는 단순 종이결 cutout) ② 파스텔 라벨 스티커 (살구·민트·연파랑·노랑) ③ sparkline 미니 차트 ④ 작은 손글씨 메모 ⑤ 작은 화살표·강조 표시
- 콜라주 = 3-5개 요소가 살짝 겹치며 코르크보드 위에 자연스럽게 배치
- HOOK은 v4.7 룰(중앙 폴라로이드 + 핀카드 3) 그대로 유지 — 콜라주는 본문 슬라이드에 우선 적용

### F. sparkline 미니 차트 분산 배치
- 본문 슬라이드 중 **데이터 관련 슬라이드 1-2개에 sparkline 미니 차트** 1-2개 삽입 (작게, 라벨 옆에 직접)
- sparkline = 작은 라인 차트 또는 미니 막대그래프 (빨강↓·녹색↑), 카드/라벨 안에 직접 배치
- 모든 sparkline은 burnt sienna 빨강(부정) 또는 무던한 녹색(긍정)으로 — 네온 색 금지
- 메인 큰 차트(S6 chart_annotated, S7 dual_panel)는 별도 유지. sparkline은 보조적 시각 보강.

### 유지하는 정체성 (변경 ❌)
- 배경: Kraft-brown 코르크보드 (그리드 페이퍼 ❌)
- 페이지 카운터: 영구 금지 (우상단 X/N 표시 ❌, binder clip ❌)
- broisinvesting 핸들: HOOK 상단 중앙만
- 마스코트: Funko Pop 머리 실사 / 좌측 코너만 / 12-18% 작게 (v4.7.1)
- 팔레트: Kraft brown + burnt sienna red + sepia + 노란 하이라이트 (v4.8 신규)
- 종가 도장: 회사 토픽 HOOK 필수
- Citation Zero (v4.6.2), Angle Zero (v4.7) 그대로

---

## 🆕 v4.9 룰 — 텍스트 절제 + 약자 절대 금지 + 폴라로이드 콜라주 (NVDA 레퍼런스 흡수)

**적용 시점**: PLTR 포스트 즉시. 모든 후속 포스트에 영구 적용.

### v4.9.A — 텍스트 절제 룰 (NEW, 최우선)
- **슬라이드 1장 = 1 메시지** 강제
- **헤드라인**: 1-2줄, **3-6단어**까지 (4줄 분할 ❌). 짧을수록 강함
- **서브헤드라인**: 옵션, 1줄, 8-12단어 이내
- **본문 텍스트 총량**: 슬라이드당 **40단어 이하** (caption + label + 결론 1줄 합산)
- **bullet list 4개 이상 ❌** — 폴라로이드 카드 또는 라벨 스티커 콜라주로 분산
- **하단 결론 1줄**: 직설적 평문, 핵심 요약 (예: "5 years ago they made $5B per quarter. Now $68B. That's 13× bigger.")
- **숫자가 텍스트보다 큼** — 큰 숫자(`$6.8B`, `+85%`, `13×` 등)가 슬라이드의 주요 시각 요소. 본문 텍스트는 보조.

### v4.9.B — 약자 절대 금지 + 초보자 친화 직설 영어 (v4.6 룰 16 강화, v4.9.1에서 재강조)

**핵심 미션**: broisinvesting의 시청자 = **18-30세 비전공 개인 투자자**. 모든 슬라이드 텍스트는 다음을 만족해야 한다:
1. **약자 0%** — 슬라이드 시각 텍스트에 약자 렌더링 절대 금지
2. **친구한테 카톡 보내듯** 친근하고 직설적인 영어
3. **한 번 읽고 즉시 이해 가능** — 두 번 읽어야 이해되면 실패
4. **추상 단어 ❌** — "ecosystem", "synergy", "multi-tenant", "vertical integration" 같은 비즈니스 jargon 금지
5. **구체적이고 짧은 평이한 동사** 사용 — "powers", "runs", "hunts", "cleans", "sells", "finds", "tracks"

- **약자 자체를 슬라이드 텍스트로 렌더링 금지**. PhD, JD, CIA, ICE, NHS, CDC, NFP, CPI, FOMC, FY, YoY, capex, EBITDA, EV, P/E, P/S, GAAP, FCF, AIP, LLM 등 **모든 약자 ❌**.
- **풀어쓰기 강제** — 친구한테 카톡 보내듯 평이한 풀네임 사용:
  - PhD → "doctorate" 또는 그냥 빼고 "studied philosophy"
  - JD → "law degree"
  - CIA → "the U.S. spy agency"
  - NHS → "UK health service"
  - CDC → "US disease agency"
  - P/S → "price vs sales"
  - P/E → "price vs profit"
  - GAAP → 그냥 "real profit"
  - FCF → "cash in hand"
  - AIP → "Palantir's AI platform"
- **acronym_glosses 필드 (v4.0) 폐기** — 더 이상 약자 풀이 footnote 사용 안 함. 약자 자체를 안 쓰면 풀이도 필요 없음.
- 초보자(18-30세, 비전공자)가 한 번 읽고 이해 가능한 평이한 영어만.

### v4.9.C — 폴라로이드 카드 콜라주 (NVDA 레퍼런스 패턴)
- 본문 콜라주(v4.8.D)의 핵심 요소: **폴라로이드 스타일 카드 4-6개**를 코르크보드에 빨간 푸시핀으로 꽂은 구성
- 각 폴라로이드 카드 안: 로고 / 인물 사진 / 큰 숫자 중 하나 (대형 시각 요소)
- 폴라로이드 카드 하단 흰 테두리: 손글씨 sepia 캡션 (예: `NVIDIA · $5.23T`, `MICROSOFT · $190B`)
- 카드들은 살짝씩 다른 방향 기울임 (자연어로만 — 각도 zero rule 준수)
- 파스텔 라벨 스티커(v4.8 collage)와 혼용 가능 — 단 폴라로이드 카드가 우선 패턴

### v4.9.D — ACT 라벨 ❌ **폐기** (v4.9.1)
- 본문 슬라이드 좌상단의 ACT 라벨(`ACT 1 · THE PERSON` 형식) **사용 금지**.
- 사용자 결정: 시청자 인지 부담 ↑, 시각 노이즈 ↑, 헤드라인만으로 충분.
- 모든 슬라이드 좌상단 ACT 라벨 자리는 비워두거나 다른 시각 요소(여백·작은 장식)로 대체.
- 기존 슬라이드에 ACT 라벨 있으면 제거.

### v4.9.E — 마스코트 = 실제 사진 머리·손 + 카툰 몸 콜라주 (NVDA 레퍼런스 완전 매칭, 절대 위반 금지)

**디자인 = "사진 콜라주" 패러다임** (NVDA 1.png 좌하단 Jensen Huang 패턴 그대로):

1. **머리(얼굴 영역) + 보이는 손**: 무조건 **실제 인물의 photograph를 잘라낸 cut-out**. 신문/뉴스/Wikipedia에서 잘라 붙인 사진 콜라주 느낌.
   - 정확한 비유: "Photoshop으로 진짜 사진의 얼굴·손을 잘라내서 만화 몸에 풀로 붙인 콜라주"
   - 또는: "Funko Pop figure인데 머리·손이 조각된 게 아니라 진짜 사진으로 교체된 형태"
2. **몸(torso, legs, clothing)**: 단순 카툰 일러스트 — flat color silhouette, simple shapes, Funko Pop 카툰 스타일. **얼굴은 절대 일러스트화하지 않음**.
3. **비율**: 머리가 figure 전체의 약 45-55% (Funko Pop oversized head)
4. **크기**: 슬라이드 높이의 12-18%, 좌측 코너만 (top-left 또는 bottom-left)
5. **장식 OK**: 머리 주변 만화 동작 라인·작은 빨간 `!`·노란 효과 라인 등 만화적 디테일 (단 얼굴 자체는 photoreal)

**모든 마스코트 등장 슬라이드의 `gemini_prompt`에 다음 표현 명시 강제** (정확히 이 비유로):
```
"The mascot is a photo-collage character — IMAGINE PRINTING OUT A REAL PHOTOGRAPH of [topic_mascot_identity]'s actual face and gluing it onto a small cartoon body. The HEAD and any visible HANDS are real photograph cut-outs (the kind you'd find in a Wikipedia article, news photo, or official portrait — sharp, photoreal, recognizable). The BODY (torso, legs, clothing) is a simple flat-color cartoon illustration in Funko Pop proportions (tiny torso, short legs). The head is oversized — about half the total figure height. The face is NOT illustrated, NOT painted, NOT drawn, NOT 3D rendered, NOT a Memoji, NOT chibi, NOT anime — it is a literal real photograph cut-out. Like a cardboard puppet where someone glued a real face photo onto a cartoon body."
```

**negative_prompt에도 강화 문구 명시**:
```
"the mascot's face must NEVER be illustrated, painted, drawn, sketched, AI-generated, 3D-rendered, Memoji, chibi, anime, or cartoon. The face is ALWAYS a literal real photograph cut-out — like printing a news photo and gluing it onto a cartoon body. If you cannot match the real person's actual face, do not invent a replacement."
```

---

## 🔄 실행 플로우

```
Phase 0: 주제 인테이크
  ↓
Phase 1: Research 병렬 (Agents 1-4 동시 실행)
  ↓
Phase 2: Validation (Agent 5, Reflection 2R)
  ↓
🛑 HITL CP1 (리서치 승인)
  ↓
Phase 3: Narrative Arc 설계 + buffett_inclusion 분배 + connector 분배 + Agent 12 사전 준비
  ↓
🛑 HITL CP2 (아크 + CTA 리포트 개요 승인)
  ↓
🆕 Phase 3.5: 9장 전체 스크립트 평문 작성 (헤드라인·본문·메시지·기승전결·연결고리 검증표)
  ↓
🛑 HITL CP2.5 (스크립트 승인) — 미통과 시 Phase 4 진입 금지
  ↓
Phase 4: 슬라이드별 생성 루프
  ├── 슬라이드 1 (HOOK) → Agents 6→7→8→9→10→11 순차
  │    └─ 배치 출력: [HOOK 단독 묶음]
  │    └─ HITL CP3a
  ├── 슬라이드 2-3 → 동일 파이프라인
  │    └─ 배치 출력: [본문 2장 묶음]
  │    └─ HITL CP3b
  ├── 슬라이드 4-5 → 동일
  │    └─ 배치 출력: [본문 2장 묶음]
  │    └─ HITL CP3c
  ├── ... (홀수면 마지막 본문 1장 단독 묶음)
  └── 슬라이드 N (CTA) → Agents 6→7→8→9→10→11 + Agent 12 (PDF)
       └─ 배치 출력: [CTA + PDF 묶음]
       └─ HITL CP3-final
  ↓
Phase 5: 최종 통합
  ↓
🛑 HITL CP4 (최종 승인)
  ↓
[사용자가 이미지 N장 토픽 폴더에 저장]
  ↓
[사용자: "포스팅 시작 {topic_slug}"]
  ↓
Phase 6: 인스타 발행 (v4.3)
  ├── Agent 14 (Caption Writer) → slide_*.json 읽고 영어 캡션 + 해시태그 5개 생성
  ├── 🛑 HITL CP5 (캡션 미리보기 → yes/수정/취소)
  ├── post_workflow.py → Cloudinary 업로드 + Graph API publish_carousel
  └── post_log.json 저장
```

---

## 🆕 v4.0 배치 페이싱 규칙 (핵심)

이미지 프롬프트 JSON 파일을 사용자에게 **2장씩 묶어서** 전달. 구조:

| 묶음 번호 | 포함 슬라이드 | 크기 | HITL CP |
|-----------|---------------|------|---------|
| 배치 1 | HOOK (커버 1장) | 1 | CP3a |
| 배치 2 | 본문 S2, S3 | 2 | CP3b |
| 배치 3 | 본문 S4, S5 | 2 | CP3c |
| 배치 4 | 본문 S6, S7 | 2 | CP3d |
| ... | ... | ... | ... |
| 마지막-1 (홀수일 때) | 본문 마지막 1장 | 1 | CP3z |
| 마지막 | CTA (1장) + **CTA PDF 리포트** | 1+1 | CP3-final |

### 예시 1: 8장 포스트 (standard_8)
- S1: HOOK → 배치 1 (단독)
- S2+S3: 배치 2
- S4+S5: 배치 3
- S6+S7: 배치 4
- S8: CTA + PDF → 배치 5 (마지막)
- **총 5개 배치**

### 예시 2: 9장 포스트 (macro_event_9)
- S1: HOOK → 배치 1
- S2+S3: 배치 2
- S4+S5: 배치 3
- S6+S7: 배치 4
- S8: 본문 홀수 잔여 → 배치 5 (단독)
- S9: CTA + PDF → 배치 6
- **총 6개 배치**

### 배치 출력 형식 (사용자에게 보여지는 포맷)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 배치 {X}/{N} — {유형} 묶음
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

슬라이드 {a}, {b} 동시 생성 완료.

📄 slide_{a}.json preview: ...
📄 slide_{b}.json preview: ...

[CTA 묶음이면 추가]
📄 cta_report.pdf preview: ...

👉 다음?
   ✅ OK → 배치 {X+1}
   ✏️ 수정: [슬라이드 번호] [에이전트 번호] [피드백]
   🔄 재생성 [슬라이드 번호]
```

---

## 🆕 v4.0 데이터 최신성 게이트

Phase 1 시작 시, Orchestrator가 리서치 에이전트들에게 **명시적으로** 다음 규칙을 전달:

```
[MANDATORY_DATA_FRESHNESS_RULE_v4.0]
- 수치 데이터 (주가, 지수, ETF가격, 유가, 금리, 환율 등): T-1 영업일 종가 강제
- 경제 지표 (CPI, NFP, 실업률, GDP, PCE 등): 최근 발표분 (날짜 명시 필수)
- 뉴스·정책·분석·해설: 공신력 소스면 기간 제한 없음, 단 현재 시장 상황 반영 필수
- T-1 규정 영업일 계산:
    * 평일 제작 → 전일 종가 (예: 화요일 제작 → 월요일 종가)
    * 월요일 제작 → 금요일 종가
    * 공휴일 → 직전 영업일
    * 시차 기준: 미국 NYSE/NASDAQ 종가 기준 (4:00 PM ET)
```

Agent 5 (Validator)가 검증 시 이 규칙을 체크리스트로 사용.

---

## 🆕 v4.0 약자 풀이 레지스트리 (Acronym Registry)

Orchestrator가 포스트 전체에 걸쳐 약자 풀이 상태를 관리:

```json
{
  "post_id": "private_credit_bubble_20260421",
  "acronym_registry": {
    "FOMC": {"first_appeared_slide": 3, "glossed_on_slide": 3},
    "PCE": {"first_appeared_slide": 5, "glossed_on_slide": 5},
    "NFP": {"first_appeared_slide": 5, "glossed_on_slide": null, "reason": "too_common"}
  }
}
```

- Agent 7 (Title), Agent 6 (Body)가 각 슬라이드에서 약자 사용 시 Orchestrator에 보고
- Orchestrator가 레지스트리 조회 → 이미 풀이한 약자면 **다시 풀이하지 않음**
- Agent 10 (Layout)에 "이 슬라이드에서 풀이해야 할 약자 목록" 전달

---

## 🛑 HITL 체크포인트 관리

| CP | 시점 | 사용자 결정 |
|----|------|-------------|
| CP1 | Layer 2 (Validation) 직후 | 리서치 품질 승인 / 재검색 요청 |
| CP2 | Narrative Arc 확정 직후 + CTA PDF 개요 | 아크 구성 승인 / 변경 / PDF 방향 조정 |
| 🆕 CP2.5 (v4.6) | Phase 3.5 — 9장 평문 스크립트 작성 직후 | **스크립트 텍스트 승인 / 특정 슬라이드 수정 / 톤·각도 변경** — 미통과 시 Phase 4 절대 진입 금지 |
| CP3a~z | 각 **배치** 완료 직후 | 배치 승인 / 특정 슬라이드 수정 / 재생성 |
| 🆕 CP3a (HOOK 강화 v4.6) | HOOK 배치 완료 직후 | 위 항목 + ① **토픽 관련 이미지 3-5개** 카운트·관련성 확인 ② **헤드라인·subtitle·broisinvesting 핸들 외 추가 텍스트가 있으면 명시 승인 필요** (default = 거부 → 텍스트 제거) |
| CP4 | 전체 완료 | 최종 승인 / 부분 수정 |
| 🆕 CP5 | Phase 6 캡션 생성 직후 (v4.3) | 캡션 승인 / 수정 지시 / 취소 — `--auto` 플래그 시 스킵 가능 |

**절대 원칙**: 모든 CP에서 **사용자 응답 전까지 대기**. 시간 절약 목적의 HITL 스킵 불가.

---

## 📤 입력 / 출력

### 입력
```json
{
  "user_topic": "string (ko or en)",
  "output_preferences": {
    "slide_count_preference": "8 | 9 | 6 | auto",
    "tone_intensity": "mild | standard | aggressive",
    "cta_reward_type": "1page_pdf_report (default v4.0)"
  }
}
```

### 출력
```json
{
  "batches": [
    {"batch_id": 1, "type": "cover", "slide_jsons": ["slide_01.json"]},
    {"batch_id": 2, "type": "body_pair", "slide_jsons": ["slide_02.json", "slide_03.json"]},
    "..."
  ],
  "cta_report_pdf_path": "cta_report.pdf",
  "acronym_registry": "...",
  "final_manifest": {
    "total_slides": "int",
    "total_batches": "int",
    "generation_timestamp": "ISO8601",
    "data_freshness_report": "object"
  }
}
```

---

## ⚠️ 절대 금지사항

1. HITL 스킵 — 어떤 이유로도 사용자 응답 전에 다음 Phase로 진행 금지
2. 2장 묶음 규칙 위반 — 3장 이상을 한 번에 전달 금지
3. 커버를 본문 배치에 포함 금지 (커버는 항상 단독)
4. CTA 슬라이드만 내보내고 PDF 리포트 없이 종료 금지
5. T-1 규칙 위반한 수치를 Validator 승인 없이 통과시키기 금지
6. 영어 이외 언어로 슬라이드 콘텐츠 생성 금지 (Orchestrator 자체 보고는 한국어 OK)
7. 🆕 v4.0/v4.5: 마스코트 `topic_mascot_inclusion = true` 슬라이드 50% 초과 분배 금지 (목표 ~40%, 허용 30-50%)
8. 🆕 v4.7 (**v4.0/v4.5 룰 대체**): **HOOK 슬라이드에 마스코트 절대 등장 금지** — `topic_mascot_inclusion = false` 강제. HOOK 슬라이드는 대표 인물(CEO 또는 토픽 representative)의 **실제 사진**(`character_cutout` 타입, photoreal polaroid)을 중앙에 `sole_focal_subject`로 배치하고 그 주변에 관련 핀 카드 3개(로고 + 플래그십 상품 + 컨텍스트 이미지)를 배치. 마스코트는 **슬라이드 2부터** 등장. CTA(마지막 슬라이드)에는 마스코트 필수 등장.
8a. 🆕 v4.7.1 (**newmoney.blog 레퍼런스 반영, v4.7 룰 강화**): **마스코트 = 머리(얼굴) 실제 + 몸 자유** — 머리(얼굴 영역, 헤어 + 안경 + 표정 포함)는 무조건 대표 인물의 **실제 photoreal cut-out** (real photograph of the person's face). 몸은 자유 — Funko Pop 만화 몸, 일러스트 몸, 단순 cartoon body, 막대 인형 같은 단순 형태도 모두 OK. **단 머리만은 실사**. 일러스트레이션·3D Memoji·만화 얼굴·랜덤 AI 생성 얼굴 절대 금지. 얼굴은 항상 HOOK 슬라이드 중앙 폴라로이드와 동일 인물의 동일한 얼굴.
8a-1. 🆕 v4.7.1 (**v4.9.4에서 정정**): **마스코트 위치 = 사방 4코너 중 하나 (small corner)** — 마스코트는 슬라이드의 네 코너 중 하나에 배치: `top-left` / `top-right` / `bottom-left` / `bottom-right`. **중앙 배치는 절대 금지** (마스코트는 중앙 주인공이 되지 않음). 사이즈는 **작게** — 슬라이드 높이의 **12-15%** (이전 12-18%에서 축소). `central_protagonist_full` 케이스 폐기. 슬라이드 메인 주제(인물 사진·차트·리스트)가 중앙에 자리하고 마스코트는 코너 리액션 캐릭터로만 등장. 슬라이드별로 위치를 다양화해 시각 변화 ↑.
8b. 🆕 v4.5: **토픽 마스코트 미결정** 상태에서 Phase 3 narrative arc 진행 금지
8c. 🆕 v4.5: **버핏을 디폴트 마스코트로 자동 분배** 금지 (가치투자/Berkshire 토픽이 아니면 다른 인물)
9. 🆕 v4.0: 비-HOOK 슬라이드에 `narrative_connector_category` 미지정 금지
10. 🆕 v4.1 (다음 포스트부터): topic_slug 폴더 미생성 상태에서 Phase 4 진행 금지
11. 🆕 v4.1 (다음 포스트부터): Phase 4 루프에서 Agent 13 호출 누락 금지
12. 🆕 v4.3: 이미지 생성 후 `slide_*.json` 삭제 금지 (Phase 6 입력으로 사용됨)
13. 🆕 v4.3: Phase 6 에서 사용자 yes 응답 없이 인스타 발행 금지 (`--auto` 플래그 없는 한)
14. 🆕 v4.3: Phase 6 캡션 생성 시 슬라이드 PNG 분석 금지 (JSON 만 사용 — 토큰 절약)
15. 🆕 v4.6: **Phase 3.5 스크립트 미작성 또는 CP2.5 미승인 상태로 Phase 4 (슬라이드 JSON·이미지 제작) 진입 절대 금지**. 슬라이드를 만들기 전에 9장 전체 평문 스크립트가 사용자 승인을 받아야 함.
16. 🆕 v4.6: 스크립트에 약어·전문용어 사용 금지 (PE, EPS, YoY, FY, capex, multiple, beat, guidance 등 → 풀어쓰기 강제). 18-30세 비전공자가 한 번에 이해 가능한 영어만.
17. 🆕 v4.6: 스크립트에서 cliffhanger 구조 강제 — 매 슬라이드 마지막은 다음 슬라이드를 안 보면 답이 없는 호기심 유발 문구로 끝나야 함.
18. 🆕 v4.6: 페이지 카운터 (X/9 둥근 사각형) 우상단 배치 영구 금지. broisinvesting 워터마크 커버에서도 금지 — 대신 회사·토픽 로고를 좌상단 핀 카드로.
19. 🆕 v4.6: 회사 토픽 커버에 최근 종가 + 종가 날짜 도장 필수 (예: `MAY 8 CLOSE / $214.94`).
20. 🆕 v4.6.1: 커버 상단 중앙에 `broisinvesting` 핸들 누락 금지 (모든 커버에 디폴트로 등장).
21. 🆕 v4.6.1: 커버에 토픽 관련 이미지 3개 (로고 + 상품 + 컨텍스트) 누락 금지. 정확히 3개, 동일 사이즈, 핀 카드 형태.
22. 🆕 v4.6.1: 커버 상단 중앙에 'WORLD'S #1 STOCK', 'COMPANY · DATE' 같은 small caps eyebrow 라벨 사용 금지 (broisinvesting 핸들로 대체됨).
23. 🆕 v4.6.2 + 🆕 v4.9.2 **강화**: **인용 태그·각주 마커 렌더링 절대 금지 (CITATION ZERO RULE — STRENGTHENED)**

   슬라이드 이미지 안에 시각 텍스트로 등장 절대 금지인 패턴 (망라):
   - `[cite:1]`, `[cite:2]`, `[cite_start]`, `[cite_end]`, `[cite]`, `[CITE]`
   - `[1]`, `[2]`, `[3]`, ... (대괄호 안 숫자만 있는 것 전부)
   - `[^1]`, `[^2]` (footnote 마커)
   - `(cite:X)`, `(citation)`, `(ref:X)`, `(source)`
   - `(1)`, `(2)`, `(3)` (괄호 안 숫자만 있는 것)
   - `^1`, `^2` (superscript footnote)
   - `cite 1`, `ref 1`, `citation 1`
   - `Source:`, `Ref:`, `Citation:` 으로 시작하는 줄
   - URL이 시각 텍스트로 나타나는 것
   - 어떤 형태의 footnote 숫자도

   **3중 강제 메커니즘** (모든 슬라이드 의무):
   1. **`negative_prompt`에 위 패턴 enumerate 명시 강제**
   2. **`gemini_prompt` 시작 부분에도 명시 강제** ("This image must contain ZERO citation markers, footnote numbers, bracketed digits, or 'cite' tags of any kind anywhere in the rendered text")
   3. **`gemini_prompt` 끝 부분에도 한 번 더 명시** (LLM이 prompt 시작과 끝 모두 가중치 높게 보므로 양쪽에 명시)

   인용 정보는 JSON `research_provenance`에만 보관. **절대로 prompt 안 본문에 `[cite:1]` 같은 표기 사용 금지** — Gemini는 prompt 안 텍스트를 그대로 이미지에 옮길 가능성 있으므로 prompt 자체에 cite 패턴 등장 금지.

   **자가 검증**: prompt 작성 후 `grep -i "cite\|\[1\]\|\[^\|ref:"` 로 검사. 발견되면 제거.
24a. 🆕 v4.9.3: **색깔 이름 렌더링 절대 금지 (COLOR NAME ZERO RULE)** — Gemini가 스티커·박스·라벨의 색깔 설명(예: `apricot peach`, `mint green`, `mustard yellow`, `powder blue`, `peach`, `green`, `yellow`)을 그 요소 안 또는 위에 시각 텍스트로 그대로 렌더링하는 사고가 빈번. **모든 슬라이드 `negative_prompt`에 색깔 이름 금지 명시 강제**: `"do not render color names (no 'apricot', no 'mint', no 'mustard', no 'peach', no 'green', no 'yellow', no 'blue') as visible text on or above any sticker — color is purely a visual property, never a printed label"`. **gemini_prompt 안 색깔 표현 가이드**: 색깔은 디자인 가이드로만 자연어 묘사 (예: "warm peach tone", "soft mint tone"), 절대 따옴표 안에 색깔 이름을 넣지 않음. 각 sticker description에 명시: `"ONLY two pieces of text appear inside: [title] and [caption]. Do NOT print the color name."`.

24. 🆕 v4.7 (**v4.9.4에서 명확화**): **각도·회전값 시각 텍스트 렌더링 금지 (ANGLE/ROTATION ZERO RULE — IMAGE-ONLY)** — 각도 표시 금지의 **범위는 "렌더링된 슬라이드 이미지 안 시각 텍스트"만**. JSON 메타데이터(`element_rotations`, `rotation_deg: -4` 같은 필드)는 자유롭게 보관 OK. 금지는 다음 두 가지로 한정: (1) **이미지에 시각 텍스트로 각도값이 나타나는 것** (`-4°`, `+3°`, `tilt: -4`, `rotation: -7`, `angle: 3°`, `deg`, °기호 등이 렌더링된 슬라이드 안에 글자로 보이는 것), (2) **gemini_prompt 안 텍스트가 각도 수치를 포함해서 Gemini가 그것을 시각 텍스트로 옮기는 것**. 회전·기울기는 시각적으로 *보여야* 하지만 인쇄된 각도 라벨을 가지면 안 됨. 모든 슬라이드의 `negative_prompt`에 명시 강제: `"no degree symbols, no numeric tilt values, no angle labels, no rotation text rendered as visible text on the image — tilts are visual only"`. `gemini_prompt` 안 각도 표현은 자연어로만 — `"tilted -4 degrees"` ❌ → `"tilted slightly counter-clockwise"` ✅. JSON 데이터 필드는 그대로 수치 사용 OK.
