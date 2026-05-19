#!/usr/bin/env python3
"""
watermark-headshot.py — Generate lower-resolution watermarked headshot
for the public press kit.

Per docs/site-reviews/2026-05-18-onenote-ajustes.md item 13.1
(PR-S07a security restructure), the public /press-kit page should expose
only a watermarked, lower-resolution headshot. The full-resolution
original lives in src/assets/sarah-headshot.jpg and is served only via
Astro Picture optimization for /about and admin-gated routes (PR-S07b).

This script:
  - reads the canonical headshot from src/assets/sarah-headshot.jpg
  - downscales to max-width 700px preserving aspect ratio
  - embeds a "Sarah Rodovalho · sarahrodovalho.com" watermark in the
    bottom-right corner with shadowed text for readability against
    both light and dark backgrounds
  - writes the result to public/press/sarah-rodovalho-headshot.jpg

Idempotent: skips regeneration if output is newer than input. Pass
--force to override.

Usage:
    python3 scripts/watermark-headshot.py
    python3 scripts/watermark-headshot.py --max-width 600 --force
"""

import argparse
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO_ROOT / "src" / "assets" / "sarah-headshot.jpg"
DEFAULT_OUTPUT = REPO_ROOT / "public" / "press" / "sarah-rodovalho-headshot.jpg"
DEFAULT_WATERMARK_TEXT = "Sarah Rodovalho · sarahrodovalho.com"
DEFAULT_MAX_WIDTH = 700
DEFAULT_QUALITY = 85

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/TTF/DejaVuSans.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]


def find_font(size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    raise RuntimeError(
        f"No font found among candidates: {FONT_CANDIDATES}. "
        "Install DejaVu Sans (Ubuntu: apt install fonts-dejavu-core)."
    )


def watermark_headshot(
    input_path: Path,
    output_path: Path,
    text: str,
    max_width: int,
    quality: int,
) -> None:
    img = Image.open(input_path).convert("RGB")

    if img.width > max_width:
        ratio = max_width / img.width
        new_size = (max_width, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    font_size = max(13, img.width // 50)
    font = find_font(font_size)

    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    padding_x = max(10, img.width // 60)
    padding_y = max(10, img.height // 60)
    x = img.width - text_w - padding_x
    y = img.height - text_h - padding_y - bbox[1]

    shadow_offset = 1
    draw.text(
        (x + shadow_offset, y + shadow_offset),
        text,
        font=font,
        fill=(0, 0, 0, 210),
    )
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 235))

    img_rgba = img.convert("RGBA")
    composed = Image.alpha_composite(img_rgba, overlay).convert("RGB")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    composed.save(output_path, format="JPEG", quality=quality, optimize=True)

    size_kb = output_path.stat().st_size // 1024
    print(
        f"✓ Watermarked: {output_path.relative_to(REPO_ROOT)} "
        f"({composed.size[0]}×{composed.size[1]}, ~{size_kb}KB)"
    )


def should_skip(input_path: Path, output_path: Path) -> bool:
    if not output_path.exists():
        return False
    return output_path.stat().st_mtime > input_path.stat().st_mtime


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate watermarked lower-res headshot for public press kit"
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--text", default=DEFAULT_WATERMARK_TEXT)
    parser.add_argument("--max-width", type=int, default=DEFAULT_MAX_WIDTH)
    parser.add_argument("--quality", type=int, default=DEFAULT_QUALITY)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate even when output is newer than input",
    )
    args = parser.parse_args(argv)

    if not args.input.exists():
        print(f"✗ Input not found: {args.input}", file=sys.stderr)
        return 1

    if not args.force and should_skip(args.input, args.output):
        print(
            f"⊘ Skip: {args.output.relative_to(REPO_ROOT)} is newer than input. "
            "Use --force to regenerate."
        )
        return 0

    watermark_headshot(
        args.input,
        args.output,
        args.text,
        args.max_width,
        args.quality,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
