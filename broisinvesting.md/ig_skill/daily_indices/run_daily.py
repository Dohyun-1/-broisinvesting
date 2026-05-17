#!/usr/bin/env python3
"""Daily indices story workflow.

1. Fetch live intraday data for S&P 500, NASDAQ, Dow Jones
2. Render brand-style 1080x1920 story image
3. Upload to Cloudinary → public URL
4. Publish as Instagram Story via Graph API

Usage:
    set -a && source ../.env && set +a
    python3 run_daily.py                  # full run
    python3 run_daily.py --dry-run        # render + upload, but skip IG publish
    python3 run_daily.py --skip-upload    # render only
"""

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
SCRIPTS = HERE.parent / "scripts"


def require_env(*keys):
    missing = [k for k in keys if not os.environ.get(k)]
    if missing:
        sys.stderr.write(f"Missing env vars: {', '.join(missing)}\n")
        sys.stderr.write("Run: set -a && source ../.env && set +a\n")
        sys.exit(1)


def fetch_and_render(style="brand"):
    sys.path.insert(0, str(HERE))
    from fetch_data import fetch_all
    from render_story import render_brand, render_yahoo

    data = fetch_all()
    out_dir = HERE / "out"
    out_dir.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    path = out_dir / f"story_{style}_{stamp}.jpg"

    if style == "brand":
        render_brand(data, path)
    else:
        render_yahoo(data, path)

    print(f"[render] {path}", file=sys.stderr)
    return path, data


def upload_to_cloudinary(file_path: Path):
    import cloudinary
    import cloudinary.uploader

    cloudinary.config(
        cloud_name=os.environ["CLOUDINARY_CLOUD_NAME"],
        api_key=os.environ["CLOUDINARY_API_KEY"],
        api_secret=os.environ["CLOUDINARY_API_SECRET"],
        secure=True,
    )
    public_id = f"daily_indices_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    result = cloudinary.uploader.upload(
        str(file_path),
        public_id=public_id,
        resource_type="image",
        overwrite=True,
        folder="broisinvesting/stories",
    )
    url = result["secure_url"]
    print(f"[upload] {url}", file=sys.stderr)
    return url


def publish_story(image_url: str):
    """Call ig_api.py publish_story via subprocess so the existing logic is reused."""
    ig_api = SCRIPTS / "ig_api.py"
    cmd = ["python3", str(ig_api), "publish_story", "--image-url", image_url]
    print(f"[publish] {' '.join(cmd)}", file=sys.stderr)
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        sys.stderr.write(res.stderr)
        sys.exit(res.returncode)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", choices=["brand", "yahoo"], default="brand")
    ap.add_argument("--dry-run", action="store_true", help="render + upload, skip publish")
    ap.add_argument("--skip-upload", action="store_true", help="render only")
    args = ap.parse_args()

    if not args.skip_upload:
        require_env("CLOUDINARY_CLOUD_NAME", "CLOUDINARY_API_KEY", "CLOUDINARY_API_SECRET")
    if not args.dry_run and not args.skip_upload:
        require_env("INSTAGRAM_ACCESS_TOKEN", "INSTAGRAM_BUSINESS_ACCOUNT_ID")

    path, _ = fetch_and_render(args.style)
    if args.skip_upload:
        return

    url = upload_to_cloudinary(path)
    if args.dry_run:
        print(json.dumps({"image_url": url, "local_path": str(path)}, indent=2))
        return

    publish_story(url)


if __name__ == "__main__":
    main()
