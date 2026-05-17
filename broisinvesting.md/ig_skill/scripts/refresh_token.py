#!/usr/bin/env python3
"""Instagram Long-lived Access Token 자동 갱신 스크립트.

작동:
    1. 현재 토큰의 만료까지 남은 일수 확인 (debug_token API)
    2. 만료까지 7일 이내면 자동 갱신
    3. 새 토큰을 .env 파일에 업데이트
    4. 결과를 token_refresh.log 에 기록
    5. 실패 시 macOS 알림 발송

사용:
    수동 실행:    python3 refresh_token.py
    강제 갱신:    python3 refresh_token.py --force
    상태 확인만:  python3 refresh_token.py --check
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ENV_PATH = SKILL_DIR / ".env"
LOG_PATH = SKILL_DIR / "token_refresh.log"
GRAPH_API_VERSION = "v25.0"
REFRESH_THRESHOLD_DAYS = 7  # 7일 이내 만료면 갱신


def log(msg, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{level}] {msg}"
    print(line, file=sys.stderr)
    with LOG_PATH.open("a") as f:
        f.write(line + "\n")


def load_env():
    if not ENV_PATH.exists():
        log(f".env not found at {ENV_PATH}", "ERROR")
        sys.exit(1)
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def update_env_token(new_token: str):
    """원본 .env 파일에서 INSTAGRAM_ACCESS_TOKEN 줄만 교체."""
    text = ENV_PATH.read_text()
    new_text = re.sub(
        r"^INSTAGRAM_ACCESS_TOKEN=.*$",
        f"INSTAGRAM_ACCESS_TOKEN={new_token}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if new_text == text:
        log("WARNING: INSTAGRAM_ACCESS_TOKEN line not found in .env — appending", "WARN")
        new_text = text.rstrip() + f"\nINSTAGRAM_ACCESS_TOKEN={new_token}\n"
    ENV_PATH.write_text(new_text)


def http_get(url, params):
    qs = urllib.parse.urlencode(params)
    full = f"{url}?{qs}"
    req = urllib.request.Request(full, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            err = json.loads(body)
        except json.JSONDecodeError:
            err = {"raw": body}
        raise RuntimeError(f"HTTP {e.code}: {json.dumps(err)}")


def check_token_expiry(token: str, app_id: str, app_secret: str):
    """debug_token API 로 토큰 만료 시각 조회. 남은 일수 반환.

    주의: Facebook 장기 토큰은 expires_at=0 (로그인 자체 만료는 없음) 이지만
    data_access_expires_at 가 있으면 그 시점부터 사용자 데이터 API 호출 거부됨.
    실질 만료는 data_access_expires_at 로 판단.
    """
    result = http_get(
        f"https://graph.facebook.com/debug_token",
        {
            "input_token": token,
            "access_token": f"{app_id}|{app_secret}",
        },
    )
    data = result.get("data", {})
    if not data.get("is_valid"):
        raise RuntimeError(f"Token is invalid: {data.get('error', {}).get('message', 'unknown')}")

    expires_at = data.get("expires_at") or 0
    data_expires_at = data.get("data_access_expires_at") or 0

    # 실질 만료 = expires_at 와 data_access_expires_at 중 더 빠른 것 (0 제외)
    candidates = [t for t in (expires_at, data_expires_at) if t > 0]
    if not candidates:
        return float("inf"), None
    effective_expiry = min(candidates)
    expiry_dt = datetime.fromtimestamp(effective_expiry)
    days_left = (expiry_dt - datetime.now()).total_seconds() / 86400
    return days_left, expiry_dt


def refresh_token(current_token: str, app_id: str, app_secret: str):
    """단기/장기 토큰을 새 60일 장기 토큰으로 교환."""
    result = http_get(
        f"https://graph.facebook.com/{GRAPH_API_VERSION}/oauth/access_token",
        {
            "grant_type": "fb_exchange_token",
            "client_id": app_id,
            "client_secret": app_secret,
            "fb_exchange_token": current_token,
        },
    )
    new_token = result.get("access_token")
    expires_in = result.get("expires_in")
    if not new_token:
        raise RuntimeError(f"No access_token in refresh response: {json.dumps(result)}")
    return new_token, expires_in


def notify_macos(title: str, message: str):
    """macOS 알림 센터로 푸시."""
    try:
        subprocess.run(
            [
                "osascript",
                "-e",
                f'display notification "{message}" with title "{title}"',
            ],
            check=False,
            timeout=5,
        )
    except Exception:
        pass  # 알림 실패는 무시


def main():
    parser = argparse.ArgumentParser(description="Auto-refresh Instagram long-lived token")
    parser.add_argument("--force", action="store_true", help="만료 일수 무관하게 강제 갱신")
    parser.add_argument("--check", action="store_true", help="갱신 안 하고 만료 시각만 출력")
    args = parser.parse_args()

    env = load_env()
    token = env.get("INSTAGRAM_ACCESS_TOKEN")
    app_id = env.get("META_APP_ID")
    app_secret = env.get("META_APP_SECRET")

    if not all([token, app_id, app_secret]):
        log("Missing required env vars: INSTAGRAM_ACCESS_TOKEN, META_APP_ID, META_APP_SECRET", "ERROR")
        notify_macos("IG 토큰 갱신 실패", ".env 자격증명 누락")
        sys.exit(1)

    # 1. 만료 확인
    try:
        days_left, expiry_dt = check_token_expiry(token, app_id, app_secret)
    except Exception as e:
        log(f"Token check failed: {e}", "ERROR")
        notify_macos("IG 토큰 상태 확인 실패", str(e)[:100])
        sys.exit(1)

    if expiry_dt:
        log(f"Token expires at {expiry_dt.strftime('%Y-%m-%d %H:%M')} ({days_left:.1f} days left)")
    else:
        log("Token never expires (likely a page token)")
        if not args.force:
            log("No refresh needed. Exit.")
            return

    if args.check:
        return

    # 2. 갱신 필요 판단
    if not args.force and days_left > REFRESH_THRESHOLD_DAYS:
        log(f"No refresh needed (>{REFRESH_THRESHOLD_DAYS} days remain). Exit.")
        return

    log(f"Refreshing token (force={args.force}, days_left={days_left:.1f})")

    # 3. 갱신 실행
    try:
        new_token, expires_in = refresh_token(token, app_id, app_secret)
    except Exception as e:
        log(f"Refresh FAILED: {e}", "ERROR")
        notify_macos(
            "IG 토큰 갱신 실패",
            f"수동 갱신 필요. 로그: {LOG_PATH.name}",
        )
        sys.exit(1)

    # 4. .env 업데이트
    update_env_token(new_token)
    new_expiry = datetime.now() + timedelta(seconds=expires_in or 0)
    log(f"Refreshed. New token expires {new_expiry.strftime('%Y-%m-%d %H:%M')} ({(expires_in or 0)/86400:.1f} days)")
    log(f"Updated {ENV_PATH}")
    notify_macos(
        "IG 토큰 갱신 완료",
        f"새 토큰: {(expires_in or 0)/86400:.0f}일 유효",
    )


if __name__ == "__main__":
    main()
