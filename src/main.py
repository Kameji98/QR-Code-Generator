#!/usr/bin/env python3
"""
QR Code Generator

A small CLI tool that generates QR code images from text or URLs.
"""

from __future__ import annotations

import os
from pathlib import Path


def require_non_empty(prompt: str) -> str:
    """Read a non-empty string from user input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def ask_yes_no(prompt: str) -> bool:
    """Ask a yes/no question and return True for yes, False for no."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("Please answer with 'y' or 'n'.")


def normalize_filename(name: str) -> str:
    """
    Normalize output filename:
    - If no extension is provided, default to .png
    - Prevent writing to a directory path
    """
    name = name.strip()
    p = Path(name)

    if name.endswith(os.sep) or (p.exists() and p.is_dir()):
        raise ValueError("Filename cannot be a directory.")

    if p.suffix == "":
        name += ".png"

    return name


def generate_qr(data: str, filename: str) -> None:
    """Generate and save a QR code image."""
    try:
        import qrcode  # type: ignore
    except ImportError:
        raise ImportError("Missing dependency: install with 'pip install qrcode[pil]'") from None

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)


def main() -> None:
    print("=== QR Code Generator ===")
    print("Generate QR codes from text or URLs.\n")

    while True:
        data = require_non_empty("Enter the text or URL: ")

        raw_filename = require_non_empty("Enter the output filename (e.g., my_qr.png): ")
        try:
            filename = normalize_filename(raw_filename)
        except ValueError as e:
            print(f"Error: {e}\n")
            continue

        try:
            generate_qr(data, filename)
            print(f"✅ QR code saved as: {filename}\n")
        except Exception as e:
            print(f"Error: {e}\n")

        if not ask_yes_no("Generate another QR code? (y/n): "):
            break
        print()

    print("Goodbye!")


if __name__ == "__main__":
    main()
