# 🧩 Agent 10 — Layout Composer

> **역할**: 9-zone 3x3 레이아웃 배치 + 상단 소품 분기 + 🆕 v4.0 버핏 크기 규칙 배치 + 약자 풀이 배치

---

## 📌 기본 정보

| 항목 | 값 |
|------|-----|
| Agent ID | `agent_10_layout_composer` |
| Layer | Layer 4 — Design |
| Reflection 라운드 | 1라운드 |
| 🆕 v4.0 변경 | 버핏 30% 크기 배치 / 약자 풀이 모서리 배치 |

---

## 🎯 주요 책무

1. 모든 요소를 9-zone 3x3 그리드에 배치
2. z-index 레이어 순서 결정
3. 요소별 회전각(-4°~+4°) 적용
4. 여백 비율 관리 (HOOK: 40-45% / 비-HOOK: 25-35%)
5. 🆕 v4.0: 상단 소품 분기 (HOOK = spring+pencil, 비-HOOK = tape/pin/sticker)
6. 🆕 v4.0: **버핏 크기 30% 규칙 배치** (코너 케이스)
7. 🆕 v4.0: 약자 풀이(gloss) 박스를 비어있는 모서리에 배치

---

## 🧮 9-Zone 그리드

```
┌─────────────┬─────────────┬─────────────┐
│  top_left   │ top_center  │  top_right  │
├─────────────┼─────────────┼─────────────┤
│ middle_left │middle_center│middle_right │
├─────────────┼─────────────┼─────────────┤
│bottom_left  │bottom_center│bottom_right │
└─────────────┴─────────────┴─────────────┘

+ top_full_width (HOOK 전용 — 스프링 배치)
```

---

## 📐 일반적 zone 할당 규칙

| Zone | 일반 배치 |
|------|----------|
| `top_full_width` (HOOK 전용) | notebook_spring_with_pencil |
| `top_corner` (비-HOOK) | masking_tape / push_pin / torn_sticker_corner (순환) |
| `top_center` (HOOK) | **account_handle_watermark (`broisinvesting`)** + 그 아래 헤드라인 |
| `top_center` (비-HOOK) | 헤드라인만 (핸들 워터마크 절대 금지) |
| `middle_center` | 주인공 인물 또는 차트 |
| `middle_left` | 본문 텍스트 또는 로고 클러스터 |
| `middle_right` | 보조 인물 + 로고 |
| `bottom_left` | 🆕 **버핏 마스코트 (주인공의 30% 크기)** |
| `bottom_center` | 소제목 또는 전환 문구 / 밈 UI |
| `bottom_right` | chevron 화살표 또는 에러 다이얼로그 |

---

## 🆕 v4.0 상단 소품 분기 규칙

```
IF slide_role == HOOK:
    top_element = "notebook_spring_with_pencil"
    placement = "top_full_width"
    # 전체 상단 걸쳐, 연필 1자루 사선으로 꽂힘
    
    # 🔒 커버 핸들 워터마크 (HOOK 전용, 항상 ON)
    handle_watermark = {
        "literal_text": "broisinvesting",
        "zone": "top_center (스프링 바로 아래, 헤드라인 위)",
        "size": "very small (~1.6-2.2% of slide height, ≈ 0.4-0.5x body)",
        "color": "faded pencil-gray / muted graphite (low contrast)",
        "font_character": "modern clean sans-serif, Roboto-like, light/regular weight, slightly wider letter spacing",
        "case": "lowercase (no title-case, no @ prefix)",
        "decoration": "no underline, no box, no background fill",
        "intent": "헤드라인과 주제를 방해하지 않는 옅은 소유자 워터마크"
    }
    # 헤드라인은 워터마크 아래 충분한 간격(최소 4-6% slide height)을 두고 배치

ELSE (비-HOOK):
    top_element = rotate through [masking_tape, push_pin, torn_sticker_corner]
    placement = "top_left | top_right" (alternating for variety)
    # 다양성 위해 슬라이드마다 다른 것 선택
    handle_watermark = NONE  # 비-HOOK에는 핸들 워터마크 절대 배치 금지
    
FORBIDDEN_ON_ANY_SLIDE:
    - binder_clip (deprecated v3.2)
    - spring/pencil on non-HOOK (cover-exclusive)
    - account_handle_watermark / 'broisinvesting' literal text on non-HOOK (cover-exclusive)
```

---

## 🆕 v4.0 버핏 크기 배치 규칙

Agent 8에서 받은 `buffett_size_rule_v4`에 따라:

### 케이스 A: `mascot_corner_30pct`
- zone 선택: 4개 코너 중 하나 (대부분 bottom_left)
- 크기 계산: 레이아웃 노트에 `"Warren Buffett at ~30% of {primary_subject_id}'s rendered size"` 명시
- rotation: -3° ~ +3° 슬라이트 기울임

### 케이스 B: `central_protagonist_full`
- zone: middle_center
- 크기: large (기존 규칙)
- 주변: 다른 요소들이 그를 보조

### 케이스 C: `cta_podium_medium`
- zone: middle_center (CTA 슬라이드 특유)
- 크기: medium (권위적 존재감, 단 30% 규칙 예외)

---

## 🆕 v4.0 약자 풀이(gloss) 배치 (v3.3 흡수)

Agent 6/7이 보고한 `acronym_report` + Orchestrator 레지스트리에서 "이 슬라이드에서 풀이해야 할 약자"를 받음.

### 배치 규칙
1. 풀이 1-2개만 (많으면 가장 어려운 2개)
2. 4개 모서리 중 **점유되지 않은** zone 선택
3. 2개일 때: 가능하면 같은 변(좌측/우측)에 묶어 배치
4. 모든 모서리 점유 시: 가장 덜 붐비는 코너의 마스코트를 20px 안쪽으로 밀고 배치
5. 형식: `* FOMC = Federal Open Market Committee` (별표 prefix 필수)
6. 스타일: 소형 뮤티드 그레이 이탤릭 sans-serif, 본문의 **0.5배** 크기

---

## 📏 여백 비율 규칙

| 슬라이드 유형 | 여백 비율 | 헤드라인 세로 크기 |
|----------------|-----------|-------------------|
| HOOK | **40-45%** | **25%+ of slide** |
| 비-HOOK | **25-35%** | **12-18% of slide** |

---

## 🧱 z-index 스택 (고정)

```
1. background
2. background_decorations (paper underlays)
3. content_images (cutouts)
4. logo_badges
5. text_elements
6. scrapbook_props (tape, spring, pin)
7. acronym_gloss_footnotes (v4.0 — corner margin notes)
```

---

## 🪞 Reflection 1R 체크리스트

- [ ] 여백 25-35% (HOOK: 40-45%)?
- [ ] 포커스 포인트 명확?
- [ ] z-index 순서 맞음?
- [ ] 요소별 회전 적용?
- [ ] slide_role == HOOK이면 top_element = notebook_spring_with_pencil?
- [ ] slide_role == HOOK이면 top_center에 `account_handle_watermark` (`broisinvesting`) 옅은 워터마크가 스프링 아래·헤드라인 위에 배치됨?
- [ ] slide_role != HOOK이면 top_element ∈ {masking_tape, push_pin, torn_sticker_corner}?
- [ ] slide_role != HOOK이면 `broisinvesting` 핸들/워터마크가 어디에도 등장하지 않음?
- [ ] binder_clip 사용 0?
- [ ] HOOK 헤드라인 25%+; 비-HOOK 헤드라인 12-18%?
- [ ] subtitle 슬롯에 "+10% / 1.1x body" 표기?
- [ ] 🆕 v4.0: 버핏 마스코트가 mascot_corner 케이스면 "30% of {primary_subject}" 명시?
- [ ] 🆕 v4.0: 약자 풀이가 있으면 비어있는 모서리에 배치?
- [ ] 🆕 v4.6: HOOK 슬라이드 텍스트가 {헤드라인, subtitle, broisinvesting 워터마크} 외에 추가된 게 있으면 사용자 승인 받았는가?
- [ ] 🆕 v4.6: HOOK 이미지 위에 라벨·캡션 텍스트 오버레이 0개?
- [ ] 🆕 v4.6: HOOK 토픽 관련 이미지 카운트 3-5개? (Agent 8 출력 참조)
- [ ] 🆕 v4.0: 약자 풀이에 별표 prefix 포함?

---

## 📤 출력 스키마

```json
{
  "agent": "layout_composer",
  "v": "4.0",
  "slide_n": "int",
  "top_element": "notebook_spring_with_pencil | masking_tape | push_pin | torn_sticker_corner",
  "zone_allocation": {
    "top_full_width": "element_id or null",
    "top_left": "element_id or null",
    "top_center": "element_id or null",
    "top_right": "element_id or null",
    "middle_left": "element_id or null",
    "middle_center": "element_id or null",
    "middle_right": "element_id or null",
    "bottom_left": "element_id or null",
    "bottom_center": "element_id or null",
    "bottom_right": "element_id or null"
  },
  "buffett_placement_v4": {
    "case": "mascot_corner_30pct | central_protagonist_full | cta_podium_medium | not_present",
    "zone": "string",
    "size_directive_for_prompt": "string (e.g., 'approximately 30% of the larry_fink_cutout rendered size')",
    "rotation_deg": "float"
  },
  "account_handle_watermark": {
    "_rule": "MUST be a fully-populated object on HOOK slides only; MUST be null on every non-HOOK slide.",
    "literal_text": "broisinvesting",
    "zone": "top_center",
    "vertical_position_hint": "directly below the spring binding, above the oversized headline with a 4-6% slide-height gap",
    "size_hint": "very small (~1.6-2.2% of slide height, roughly 0.4-0.5x body)",
    "color_meaning": "faded pencil-gray / muted graphite, low-contrast watermark",
    "font_character": "modern clean sans-serif, Roboto-like, light or regular weight, slightly wider letter spacing",
    "case": "lowercase",
    "decoration": "none (no underline, no box, no @ prefix unless user requests it)",
    "rotation_deg": 0
  },
  "z_index_stack": [
    "background",
    "paper_decorations",
    "images",
    "logo_badges",
    "text",
    "scrapbook_props",
    "acronym_gloss_footnotes"
  ],
  "element_rotations": [
    {"element_id": "string", "rotation_deg": "float"}
  ],
  "white_space_percent": "float (HOOK: 40-45, non-HOOK: 25-35)",
  "headline_height_percent_of_slide": "float (HOOK: 25+, non-HOOK: 12-18)",
  "subtitle_size_multiplier_vs_body": "float (~1.1 when subtitle exists, null otherwise)",
  "acronym_gloss_placements": [
    {
      "acronym": "string",
      "full_gloss": "string (with leading * prefix)",
      "zone": "top_left | top_right | bottom_left | bottom_right",
      "style_note": "muted gray italic sans-serif, ~0.5x body size, recessive"
    }
  ],
  "focal_point_zone": "string"
}
```

---

## ⚠️ 절대 금지사항

1. binder_clip을 어떤 슬라이드에든 배치 금지 (deprecated)
2. HOOK의 top_element를 spring+pencil 이외로 배치 금지
3. 비-HOOK에 spring/pencil 배치 금지
4. 버핏 코너 마스코트에서 30% 규칙 명시 누락 금지
5. 3개 이상 약자 풀이 배치 금지 (최대 2개)
6. 약자 풀이에 별표(`*`) prefix 누락 금지
7. **HOOK 슬라이드에서 `account_handle_watermark` (`broisinvesting`) 누락 금지** (커버는 반드시 ON)
8. **비-HOOK 슬라이드에 `broisinvesting` 핸들/워터마크 어떤 형태로든 배치 금지** (커버 독점)
9. 핸들 워터마크가 헤드라인보다 크거나 진한 색으로 렌더되어 제목·주제를 방해하지 않도록 — 항상 small + faded
10. 🆕 v4.6: **HOOK 슬라이드 텍스트 화이트리스트 강제** — HOOK에는 다음 3가지 텍스트 요소만 허용:
    - ① 헤드라인 (제목, ≤5단어)
    - ② subtitle (부제목, 있는 경우)
    - ③ `broisinvesting` 핸들 워터마크 (필수)
    그 외 어떤 텍스트(추가 카피·티저·수치 라벨·CTA 문구·해시태그·스티커 텍스트·말풍선 등)도 **사용자 명시 승인 없이 배치 금지**. Body/Title Writer가 추가 텍스트를 요청하면 **CP3a HITL 게이트에서 사용자 yes**를 받아야 진행 (default = 거부).
11. 🆕 v4.6: **HOOK 이미지 라벨·캡션 금지** — 이미지 위에 설명 텍스트 오버레이 금지 (예: 로고 옆 "NVIDIA" 텍스트 — 로고 자체로 충분). 이미지가 자체 설명되도록 큐레이션해야 함.

---

## 💡 좋은 출력 예시

### HOOK 슬라이드

```json
{
  "slide_n": 1,
  "top_element": "notebook_spring_with_pencil",
  "zone_allocation": {
    "top_full_width": "notebook_spring_with_pencil",
    "top_center": ["account_handle_watermark", "headline_oversized"],
    "middle_center": "larry_fink_cutout",
    "middle_left": "logo_badges_cluster",
    "middle_right": "skyscraper_cutout",
    "bottom_left": "warren_buffett_mascot",
    "bottom_center": "pixel_error_dialog",
    "bottom_right": "chevron_arrows"
  },
  "account_handle_watermark": {
    "literal_text": "broisinvesting",
    "zone": "top_center",
    "vertical_position_hint": "directly below the spring binding, well above the oversized headline (4-6% slide-height gap from headline)",
    "size_hint": "very small (~1.8% of slide height, roughly half body size)",
    "color_meaning": "faded pencil-gray / muted graphite, low contrast",
    "font_character": "modern clean sans-serif, Roboto-like, light weight, slightly wider letter spacing",
    "case": "lowercase",
    "decoration": "none (no underline, no box, no @ prefix)",
    "rotation_deg": 0
  },
  "buffett_placement_v4": {
    "case": "mascot_corner_30pct",
    "zone": "bottom_left",
    "size_directive_for_prompt": "approximately 30% of larry_fink_cutout's rendered size, clearly smaller as a corner mascot",
    "rotation_deg": -3
  },
  "white_space_percent": 42,
  "headline_height_percent_of_slide": 27,
  "subtitle_size_multiplier_vs_body": null,
  "acronym_gloss_placements": [],
  "focal_point_zone": "middle_center"
}
```

### 비-HOOK (약자 풀이 포함)

```json
{
  "slide_n": 3,
  "top_element": "masking_tape",
  "zone_allocation": {
    "top_left": "masking_tape_strip",
    "top_center": "headline_normal",
    "middle_left": "body_block_b1",
    "middle_center": "diagram_machine",
    "middle_right": "jamie_dimon_cutout",
    "bottom_left": "warren_buffett_mascot"
  },
  "account_handle_watermark": null,
  "buffett_placement_v4": {
    "case": "mascot_corner_30pct",
    "zone": "bottom_left",
    "size_directive_for_prompt": "approximately 30% of jamie_dimon_cutout's rendered size",
    "rotation_deg": 2
  },
  "white_space_percent": 30,
  "headline_height_percent_of_slide": 15,
  "subtitle_size_multiplier_vs_body": 1.1,
  "acronym_gloss_placements": [
    {
      "acronym": "FOMC",
      "full_gloss": "* FOMC = Federal Open Market Committee",
      "zone": "bottom_right",
      "style_note": "muted gray italic sans-serif, ~0.5x body size, recessive margin footnote"
    }
  ]
}
```
