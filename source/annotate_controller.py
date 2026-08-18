#!/usr/bin/env python3
"""Annotate the Q-Logic 3 controller photo with numbered callouts.

Numbers only, no words baked in — the legend lives in the HTML so it can be
rendered in both English and Spanish from one image.

  1  On/off toggle (left side): forward = on, back = off
  2  Drive-mode button, marked "1"
  3  Green indicator and screen: lit = system is on
"""
from PIL import Image, ImageDraw, ImageFont

SRC, OUT = "ql.jpg", "img-controller.jpg"
SCALE = 3
RED = (164, 22, 26)

im = Image.open(SRC).convert("RGB")
im = im.crop((44, 14, 371, 386))                     # trim white margin
im = im.resize((im.width * SCALE, im.height * SCALE), Image.LANCZOS)
d = ImageDraw.Draw(im)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 46)

# Feature anchors in ORIGINAL 400x400 coordinates, mapped into the crop+scale.
def pt(x, y):
    return ((x - 44) * SCALE, (y - 14) * SCALE)

FEATURES = [
    # (number, target on the device, badge centre)
    ("1", pt(184, 103), pt(112, 78)),    # on/off toggle, left side
    ("2", pt(185, 162), pt(105, 178)),   # drive-mode button "1"
    ("3", pt(263,  57), pt(350, 30)),    # green power indicator on the screen
]

R = 34          # badge radius
LW = 6          # leader line width

for label, target, badge in FEATURES:
    # leader line, stopped short of the badge so it doesn't run under the number
    bx, by = badge
    tx, ty = target
    dx, dy = tx - bx, ty - by
    dist = (dx * dx + dy * dy) ** 0.5
    sx, sy = bx + dx / dist * (R + 2), by + dy / dist * (R + 2)
    d.line([(sx, sy), (tx, ty)], fill=RED, width=LW)
    # arrowhead
    ah = 22
    import math
    ang = math.atan2(dy, dx)
    for s in (+1, -1):
        a2 = ang + s * 0.42
        d.line([(tx, ty), (tx - ah * math.cos(a2), ty - ah * math.sin(a2))],
               fill=RED, width=LW)
    # badge
    d.ellipse([bx - R, by - R, bx + R, by + R], fill=RED, outline="white", width=5)
    tb = d.textbbox((0, 0), label, font=font)
    d.text((bx - (tb[2] - tb[0]) / 2 - tb[0], by - (tb[3] - tb[1]) / 2 - tb[1]),
           label, font=font, fill="white")

w = 760
im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
im.save(OUT, quality=82, optimize=True, progressive=True)
print(OUT, im.size)
