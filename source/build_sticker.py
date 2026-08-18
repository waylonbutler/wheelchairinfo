#!/usr/bin/env python3
"""Build the QR sticker — one bilingual sticker, 2:1 landscape (twice as wide as tall).

Page 1 — 6 x 3 in, full rule set, QR + English + Spanish in three columns.
Page 2 — 4 x 2 in, compact fallback; merged bilingual lines, QR carries the rest.
"""
import subprocess, os

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PHONE = "+1 (631) 772-9702"

SHARED = """
*{box-sizing:border-box;margin:0;padding:0}
body{font:6pt/1.2 "Helvetica Neue",Helvetica,Arial,sans-serif;color:#000}
.bar{background:#a4161a;color:#fff;text-align:center;flex:0 0 auto}
.bar .en{font-weight:700;letter-spacing:.3pt;text-transform:uppercase;line-height:1.1}
.bar .es{font-weight:700;letter-spacing:.3pt;text-transform:uppercase;line-height:1.15}
b{font-weight:700}
"""

# ---------------------------------------------------------------- 6 x 3 in ----

BIG = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>
@page{size:6in 3in;margin:0}
""" + SHARED + """
.card{width:6in;height:2.97in;padding:.09in;border:1.7pt solid #000;display:flex;flex-direction:column}
.bar{padding:2.6pt 4pt}
.bar .en{font-size:13pt}
.bar .es{font-size:10pt;margin-top:1pt}
.body{flex:1;display:flex;gap:.10in;padding:4pt 0 3pt;min-height:0}
.qrcol{flex:0 0 1.12in;text-align:center;display:flex;flex-direction:column;align-items:center}
.qrcol img{width:1.06in;height:1.06in;display:block}
.qrcol .lab{font-size:6.4pt;font-weight:700;letter-spacing:.4pt;text-transform:uppercase;
  color:#a4161a;line-height:1.2;margin-top:2.4pt}
.col{flex:1;min-width:0;border-left:.7pt solid #999;padding-left:.10in}
.lang{font-size:6.6pt;font-weight:700;letter-spacing:.9pt;text-transform:uppercase;
  color:#a4161a;margin-bottom:2.2pt}
.col .r{font-size:8.6pt;line-height:1.21;margin-bottom:4.4pt}
.foot{flex:0 0 auto;border-top:1.3pt solid #000;padding-top:3.4pt;
  display:flex;align-items:baseline;gap:.12in;font-size:7.4pt;line-height:1.25}
.foot .m{font-size:9.6pt;font-weight:700;letter-spacing:-.1pt}
.foot .ph{font-size:11pt;font-weight:700}
.foot .a{flex:1;min-width:0}
.foot .b{flex:0 0 auto;text-align:right}
</style></head><body>
<div class="card">
  <div class="bar">
    <div class="en">Keep upright &middot; Do not tilt</div>
    <div class="es">Mantener vertical &middot; No inclinar</div>
  </div>
  <div class="body">
    <div class="qrcol">
      <img src="qr.png">
      <div class="lab">Scan for full<br>instructions<br>Escanee para<br>instrucciones</div>
    </div>
    <div class="col">
      <div class="lang">English</div>
      <div class="r"><b>425 lbs.</b> Seat rigid, <b>back bolted</b> &mdash; neither folds.</div>
      <div class="r"><b>Lift and strap only</b> by the base frame and the 4 labeled tie-down points.</div>
      <div class="r"><b>Never</b> by armrests, footplate, joystick, headrest, or the <b>yellow</b> freewheel levers.</div>
      <div class="r"><b>Power off</b> at the joystick before moving.</div>
      <div class="r"><b>Batteries stay in</b> &mdash; sealed gel, no lithium.</div>
    </div>
    <div class="col">
      <div class="lang">Espa&ntilde;ol</div>
      <div class="r"><b>425 lb (193 kg).</b> Asiento r&iacute;gido, <b>respaldo atornillado</b> &mdash; no se pliegan.</div>
      <div class="r"><b>Levantar y sujetar solo</b> por el bastidor y los 4 puntos de anclaje marcados.</div>
      <div class="r"><b>Nunca</b> por apoyabrazos, reposapi&eacute;s, joystick, reposacabezas ni las palancas <b>amarillas</b> de rueda libre.</div>
      <div class="r"><b>Apagar</b> en el joystick antes de moverla.</div>
      <div class="r"><b>Las bater&iacute;as no se retiran</b> &mdash; gel sellado, sin litio.</div>
    </div>
  </div>
  <div class="foot">
    <div class="a"><span class="m">Quantum Q6 Edge 3</span> &middot; S/N JE733123218020 &middot; 24&quot;W &times; 39&quot;L &times; 40&quot;H</div>
    <div class="b">Waylon Butler &middot; <span class="ph">__PHONE__</span></div>
  </div>
</div>
</body></html>
"""

# ---------------------------------------------------------------- 4 x 2 in ----

SMALL = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>
@page{size:4in 2in;margin:0}
""" + SHARED + """
.card{width:4in;height:1.97in;padding:.075in;border:1.5pt solid #000;display:flex;gap:.08in}
.qr{flex:0 0 auto;text-align:center}
.qr img{width:1.02in;height:1.02in;display:block}
.qr .lab{font-size:4.8pt;letter-spacing:.3pt;text-transform:uppercase;font-weight:700;
  margin-top:1.6pt;line-height:1.2;color:#a4161a}
.txt{flex:1;min-width:0;display:flex;flex-direction:column}
.bar{padding:2pt 3pt}
.bar .en{font-size:8pt}
.bar .es{font-size:6.4pt;margin-top:.6pt}
.r{font-size:5.9pt;line-height:1.18;margin-top:2.4pt}
.r .e{color:#444}
.spec{margin-top:auto;border-top:1pt solid #000;padding-top:2.4pt;font-size:5.5pt;line-height:1.26}
.spec .m{font-size:6.6pt;font-weight:700}
.spec .ph{font-size:7.6pt;font-weight:700}
</style></head><body>
<div class="card">
  <div class="qr">
    <img src="qr.png">
    <div class="lab">Scan &middot; Escanee</div>
  </div>
  <div class="txt">
    <div class="bar">
      <div class="en">Keep upright &middot; Do not tilt</div>
      <div class="es">Mantener vertical &middot; No inclinar</div>
    </div>
    <div class="r"><b>425 lbs / 193 kg.</b> Seat rigid, <b>back bolted</b> &mdash; neither folds.<br>
      <span class="e">Asiento r&iacute;gido, <b>respaldo atornillado</b> &mdash; no se pliegan.</span></div>
    <div class="r"><b>Lift and strap only</b> by the base frame and the four labeled tie-down points.<br>
      <span class="e"><b>Levantar y sujetar solo</b> por el bastidor y los cuatro puntos de anclaje.</span></div>
    <div class="r"><b>Batteries stay in</b> &mdash; sealed gel, no lithium.<br>
      <span class="e"><b>Las bater&iacute;as no se retiran</b> &mdash; gel sellado, sin litio.</span></div>
    <div class="spec">
      <span class="m">Quantum Q6 Edge 3</span> &middot; S/N JE733123218020 &middot; 24&quot;W &times; 39&quot;L &times; 40&quot;H<br>
      Waylon Butler &middot; <span class="ph">__PHONE__</span>
    </div>
  </div>
</div>
</body></html>
"""

for name, html in (("stick-6x3", BIG), ("stick-4x2", SMALL)):
    open(f"{name}.html", "w").write(html.replace("__PHONE__", PHONE))
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={name}.pdf", f"{name}.html"],
                   capture_output=True)
    info = subprocess.run(["pdfinfo", f"{name}.pdf"], capture_output=True, text=True).stdout
    print(name, [l for l in info.split("\n") if l.startswith(("Pages", "Page size"))])

subprocess.run(["pdfunite", "stick-6x3.pdf", "stick-4x2.pdf", "Wheelchair QR Sticker.pdf"], check=True)
print("merged ->", os.path.getsize("Wheelchair QR Sticker.pdf"))
