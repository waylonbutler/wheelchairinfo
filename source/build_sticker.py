#!/usr/bin/env python3
"""Build the QR sticker — 4 x 2.5 in, English in large type, Spanish via the QR."""
import subprocess, os

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PHONE = "+1 (631) 772-9702"

HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>
@page{size:4in 2.5in;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font:8pt/1.2 "Helvetica Neue",Helvetica,Arial,sans-serif;color:#000;width:4in;height:2.5in}
.card{width:4in;height:2.47in;padding:.075in;border:1.8pt solid #000;display:flex;flex-direction:column}
.bar{background:#a4161a;color:#fff;text-align:center;padding:3pt 3pt;flex:0 0 auto;
  font-size:13.5pt;font-weight:700;letter-spacing:.3pt;text-transform:uppercase;line-height:1.08}
.body{flex:1;display:flex;gap:.085in;padding:4pt 0 0;min-height:0}
.qr{flex:0 0 1.02in;display:flex;flex-direction:column;align-items:center}
.qr img{width:1.00in;height:1.00in;display:block}
.qr .lab{font-size:5.6pt;font-weight:700;letter-spacing:.3pt;text-transform:uppercase;
  color:#a4161a;line-height:1.15;margin-top:2.2pt;text-align:center}
.rules{flex:1;min-width:0}
.rules div{font-size:9.4pt;line-height:1.16;margin-bottom:3.6pt}
.rules .big{font-size:11.5pt;font-weight:700;letter-spacing:-.1pt;margin-bottom:4pt}
.es{flex:0 0 auto;background:#f1f3f6;border:.8pt solid #b9c0c9;border-radius:2pt;
  padding:2.6pt 5pt;margin-top:2pt;font-size:7.4pt;line-height:1.2}
.foot{flex:0 0 auto;border-top:1.4pt solid #000;margin-top:3.4pt;padding-top:3pt;
  display:flex;align-items:baseline;gap:.08in;font-size:7.2pt}
.foot .m{font-weight:700;font-size:8.4pt}
.foot .a{flex:1;min-width:0}
.foot .ph{font-size:10.5pt;font-weight:700}
b{font-weight:700}
</style></head><body>
<div class="card">
  <div class="bar">Keep upright &middot; Do not tilt</div>
  <div class="body">
    <div class="qr">
      <img src="qr.png">
      <div class="lab">Scan for full<br>instructions</div>
    </div>
    <div class="rules">
      <div class="big">425 lbs. It does not fold.</div>
      <div><b>Lift only</b> by the metal frame at the bottom.</div>
      <div><b>Never</b> by the arms, joystick, headrest, or footplate.</div>
      <div><b>Batteries stay in.</b> Sealed gel. No lithium.</div>
    </div>
  </div>
  <div class="es"><b>Espa&ntilde;ol:</b> escanee el c&oacute;digo QR para ver estas instrucciones en espa&ntilde;ol.</div>
  <div class="foot">
    <div class="a"><span class="m">Quantum Q6 Edge 3</span><br>S/N JE733123218020 &middot; 24&quot;W &times; 39&quot;L &times; 40&quot;H</div>
    <div><span class="ph">__PHONE__</span></div>
  </div>
</div>
</body></html>
"""

open("stick-4x25.html", "w").write(HTML.replace("__PHONE__", PHONE))
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                "--print-to-pdf=Wheelchair QR Sticker.pdf", "stick-4x25.html"], capture_output=True)
info = subprocess.run(["pdfinfo", "Wheelchair QR Sticker.pdf"], capture_output=True, text=True).stdout
print([l for l in info.split("\n") if l.startswith(("Pages", "Page size"))])
