#!/usr/bin/env python3
"""Check a finished short against the Shorts Production Standard.

Usage:
    python scripts/verify.py path/to/short.mp4
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def probe(path: Path) -> dict:
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        sys.exit("ffprobe not found. Install FFmpeg and add it to PATH.")
    proc = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(path),
        ],
        capture_output=True,
        text=True,
    )
    if proc.returncode:
        sys.exit(f"Cannot read {path}:\n{proc.stderr.strip()}")
    return json.loads(proc.stdout)


def fps(stream: dict) -> float:
    raw = stream.get("avg_frame_rate") or stream.get("r_frame_rate") or "0/0"
    try:
        num, den = raw.split("/")
        return int(num) / int(den) if int(den) else 0.0
    except ValueError:
        return 0.0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verify 9:16 shorts against the production standard."
    )
    parser.add_argument("video", type=Path)
    args = parser.parse_args()

    if not args.video.is_file():
        sys.exit(f"File not found: {args.video}")

    data = probe(args.video)
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), {})
    audio = next((s for s in streams if s.get("codec_type") == "audio"), {})
    duration = float(
        data.get("format", {}).get("duration") or video.get("duration") or 0
    )

    width = video.get("width")
    height = video.get("height")
    measured_fps = fps(video)

    checks = [
        ("1080x1920", (width, height) == (1080, 1920), f"{width}x{height}"),
        ("30 fps", round(measured_fps, 2) == 30.0, f"{measured_fps:.2f} fps"),
        ("H.264", video.get("codec_name") == "h264", str(video.get("codec_name"))),
        ("AAC audio", audio.get("codec_name") == "aac", str(audio.get("codec_name"))),
        ("duration > 0", duration > 0.1, f"{duration:.2f}s"),
    ]

    print(f"\nShorts Production Standard - {args.video}")
    for label, ok, detail in checks:
        suffix = "" if ok else f"  (got {detail})"
        print(f"  {'PASS' if ok else 'FAIL'}  {label}{suffix}")

    failed = sum(not ok for _, ok, _ in checks)
    if failed:
        print(f"\n{failed} check(s) failed - not delivery-ready.\n")
        raise SystemExit(1)

    print(f"\n{len(checks)}/{len(checks)} passed - ready to post.\n")


if __name__ == "__main__":
    main()
