#!/usr/bin/env python3
"""Cloudinary 업로드 + PNG→JPG 변환.

사용:
    python3 upload_cloudinary.py --folder /path/to/topic_folder
    → 폴더의 1.png ~ N.png 를 정렬해서 JPG 변환 + 업로드
    → stdout 에 콤마 구분 URL 출력 (publish_carousel 입력 형식)

요구 패키지:
    pip install cloudinary Pillow
"""

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path


def natural_sort_key(path: Path):
    """1.png, 2.png, ..., 10.png 순서로 정렬 (10이 2 앞에 오면 안 됨)."""
    parts = re.split(r"(\d+)", path.stem)
    return [int(p) if p.isdigit() else p for p in parts]


def collect_images(folder: Path):
    """폴더에서 이미지 파일 수집 (.png, .jpg, .jpeg). 자연 정렬."""
    exts = {".png", ".jpg", ".jpeg", ".webp"}
    images = [f for f in folder.iterdir() if f.is_file() and f.suffix.lower() in exts]
    images.sort(key=natural_sort_key)
    return images


def convert_to_jpeg(src: Path, dst: Path, quality=92):
    """PNG/WebP → JPEG. 알파 채널은 흰 배경으로 합성."""
    from PIL import Image

    img = Image.open(src)
    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")
    img.save(dst, "JPEG", quality=quality, optimize=True)


def upload_to_cloudinary(file_path: Path, public_id: str):
    """단일 파일 Cloudinary 업로드. secure_url 반환."""
    import cloudinary
    import cloudinary.uploader

    cloudinary.config(
        cloud_name=os.environ["CLOUDINARY_CLOUD_NAME"],
        api_key=os.environ["CLOUDINARY_API_KEY"],
        api_secret=os.environ["CLOUDINARY_API_SECRET"],
        secure=True,
    )

    result = cloudinary.uploader.upload(
        str(file_path),
        public_id=public_id,
        resource_type="image",
        overwrite=True,
        folder="broisinvesting",
    )
    return result["secure_url"], result["public_id"]


def check_env():
    required = ["CLOUDINARY_CLOUD_NAME", "CLOUDINARY_API_KEY", "CLOUDINARY_API_SECRET"]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        print(f"Error: missing env vars: {', '.join(missing)}", file=sys.stderr)
        print("Run: set -a && source .env && set +a", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Convert PNG→JPG and upload to Cloudinary")
    parser.add_argument("--folder", required=True, help="Topic folder containing 1.png ~ N.png")
    parser.add_argument("--prefix", default=None, help="public_id prefix (default: folder name)")
    parser.add_argument("--quality", type=int, default=92, help="JPEG quality (default 92)")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of comma-separated URLs")
    args = parser.parse_args()

    check_env()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.is_dir():
        print(f"Error: folder not found: {folder}", file=sys.stderr)
        sys.exit(1)

    images = collect_images(folder)
    if len(images) < 2:
        print(f"Error: carousel requires 2+ images, found {len(images)} in {folder}", file=sys.stderr)
        sys.exit(1)
    if len(images) > 10:
        print(f"Error: carousel max 10 images, found {len(images)} in {folder}", file=sys.stderr)
        sys.exit(1)

    prefix = args.prefix or folder.name.replace(" ", "_").replace("&", "and")
    timestamp = __import__("time").strftime("%Y%m%d_%H%M%S")

    urls = []
    public_ids = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        for i, src in enumerate(images, 1):
            print(f"[{i}/{len(images)}] {src.name}", file=sys.stderr)

            if src.suffix.lower() == ".jpg" or src.suffix.lower() == ".jpeg":
                upload_src = src
            else:
                jpg_path = tmp_path / f"{src.stem}.jpg"
                convert_to_jpeg(src, jpg_path, quality=args.quality)
                upload_src = jpg_path
                print(f"      converted to JPEG ({jpg_path.stat().st_size // 1024} KB)", file=sys.stderr)

            public_id = f"{prefix}_{timestamp}_{i:02d}"
            url, full_public_id = upload_to_cloudinary(upload_src, public_id)
            print(f"      → {url}", file=sys.stderr)
            urls.append(url)
            public_ids.append(full_public_id)

    if args.json:
        print(json.dumps({"urls": urls, "public_ids": public_ids, "count": len(urls)}, indent=2))
    else:
        print(",".join(urls))


if __name__ == "__main__":
    main()
