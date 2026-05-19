#!/usr/bin/env python3
"""
Embed diagonal watermark on speaking deck assets.

Pattern: 4 lines of "© Sarah Rodovalho · sarahrodovalho.com" rendered
diagonally (-30°) at ~22% opacity across the image, spaced uniformly to
make crop-out difficult. White text with thin black stroke for legibility
on both light and dark backgrounds.

Idempotent: skips outputs that already exist with mtime > input.

Usage:
    python3 scripts/watermark-images.py            # process new/updated only
    python3 scripts/watermark-images.py --force    # rewrite all outputs

Inputs:  src/assets/speaking/_originals/*.{png,jpg,jpeg}
Outputs: src/assets/speaking/<same-filename>

The _originals/ folder is gitignored — kept locally only. The watermarked
outputs are committed to git as the canonical assets rendered by
speaking.astro.
"""

import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WATERMARK_TEXT = "© Sarah Rodovalho · sarahrodovalho.com"
OPACITY = 56  # ~22% on 0-255 alpha
ROTATION_DEG = -30
LINE_SPACING_FRAC = 0.28  # spacing between watermark lines (fraction of diagonal)
FONT_SIZE_FRAC = 0.024  # font size as fraction of min(W, H)
NUM_LINES = 4

ROOT = Path(__file__).resolve().parent.parent
ORIGINALS = ROOT / "src" / "assets" / "speaking" / "_originals"
OUTPUT_DIR = ROOT / "src" / "assets" / "speaking"

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/liberation/LiberationSans-Bold.ttf",
]


def find_font(size: int) -> ImageFont.ImageFont:
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def watermark_image(src: Path, dst: Path) -> None:
    img = Image.open(src).convert("RGBA")
    width, height = img.size
    font_size = max(20, int(min(width, height) * FONT_SIZE_FRAC))
    font = find_font(font_size)

    bbox = font.getbbox(WATERMARK_TEXT)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    pad = max(40, font_size * 2)
    strip = Image.new("RGBA", (text_w + pad, text_h + pad), (0, 0, 0, 0))
    strip_draw = ImageDraw.Draw(strip)
    strip_draw.text(
        (pad // 2, pad // 2),
        WATERMARK_TEXT,
        font=font,
        fill=(255, 255, 255, OPACITY),
        stroke_width=max(1, font_size // 14),
        stroke_fill=(0, 0, 0, OPACITY),
    )

    rotated = strip.rotate(ROTATION_DEG, expand=True, resample=Image.BICUBIC)
    rotated_w, rotated_h = rotated.size

    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    diagonal = math.hypot(width, height)
    step = int(diagonal * LINE_SPACING_FRAC)

    cx, cy = width // 2, height // 2
    angle_rad = math.radians(ROTATION_DEG)
    nx = -math.sin(angle_rad)
    ny = math.cos(angle_rad)

    offsets = [k - (NUM_LINES - 1) / 2 for k in range(NUM_LINES)]
    for k in offsets:
        ox = int(cx + k * step * nx) - rotated_w // 2
        oy = int(cy + k * step * ny) - rotated_h // 2
        overlay.alpha_composite(rotated, (ox, oy))

    result = Image.alpha_composite(img, overlay)

    suffix = src.suffix.lower()
    if suffix in (".jpg", ".jpeg"):
        result.convert("RGB").save(dst, quality=92, optimize=True)
    else:
        result.save(dst, optimize=True)


def main() -> int:
    force = "--force" in sys.argv

    if not ORIGINALS.exists():
        print(f"ERROR: originals folder missing: {ORIGINALS}", file=sys.stderr)
        print(
            "  Move existing src/assets/speaking/*.{png,jpg} into _originals/ first.",
            file=sys.stderr,
        )
        return 1

    files = sorted(
        p for p in ORIGINALS.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg")
    )
    if not files:
        print(f"No images found in {ORIGINALS}")
        return 0

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for src in files:
        dst = OUTPUT_DIR / src.name
        if dst.exists() and not force and dst.stat().st_mtime > src.stat().st_mtime:
            print(f"skip (idempotent): {src.name}")
            continue
        print(f"watermarking: {src.name}")
        watermark_image(src, dst)
    print("done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
