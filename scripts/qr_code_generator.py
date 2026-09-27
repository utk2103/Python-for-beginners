#!/usr/bin/env python3
"""
QR Code Generator
------------------
Turns text or a URL into a QR code PNG image.

Install the required dependency first:
    pip install "qrcode[pil]"

Usage:
    python scripts/qr_code_generator.py "https://example.com" -o qr.png
"""

import argparse
import os
import sys


def generate_qr_code(data: str, output_path: str) -> None:
    """Generate a QR code PNG from `data` and save it to `output_path`."""
    try:
        import qrcode
    except ImportError:
        print('Missing dependency. Install it with:\n    pip install "qrcode[pil]"')
        sys.exit(1)

    if os.path.exists(output_path):
        print(
            f"Error: '{output_path}' already exists. Choose a different "
            f"--output path or remove the existing file first."
        )
        sys.exit(1)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

    width, height = img.size
    print(f"Saved QR code to '{output_path}' ({width}x{height} pixels)")


def main():
    parser = argparse.ArgumentParser(
        description="Turn text or a URL into a QR code PNG."
    )
    parser.add_argument("data", help="The text or URL to encode")
    parser.add_argument(
        "-o",
        "--output",
        default="qr.png",
        help="Path to save the PNG file (default: qr.png)",
    )
    args = parser.parse_args()

    generate_qr_code(args.data, args.output)


if __name__ == "__main__":
    main()
