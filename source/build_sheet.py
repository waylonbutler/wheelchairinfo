#!/usr/bin/env python3
"""Build the one-page handling sheet — page 1 English, page 2 Spanish.

Written for a baggage handler in a hurry, in poor light. Plain words, short
sentences, large type. Regulatory citations and full detail live on the web page
behind the QR code, not here.
"""
import subprocess, os

CSS = """
@page{size:letter;margin:0.34in}
*{box-sizing:border-box;margin:0;padding:0}
.scale{zoom:%(zoom)s}
body{font:12pt/1.3 "Helvetica Neue",Helvetica,Arial,sans-serif;color:#000}

.hdr{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;
  border-bottom:4pt solid #000;padding-bottom:7pt;margin-bottom:9pt}
.hdr h1{font-size:31pt;line-height:.98;letter-spacing:-.8pt;text-transform:uppercase}
.hdr .sub{font-size:13pt;font-weight:700;margin-top:5pt;line-height:1.2}
.hdr .sn{font-size:9pt;color:#333;margin-top:4pt}
.hdr .qrbox{flex:0 0 auto;text-align:center}
.hdr .qrbox img{width:1.16in;height:1.16in;display:block}
.hdr .qrbox span{font-size:7.4pt;font-weight:700;text-transform:uppercase;
  letter-spacing:.3pt;color:#a4161a;display:block;margin-top:2pt;line-height:1.15}
.lang{font-size:7.6pt;letter-spacing:1pt;text-transform:uppercase;color:#666;
  font-weight:700;margin-bottom:3pt}

ol.steps{list-style:none;counter-reset:st;margin:0}
ol.steps > li{counter-increment:st;position:relative;padding-left:.52in;margin-bottom:10pt}
ol.steps > li::before{content:counter(st);position:absolute;left:0;top:-1pt;
  width:.38in;height:.38in;border-radius:50%;background:#000;color:#fff;
  font-size:16pt;font-weight:700;text-align:center;line-height:.38in}
.h{font-size:15.5pt;font-weight:700;line-height:1.14;letter-spacing:-.2pt}
.d{font-size:11.5pt;line-height:1.26;margin-top:2pt}
.no{color:#a4161a;font-weight:700}

.stop{border:2.4pt solid #a4161a;background:#fdf1f1;border-radius:3pt;
  padding:7pt 10pt;margin:0 0 10pt}
.stop .t{color:#a4161a;font-size:14pt;font-weight:700;text-transform:uppercase;
  letter-spacing:.3pt;margin-bottom:2pt}
.stop .b{font-size:11.5pt;line-height:1.26}

.grid{display:flex;gap:12pt;margin-top:2pt}
.box{flex:1;border:1.2pt solid #000;border-radius:3pt;padding:6pt 9pt}
.box.call{flex:1.55}
.box .t{font-size:9pt;font-weight:700;text-transform:uppercase;letter-spacing:.7pt;
  color:#555;margin-bottom:3pt}
.box .big{font-size:15.5pt;font-weight:700;line-height:1.32;letter-spacing:-.2pt}
.box .sm{font-size:10pt;line-height:1.25;margin-top:3pt;color:#444}
.ph{font-size:17pt;font-weight:700;letter-spacing:-.2pt;line-height:1.15}
.nm{font-size:10.5pt;line-height:1.2}

.foot{margin-top:8pt;padding-top:5pt;border-top:1pt solid #999;font-size:8pt;color:#555;
  display:flex;align-items:center;gap:10px;min-height:0.86in}
.foot.rtl{flex-direction:row-reverse}
.foot .ftext{flex:1;min-width:0}
.foot .gap{flex:0 0 1.15in}
/* Punch target sits OUTSIDE the scaled wrapper so English and Spanish land on
   the same physical spot when printed double-sided (flip on long edge). */
.punchmark{position:fixed;bottom:.02in;width:.86in;height:.60in}
.punchmark.r{right:.02in}
.punchmark.l{left:.02in}
.punchmark .ring{position:absolute;left:50%;top:.20in;transform:translateX(-50%);
  width:.26in;height:.26in;border:1.1pt dashed #a4161a;border-radius:50%}
.punchmark .ring i{position:absolute;left:-.07in;right:-.07in;top:-.07in;bottom:-.07in}
.punchmark .ring::before,.punchmark .ring::after,
.punchmark .ring i::before,.punchmark .ring i::after{content:"";position:absolute;background:#a4161a}
.punchmark .ring::before{left:50%;top:-.07in;width:.6pt;height:.12in;transform:translateX(-50%)}
.punchmark .ring::after{top:50%;left:-.07in;height:.6pt;width:.12in;transform:translateY(-50%)}
.punchmark .ring i::before{left:50%;bottom:0;width:.6pt;height:.12in;transform:translateX(-50%)}
.punchmark .ring i::after{top:50%;right:0;height:.6pt;width:.12in;transform:translateY(-50%)}
.punchmark .plab{position:absolute;left:-.1in;right:-.1in;bottom:0;text-align:center;
  font-size:5.4pt;letter-spacing:.5pt;text-transform:uppercase;font-weight:700;
  color:#a4161a;line-height:1.1}
b{font-weight:700}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="scale">

<div class="hdr">
  <div>
    <div class="lang">{langnote}</div>
    <h1>{title}</h1>
    <div class="sub">{sub}</div>
  </div>
  <div class="qrbox"><img src="qr.png"><span>{qrlabel}</span></div>
</div>

<ol class="steps">{steps}</ol>

<div class="stop">
  <div class="t">{stop_h}</div>
  <div class="b">{stop_b}</div>
</div>

<div class="grid">
  <div class="box">
    <div class="t">{us_h}</div>
    <div class="big">{us}</div>
  </div>
  <div class="box">
    <div class="t">{met_h}</div>
    <div class="big">{met}</div>
  </div>
  <div class="box call">
    <div class="t">{call_h}</div>
    <div class="nm">Waylon Butler &mdash; {c_owner}</div>
    <div class="ph">+1 (631) 772-9702</div>
    <div class="nm" style="margin-top:4pt">Danielle Butler &mdash; {c_backup}</div>
    <div class="ph">+1 (703) 967-8487</div>
  </div>
</div>

<div class="foot{footdir}">
  <div class="ftext">{footer}</div>
  <div class="gap"></div>
</div>
</div>
<div class="punchmark {punchside}"><div class="ring"><i></i></div><div class="plab">{punchlab}</div></div>
</body></html>
"""

def step(head, detail):
    return f'  <li><div class="h">{head}</div><div class="d">{detail}</div></li>\n'

EN = dict(
    zoom="1.00", lang="en", footdir="", punchside="r", punchlab="Punch here",
    langnote="English &middot; Espa&ntilde;ol al reverso",
    title="How to handle<br>this wheelchair",
    sub="It does not fold. Keep it upright.",
    qrlabel="Scan for<br>photos &amp; more",
    steps=(
        step("Keep it upright. Never lay it on its side or on its back.",
             "The seat and the back are bolted to the frame. They do not fold down. Laying it over will bend the seat."),
        step("Lift only by the metal frame at the bottom.",
             '<span class="no">Never lift by the arms, the footplate, the joystick, the headrest, or the seat back.</span> Those parts break off.'),
        step("Strap it down at the 4 marked points.",
             "Look for the anchor symbol &mdash; two in front, two in back, low on the base. Use all 4. Do not strap to anything else."),
        step("To push it: turn it off, then push both yellow levers down.",
             "The two yellow levers are on the motors, in the middle of the chair. "
             "Push using the <b>two poles on the back of the seat</b>. Two people. "
             '<span class="no">Do not push or pull by the joystick, the arms, or the headrest.</span> '
             "When you are done, pull both yellow levers back up."),
        step("The batteries stay in the chair.",
             "They are sealed gel batteries. There is no lithium. Do not take them out and do not unplug them."),
        step("Bring it back to the aircraft door.",
             "The owner cannot walk. He has no other way to move without this chair."),
    ),
    stop_h="Stop &mdash; read this before you push it",
    stop_b="With the yellow levers <b>down</b>, the chair has <b>no brakes</b>. It weighs 425 lbs. "
           "On a ramp or a slope it will roll away, and you will not stop it by hand. "
           "Only push it on flat ground. Put the levers back <b>up</b> when you are done.",
    us_h="Inches / pounds",
    us="24&quot; wide<br>39&quot; long<br>40&quot; tall<br>425 lbs",
    met_h="Centimetres / kilos",
    met="61 cm wide<br>99 cm long<br>102 cm tall<br>193 kg",
    call_h="If anything goes wrong, call",
    c_owner="owner", c_backup="backup",
    footer="Damage? Tell the owner before he leaves the gate, and file a written report at the airport. "
           "&middot; Scan the QR code for photos, Spanish, and full instructions.",
)

ES = dict(
    zoom="1.02", lang="es", footdir=" rtl", punchside="l", punchlab="Perforar aqu&iacute;",
    langnote="Espa&ntilde;ol &middot; English on the reverse",
    title="C&oacute;mo manejar<br>esta silla de ruedas",
    sub="No se pliega. Mant&eacute;ngala vertical.",
    qrlabel="Escanee para<br>fotos y m&aacute;s",
    steps=(
        step("Mant&eacute;ngala vertical. Nunca la acueste de lado ni sobre el respaldo.",
             "El asiento y el respaldo est&aacute;n atornillados al bastidor. No se pliegan. Acostarla dobla el asiento."),
        step("Lev&aacute;ntela solo por el bastidor met&aacute;lico de abajo.",
             '<span class="no">Nunca la levante por los brazos, el reposapi&eacute;s, el joystick, el reposacabezas ni el respaldo.</span> Esas piezas se rompen.'),
        step("Suj&eacute;tela en los 4 puntos marcados.",
             "Busque el s&iacute;mbolo de ancla &mdash; dos adelante y dos atr&aacute;s, abajo en la base. Use los 4. No sujete nada m&aacute;s."),
        step("Para empujarla: ap&aacute;guela y baje las dos palancas amarillas.",
             "Las dos palancas amarillas est&aacute;n en los motores, al centro de la silla. "
             "Empuje usando los <b>dos postes del respaldo</b>. Dos personas. "
             '<span class="no">No empuje ni jale por el joystick, los brazos ni el reposacabezas.</span> '
             "Al terminar, suba otra vez las dos palancas amarillas."),
        step("Las bater&iacute;as se quedan en la silla.",
             "Son bater&iacute;as de gel selladas. No llevan litio. No las saque ni las desconecte."),
        step("Devu&eacute;lvala en la puerta del avi&oacute;n.",
             "El propietario no puede caminar. Sin esta silla no tiene c&oacute;mo moverse."),
    ),
    stop_h="Alto &mdash; lea esto antes de empujarla",
    stop_b="Con las palancas amarillas <b>abajo</b>, la silla <b>no tiene frenos</b>. Pesa 425 lb (193 kg). "
           "En una rampa o pendiente se ir&aacute; sola y no la detendr&aacute; a mano. "
           "Emp&uacute;jela solo en piso plano. Al terminar, suba las palancas otra vez.",
    us_h="Pulgadas / libras",
    us="24&quot; de ancho<br>39&quot; de largo<br>40&quot; de alto<br>425 lb",
    met_h="Cent&iacute;metros / kilos",
    met="61 cm de ancho<br>99 cm de largo<br>102 cm de alto<br>193 kg",
    call_h="Si algo sale mal, llame",
    c_owner="propietario", c_backup="alterno",
    footer="&iquest;Da&ntilde;os? Avise al propietario antes de que salga de la puerta y presente un informe escrito en el aeropuerto. "
           "&middot; Escanee el c&oacute;digo QR para fotos e instrucciones completas.",
)

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
for name, data in (("sheet-en", EN), ("sheet-es", ES)):
    d2 = dict(data, steps="".join(data["steps"]))
    html = TEMPLATE.format(css=CSS.replace("%(zoom)s", d2["zoom"]), **d2)
    open(f"{name}.html", "w").write(html)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={name}.pdf", f"{name}.html"],
                   capture_output=True)
    info = subprocess.run(["pdfinfo", f"{name}.pdf"], capture_output=True, text=True).stdout
    print(name, [l for l in info.split("\n") if l.startswith("Pages")])

subprocess.run(["pdfunite", "sheet-en.pdf", "sheet-es.pdf", "Wheelchair Handling Sheet.pdf"], check=True)
print("merged ->", os.path.getsize("Wheelchair Handling Sheet.pdf"))
