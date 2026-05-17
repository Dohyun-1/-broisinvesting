# 🚀 인스타 포스팅 자동화 — 셋업 가이드

> **목표**: 1회성 셋업 후 `포스팅 시작 [폴더명]` 한 줄로 인스타 캐러셀 포스팅
> **소요 시간**: 약 30~60분 (대부분 페이스북/인스타 검토 대기 시간)

---

## 📋 셋업 체크리스트 (순서 중요)

- [ ] 1. 인스타 계정을 **비즈니스 또는 크리에이터** 계정으로 전환
- [ ] 2. **페이스북 페이지** 생성 및 인스타 계정과 연결
- [ ] 3. **Meta for Developers** 가입 + 앱 생성
- [ ] 4. **Long-lived Access Token** 발급
- [ ] 5. **Instagram Business Account ID** 확인
- [ ] 6. **Cloudinary** 무료 가입 + API 키 받기
- [ ] 7. `.env` 파일 작성
- [ ] 8. 테스트 실행

---

## 1️⃣ 인스타 계정 전환 (이미 했으면 스킵)

1. 인스타 앱 → 프로필 → 메뉴 → **설정 및 개인정보**
2. **계정 유형 및 도구** → **프로페셔널 계정으로 전환**
3. 카테고리 선택 (예: "투자/금융")
4. **비즈니스** 또는 **크리에이터** 중 하나 선택 (둘 다 Graph API 사용 가능)

> ⚠️ 개인 계정으로는 Graph API 포스팅 불가능

---

## 2️⃣ 페이스북 페이지 연결

Graph API는 인스타 계정이 페이스북 페이지에 연결돼 있어야 작동.

### 2-A. 페이스북 페이지 생성 (없으면)
1. [facebook.com/pages/create](https://www.facebook.com/pages/create) 접속
2. 페이지 이름 (예: "Bro is Investing") + 카테고리 선택
3. 생성 완료

### 2-B. 인스타 계정에 페이지 연결
1. 인스타 앱 → 프로필 편집 → **페이지** 항목
2. 위에서 만든 페이스북 페이지 선택 → 연결

---

## 3️⃣ Meta for Developers 앱 생성

1. [developers.facebook.com](https://developers.facebook.com/) 접속 → 페이스북 계정으로 로그인
2. 우측 상단 **My Apps** → **Create App**
3. **Use Case**: "Other" 선택 → Next
4. **App Type**: **Business** 선택 → Next
5. App 이름 입력 (예: "broisinvesting-poster") → Create App

### 3-A. Instagram 제품 추가
1. 좌측 사이드바 → **Add Product**
2. **Instagram** 카드 → **Set up** 클릭
3. **Instagram Graph API** 선택

### 3-B. 권한 설정
앱 대시보드 → **App Review → Permissions and Features** 에서 다음 권한 신청:

| 권한 | 용도 |
|------|------|
| `instagram_basic` | 프로필 정보 |
| `instagram_content_publish` | **포스팅 (필수)** |
| `pages_show_list` | 연결된 페이지 목록 |
| `pages_read_engagement` | 페이지 정보 읽기 |
| `business_management` | 비즈니스 자산 관리 |

> ⚠️ 처음에는 **Development Mode**라 본인 계정만 사용 가능. 우리는 본인이 본인 계정에 포스팅하는 거니까 **Live 모드 신청 불필요**.

---

## 4️⃣ Access Token 발급 (60일 유효)

### 4-A. 단기 토큰 발급
1. [developers.facebook.com/tools/explorer](https://developers.facebook.com/tools/explorer) (Graph API Explorer)
2. 우측 **Meta App** 드롭다운 → 위에서 만든 앱 선택
3. **User or Page** → "Get User Access Token" 선택
4. 권한 체크박스에서 위 5개 권한 선택
5. **Generate Access Token** 클릭 → 페이스북 계정으로 인증
6. 발급된 토큰 복사 (1시간만 유효 — 다음 단계에서 60일 토큰으로 교환)

### 4-B. 장기 토큰으로 교환
터미널에서:
```bash
curl -i -X GET "https://graph.facebook.com/v25.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={SHORT_TOKEN}"
```

값 치환:
- `{APP_ID}`: 앱 대시보드 → Settings → Basic → App ID
- `{APP_SECRET}`: 같은 곳에서 App Secret 보기
- `{SHORT_TOKEN}`: 4-A에서 복사한 토큰

응답:
```json
{"access_token": "EAAxxxxx...", "token_type": "bearer", "expires_in": 5183999}
```

→ 이 `access_token`이 **Long-lived Token** (60일). `.env`에 저장.

> 💡 60일 후 만료되니까 갱신 필요. 만료 직전 같은 명령으로 재발급 가능.

---

## 5️⃣ Instagram Business Account ID 확인

페이지 ID 찾기:
```bash
curl -i -X GET "https://graph.facebook.com/v25.0/me/accounts?access_token={LONG_TOKEN}"
```

→ 응답에서 `id` 값이 페이지 ID. 그 ID로 인스타 계정 ID 조회:
```bash
curl -i -X GET "https://graph.facebook.com/v25.0/{PAGE_ID}?fields=instagram_business_account&access_token={LONG_TOKEN}"
```

→ 응답의 `instagram_business_account.id` 가 **INSTAGRAM_BUSINESS_ACCOUNT_ID**.

---

## 6️⃣ Cloudinary 가입 (이미지 호스팅)

Graph API는 공개 URL 이미지만 받음. Cloudinary가 무료로 호스팅해줌.

1. [cloudinary.com/users/register/free](https://cloudinary.com/users/register/free) 가입
2. 로그인 후 **Dashboard** → 우측 상단 "API Keys" 영역
3. 다음 3개 값 복사:
   - **Cloud Name**
   - **API Key**
   - **API Secret**

> 무료 플랜: 월 25 credits (약 25GB 스토리지/대역폭) — 개인 인스타 포스팅엔 충분.

---

## 7️⃣ .env 파일 작성

`사용중/ig_skill/.env` 파일 생성:
```bash
INSTAGRAM_ACCESS_TOKEN=EAAxxxxx_여기에_60일_토큰
INSTAGRAM_BUSINESS_ACCOUNT_ID=17841xxxxx_여기에_IG_계정_ID

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=abcdef_여기에_시크릿
```

**`.env`는 절대 git에 커밋하지 마**. (이미 `.gitignore` 설정 권장)

---

## 8️⃣ 테스트

### 8-A. 토큰 유효성 확인
```bash
cd "사용중/ig_skill"
set -a && source .env && set +a
python3 scripts/ig_api.py validate_token
```

✅ JSON 응답 + `id` 필드 보이면 정상.

### 8-B. 프로필 정보 조회
```bash
python3 scripts/ig_api.py get_profile
```

✅ 본인 인스타 username, follower 수 등이 보이면 정상.

### 8-C. 발행 가능 횟수 확인
```bash
python3 scripts/ig_api.py publishing_limit
```

✅ `quota_usage: 0`, `config.quota_total: 100` 보이면 정상.

---

## ✅ 셋업 완료 후

이제 `포스팅 시작 [토픽폴더명]` 한 줄이면 자동 포스팅 가능.

자세한 동작은 [POSTING_PROTOCOL.md](POSTING_PROTOCOL.md) 참고.

---

## 🆘 트러블슈팅

| 에러 | 원인 | 해결 |
|------|------|------|
| `Invalid OAuth access token` | 토큰 만료 또는 오타 | 4-B 단계 재실행 |
| `(#10) Application does not have permission` | 권한 미허용 | 3-B 권한 재신청 |
| `Media type not supported` | PNG 업로드 시도 | post_workflow가 자동 JPG 변환함 — 그래도 발생 시 이미지 손상 의심 |
| `(#36003) Service temporarily unavailable` | 인스타 서버 일시 오류 | 5분 대기 후 재시도 |
| Container `ERROR` 상태 | 이미지 URL 접근 불가 | Cloudinary 업로드 성공 여부 확인 |

---

## 📌 참고 문서

- [공식 Instagram Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing)
- [Long-Lived Token 갱신](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/long-lived-access-tokens)
- [Cloudinary Python SDK](https://cloudinary.com/documentation/python_quickstart)
