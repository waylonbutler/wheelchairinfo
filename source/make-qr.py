#!/usr/bin/env python3
"""Regenerate qr.png for the wheelchair info page.

Usage:  python make-qr.py https://YOURNAME.github.io/chair/

Requires: pip install "qrcode[pil]"
"""
import sys
import qrcode

if len(sys.argv) != 2:
    sys.exit("usage: python make-qr.py <url>")

url = sys.argv[1].strip()

q = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,  # 25% damage tolerance
    box_size=12,
    border=2,
)
q.add_data(url)
q.make(fit=True)
q.make_image(fill_color="black", back_color="white").save("qr.png")

print(f"wrote qr.png -> {url}  (version {q.version}, {q.modules_count} modules, Q error correction)")
