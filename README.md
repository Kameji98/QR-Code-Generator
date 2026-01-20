# QR Code Generator (Python)

A small CLI tool that generates a QR code image from text or a URL.

## Features
- Creates QR codes from any text or URL
- Validates input and output filename
- Automatically adds `.png` if no extension is provided
- Option to generate multiple QR codes in one session

## Tech Stack
- Python 3
- Third-party dependency: `qrcode` (uses Pillow under the hood)

## Install
```bash
pip install qrcode[pil]
```

## Run Locally
```bash
python src/main.py
```

## What I practiced
- Input validation and file naming
- Basic dependency usage and error handling
- User-friendly CLI flow
