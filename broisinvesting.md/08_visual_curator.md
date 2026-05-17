# 🎭 Agent 8 — Visual Asset Curator

> **역할**: 시각 자료(인물 컷아웃·밈·로고·아이콘) 선정 + **🆕 v4.5 토픽 마스코트 시스템 (주제 관련 핵심 인물)**

---

## 📌 기본 정보

| 항목 | 값 |
|------|-----|
| Agent ID | `agent_8_visual_curator` |
| Layer | Layer 3 — Content |
| Reflection 라운드 | 1라운드 |
| 🆕 v4.0 변경 | **마스코트 = 주인공 인물의 30% 크기 (코너 배치 시)** |
| 🆕 v4.5 변경 | **버핏 단일 마스코트 폐기 → 토픽 마스코트 시스템.** 주제 관련 대표 인물(CEO/리더)이 그 포스트의 마스코트. 예: NVDA → Jensen Huang, Apple → Tim Cook, Samsung → 이재용. 빈도 룰(~40%, HOOK+CTA 필수)은 동일. |

---

## 🎯 주요 책무 (v4.5)

1. 슬라이드 본문·역할에 맞는 시각 자료 5-8개 큐레이션 (단, **HOOK 슬라이드는 토픽 관련 이미지 최소 3개·최대 5개** — 아래 v4.6 룰 참조)
2. 🆕 v4.5: **토픽 마스코트 결정** — 주제 관련 대표 인물(CEO/리더) 1명 선정, 그 포스트 전체에서 마스코트 역할
3. 토픽 마스코트 포즈 선정 (**전체 포스트의 ~40% 슬라이드에만**, 선택적 등장)
4. 기타 실제 인물 컷아웃 선정 (마스코트 외 등장 인물 — 정치인·다른 CEO)
5. 밈 UI 요소 (pixel_error_dialog 등 — ⚠️ v4.1부터 meme 큐레이션은 **Agent 13에 위임**)
6. 회사 로고 뱃지
7. 영화 스틸 (1-2개/포스트)
8. 🆕 v4.0: 마스코트 크기 **주인공 30%** (코너 배치 시)
9. 🆕 v4.0: 마스코트가 **중앙 주인공**일 때는 크기 유지
10. 🆕 v4.0: 마스코트 **등장 빈도 ~40% 규칙** (Orchestrator의 `topic_mascot_inclusion` 플래그 기반)
11. 🆕 v4.1: Agent 13의 `selected_meme` 객체를 받아 `visual_assets` 배열에 통합

> ⚠️ **v4.5 적용 시점**: 다음 신규 포스트(NVDA부터)부터 즉시. 기존 발행 포스트(Google, UNH 등)는 v4.0/v4.4 유지.

---

## 🆕 v4.6 HOOK 슬라이드 이미지 개수 룰 (NEW — 강제)

### 🆕 v4.7 HOOK 중앙 구성 강제 (NEW — 최우선)

HOOK 슬라이드는 다음 구성을 **반드시** 따른다:

1. **중앙 (middle_center)** = 대표 인물(CEO 또는 토픽 representative)의 **실제 사진** 폴라로이드 (`character_cutout`, photoreal, 두꺼운 흰 폴라로이드 테두리 + 빨간 푸시핀 1개). 이 인물이 sole_focal_subject. 인물은 photoreal — 실제 그 인물의 얼굴이어야 하며 일러스트·3D Memoji 금지.
2. **폴라로이드 우상단** = 종가 도장 (회사 토픽 시): `MAY 8 CLOSE / $XXX.XX`
3. **폴라로이드 하단 흰 테두리** = 손글씨 sepia 한 줄 메타데이터 (예: `Market Cap — $330B`)
4. **주변 (top-left / top-right / middle-right)** = 토픽 관련 핀카드 3개 (v4.6.1 룰: 로고 + 플래그십 상품 + 컨텍스트 이미지)
5. **마스코트 등장 금지** (v4.7 룰 8) — Funko Pop 마스코트는 HOOK에 절대 추가 금지. 마스코트는 S2부터.
6. **상단 중앙** = `broisinvesting` 핸들
7. **하단 중앙** = 헤드라인 (오버사이즈 신문 serif)

### 규칙
HOOK (S1) 슬라이드는 **토픽·주제와 직접 관련된 이미지를 최소 4개, 최대 5개** 포함해야 함. (v4.7: 중앙 폴라로이드 1 + 핀카드 3 = 4개 최소)

### 카운트 대상 (이미지로 인정되는 자산 타입)
- `topic_mascot` (마스코트 인물 컷아웃)
- `character_cutout` (기타 인물)
- `logo_badge` (회사 로고)
- `icon` (제품·산업 상징 아이콘)
- `news_screenshot` / `newspaper_clipping_aesthetic` (뉴스 클리핑)
- `chart` / `chart_annotated` (관련 차트)
- `bloomberg_terminal_mock` / `stat_card` (데이터 비주얼)
- `movie_still` (관련 영화/문화 레퍼런스)

> **카운트 제외**: 배경 종이결, 마스킹 테이프/핀/스프링 같은 scrapbook props, 헤드라인 텍스트 자체.

### 토픽 관련성 기준 (강제)
모든 HOOK 이미지는 다음 중 하나에 직접 연결돼야 함:
1. **회사 정체성** — 로고, CEO/마스코트, 본사 사진
2. **제품·서비스** — 대표 제품 (예: NVDA → GPU, Apple → iPhone, Samsung → Galaxy/반도체)
3. **산업 맥락** — 그 회사가 속한 산업의 상징 (예: NVDA → 데이터센터·AI 칩, Samsung → 반도체 fab)
4. **포스트 핵심 데이터** — 헤드라인이 가리키는 차트/수치 비주얼

> ❌ 토픽과 무관한 일반 스톡 이미지·장식용 아이콘·관계없는 인물 금지.

### 예시 (v4.7 — PLTR 포스트 HOOK)
- ✅ Karp 중앙 폴라로이드 실사 (1) + Palantir 로고 핀카드 (2) + B-2 폭격기 실사 핀카드 (3) + Tomahawk 미사일 실사 핀카드 (4) → **4개 = OK (v4.7 권장)**
- ❌ Karp Funko Pop 마스코트 좌하단 추가 → **HOOK 마스코트 금지 (v4.7)**
- ❌ 중앙에 Karp 일러스트·3D Memoji → **photoreal 강제 (v4.7)**

### 구 예시 (v4.6 — NVIDIA 포스트, 더 이상 권장 아님)
- (v4.6) Jensen Huang 마스코트 + NVIDIA 로고 + GPU 아이콘 → 3개. v4.7부터는 중앙 Jensen **실사 폴라로이드**로 교체 + 마스코트 제거.

### 자가 검증
- [ ] HOOK 슬라이드 `visual_assets` 중 카운트 대상 ≥ 3 그리고 ≤ 5?
- [ ] 모든 이미지가 토픽 관련성 기준 1-4 중 하나에 매핑되는가?
- [ ] (마스코트 등장 룰과 충돌 없는가 — 마스코트는 카운트에 포함됨)

---

## 🆕 v4.5 토픽 마스코트 시스템 (NEW — 핵심)

### 1단계: 토픽 마스코트 결정

Phase 3 시작 시 Orchestrator가 토픽 분석 → **단 1명의 마스코트** 선정.

#### 토픽 → 마스코트 매핑 테이블

| 토픽 카테고리 | 토픽 마스코트 | 시그니처 외형 |
|---|---|---|
| **NVIDIA / NVDA** | Jensen Huang | 검정 가죽 자켓, 회색 머리, 안경 |
| **Apple / AAPL** | Tim Cook | 흰 머리, 회색 셔츠 또는 정장 |
| **Microsoft / MSFT** | Satya Nadella | 안경, 정장, 차분 |
| **Tesla / SpaceX / TSLA** | Elon Musk | 다양 (티셔츠/정장 변동), 갈색 머리 |
| **Meta / META** | Mark Zuckerberg | 회색 티셔츠, 곱슬머리 |
| **Google / GOOGL** | Sundar Pichai | 안경, 짧은 회색 머리, 차분 |
| **Amazon / AMZN** | Andy Jassy | 회색 머리, 정장 |
| **Samsung** | 이재용 (Lee Jae-yong) | 검정 정장, 안경 |
| **OpenAI / Anthropic / AI 일반** | Sam Altman / Dario Amodei | 캐주얼 |
| **Berkshire / 가치투자** | Warren Buffett | 회색 정장, 큰 안경 |
| **JPMorgan / 은행** | Jamie Dimon | 정장, 흰 머리 |
| **BlackRock / 자산운용** | Larry Fink | 안경, 정장 |
| **UnitedHealth / 헬스케어** | Andrew Witty (CEO) | 정장 |
| **Fed / 금리 / 매크로** | Jerome Powell | 흰 머리, 정장 |
| **Treasury / 재무** | 현직 재무장관 | 변동 |
| **US 정치 / 대선** | 현직 대통령 | 변동 |
| **OPEC / 원유** | 사우디 에너지장관 또는 OPEC 사무총장 | 변동 |
| **중국 / 위안화** | Xi Jinping | 검정 정장 |

> ⚠️ **버핏은 더 이상 디폴트 마스코트 아님.** 가치투자·Berkshire·장기관점 토픽일 때만 버핏 마스코트.

#### 매핑에 없는 토픽

매크로/거시 경제 일반 (인플레, 실업률 등) → **마스코트 없음** 가능. 또는 Powell/Yellen 등 정책 입안자.

### 2단계: 등장 빈도 규칙 (🆕 v4.7 — HOOK 마스코트 금지로 변경)

전체 포스트의 **~40% 슬라이드에만** 토픽 마스코트 등장 (8장 = 3-4장).

#### 🆕 v4.7 **금지 슬라이드**
- **HOOK (S1)** — 마스코트 절대 등장 금지 (`topic_mascot_inclusion = false` 강제). HOOK 중앙에는 대표 인물의 **실제 사진 폴라로이드**(`character_cutout`)가 sole_focal_subject로 배치되며, 마스코트(Funko Pop)는 별도로 추가 금지. 마스코트 정체성은 S2 첫 등장 시 정립.

#### 필수 등장 슬라이드
- **S2 (마스코트 정체성 정립 슬라이드)** — HOOK 중앙 폴라로이드 인물과 동일 인물의 Funko Pop 마스코트 첫 등장 (`mascot_corner_30pct` 또는 `central_protagonist_full`)
- **CTA (마지막)** — 권위 엔도스먼트 (`cta_podium_medium`)
- **본문 중 1-2개** — 감정 리액션 핵심 슬라이드

#### 제외 권장 슬라이드
- 차트·데이터가 주역인 슬라이드
- **다른 실제 인물(경쟁사 CEO, 정치인 등)이 중심인 슬라이드** — 마스코트가 그 인물에 압도되지 않게
- DEFINITION/THE_MACHINE 등 설명 위주 슬라이드

### 🆕 v4.7.1 마스코트 룰 (NEW — 강제, newmoney.blog 레퍼런스 기반)

**마스코트 구성**:
- **머리(얼굴 영역, 헤어 + 안경 + 표정 포함) = 무조건 대표 인물의 실제 photoreal cut-out** (real photograph)
- **몸 = 자유 스타일** — Funko Pop 만화 몸 / 일러스트 몸 / 단순 cartoon body / 막대 인형 / 무엇이든 OK
- **얼굴**은 HOOK 중앙 폴라로이드의 인물과 **동일 인물의 동일한 얼굴**

**마스코트 위치 (v4.9.4 정정)**:
- **4코너 중 하나에 배치** — `top-left` / `top-right` / `bottom-left` / `bottom-right` 모두 OK
- **중앙 배치만 ❌** (마스코트는 절대 중앙 주인공이 되지 않음)
- `central_protagonist_full` 케이스 **폐기**
- 슬라이드별로 코너 위치를 다양화해 시각 변화 ↑

**마스코트 사이즈 (v4.9.4 정정)**:
- **작게** — 슬라이드 높이의 **12-15%** (이전 12-18% → 더 축소)
- 슬라이드의 메인 시각 요소의 약 **30% 이하** 크기
- "small corner reaction character" 역할

**금지 사항**:
- ❌ 3D Memoji 얼굴
- ❌ chibi / anime / 카툰 일러스트 얼굴
- ❌ AI 생성된 닮지 않은 랜덤 얼굴
- ❌ 일러스트레이션·페인팅·스케치 얼굴
- ❌ **중앙 배치** (사방 코너는 모두 OK)
- ❌ 큰 사이즈 (슬라이드 높이 15% 초과)

**모든 마스코트 등장 슬라이드의 `negative_prompt`에 명시 강제**:
```
"no 3D Memoji, no chibi cartoon, no illustrated face — the mascot's head must be a real photograph of [topic_mascot_identity]'s face. mascot is always small (12-15% slide height) and in one of the four corners (top-left / top-right / bottom-left / bottom-right), never center."
```

### 3단계: 슬라이드별 의사결정 프로토콜

1. **Orchestrator가 Phase 3 시 토픽 마스코트 ID 결정**: `topic_mascot_identity = "Jensen Huang"` 등
2. **슬라이드별 `topic_mascot_inclusion: bool` 사전 지정**
3. Agent 8이 이 플래그를 받아 등장 여부 + 포즈 + 배치 결정
4. 등장하지 않는 슬라이드는 `mascot_role_classification = "not_present"` 출력

### 4단계: 빈도 자가 검증
- 8장 포스트: 3-4장 등장 (37.5%-50%)
- 9장 포스트: 3-4장 등장 (33%-44%)
- 50% 초과 → 자동 경고

### 토픽 마스코트와 narrative figure 충돌 시

토픽 마스코트가 그 슬라이드의 **중앙 주인공**일 때 (예: S4에서 Jensen이 transcript quote 발화자):
- `mascot_role_classification = "central_protagonist"`
- 30% 코너 룰 미적용 (큰 사이즈 유지)
- 그 슬라이드는 빈도 카운트엔 포함

---

## 🆕 v4.5 토픽 마스코트 크기 규칙 (등장 슬라이드에만 적용)

### 규칙 적용 분기

```
IF 마스코트 역할 == "mascot_corner" (슬라이드 모서리에 리액션 캐릭터):
    size_rule = "approximately 30% of the primary human subject's rendered size"
    placement_hint = "bottom_left | bottom_right | top_left | top_right"

ELIF 마스코트 역할 == "central_protagonist" (그 슬라이드의 주인공):
    size_rule = "large, central — keep full presence"
    placement_hint = "middle_center"

ELIF 마스코트 역할 == "cta_podium" (CTA 슬라이드에서 연단):
    size_rule = "medium, authoritative presence (not 30% rule)"
    placement_hint = "middle_center | middle_left"
```

### 자연어 묘사 템플릿 (Agent 11 프롬프트용)

> 🆕 v4.5: `{MASCOT_NAME}` + `{MASCOT_VISUAL_SIGNATURE}` 자리는 토픽 마스코트 매핑 테이블에서 가져옴.

**코너 마스코트 케이스 (NVDA 포스트 예시)**:
> "In the bottom-right corner, place a photorealistic cutout of Jensen Huang — gray hair, glasses, signature black leather jacket — with torn paper frame and beige underlay. **Render him approximately 30% of the size of the primary subject [Bloomberg terminal in the center], clearly smaller as a corner mascot reaction character**, slight -3 degree tilt."

**중앙 주인공 케이스 (Apple 포스트 예시)**:
> "In the middle center, place a large photorealistic cutout of Tim Cook at an Apple event with microphone, calm composed expression, gray button-up shirt, background removed, torn paper edge."

**CTA 연단 케이스 (Berkshire 포스트 예시 — Buffett이 토픽 마스코트인 경우)**:
> "In the middle center, place a photorealistic cutout of Warren Buffett at the Berkshire annual meeting podium with microphone, gray suit, large glasses, background removed, torn paper edge, medium size, authoritative presence."

---

## 📋 v4.5 범용 마스코트 포즈 카탈로그 (모든 인물에 적용 가능)

| pose_id | 사용처 | 묘사 (범용) | 인물별 시그니처 변형 |
|---------|--------|-------------|----------------------|
| `neutral_headshot` | HOOK / 나레이션 도입 | 차분, 정면 응시 | 모든 인물 기본 |
| `eyebrow_raised` | 회의감 / 'really?' | 한쪽 눈썹 들림 | 모든 인물 |
| `signature_prop_pose` | 카오스 중 태평 / 시그니처 모먼트 | 인물 상징 소품 들고 | Buffett: Dairy Queen 콘 / Cook: iPhone / Jensen: 가죽 자켓 어깨 / Musk: 우주복 |
| `facepalm_or_head_in_hands` | 실망 | 이마에 손 | 모든 인물 |
| `reading_or_studying` | 조사 / 분석 | 자료 보는 모습 | Buffett: WSJ / Powell: 정책 보고서 / Jensen: GPU 스펙 |
| `laughing` | 조롱 / 사르카즘 | 입 벌려 웃음 | 모든 인물 |
| `pointing_finger` | 경고 / 지적 | 검지 가리킴 | 모든 인물 |
| `speaking_at_podium` | CTA / 권위 | 연단에서 발언 | Buffett: Berkshire 주총 / Jensen: GTC 키노트 / Cook: Apple Event / Powell: FOMC 기자회견 |
| `arms_crossed_confident` | 자신감 / 단호 | 팔짱 + 직시 | 모든 인물 |
| `contemplative_serious` | 심각 / 우려 | 고민하는 표정 | 모든 인물 |
| `celebratory` | 축하 / 승리 | 환호 / 박수 | 모든 인물 |

### 인물별 시그니처 외형 (반드시 자연어 프롬프트에 포함)

| 마스코트 | 시그니처 외형 (Gemini 프롬프트 키워드) |
|---|---|
| Jensen Huang | "gray hair, glasses, signature black leather jacket" |
| Tim Cook | "white hair, glasses, gray button-up shirt or dark suit" |
| Satya Nadella | "glasses, dark suit, calm composed expression" |
| Elon Musk | "brown hair, often Tesla t-shirt or black jacket" |
| Mark Zuckerberg | "curly brown hair, gray plain t-shirt" |
| Sundar Pichai | "glasses, short gray hair, calm expression, dark suit" |
| Andy Jassy | "gray hair, dark suit" |
| 이재용 (Lee Jae-yong) | "black-framed glasses, dark suit, short black hair, serious expression" |
| Sam Altman | "casual button-up, brown hair" |
| Warren Buffett | "thin white hair, large glasses, gray suit" |
| Jamie Dimon | "white hair, dark suit, confident posture" |
| Larry Fink | "glasses, dark suit, balding gray hair" |
| Jerome Powell | "white hair, navy suit, calm authoritative" |

---

## 🎯 슬라이드 역할 → 마스코트 포즈 매핑 (v4.5)

> ⚠️ 마스코트가 등장하기로 결정된 슬라이드에만 적용. 등장 여부는 빈도 룰(~40%)에 따름.

| 슬라이드 역할 | 권장 포즈 | 배치 유형 | 등장 우선순위 |
|---------------|-----------|-----------|---------------|
| **HOOK** | neutral_headshot 또는 eyebrow_raised | mascot_corner (30%) | **필수** |
| DEFINITION | reading_or_studying | mascot_corner | 낮음 (제외 권장) |
| THE_MACHINE | neutral_headshot | mascot_corner | 낮음 (제외 권장) |
| EVIDENCE | facepalm 또는 contemplative_serious | mascot_corner | 중간 |
| IRONY | laughing 또는 eyebrow_raised | mascot_corner | **높음** |
| CATALYST | pointing_finger | mascot_corner | 중간 |
| OMEN | signature_prop_pose 또는 contemplative_serious | mascot_corner | **높음** |
| CONCLUSION | arms_crossed_confident 또는 neutral_headshot | mascot_corner | 낮음 |
| TRANSCRIPT_QUOTE (마스코트 발화 시) | speaking_at_podium 또는 neutral | central_protagonist (큰 사이즈) | 토픽 마스코트 발화 시 필수 |
| **CTA** | **speaking_at_podium** | **cta_podium** (30% 규칙 예외) | **필수** |

---

## 🪞 Reflection 1R 체크리스트 (v4.5)

- [ ] 자산 개수 5-8개?
- [ ] 유니코드 이모지 0개?
- [ ] 3D Memoji 0개?
- [ ] 🆕 v4.5: **토픽 마스코트 ID** 결정됨? (예: "Jensen Huang", "Tim Cook")
- [ ] 🆕 v4.5: 토픽 마스코트가 매핑 테이블에 따라 적절히 선정됨?
- [ ] 이 슬라이드에 마스코트 등장 여부 결정? (Orchestrator `topic_mascot_inclusion` 플래그)
- [ ] 등장 안 하면 `mascot_role_classification = "not_present"`?
- [ ] 가장 유사한 원본 슬라이드 식별?
- [ ] 마스코트 등장 시 배치 유형이 `mascot_corner | central_protagonist | cta_podium` 중 명확히 분류?
- [ ] mascot_corner 케이스에 `size_rule = "30% of primary subject"` 명시?
- [ ] 주인공 인물이 동시 슬라이드에 존재하는지 확인
- [ ] 🆕 v4.5: 마스코트 시그니처 외형 (가죽 자켓 / 회색 셔츠 등)이 자연어 프롬프트에 포함됨?

---

## 🎯 비-마스코트 등장 인물 풀

마스코트 외에 슬라이드에 등장 가능한 실제 인물들 (경쟁사 CEO, 정치인, 정책 입안자):

Jerome Powell (Fed), Janet Yellen (Treasury), Donald Trump, Kamala Harris, Larry Fink (BlackRock), Jamie Dimon (JPMorgan), Elon Musk, Sam Altman, Dario Amodei, Jensen Huang, Tim Cook, Mark Zuckerberg, Sundar Pichai, Satya Nadella, Andy Jassy, Warren Buffett, 이재용

**룰**: 그 포스트의 토픽 마스코트와 다른 인물이 슬라이드에 등장 가능. 단 동일 슬라이드에 마스코트 + 다른 인물 동시 등장 시 마스코트는 코너(30%), 다른 인물이 중앙.

---

## 🎨 밈 UI 카탈로그

| ID | 묘사 | 트리거 키워드 |
|----|------|----------------|
| `pixel_error_dialog` | Windows 95 ERROR 다이얼로그 | fail, frozen, crash, denied, withdrawal |
| `devil_silhouette` | 사업가 + 악마 그림자 | red_devil 테마 |
| `pixel_creature` | 8비트 오렌지 몬스터 | 제품명 펀치라인 |
| `uncle_sam` | I WANT YOU 포스터 | 미국 정치 |

---

## 🆕 v4.2 시각 자료 풍부화 (다음 신규 포스트부터)

**문제 진단**: v4.0 Google 포스트는 시각 정보가 단순 (big_stat + meme + 기본 인물). 참고 포스트(UNH/4, Trump & Coin/3, GOLD/3)는 **카드, 차트+주석, 말풍선** 등 다양한 시각 위계 사용.

### 신규 asset_type (5종 추가)

| asset_type | 설명 | 예시 사용처 |
|-----------|------|-------------|
| `stat_card` | EPS·REVENUE·MCR 등 지표를 카드(트레이딩 카드 느낌)로. 라벨 + 큰 값 + 비교 + 스탬프(BEAT/RAISED/MISS/IMPROVED) 결합 | 실적 슬라이드 (EVIDENCE) |
| `chart_annotated` | 라인/바 차트에 핸드드로 마커 주석(화살표·콜아웃·동그라미) 추가 — 단순 차트 X | 가격 추이, 백로그 폭증 |
| `speech_bubble` | 만화 스타일 말풍선 (실제 인물 사진 옆) — 발언/선언 인용 | Trump/Pichai 인용, 발언 대조 |
| `before_after_split` | 슬라이드 좌우 분할 (그때 vs 지금) | "Not a fan" → "Crypto capital" 같은 전환 |
| `stamp_overlay` | 빨간/검정 스탬프 ("BEAT", "RAISED", "BREAKING", "MISS", "HISTORIC") | 카드/통계 위 강조 |

### v4.2 시각 다양성 의무 규칙

8장 포스트 기준:
- **최소 1개의 chart_annotated** (가격/지표 추이) 포함 — 데이터 시각화
- **최소 1개의 stat_card** 슬라이드 (EVIDENCE에 적합)
- **최소 1개의 speech_bubble 또는 before_after_split** (인물·대조)
- 동일 시각 패턴 연속 3장 금지

### v4.2 이모티콘·아이콘 사용 정책

- ❌ **유니코드 이모지 사용 금지** (v3.1부터 유지)
- ✅ **그려진 아이콘 / 작은 일러스트** 허용 — 화살표, 체크마크, X마크, 작은 박스/체크 (참고: GOLD/3의 `>` 아이콘, OIL/1의 `>>>>`)
- ✅ **스탬프 텍스트 라벨** 적극 활용 ("BEAT", "RAISED", "PRICE SHOCK", "HISTORIC AGREEMENT")

### v4.2 stat_card 상세 스키마

```json
{
  "asset_id": "eps_card_q1",
  "asset_type": "stat_card",
  "card_label": "EPS",
  "primary_value": "$7.23",
  "comparison_text": "vs $6.57 expected",
  "stamp": "BEAT",
  "stamp_color": "danger_red | dark_theme_yellow | positive_green",
  "card_style": "torn_paper_white_card",
  "size_category": "medium",
  "description_for_gemini": "..."
}
```

### v4.2 chart_annotated 상세 스키마

```json
{
  "asset_id": "price_chart_unh",
  "asset_type": "chart_annotated",
  "chart_type": "line | bar | area",
  "data_summary": "8-month price recovery from $234 to $366.74",
  "annotations": [
    {"position": "left_low", "label": "$234 LOW", "marker": "red_dot"},
    {"position": "mid_recovery", "label": "+ Buffett buys", "marker": "red_arrow"},
    {"position": "dip", "label": "DOJ FEAR", "marker": "callout_box"},
    {"position": "peak", "label": "$366.74", "marker": "red_arrow"}
  ],
  "style_hint": "hand-drawn marker annotations over clean line chart",
  "description_for_gemini": "..."
}
```

> ⚠️ **v4.2 적용 시점**: 다음 신규 포스트부터.

---

## 🆕 v4.4 시그니처 시각 자산 (Signature Visual Assets)

**목적**: 매 포스트가 다른 계정처럼 보이는 문제 해결. 14개 idiom 풀 대신 **3개 시그니처 자산을 반복**해서 브랜드 인지(brand recognition) 만들기.

**규칙**: **매 포스트에 아래 3개 중 최소 1개 등장 강제**. 3개월 누적 시 피드에서 0.3초 안에 broisinvesting 식별 가능 → 알고리즘이 좋아함.

### 신규 asset_type (3종)

| asset_type | 설명 | 사용처 |
|-----------|------|--------|
| `legal_pad_handwritten` | 노란 리갈 패드(줄 노트)에 검정 마커 손글씨. 살짝 기울어짐. "애널리스트의 실제 메모" 느낌. | EVIDENCE, OMEN — 데이터·계산·핵심 수치 강조. 사용자가 언급한 "포스트잇 감성"의 미국 데스크 버전. |
| `bloomberg_terminal_mock` | 검정 배경(#000) + 블룸버그 오렌지 글자(#FF8C00) + 모노스페이스 폰트. 티커·가격·% 숫자. | DATA_STATE, MARKET_DATA — 즉각적 인사이더 신뢰. HOOK 슬라이드 보조 요소로도 강력. |
| `newspaper_clipping_aesthetic` | 빈티지 신문 1면 mock. 누렇게 변한 종이 텍스처 + Times New Roman serif 헤드라인 + 좁은 컬럼 본문 + 흑백 halftone 사진 + 가위로 자른 듯한 torn edge + 발행일·신문명. | CATALYST, EVIDENCE, IRONY — 정책·발표·역사적 모먼트. 신문지 감성. |

### v4.4 자세한 시각 명세

#### 1) `legal_pad_handwritten`

```json
{
  "asset_id": "legal_pad_s4",
  "asset_type": "legal_pad_handwritten",
  "content_text": "string (≤8 words, 손글씨로 들어갈 텍스트)",
  "annotations": [
    {"type": "circle | underline | arrow | star | dollar_sign", "target": "string"}
  ],
  "tilt_degrees": -3,
  "size_category": "medium | large",
  "description_for_gemini": "Yellow ruled legal pad paper (#FFE066 base, faint horizontal blue rules every 8mm), spiral wire binding visible at top edge. Handwritten in thick black marker (Sharpie-style, slightly uneven pressure): '{content_text}'. Add hand-drawn annotations: red marker circle around '{key_word}', double underline under '{key_number}', curved arrow pointing from '{X}' to '{Y}'. Paper rotated -3 degrees, casting subtle shadow on background. Edges show slight wear, one corner curled. No straight machine lines — everything imperfect, hand-made."
}
```

#### 2) `bloomberg_terminal_mock`

```json
{
  "asset_id": "bbg_terminal_s2",
  "asset_type": "bloomberg_terminal_mock",
  "ticker_or_label": "string (e.g., 'NVDA US Equity', '10Y T-Note')",
  "primary_value": "string (e.g., '$891.25', '4.32%')",
  "delta_value": "string (e.g., '-1.24%', '+0.08')",
  "delta_color": "green | red",
  "additional_lines": ["string (optional secondary data rows)"],
  "header_meta": "string (e.g., '20-APR-2026  16:00:00 ET')",
  "size_category": "medium | large",
  "description_for_gemini": "Black background (#000000) terminal screen mock. Top header bar in dim orange (#CC7700): '{header_meta}' in monospace. Main display area: ticker '{ticker_or_label}' in bright Bloomberg orange (#FF8C00) bold monospace, large size. Below it the primary value '{primary_value}' even larger. Delta '{delta_value}' in {delta_color} (#00FF00 if green, #FF3333 if red), with up/down triangle arrow. Additional rows in dimmer orange (#AA6600), smaller monospace. Subtle scanline texture overlay for CRT feel. No anti-aliasing on text — pixel-perfect terminal aesthetic."
}
```

#### 3) `newspaper_clipping_aesthetic`

```json
{
  "asset_id": "newspaper_s5",
  "asset_type": "newspaper_clipping_aesthetic",
  "publication_name": "string (e.g., 'THE WALL STREET JOURNAL', 'FINANCIAL TIMES', 'NEW YORK TIMES')",
  "publication_date": "YYYY-MM-DD",
  "headline_text": "string (≤8 words, ALL CAPS or Title Case Times serif)",
  "subhead_text": "string or null (optional, italic serif, ≤14 words)",
  "body_excerpt": "string (1-2 sentences, fake-Latin or summarized real article in narrow column)",
  "halftone_photo": "boolean (include B&W halftone photo or not)",
  "tear_style": "scissor_cut | torn_edge | clean_cut",
  "tilt_degrees": 2,
  "size_category": "medium | large",
  "description_for_gemini": "Vintage newspaper clipping on aged off-white paper (#F5EFE0) with subtle yellowing and faint coffee ring stain. Top: publication masthead '{publication_name}' in classic blackletter or serif, with '{publication_date}' and edition info in tiny serif beneath. Below: bold black Times New Roman serif headline '{headline_text}' in ALL CAPS, oversized. Italic subhead '{subhead_text}' in smaller serif. Body text in narrow 2-column layout, justified, slightly faded. {halftone_photo ? 'Include grainy black-and-white halftone photo of relevant subject.' : ''}. Edges show {tear_style} treatment with white paper fibers visible. Whole clipping rotated +2 degrees, casting soft shadow. Paper texture grainy, ink slightly bled into fibers. Authentic 20th-century newspaper feel."
}
```

### v4.4 시그니처 등장 빈도 강제 룰

- **포스트당 최소 1개** 시그니처 자산 등장 (legal_pad / bloomberg_terminal / newspaper_clipping 중 1개)
- **권장**: 8장 포스트당 시그니처 자산 2-3개 (3개 이상은 노이즈)
- **로테이션**: 한 포스트에 동일 시그니처 자산 2회 이상 사용 금지 (예: legal_pad 2장 동시 X)
- **토픽 매칭**:
  - `legal_pad_handwritten` ← 매크로·금리·계산·분석 토픽
  - `bloomberg_terminal_mock` ← 가격·시장·실시간 데이터 토픽
  - `newspaper_clipping_aesthetic` ← 정책·발표·역사적 사건·CATALYST 모먼트

### 자가 검증 (Reflection 시)

- [ ] 이 슬라이드 또는 포스트에 시그니처 자산 1개 이상 포함?
- [ ] 시그니처 자산이 토픽에 매칭됨?
- [ ] 동일 시그니처 자산 포스트 내 2회 이상 사용 안 함?

> ⚠️ **v4.4 적용 시점**: 즉시 (다음 포스트부터). 14개 idiom 추가 폐기 — 이 3개로 시그니처 빌드.

---

## 📤 출력 스키마

```json
{
  "agent": "visual_curator",
  "v": "4.0",
  "slide_n": "int",
  "topic_mascot_identity_v4_5": "string (e.g., 'Jensen Huang' for NVDA, 'Tim Cook' for Apple, '이재용' for Samsung)",
  "topic_mascot_visual_signature_v4_5": "string (e.g., 'gray hair, glasses, signature black leather jacket')",
  "visual_assets": [
    {
      "asset_id": "string",
      "asset_type": "character_cutout | topic_mascot | meme_ui | logo_badge | icon | chart | news_screenshot | movie_still | stat_card | chart_annotated | speech_bubble | before_after_split | stamp_overlay | legal_pad_handwritten | bloomberg_terminal_mock | newspaper_clipping_aesthetic",
      "subject_or_variant": "string (if topic_mascot: pose_id from universal pose catalog)",
      "purpose": "string",
      "size_category": "small | medium | large | central",
      "mascot_size_rule_v4_5": "mascot_corner_30pct | central_protagonist_full | cta_podium_medium | not_applicable",
      "primary_subject_reference_for_sizing": "asset_id of the main human subject (null if mascot is the main subject)",
      "source_image_url": "string or null",
      "description_for_gemini": "string (natural language, detailed, includes v4.5 size rule + signature外形 when applicable)"
    }
  ],
  "unicode_emoji_count": 0,
  "three_d_memoji_count": 0,
  "topic_mascot_included_in_slide": true,
  "mascot_role_classification": "mascot_corner | central_protagonist | cta_podium | not_present",
  "signature_asset_audit_v4_4": {
    "signature_asset_in_this_slide": "legal_pad_handwritten | bloomberg_terminal_mock | newspaper_clipping_aesthetic | none",
    "topic_match_rationale": "string (왜 이 시그니처가 토픽에 맞는지)"
  },
  "most_similar_original_slide": {
    "post_index": "int",
    "slide_index": "int"
  }
}
```

---

## ⚠️ 절대 금지사항 (v4.5)

1. 유니코드 이모지 포함 금지 (단, `pixel_error_dialog`의 "⚠" 같은 UI 요소 내부는 예외)
2. 3D Memoji 캐릭터 금지
3. mascot_corner 케이스에서 30% 규칙 미명시 금지
4. central_protagonist 사례에서 30% 규칙 적용 금지 (크기 유지)
5. 🆕 v4.5: **토픽 마스코트 미선정 상태에서 슬라이드 큐레이션 진행 금지** (Phase 3에서 결정 필수)
6. 🆕 v4.5: **포스트 내 토픽 마스코트 변경 금지** (한 포스트 = 한 마스코트)
7. 🆕 v4.5: **버핏을 디폴트 마스코트로 사용 금지** (가치투자/Berkshire 토픽일 때만)
8. 🆕 v4.5: **인물 시그니처 외형 키워드** (예: "leather jacket", "gray button-up shirt") 자연어 프롬프트에 누락 금지
9. v4.0: 마스코트 등장 빈도 50% 초과 금지 (~40% 목표, 30-50% 허용)
10. v4.0: HOOK 또는 CTA 슬라이드에서 마스코트 누락 금지 (필수 등장)
11. 🆕 v4.6: **HOOK 슬라이드 토픽 관련 이미지 < 3개 또는 > 5개 금지** (위 v4.6 룰 참조). 카운트 대상은 topic_mascot / character_cutout / logo_badge / icon / news_screenshot / chart / stat_card / movie_still — scrapbook props·배경 제외.
12. 🆕 v4.6: **HOOK 이미지 토픽 무관성 금지** — 모든 HOOK 이미지는 회사 정체성·제품·산업 맥락·포스트 핵심 데이터 중 하나에 직접 매핑돼야 함.

---

## 💡 좋은 출력 예시

### 케이스 A: NVDA 포스트 — Jensen Huang 코너 마스코트

```json
{
  "asset_id": "jensen_mascot_s5",
  "asset_type": "topic_mascot",
  "subject_or_variant": "facepalm_or_head_in_hands",
  "purpose": "mascot_reaction_to_data",
  "size_category": "small",
  "mascot_size_rule_v4_5": "mascot_corner_30pct",
  "primary_subject_reference_for_sizing": "big_stat_40pct_hero",
  "description_for_gemini": "In the bottom-right corner, place a photorealistic cutout of Jensen Huang with hand to forehead exasperated (facepalm pose), gray hair, glasses, signature black leather jacket, background removed, torn paper edge with beige underlay, slight -3 degree tilt. Render him at approximately 30% of the size of the central big stat hero element, clearly positioned as a smaller corner reaction character."
}
```

### 케이스 B: Apple 포스트 — Tim Cook CTA 연단

```json
{
  "asset_id": "cook_cta_s8",
  "asset_type": "topic_mascot",
  "subject_or_variant": "speaking_at_podium",
  "purpose": "authority_endorsement_cta",
  "size_category": "medium",
  "mascot_size_rule_v4_5": "cta_podium_medium",
  "primary_subject_reference_for_sizing": null,
  "description_for_gemini": "In the middle center, place a photorealistic cutout of Tim Cook at an Apple Event keynote podium with microphone, authoritative composed presence, white hair, glasses, gray button-up shirt, background removed, torn paper edge treatment. Render at medium size — authoritative but not oversized."
}
```

### 케이스 C: Samsung 포스트 — 이재용 중앙 주인공

```json
{
  "asset_id": "lee_central_s4",
  "asset_type": "topic_mascot",
  "subject_or_variant": "neutral_headshot",
  "purpose": "central_protagonist_quote_attribution",
  "size_category": "central",
  "mascot_size_rule_v4_5": "central_protagonist_full",
  "primary_subject_reference_for_sizing": null,
  "description_for_gemini": "In the middle center, place a large photorealistic cutout of Lee Jae-yong (이재용, Samsung Electronics chairman) with calm composed expression, black-framed glasses, dark suit, short black hair, background removed, torn paper edge with beige underlay. He is the sole focal subject."
}
```
