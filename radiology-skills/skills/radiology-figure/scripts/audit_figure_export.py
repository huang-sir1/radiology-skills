#!/usr/bin/env python3
"""Audit raster figure geometry, white background, DPI, and clipping risk."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageStat


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image")
    parser.add_argument("--require-white", action="store_true")
    parser.add_argument("--min-dpi", type=float, default=300.0)
    parser.add_argument("--min-bbox-fill", type=float, default=0.35)
    parser.add_argument("--max-edge-ink", type=float, default=0.08)
    return parser.parse_args()


def ratio_nonzero(mask: Image.Image) -> float:
    stat = ImageStat.Stat(mask)
    return float(stat.mean[0]) / 255.0


def main() -> int:
    args = parse_args()
    path = Path(args.image).expanduser().resolve()
    findings: list[dict[str, object]] = []
    try:
        with Image.open(path) as opened:
            dpi = opened.info.get("dpi")
            original_mode = opened.mode
            alpha = "A" in opened.getbands()
            image = opened.convert("RGBA")
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "FAIL", "findings": [{"severity": "ERROR", "message": str(exc)}]}, indent=2))
        return 1

    if alpha:
        white_base = Image.new("RGBA", image.size, (255, 255, 255, 255))
        image = Image.alpha_composite(white_base, image)
        findings.append({"severity": "WARNING", "code": "ALPHA", "message": "Image contains alpha; verify the submitted export is flattened onto white"})

    rgb = image.convert("RGB")
    width, height = rgb.size
    scale = min(1.0, 1200.0 / max(width, height))
    if scale < 1.0:
        sample = rgb.resize((max(1, round(width * scale)), max(1, round(height * scale))))
    else:
        sample = rgb

    white = Image.new("RGB", sample.size, "white")
    diff = ImageChops.difference(sample, white).convert("L")
    mask = diff.point(lambda value: 255 if value > 12 else 0)
    bbox = mask.getbbox()
    ink_ratio = ratio_nonzero(mask)

    if bbox is None or ink_ratio < 0.001:
        findings.append({"severity": "ERROR", "code": "BLANK", "message": "Figure is blank or nearly blank"})
        bbox_fill = 0.0
        margins = None
    else:
        left, top, right, bottom = bbox
        bbox_fill = ((right - left) * (bottom - top)) / (sample.width * sample.height)
        margins = {
            "left": left / sample.width,
            "right": (sample.width - right) / sample.width,
            "top": top / sample.height,
            "bottom": (sample.height - bottom) / sample.height,
        }
        if bbox_fill < args.min_bbox_fill:
            findings.append({"severity": "WARNING", "code": "WHITESPACE", "message": f"Content bounding box fills only {bbox_fill:.1%} of canvas"})

    band = max(1, round(min(sample.size) * 0.01))
    edge_regions = [
        mask.crop((0, 0, sample.width, band)),
        mask.crop((0, sample.height - band, sample.width, sample.height)),
        mask.crop((0, 0, band, sample.height)),
        mask.crop((sample.width - band, 0, sample.width, sample.height)),
    ]
    edge_ink = max(ratio_nonzero(region) for region in edge_regions)
    if edge_ink > args.max_edge_ink:
        findings.append({"severity": "WARNING", "code": "EDGE_INK", "message": f"Non-white content touches an edge ({edge_ink:.1%}); inspect clipping"})

    corner = max(1, round(min(sample.size) * 0.04))
    corners = [
        sample.crop((0, 0, corner, corner)),
        sample.crop((sample.width - corner, 0, sample.width, corner)),
        sample.crop((0, sample.height - corner, corner, sample.height)),
        sample.crop((sample.width - corner, sample.height - corner, sample.width, sample.height)),
    ]
    corner_means = [sum(ImageStat.Stat(region).mean) / 3.0 for region in corners]
    white_corners = sum(value >= 245 for value in corner_means)
    if args.require_white and white_corners < 4:
        findings.append({"severity": "ERROR", "code": "BACKGROUND", "message": f"Only {white_corners}/4 corners are near white"})

    dpi_values = tuple(float(value) for value in dpi[:2]) if isinstance(dpi, tuple) and len(dpi) >= 2 else None
    if dpi_values is None:
        findings.append({"severity": "WARNING", "code": "DPI_MISSING", "message": "No raster DPI metadata found"})
    elif min(dpi_values) + 0.5 < args.min_dpi:
        findings.append({"severity": "ERROR", "code": "DPI_LOW", "message": f"DPI {dpi_values} is below {args.min_dpi:g}"})

    errors = sum(item["severity"] == "ERROR" for item in findings)
    report = {
        "file": str(path),
        "status": "PASS" if errors == 0 else "FAIL",
        "mode": original_mode,
        "pixels": {"width": width, "height": height},
        "dpi": dpi_values,
        "ink_ratio": round(ink_ratio, 5),
        "bbox_fill": round(bbox_fill, 5),
        "normalized_margins": margins,
        "edge_ink_max": round(edge_ink, 5),
        "near_white_corners": white_corners,
        "findings": findings,
        "note": "This audit cannot detect semantic errors or all text/legend overlaps; inspect the final-size render visually.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
