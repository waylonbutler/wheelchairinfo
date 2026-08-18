#!/usr/bin/env python3
"""Annotate the owner's own chair photo with the circuit breaker location.

Numbers only, no words baked in — the legend lives in the HTML so one image
serves both languages.

  1  Main circuit breaker reset button, below the EDGE 3 logo
  2  Yellow freewheel lever (one of two)
"""
import math
from PIL import Image, ImageDraw, ImageFont

SRC, OUT = "chair.jpg", "img-breaker.jpg"
CROP = (700, 800, 1130, 1160)      # bottom-right quadrant of the source photo
SCALE = 2.5
RED = (164, 22, 26)

im = Image.open(SRC).convert("RGB").crop(CROP)
im = im.resize((int(im.width * SCALE), int(im.height * SCALE)), Image.LANCZOS)
d = ImageDraw.Draw(im)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)

def pt(x, y):
    return ((x - CROP[0]) * SCALE, (y - CROP[1]) * SCALE)

FEATURES = [
    ("1", pt(876,  919), pt(1010, 838)),   # circuit breaker reset
    ("2", pt(867, 1049), pt(755, 1120)),   # yellow freewheel lever
]

R, LW, AH = 32, 6, 21

for label, target, badge in FEATURES:
    bx, by = badge
    tx, ty = target
    dx, dy = tx - bx, ty - by
    dist = math.hypot(dx, dy)
    sx, sy = bx + dx / dist * (R + 3), by + dy / dist * (R + 3)
    # stop the line short of the target so the ring stays clean
    ex, ey = tx - dx / dist * 26, ty - dy / dist * 26
    d.line([(sx, sy), (ex, ey)], fill=RED, width=LW)
    ang = math.atan2(dy, dx)
    for s in (+1, -1):
        a2 = ang + s * 0.42
        d.line([(ex, ey), (ex - AH * math.cos(a2), ey - AH * math.sin(a2))], fill=RED, width=LW)
    # ring highlighting the part itself
    rr = 24
    d.ellipse([tx - rr, ty - rr, tx + rr, ty + rr], outline=RED, width=5)
    # numbered badge
    d.ellipse([bx - R, by - R, bx + R, by + R], fill=RED, outline="white", width=5)
    tb = d.textbbox((0, 0), label, font=font)
    d.text((bx - (tb[2] - tb[0]) / 2 - tb[0], by - (tb[3] - tb[1]) / 2 - tb[1]),
           label, font=font, fill="white")

w = 760
im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
im.save(OUT, quality=84, optimize=True, progressive=True)
print(OUT, im.size)
