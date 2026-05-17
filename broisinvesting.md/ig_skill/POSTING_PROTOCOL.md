# 📮 포스팅 트리거 프로토콜

> **Claude가 `포스팅 시작 [폴더명]` 메시지를 받았을 때 정확히 무엇을 해야 하는지 정의**

---

## 🎬 트리거 명령

```
포스팅 시작 [토픽폴더명]
```

### 예시
```
포스팅 시작 UNH
포스팅 시작 Trump & Coin
포스팅 시작 Peter_Lynch
```

### 옵션 플래그 (선택)
```
포스팅 시작 UNH --auto       # 캡션 미리보기 스킵, 바로 발행
포스팅 시작 UNH --dry-run    # Cloudinary 업로드까지만, 인스타 발행 X
포스팅 시작 UNH --quality=85 # JPEG 품질 조정 (기본 92)
```

기본은 **확인 모드** — 캡션 미리보기 후 사용자 yes 입력 필요.

---

## 🔄 Claude 실행 단계 (정확히 이 순서)

### Step 1. 폴더 검증
```python
folder = "/Users/dohyun/Desktop/개인 인스타/broisinvesting/{토픽폴더명}"
```
- 폴더 존재 확인 (Bash `ls`)
- 이미지 파일 (`.png`, `.jpg`, `.jpeg`, `.webp`) 개수 확인 → **2~10장** 범위인지 검증
- JSON 파일 (`slide_*.json`) 존재 확인

❌ 폴더 없음 / 이미지 없음 / 11장 이상 → 에러 보고 후 중단

### Step 2. 슬라이드 JSON 읽기
- 모든 `slide_*.json` 을 Read 툴로 읽기
- **이미지 PNG 자체는 절대 읽지 않음** (토큰 낭비)
- JSON 이 없으면 사용자에게 알림: "JSON 파일이 없어서 캡션 자동 생성 불가. 직접 캡션 입력해줄래?"

### Step 3. 캡션 생성
[14_caption_writer.md](../14_caption_writer.md) 룰 100% 준수:
- 슬라이드 내용 3문단 + Comment 1문단 (영어)
- `.` 구분자 (문단 사이 1개, Comment ↔ 해시태그 사이 4개)
- 해시태그 5개 (`#broisinvesting` + 4개)

### Step 4. 미리보기 (확인 모드일 때만)
```
📝 생성된 캡션:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[캡션 전문 출력]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 메타정보:
  - 슬라이드: {N}장
  - 해시태그: 5개 ({태그1}, {태그2}, ...)
  - 캡션 길이: {len}자

👉 진행할까?
  ✅ yes → 인스타 발행
  ✏️ 수정 [지시사항] → 재생성 (예: "수정 Para 1을 더 강하게")
  ❌ 취소
```

→ 사용자 응답 대기. **절대 자동 진행 금지** (`--auto` 플래그 없는 한).

### Step 5. 발행 실행
사용자 `yes` 응답 시 Bash 실행:

```bash
cd "사용중/ig_skill"
set -a && source .env && set +a
python3 scripts/post_workflow.py \
  --folder "/Users/dohyun/Desktop/개인 인스타/broisinvesting/UNH" \
  --caption "$(cat <<'CAPTION_EOF'
[Para 1]
.
[Para 2]
.
[Para 3]
.
Comment "..." below ↓
.
.
.
.
#broisinvesting #stocks #valueinvesting #unitedhealth #warrenbuffett
CAPTION_EOF
)"
```

> ⚠️ 캡션은 반드시 HEREDOC 으로 전달 — `.` 줄바꿈 보존 필요

### Step 6. 결과 보고
post_workflow.py 의 출력 (JSON) 을 파싱해서 사용자에게:

```
✅ 포스팅 완료!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📍 미디어 ID: 17891234567890
  🔗 URL: https://www.instagram.com/p/CxYz123abc/
  🖼  슬라이드: 8장
  ⏱  총 소요: 38.2초
  💾 로그 저장: UNH/post_log.json
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 7. 실패 시 처리
- Cloudinary 실패 → 원인 보고 (예: API 키 오류, 이미지 손상)
- Graph API 실패 → 에러 코드 보고 + 흔한 원인 매핑:
  - `Invalid OAuth access token` → 토큰 만료, SETUP_GUIDE 4-B 재실행 안내
  - `(#36003) Service temporarily unavailable` → 5분 후 재시도 안내
  - `Media type not supported` → 이미지 손상 가능, 재생성 안내

---

## 🎯 사용자 응답 처리 룰

| 사용자 응답 | Claude 동작 |
|-----------|-----------|
| `yes`, `ㅇ`, `ㄱㄱ`, `진행` | Step 5 실행 |
| `cancel`, `취소`, `ㄴ` | 작업 중단 보고 |
| `수정 [지시]` | Step 3 재실행 (지시사항 반영) → Step 4 재미리보기 |
| `--auto` 추가 | 다음 미리보기 스킵 (해당 트리거에 한함) |
| 응답 없이 다른 메시지 | 포스팅 컨텍스트 일시 보류, 새 메시지 우선 처리. 사용자가 "위 캡션 진행" 같이 명시하면 재개 |

---

## 🔐 보안 / 안전 룰

1. **토큰 노출 금지**: `.env` 내용을 사용자에게 출력 금지. 디버깅 시에도 토큰 마스킹 (`EAA****`).
2. **재발행 방지**: 같은 폴더에 `post_log.json`이 있고 24시간 이내면 사용자에게 "이미 발행된 폴더야. 재발행할까?" 확인.
3. **Rate limit 사전 체크**: 발행 전 `publishing_limit` 명령으로 잔여 횟수 확인. 0이면 중단.
4. **이미지 손상 검증**: `upload_cloudinary.py` 가 0바이트 파일은 자동 거부. 발생 시 사용자에게 알림.

---

## 📁 폴더 구조 (포스팅 후)

```
broisinvesting/UNH/
├── 1.png ~ 8.png             ← 원본 이미지
├── slide_01.json ~ slide_08.json  ← 슬라이드 스펙 (절대 삭제 금지)
├── manifest.json             ← v4.1 매니페스트
└── post_log.json             ← 🆕 포스팅 로그 (자동 생성)
```

`post_log.json` 예시:
```json
[
  {
    "started_at": "2026-05-02T14:32:11",
    "completed_at": "2026-05-02T14:32:49",
    "image_count": 8,
    "instagram_media_id": "17891234567890",
    "permalink": "https://www.instagram.com/p/CxYz/",
    "caption_preview": "UnitedHealth lost 18%...",
    "caption_length": 487,
    "duration_seconds": 38.2
  }
]
```

---

## ⚠️ Claude 절대 금지사항

1. 사용자 yes 응답 없이 발행 (--auto 플래그 없는 한)
2. 캡션 생성 시 슬라이드 PNG 이미지 분석 (JSON만 사용)
3. 해시태그 5개 룰 위반
4. `.env` 내용을 채팅창에 출력
5. `slide_*.json` 파일 삭제
6. 24시간 내 같은 폴더 재발행을 사용자 확인 없이 진행
7. Rate limit 잔여 0인 상태에서 발행 시도
