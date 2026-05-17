#!/usr/bin/env python3
"""Render daily-indices Instagram Story image (1080x1920).

Layout (top → bottom): S&P 500, NASDAQ, DOW JONES.
Two styles available:
    yahoo  — dark Yahoo-Finance-style minimal
    brand  — broisinvesting dark_neon DNA (chromatic glow, gold accents)
"""

import argparse
import datetime as dt
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

CANVAS = (1080, 1920)
SAFE_TOP = 240        # avoid IG header / camera notch
SAFE_BOTTOM = 230     # avoid IG reply UI
PANEL_GAP = 24
PANEL_COUNT = 5
SAFE_ZONE_SCALE = 0.90  # shrink content to 90% so edges aren't clipped by IG UI

HELV = "/System/Library/Fonts/HelveticaNeue.ttc"
HELV_BOLD = "/System/Library/Fonts/HelveticaNeue.ttc"


def font(size, weight="regular"):
    # HelveticaNeue.ttc face indices: 0 regular, 1 bold, 2 italic, 3 bold italic
    idx = 1 if weight == "bold" else 0
    return ImageFont.truetype(HELV, size, index=idx)


def fmt_price(p):
    return f"{p:,.2f}"


def fmt_change(c, pct):
    sign = "+" if c >= 0 else "-"
    return f"{sign}{abs(c):,.2f} ({sign}{abs(pct):.2f}%)"


def panel_height():
    return (CANVAS[1] - SAFE_TOP - SAFE_BOTTOM - (PANEL_COUNT - 1) * PANEL_GAP) // PANEL_COUNT


def _apply_safe_zone(img, scale=SAFE_ZONE_SCALE, bg=(0, 0, 0)):
    """Scale rendered content and center it on a fresh canvas so IG UI doesn't clip edges."""
    w, h = img.size
    new_w, new_h = int(w * scale), int(h * scale)
    scaled = img.resize((new_w, new_h), Image.LANCZOS)
    canvas = Image.new("RGB", (w, h), bg)
    canvas.paste(scaled, ((w - new_w) // 2, (h - new_h) // 2))
    return canvas


def draw_sparkline(panel, series, color, fill_color=None, width=4, padding=(40, 30)):
    """Draw a sparkline onto `panel` (PIL.Image) using the series of (ts, close)."""
    if len(series) < 2:
        return
    pw, ph = panel.size
    px, py = padding
    inner_w = pw - 2 * px
    inner_h = ph - 2 * py

    closes = [c for _, c in series]
    lo, hi = min(closes), max(closes)
    rng = (hi - lo) or 1e-9

    points = []
    for i, c in enumerate(closes):
        x = px + (i / (len(closes) - 1)) * inner_w
        y = py + (1 - (c - lo) / rng) * inner_h
        points.append((x, y))

    draw = ImageDraw.Draw(panel, "RGBA")
    if fill_color is not None:
        poly = points + [(points[-1][0], py + inner_h), (points[0][0], py + inner_h)]
        draw.polygon(poly, fill=fill_color)
    draw.line(points, fill=color, width=width, joint="curve")


# ────────────────────────── YAHOO STYLE ──────────────────────────

YAHOO_BG = (16, 18, 25)
YAHOO_PANEL_BG = (24, 27, 36)
YAHOO_TEXT = (245, 246, 250)
YAHOO_SUB = (155, 160, 175)
YAHOO_UP = (0, 195, 137)
YAHOO_DOWN = (242, 75, 80)


def render_yahoo_panel(index):
    ph = panel_height()
    panel = Image.new("RGB", (CANVAS[0] - 80, ph), YAHOO_PANEL_BG)
    draw = ImageDraw.Draw(panel)

    is_up = index["change"] >= 0
    accent = YAHOO_UP if is_up else YAHOO_DOWN
    fill = (*accent, 35)

    # left text block
    draw.text((38, 22), index["label"], fill=YAHOO_SUB, font=font(28, "bold"))
    draw.text((38, 56), fmt_price(index["price"]), fill=YAHOO_TEXT, font=font(64, "bold"))
    draw.text(
        (38, 138),
        fmt_change(index["change"], index["pct"]),
        fill=accent,
        font=font(30, "bold"),
    )

    # right sparkline
    spark_x = panel.size[0] // 2 + 30
    spark_w = panel.size[0] - spark_x - 24
    spark = Image.new("RGBA", (spark_w, ph), (0, 0, 0, 0))
    draw_sparkline(spark, index["series"], accent + (255,), fill_color=fill, padding=(8, 20), width=3)
    panel.paste(spark, (spark_x, 0), spark)

    return panel


def render_yahoo(data, out_path):
    img = Image.new("RGB", CANVAS, YAHOO_BG)
    draw = ImageDraw.Draw(img)

    # header
    now = dt.datetime.now().strftime("%a %b %d  ·  %I:%M %p PT")
    draw.text((80, 100), "MARKETS", fill=YAHOO_SUB, font=font(34, "bold"))
    draw.text((80, 142), now, fill=YAHOO_TEXT, font=font(42, "bold"))

    ph = panel_height()
    for i, idx in enumerate(data["indices"]):
        panel = render_yahoo_panel(idx)
        y = SAFE_TOP + i * (ph + PANEL_GAP)
        img.paste(panel, (40, y))

    # footer
    draw.text(
        (80, CANVAS[1] - 160),
        "data: yahoo finance · intraday",
        fill=YAHOO_SUB,
        font=font(26),
    )
    img = _apply_safe_zone(img, bg=YAHOO_BG)
    img.save(out_path, "JPEG", quality=92)


# ────────────────────────── BRAND (dark_neon DNA) ──────────────────────────

BRAND_BG = (0, 0, 0)
BRAND_TEXT = (255, 255, 255)
BRAND_ACCENT = (240, 240, 245)
BRAND_LABEL = (95, 195, 245)
BRAND_SUB = (150, 150, 160)
BRAND_UP = (90, 230, 160)
BRAND_DOWN = (255, 95, 110)


def render_brand_panel(index):
    ph = panel_height()
    w = CANVAS[0] - 80
    panel = Image.new("RGBA", (w, ph), (0, 0, 0, 0))
    draw = ImageDraw.Draw(panel, "RGBA")

    # rounded card with hairline border
    radius = 28
    draw.rounded_rectangle(
        (0, 0, w - 1, ph - 1),
        radius=radius,
        fill=(12, 12, 16, 255),
        outline=(255, 255, 255, 50),
        width=2,
    )

    is_up = index["change"] >= 0
    accent = BRAND_UP if is_up else BRAND_DOWN
    fill = (*accent, 55)

    # label with accent dot
    draw.ellipse((38, 32, 54, 48), fill=BRAND_LABEL)
    draw.text((64, 22), index["label"], fill=BRAND_LABEL, font=font(32, "bold"))

    # big price
    draw.text((38, 66), fmt_price(index["price"]), fill=BRAND_TEXT, font=font(78, "bold"))

    # change
    draw.text(
        (38, 162),
        fmt_change(index["change"], index["pct"]),
        fill=accent,
        font=font(36, "bold"),
    )

    # sparkline (right half)
    spark_x = w // 2 + 20
    spark_w = w - spark_x - 30
    spark = Image.new("RGBA", (spark_w, ph), (0, 0, 0, 0))
    draw_sparkline(
        spark,
        index["series"],
        accent + (255,),
        fill_color=fill,
        padding=(10, 30),
        width=4,
    )
    panel.paste(spark, (spark_x, 0), spark)

    return panel


def render_brand(data, out_path):
    img = Image.new("RGB", CANVAS, BRAND_BG)
    draw = ImageDraw.Draw(img, "RGBA")

    # header
    now = dt.datetime.now().strftime("%a · %b %d · %I:%M %p PT")
    draw.text((80, 100), "MARKET PULSE", fill=BRAND_ACCENT, font=font(42, "bold"))
    draw.text((80, 152), now, fill=BRAND_TEXT, font=font(36, "bold"))
    draw.line((80, 208, CANVAS[0] - 80, 208), fill=(255, 255, 255, 50), width=2)

    ph = panel_height()
    for i, idx in enumerate(data["indices"]):
        panel = render_brand_panel(idx)
        y = SAFE_TOP + i * (ph + PANEL_GAP)
        img.paste(panel, (40, y), panel)

    # footer
    draw.text((80, CANVAS[1] - 175), "@broisinvesting", fill=BRAND_ACCENT, font=font(34, "bold"))
    draw.text(
        (80, CANVAS[1] - 128),
        "source: yahoo finance · intraday",
        fill=BRAND_SUB,
        font=font(26),
    )
    img = _apply_safe_zone(img, bg=BRAND_BG)
    img.save(out_path, "JPEG", quality=92)


# ────────────────────────── CLI ──────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", choices=["yahoo", "brand", "both"], default="both")
    ap.add_argument("--data", default=None, help="path to data JSON; if omitted, fetch live")
    ap.add_argument("--out-dir", default=str(Path(__file__).parent / "out"))
    args = ap.parse_args()

    if args.data:
        import json
        with open(args.data) as f:
            data = json.load(f)
    else:
        from fetch_data import fetch_all
        data = fetch_all()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    paths = []

    if args.style in ("yahoo", "both"):
        p = out_dir / f"story_yahoo_{stamp}.jpg"
        render_yahoo(data, p)
        paths.append(str(p))

    if args.style in ("brand", "both"):
        p = out_dir / f"story_brand_{stamp}.jpg"
        render_brand(data, p)
        paths.append(str(p))

    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
