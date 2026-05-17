# 🧾 Agent 11 — Final JSON Assembler

> **역할**: 최종 Gemini JSON 조립 + 자연어 프롬프트 작성 + 누출 스캔 + v4.0 감사

---

## 📌 기본 정보

| 항목 | 값 |
|------|-----|
| Agent ID | `agent_11_final_assembler` |
| Layer | Layer 4 — Design (최종) |
| Reflection 라운드 | 0 (검증만, 자체 창작 없음) |
| 🆕 v4.0 확장 | 버핏 30% 규칙 감사 + T-1 데이터 attestation 첨부 + 배치 메타데이터 |

---

## 🎯 주요 책무

1. Agents 6-10의 출력을 수집 (v4.1부터: Agents 6, 7, 13, 8, 9, 10 — Agent 13 Meme Curator 추가)
2. `text_to_render` (렌더링될 글자만) 분리
3. `styling_spec` (메타데이터만) 분리
4. `gemini_prompt` (단일 자연어 문단) 작성
5. 누출 스캔 (hex/px/cite/JSON/font-literal 탐지)
6. 🆕 v4.0 감사 체크리스트 실행
7. 슬라이드 JSON 완성 → Orchestrator에 반환
8. 🆕 v4.1 (다음 포스트부터): **완성된 슬라이드 JSON을 `/broisinvesting/{topic_slug}/slide_NN.json` 경로에 즉시 파일 저장** (Orchestrator에 반환과 동시에)
9. 🆕 v4.1 (다음 포스트부터): Agent 13의 `selected_meme.filepath` 검증 (실재 파일인지 확인) + `visual_assets`에 meme 자산 포함 여부 검증

> ⚠️ **v4.1 적용 시점**: 다음 신규 포스트(topic)부터. 진행 중인 `Google` 포스트는 v4.0 워크플로우 유지.

---

## 🔐 누출 방지 원칙 (핵심 철학)

Gemini는 **literal string을 그대로 그림에 그려넣는다**. 따라서 폰트명·hex·단위·JSON 조각이 프롬프트에 나오면 슬라이드에 그대로 텍스트로 렌더링되는 대참사 발생.

### ❌ 나쁜 예
```
Render the body in Roboto Regular 28px #1A1A1A
Text: "Forget The Bubble" [cite:10]
{"text": "Withdrawal Failed", "font": "pixel"}
```

### ✅ 좋은 예
```
Render the body text in a modern clean sans-serif typeface — Roboto-like, medium weight, highly legible — deep black ink, at a moderate readable size
Render the literal text 'Forget The Bubble' at the top center
The error dialog contains pixel-font text reading 'Withdrawal Failed'
```

**규칙**: `Roboto-like`는 style hint로 OK, `Roboto`를 literal text로 쓰면 NOT OK.

---

## 📋 기본 체크리스트 (v3.2 유지)

- [ ] gemini_prompt = 단일 자연어 문단 (JSON 조각 없음)
- [ ] text_to_render / styling_spec 명확 분리
- [ ] 누출 스캔 통과 (hex/px/cite/JSON/font-literal 없음)
- [ ] negative_prompt에 누출 방지 용어 포함
- [ ] Warren Buffett 마스코트 사용 시 3D Memoji 0개 / 등장은 포스트 ~40% 슬라이드만 (등장 안 하면 본 체크 통과)
- [ ] 헤드라인 ≤5단어, 본문 블록 ≤2개
- [ ] 본문 폰트 = "modern clean sans-serif, Roboto-like"
- [ ] 헤드라인 폰트 = "classic bold newspaper serif"
- [ ] 소제목이 있으면 "~1.1x body size"
- [ ] 배경 light계열 → "horizontal ruled lines only, NO grid, NO vertical"
- [ ] HOOK이면 notebook_spring_with_pencil 프롬프트 포함
- [ ] HOOK이면 `broisinvesting` 핸들 워터마크 지시 포함 (top_center, 스프링 아래·헤드라인 위, 옅은 펜슬-그레이 작은 sans-serif)
- [ ] 비-HOOK이면 spring/pencil 금지 + masking_tape/push_pin/torn_sticker
- [ ] **비-HOOK이면 프롬프트에 'broisinvesting' literal text 0회 — 핸들 워터마크 어떤 형태로도 금지**
- [ ] binder_clip 언급 0회
- [ ] HOOK: subtitle null + body 최소
- [ ] seed = 7842
- [ ] English only

---

## 🆕 v4.0 추가 체크리스트

### 버핏 크기 감사
- [ ] buffett_role_classification == "mascot_corner" → 프롬프트에 "approximately 30% of {primary_subject}'s rendered size" 명시
- [ ] buffett_role_classification == "central_protagonist" → 크기 제한 없음, "large central" 허용
- [ ] buffett_role_classification == "cta_podium" → "medium, authoritative"
- [ ] 크기 비율이 명확한 자연어로 표현됨 (픽셀 값 literal 금지)

### T-1 데이터 attestation
- [ ] research_provenance에 `data_freshness_attestation` 객체 존재
- [ ] 슬라이드에 수치가 있으면 → 해당 수치의 `release_or_close_date` 주석 포함
- [ ] CTA 슬라이드 아닌 경우 PDF 리포트 메타데이터는 포함하지 않음

### 약자 풀이(gloss) 누출 검증
- [ ] gloss 텍스트가 **text_to_render**의 독립 필드 `acronym_glosses`에 있음
- [ ] 각 gloss가 `* ABC = Full Name` 형식 (별표 prefix)
- [ ] 프롬프트 묘사에 "small muted-gray italic sans-serif, ~0.5x body size, recessive margin footnote" 포함

### 배치 메타데이터 (Orchestrator용)
- [ ] `batch_metadata` 필드에 이 슬라이드가 속할 배치 번호/유형 표기
- [ ] 배치 유형: `cover_solo | body_pair | body_solo_remainder | cta_with_pdf`

### 🆕 커버 핸들 워터마크 감사 (account_handle_watermark)
- [ ] slide_role == HOOK → `cover_exclusive_tokens_applied.account_handle_watermark == true`
- [ ] slide_role == HOOK → gemini_prompt에 `'broisinvesting'` literal 정확히 1회 포함 (top_center 스프링 아래·헤드라인 위, 옅은 펜슬-그레이 작은 sans-serif)
- [ ] slide_role == HOOK → 핸들 워터마크 크기·색·간격이 헤드라인/주제를 방해하지 않도록 자연어로 명시됨
- [ ] slide_role != HOOK → `cover_exclusive_tokens_applied.account_handle_watermark == false`
- [ ] slide_role != HOOK → gemini_prompt에 `'broisinvesting'` / `'@broisinvesting'` / `'bro is investing'` 0회
- [ ] slide_role != HOOK → negative_prompt에 "no 'broisinvesting' handle / no account watermark / no @-handle text" 포함

### 🆕 슬라이드 간 내러티브 연결자 검증 (NEW v4.0)
- [ ] HOOK 슬라이드면 연결자 검증 생략 (시작점)
- [ ] 비-HOOK 슬라이드면 헤드라인 또는 본문 첫 줄에 전환어/연결구 존재
- [ ] 전환어 카테고리: 대조(but/however/yet) / 추가(and/plus/also) / 인과(therefore/this is why) / 강조(why?/look) / 시간(then/now) / 결론(in short/bottom line) 중 하나
- [ ] CTA 슬라이드면 결론 카테고리 우선
- [ ] `narrative_connector` 필드가 Body Writer 또는 Title Writer 출력에 포함됨

### 🆕 버핏 등장 빈도 포스트-레벨 감사 (NEW v4.0)
- [ ] 포스트 전체 슬라이드 중 버핏 등장 비율 = 30%-50% 범위 (목표 ~40%)
- [ ] HOOK + CTA에 등장 (필수)
- [ ] 본문 등장 슬라이드 수 = 1-3개
- [ ] 등장 안 하는 슬라이드는 `buffett_role_classification = "not_present"` 명시
- [ ] 50% 초과 시 자동 경고 → 일부 슬라이드에서 버핏 제거 권장

### 🆕 의미 전달 우선 검증 (Meaning-First) (NEW v4.0)
- [ ] 헤드라인 ≤7 단어 (목표 2-5)
- [ ] 불릿 ≤7 단어 (목표 2-5)
- [ ] 문단 ≤14 단어 (목표 ≤12)
- [ ] 의미 손실·왜곡 없음 (간결성 추구로 의미가 망가지지 않음)

---

## 🧮 프롬프트 작성 절차 (v4.0)

```
1. text_to_render 수집 (Agents 6, 7에서):
   - headline, subtitle, body_blocks, labels, cta_line, acronym_glosses

2. styling_spec 수집 (Agents 6, 7, 9에서):
   - headline_style.font_character
   - body_style.font_character = "modern clean sans-serif, Roboto-like, ..."
   - subtitle_style.size_hint = "approximately 1.1x body"
   - background_spec.prompt_description_for_gemini

3. visual_elements 수집 (Agent 8):
   - 각 요소의 description_for_gemini (자연어)
   - 버핏 30% 규칙 자연어 묘사 포함

4. layout 수집 (Agent 10):
   - top_element (HOOK = spring+pencil, 비-HOOK = tape/pin/sticker)
   - zone_allocation
   - acronym_gloss_placements

5. 자연어 문단 작성 순서:
   a) 신 셋업: "Create a vertical 4:5 Instagram card news slide in scrapbook style..."
   b) 배경 묘사 (Agent 9의 prompt_description_for_gemini)
   c) 상단 소품 묘사 (HOOK = spring+pencil / 비-HOOK = 선택된 prop)
   c-2) 🆕 HOOK 전용 핸들 워터마크: spring 묘사 직후, 헤드라인 묘사 직전에 삽입.
        예시 문구: "Just below the spring binding, at the top center, render the literal lowercase text 'broisinvesting' as a very small, faded pencil-gray modern sans-serif watermark — roughly half the body text size, low contrast, slightly wider letter spacing, sitting clearly above the oversized headline so it never competes with the title or subject. No underline, no box, no @ prefix."
        ⚠️ 비-HOOK 슬라이드에서는 이 단계를 통째로 생략하고 프롬프트 어디에도 'broisinvesting' literal을 절대 포함하지 않는다.
   d) 헤드라인 지시 (literal 텍스트 인용 + "classic newspaper serif, large/oversized")
   e) 소제목 지시 (있으면 "modern sans-serif Roboto-like, about 1.1x body, moderately prominent")
   f) 본문 지시 (있으면 "modern clean sans-serif Roboto-like, medium weight, highly legible")
   g) 각 시각 요소 묘사 (v4.0: 버핏에 30% 규칙 명시)
   h) 약자 풀이 묘사 (있으면 "small muted-gray italic... reading: * ABC = Full Name")
   i) 레이아웃 지시 (여백 비율 등)
   j) Negative constraints (비-HOOK 슬라이드용 negative_prompt에는 "no 'broisinvesting' handle, no account watermark, no @-tag" 추가)

6. 누출 스캔:
   - `#` + 6 hex chars → FAIL
   - `px` 단위 → FAIL
   - `[cite`, `[1]`, `[source]` → FAIL
   - `{`, `}` JSON → FAIL
   - 'Roboto', 'Old Standard TT', 'Courier', 'Bold' as render text → FAIL
   - 🆕 슬라이드 역할 vs 'broisinvesting' literal 일치성:
       - slide_role == HOOK → 프롬프트에 정확히 1회 'broisinvesting' literal 포함 (워터마크 지시문 안). 0회 또는 2회+ → FAIL.
       - slide_role != HOOK → 프롬프트에 'broisinvesting' / 'bro is investing' / '@broisinvesting' 어떤 변형도 0회. 1회 이상 → FAIL.

7. v4.0 감사:
   - buffett_placement_v4 규칙 프롬프트 반영 확인
   - T-1 수치 맥락 주석 확인 (수치 슬라이드만)
   - 약자 풀이 별표 prefix 확인
   - 배치 메타데이터 삽입

8. 최종 JSON 조립
```

---

## 📤 출력 스키마 (슬라이드 JSON 최종)

```json
{
  "v": "4.0",
  "slide_number": "int",
  "total_slides": "int",
  "slide_role": "string",
  "theme": "string",
  "batch_metadata": {
    "batch_id": "int",
    "batch_type": "cover_solo | body_pair | body_solo_remainder | cta_with_pdf",
    "batch_size": "int",
    "position_in_batch": "int"
  },
  "research_provenance": {
    "data_sources_used": [],
    "data_freshness_attestation": {
      "t1_numbers_on_this_slide": "int",
      "indicator_releases_on_this_slide": "int",
      "reference_close_date": "YYYY-MM-DD",
      "source_tier_distribution": {"primary_gov": "int", "major_media": "int"}
    },
    "overall_research_quality": 0.0,
    "fact_checked": true
  },
  "image_generation_target": "gemini-2.5-flash-image",
  "output_specification": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350",
    "format": "PNG",
    "seed": 7842,
    "negative_prompt": "string (comprehensive anti-leakage)"
  },
  "cover_exclusive_tokens_applied": {},
  "text_to_render": {
    "headline": "string",
    "subtitle": "string | null",
    "body_blocks": [],
    "labels_on_visuals": [],
    "cta_line": "string | null",
    "acronym_glosses": [
      {"acronym": "FOMC", "gloss": "* FOMC = Federal Open Market Committee"}
    ]
  },
  "styling_spec": {
    "headline_style": {},
    "subtitle_style": {},
    "body_style": {},
    "acronym_gloss_style": {
      "font_character": "small muted-gray italic sans-serif",
      "size_hint": "approximately 0.5x body size, recessive margin footnote"
    }
  },
  "background_spec": {},
  "layout_spec": {
    "buffett_placement_v4": {}
  },
  "visual_elements": [],
  "gemini_prompt": "string (single natural-language paragraph)",
  "scrapbook_treatment": {},
  "reference_similarity": {},
  "quality_checklist_passed": {
    "master_prompt_complete": true,
    "leakage_scan_passed": true,
    "v4_buffett_size_rule_verified": true,
    "v4_buffett_frequency_post_level_verified": true,
    "v4_t1_data_attestation_present": true,
    "v4_acronym_gloss_format_valid": true,
    "v4_batch_metadata_set": true,
    "v4_narrative_connector_present": true,
    "v4_meaning_first_word_limits_respected": true,
    "cover_exclusive_tokens_correctly_applied": true,
    "v4_account_handle_watermark_hook_only": true
  }
}
```

---

## ⚠️ 절대 금지사항

1. gemini_prompt에 JSON 조각/hex/px 포함
2. `Roboto` 리터럴을 render text로 포함 (`Roboto-like` 힌트는 OK)
3. 버핏 mascot_corner인데 30% 규칙 누락
4. 수치가 들어간 슬라이드에서 attestation 누락
5. 약자 풀이에 별표 prefix 누락
6. binder_clip 언급 (deprecated)
7. 자체 창작 (Agent 11은 조립만, 새 콘텐츠 생성 금지)
8. 🆕 v4.0: 비-HOOK 슬라이드에서 `narrative_connector` 누락 통과 금지
9. 🆕 v4.0: 버핏 등장 빈도 50% 초과 통과 금지 (포스트 레벨 감사)
10. 🆕 v4.0: 헤드라인 8단어 이상 또는 불릿 8단어 이상 통과 금지 (의미 우선이라도 절대 상한 존재)
11. 🆕 HOOK 슬라이드에서 `broisinvesting` 핸들 워터마크 누락 통과 금지 (반드시 옅은 작은 글씨로 top_center 포함)
12. 🆕 비-HOOK 슬라이드에서 `broisinvesting` literal text(또는 변형/핸들/워터마크) 등장 통과 금지 — 발견 즉시 FAIL 처리하고 Agent 11이 자동 제거 후 재조립

---

## 💡 좋은 gemini_prompt 예시 (HOOK 슬라이드)

> "Create a vertical 4:5 Instagram card news slide in the style of a physical paper scrapbook made by a US economy influencer. This is the COVER slide of a series — it must look visually distinct and arresting compared to the later slides.
>
> Background: bright cream off-white notebook paper — brighter than a vintage cream — with ONLY horizontal ruled lines, soft faded blue-gray rules about 8mm apart. NO vertical lines. NO grid pattern. Just gentle horizontal lines like a school composition notebook. Subtle paper grain.
>
> Across the very top edge of the slide, render a full-width metal spiral-bound notebook binding — silver chrome coils evenly spaced — with exactly ONE yellow wooden pencil inserted diagonally through one of the coils, tip pointing down-left.
>
> Just below the spring binding, at the top center, render the literal lowercase text 'broisinvesting' as a very small, faded pencil-gray modern sans-serif watermark — roughly half the body text size, low contrast, slightly wider letter spacing, sitting clearly above the oversized headline so it never competes with the title or main subject. No underline, no box, no @ prefix. (HOOK slide only — never include this handle on any other slide.)
>
> At the top center (below the handle watermark with a comfortable gap), render the oversized hero headline: 'Forget The Bubble' — set in a classic bold newspaper serif typeface, deep black ink, extra large and dominant, taking up roughly a quarter of the slide height. Under the word 'Bubble' draw a hand-drawn red marker underline.
>
> No subtitle. No body text. This is a minimal cover.
>
> In the middle center, place a photorealistic cutout of Larry Fink (BlackRock CEO) — older man with glasses, dark suit — background removed, torn paper edge with tan-beige underlay. He is the sole focal human subject, large size.
>
> **In the bottom-left corner, place a photorealistic cutout of Warren Buffett with calm neutral expression — thin white hair, large glasses, gray suit — background removed, torn paper frame with beige underlay, slight -3° tilt. Render him at approximately 30% of the size of Larry Fink's cutout, clearly smaller as a corner mascot reaction character.**
>
> [... continuing with other elements, layout, whitespace, negative constraints ...]"
