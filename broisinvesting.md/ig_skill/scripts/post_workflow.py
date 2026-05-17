#!/usr/bin/env python3
"""인스타 포스팅 전체 오케스트레이션.

흐름:
    1. 토픽 폴더에서 이미지 수집 (1.png~N.png)
    2. PNG→JPG 변환 + Cloudinary 업로드 → 공개 URL 획득
    3. ig_api.py publish_carousel 호출 → 인스타 발행
    4. (선택) Cloudinary 이미지 삭제
    5. 결과 JSON 출력 + 포스팅 로그 저장

사용:
    set -a && source .env && set +a
    python3 scripts/post_workflow.py \
        --folder "/path/to/UNH" \
        --caption "$(cat caption.txt)"

캡션은 Claude가 생성한 텍스트를 인자로 전달.
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def check_env():
    required = [
        "INSTAGRAM_ACCESS_TOKEN",
        "INSTAGRAM_BUSINESS_ACCOUNT_ID",
        "CLOUDINARY_CLOUD_NAME",
        "CLOUDINARY_API_KEY",
        "CLOUDINARY_API_SECRET",
    ]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        print(f"Error: missing env vars: {', '.join(missing)}", file=sys.stderr)
        print("Run: set -a && source .env && set +a", file=sys.stderr)
        sys.exit(1)


def upload_images(folder: Path):
    """upload_cloudinary.py 호출. URL 리스트 + public_id 리스트 반환."""
    cmd = [
        sys.executable,
        str(SCRIPT_DIR / "upload_cloudinary.py"),
        "--folder", str(folder),
        "--json",
    ]
    print(f"☁️  Cloudinary 업로드 중... ({folder.name})", file=sys.stderr)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stderr, file=sys.stderr)
        sys.exit(1)
    # stderr 는 진행 로그, stdout 은 최종 JSON
    if proc.stderr:
        sys.stderr.write(proc.stderr)
    data = json.loads(proc.stdout)
    return data["urls"], data["public_ids"]


def publish_carousel(media_urls, caption):
    """ig_api.py publish_carousel 호출."""
    cmd = [
        sys.executable,
        str(SCRIPT_DIR / "ig_api.py"),
        "publish_carousel",
        "--media-urls", ",".join(media_urls),
        "--caption", caption,
    ]
    print(f"📤 Instagram Graph API 발행 중... ({len(media_urls)}장)", file=sys.stderr)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.stderr:
        sys.stderr.write(proc.stderr)
    if proc.returncode != 0:
        print(f"❌ 발행 실패. stdout:\n{proc.stdout}", file=sys.stderr)
        sys.exit(1)
    # ig_api.py 는 마지막에 JSON을 출력하지만 진행 로그도 stdout으로 섞임
    # 마지막 JSON 블록만 파싱
    output = proc.stdout.strip()
    last_brace = output.rfind("{")
    if last_brace == -1:
        print(f"❌ JSON 응답 없음:\n{output}", file=sys.stderr)
        sys.exit(1)
    try:
        publish_result = json.loads(output[last_brace:])
    except json.JSONDecodeError:
        publish_result = {"raw_output": output}
    return publish_result, output


def get_permalink(media_id):
    """발행된 미디어 permalink 조회."""
    cmd = [
        sys.executable,
        str(SCRIPT_DIR / "ig_api.py"),
        "get_media",
        "--limit", "5",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    try:
        data = json.loads(proc.stdout)
        for item in data.get("data", []):
            if item.get("id") == media_id:
                return item.get("permalink")
    except json.JSONDecodeError:
        pass
    return None


def cleanup_cloudinary(public_ids):
    """포스팅 후 Cloudinary 이미지 삭제 (옵션)."""
    if os.environ.get("CLOUDINARY_AUTO_DELETE", "false").lower() != "true":
        return
    try:
        import cloudinary
        import cloudinary.uploader
        cloudinary.config(
            cloud_name=os.environ["CLOUDINARY_CLOUD_NAME"],
            api_key=os.environ["CLOUDINARY_API_KEY"],
            api_secret=os.environ["CLOUDINARY_API_SECRET"],
            secure=True,
        )
        for pid in public_ids:
            cloudinary.uploader.destroy(pid)
        print(f"🗑  Cloudinary {len(public_ids)}장 삭제 완료", file=sys.stderr)
    except Exception as e:
        print(f"⚠️  Cloudinary 삭제 실패 (무시): {e}", file=sys.stderr)


def save_log(folder: Path, log_data: dict):
    """포스팅 로그를 토픽 폴더에 저장."""
    log_path = folder / "post_log.json"
    existing = []
    if log_path.exists():
        try:
            existing = json.loads(log_path.read_text())
            if not isinstance(existing, list):
                existing = [existing]
        except json.JSONDecodeError:
            existing = []
    existing.append(log_data)
    log_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Instagram carousel posting orchestrator")
    parser.add_argument("--folder", required=True, help="Topic folder with N.png images")
    parser.add_argument("--caption", required=True, help="Full caption text (English + hashtags)")
    parser.add_argument("--dry-run", action="store_true", help="Upload to Cloudinary but skip IG publish")
    args = parser.parse_args()

    check_env()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.is_dir():
        print(f"Error: folder not found: {folder}", file=sys.stderr)
        sys.exit(1)

    started = time.time()
    log = {
        "folder": str(folder),
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "caption_preview": args.caption[:200],
        "caption_length": len(args.caption),
    }

    # 1. Upload
    urls, public_ids = upload_images(folder)
    log["cloudinary_urls"] = urls
    log["cloudinary_public_ids"] = public_ids
    log["image_count"] = len(urls)

    if args.dry_run:
        print("🟡 dry-run 모드 — 인스타 발행 스킵", file=sys.stderr)
        print(json.dumps({"dry_run": True, "urls": urls}, indent=2))
        return

    # 2. Publish
    publish_result, raw_output = publish_carousel(urls, args.caption)
    media_id = publish_result.get("id")
    log["instagram_media_id"] = media_id
    log["raw_publish_output"] = raw_output[-2000:]

    # 3. Permalink (발행 직후엔 잠시 후에야 조회 가능 — 1초 대기)
    permalink = None
    if media_id:
        time.sleep(2)
        permalink = get_permalink(media_id)
    log["permalink"] = permalink

    # 4. Cleanup (옵션)
    cleanup_cloudinary(public_ids)

    log["completed_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    log["duration_seconds"] = round(time.time() - started, 1)

    save_log(folder, log)

    print(json.dumps({
        "status": "success",
        "media_id": media_id,
        "permalink": permalink,
        "image_count": len(urls),
        "duration_seconds": log["duration_seconds"],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
