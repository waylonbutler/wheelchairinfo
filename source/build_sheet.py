#!/usr/bin/env python3
"""Build the two-sided handling sheet (page 1 English, page 2 Spanish)."""
import subprocess, os

CSS = """
@page{size:letter;margin:0.34in}
*{box-sizing:border-box;margin:0;padding:0}
.scale{zoom:%(zoom)s}
body{font:8.3pt/1.25 "Helvetica Neue",Helvetica,Arial,sans-serif;color:#111}
.hdr{border-bottom:3px solid #000;padding-bottom:5px;margin-bottom:6px;display:flex;justify-content:space-between;align-items:flex-end;gap:12px}
.hdr h1{font-size:19.5pt;line-height:1.02;letter-spacing:-.4pt}
.hdr .kick{font-size:7pt;letter-spacing:1.4pt;text-transform:uppercase;font-weight:700;color:#555;margin-bottom:2px}
.hdr .sn{font-size:8.6pt;color:#333;margin-top:3px}
.hdr .qrbox{text-align:center;flex:0 0 auto}
.hdr .qrbox img{width:1.00in;height:1.00in;display:block}
.hdr .qrbox span{font-size:6.2pt;letter-spacing:.4pt;text-transform:uppercase;color:#555;display:block;margin-top:1px}
.lang{font-size:6.4pt;letter-spacing:.9pt;text-transform:uppercase;color:#666;font-weight:700;margin-bottom:3px}
.alert{border:1.6pt solid #a4161a;border-left:7pt solid #a4161a;background:#fdf1f1;padding:6px 10px;margin-bottom:6px}
.alert h2{color:#a4161a;font-size:11pt;margin-bottom:3px;letter-spacing:-.2pt}
.alert ol{padding-left:14px}
.alert li{margin-bottom:2px}
.cols{display:flex;gap:14px}
.col{flex:1;min-width:0}
h2.s{font-size:9.6pt;border-bottom:1.2pt solid #000;padding-bottom:2px;margin:8px 0 3.5px;letter-spacing:-.2pt}
h2.s:first-child{margin-top:0}
ol.n,ul.n{padding-left:14px}
ol.n li,ul.n li{margin-bottom:2px}
table{width:100%;border-collapse:collapse;font-size:8.1pt}
td{padding:1.9px 3px;border-bottom:.5pt solid #ccc;vertical-align:top}
td.k{color:#555;width:42%}
.batt{border:1pt solid #1b5e4a;border-left:7pt solid #1b5e4a;background:#eef6f2;padding:5px 9px;margin-bottom:7px;font-size:8.4pt}
.batt b{color:#1b5e4a}
.warn{background:#fdf1f1;border:.8pt solid #e8b4b6;padding:4px 7px;margin-top:4px;font-size:8.4pt}
.quote{background:#f4f6f9;border-left:3pt solid #888;padding:4px 7px;margin-top:4px;font-size:8pt;font-style:italic}
.ct{border:.8pt solid #bbb;background:#f5f6f8;padding:4px 8px;margin-bottom:4px}
.ct .w{font-weight:700;font-size:9pt}
.ct .r{font-size:7.4pt;color:#555}
.ct .p{font-size:12pt;font-weight:700;letter-spacing:.2pt;margin-top:1px}
.ct .x{font-size:7.4pt;color:#555;margin-top:2px}
.foot{margin-top:6px;padding-top:4px;border-top:.8pt solid #999;font-size:6.9pt;color:#555;
  display:flex;align-items:center;gap:10px;min-height:0.86in}
.foot.rtl{flex-direction:row-reverse}
.foot .ftext{flex:1;min-width:0}
.foot .gap{flex:0 0 1.15in}
/* Punch target sits OUTSIDE the scaled wrapper so English and Spanish land on the
   same physical spot when printed double-sided (flip on long edge). */
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
  font-size:5.4pt;letter-spacing:.5pt;text-transform:uppercase;font-weight:700;color:#a4161a;line-height:1.1}
b{font-weight:700}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="scale">
<div class="hdr">
  <div>
    <div class="lang">{langnote}</div>
    <div class="kick">{kicker}</div>
    <h1>{title}</h1>
    <div class="sn">Quantum Rehab <b>Q6 Edge 3</b> &middot; {sn_serial} <b>JE733123218020</b> &middot; <b>{sn_weight}</b> &middot; {sn_owner} Waylon Butler</div>
  </div>
  <div class="qrbox"><img src="qr.png"><span>{qrlabel}</span></div>
</div>

<div class="alert">
  <h2>{rules_h}</h2>
  <ol>{rules}</ol>
</div>

<div class="batt">{battery}</div>

<div class="cols">
  <div class="col">
    <h2 class="s">{specs_h}</h2>
    <table>{specs}</table>

    <h2 class="s">{apart_h}</h2>
    {apart}

    <h2 class="s">{secure_h}</h2>
    <ul class="n">{secure}</ul>
  </div>
  <div class="col">
    <h2 class="s">{free_h}</h2>
    <ol class="n">{free}</ol>
    <div class="warn">{free_warn}</div>

    <h2 class="s">{ret_h}</h2>
    <ul class="n">{ret}</ul>

    <h2 class="s">{contact_h}</h2>
    <div class="ct">
      <div class="w">Waylon Butler &mdash; {c_owner}</div>
      <div class="r">{c_owner_note}</div>
      <div class="p">+1 (631) 772-9702</div>
    </div>
    <div class="ct">
      <div class="w">Danielle Butler &mdash; {c_backup}</div>
      <div class="r">{c_backup_note}</div>
      <div class="p">+1 (703) 967-8487</div>
    </div>

    <h2 class="s">{rights_h}</h2>
    <ul class="n">{rights}</ul>
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

EN = dict(
    zoom="0.935",
    footdir="", punchside="r", punchlab="Punch here",
    lang="en",
    langnote="English &middot; Espa&ntilde;ol al reverso",
    kicker="Do not remove — handling instructions",
    title="Power Wheelchair · Handling &amp; Airline Card",
    sn_serial="Serial", sn_weight="425 lbs", sn_owner="Owner:",
    qrlabel="Full instructions",
    rules_h="Five rules — read before touching this chair",
    rules="""
    <li><b>Keep it upright.</b> Never lay it on its side, back, or end. The seat is rigid — it does not fold flat and will be damaged by side-loading.</li>
    <li><b>Lift only by the solid metal frame of the power base</b>, below the seat. Never by armrests, footplate, joystick, headrest, seat back, or the yellow freewheel levers.</li>
    <li><b>Power OFF at the joystick before moving it.</b> Then use freewheel (right). Never force it against the motors.</li>
    <li><b>Freewheel only on level ground.</b> Freewheel releases the brakes — on any slope a 425 lb chair rolls away and cannot be stopped by hand.</li>
    <li><b>Batteries stay in the chair.</b> Sealed, non-spillable gel cells. Do not disconnect, remove, or drain.</li>""",
    battery="""<b>BATTERY STATEMENT FOR CHECK-IN:</b> Two 12-volt NF-22 <b>sealed gel-cell (non-spillable)</b> batteries, factory-installed in an enclosed tray, terminals protected. <b>No lithium battery on this chair.</b> Under 49 CFR 175.10(a)(15) and 14 CFR 382.127, non-spillable batteries may remain installed and connected; carriers must not remove, disconnect, or drain them.""",
    specs_h="Specifications",
    specs="""
      <tr><td class="k">Total weight</td><td><b>425 lbs / 193 kg</b></td></tr>
      <tr><td class="k">Width</td><td>24 in — the drive wheels are the widest point; armrests do not extend past them</td></tr>
      <tr><td class="k">Length</td><td>39 in with the footplate folded up</td></tr>
      <tr><td class="k">Height</td><td>40 in with the headrest removed (removed before travel)</td></tr>
      <tr><td class="k">Ground clearance</td><td>2.7 in — ramp required, will not clear a curb</td></tr>
      <tr><td class="k">Seating</td><td>TRU-Balance 3 power tilt / recline / 12 in power lift — <b>rigid, does not fold</b></td></tr>
      <tr><td class="k">Batteries</td><td>2 × 12 V NF-22 gel, ~38 lbs each, installed in the base</td></tr>""",
    apart_h="What comes apart — and what does not",
    apart="""<p style="margin-bottom:3px">The owner prepares the chair before handing it over: <b>headrest removed, joystick swung in and secured, footplate folded up.</b> It arrives at the aircraft ready to load.</p>
    <ul class="n">
      <li><b>Nothing else on this chair comes apart for transport.</b> Do not remove the seat, seat back, armrests, tilt/recline actuators, seat lift column, wheels, or batteries.</li>
      <li>The <b>seat back is bolted to the frame</b> — no pin, no release lever. It does not fold or flip forward. <b>Do not force it.</b></li>
      <li>The armrests are <b>fixed-width</b>. Moving them does not make the chair narrower — 24 in is the width, at the drive wheels.</li>
      <li>The joystick is <b>not quickly removable</b>. It is swung in and secured. It is the most easily damaged part of the chair — nothing should press against it.</li>
    </ul>
    <div class="quote">Manufacturer: &ldquo;Do not attempt to lift or move your power chair or seating system by any of its removable parts, including the armrest(s), front rigging(s), seat cushions, seatback, shrouds, or controller. Use only solid, non-removable frame components.&rdquo;</div>""",
    secure_h="Securing in the hold — use the four tie-down points",
    secure="""
      <li>This chair has <b>four labeled tie-down points</b> — two front, two rear, on the power base, marked with <b>anchor symbols</b>. <b>Use all four.</b> Do not improvise straps around frame tubes.</li>
      <li>Stow <b>upright, wheels down</b>, facing forward. No cargo stacked on the seat, back, or joystick.</li>
      <li><b>Never attach a strap to:</b> the yellow freewheel levers, armrests, footplate, joystick, headrest, seat back, wheels, or any adjustable or removable part.</li>
      <li>Leave the freewheel levers <b>UP</b> (drive mode) so the brakes hold.</li>
      <li><b>Never raise or elevate the seat</b> while the chair is secured for transport.</li>""",
    free_h="Moving it without power — freewheel",
    free="""
      <li>Bring the chair to <b>level ground</b>. Nobody seated in it.</li>
      <li><b>Turn power off</b> at the joystick, or the controller throws an error code.</li>
      <li>Find the <b>two yellow freewheel levers</b> — one on each drive motor, mid-chair behind the drive wheels. <b>Push both down.</b></li>
      <li>Push from the <b>frame of the power base</b>. Two people. Never push on the seat back, joystick, armrests, or footplate.</li>
      <li>When in position, <b>pull both levers back up</b> to re-engage the motors and restore the brakes. Confirm both are up.</li>""",
    free_warn="<b>Levers down = no brakes.</b> 425 lbs will roll away on any ramp or incline and cannot be stopped by hand.",
    ret_h="Returning the chair",
    ret="""
      <li>Return it <b>at the aircraft door</b> — the owner cannot walk and has no other mobility.</li>
      <li>Confirm <b>both freewheel levers are up</b> before the owner transfers in.</li>
      <li>Return every part that came off the chair, including the headrest.</li>
      <li>Report any damage <b>before</b> the owner leaves the gate.</li>""",
    contact_h="Contacts",
    c_owner="owner", c_owner_note="Call first for anything involving this chair",
    c_backup="backup contact", c_backup_note="If the owner cannot be reached",
    rights_h="Owner's rights — 14 CFR Part 382",
    rights="""
      <li><b>§ 382.125</b> — Wheelchairs get <i>priority for stowage in the baggage compartment over other cargo and baggage</i>, and must be returned <i>as close as possible to the door of the aircraft</i>.</li>
      <li><b>§ 382.127</b> — A manufacturer-labeled non-spillable battery <b>may not be required to be removed</b>; carriers must not disconnect an enclosed non-spillable battery, and must not drain batteries.</li>
      <li><b>§ 382.129</b> — The passenger may give <b>written directions</b> for disassembly and reassembly; the carrier must follow them so far as feasible. <b>This card is that written direction.</b> The device must be returned <i>in the condition in which you received it</i>.</li>""",
    footer="Manufacturer manual: quantumrehab.com/pdf/owners-manuals/us_uk_au_q6_edge_2.0_2.0x_3_2.0hd_series_om.pdf · Quantum Rehab, 401 York Ave, Duryea PA 18642 · Manufactured 2023, delivered 13 Dec 2023 · Scan the QR code for full instructions online. · <b>Print double-sided, flip on LONG edge</b>, so the punch marks align.",
)

ES = dict(
    zoom="0.895",
    footdir=" rtl", punchside="l", punchlab="Perforar aqu&iacute;",
    lang="es",
    langnote="Espa&ntilde;ol &middot; English on the reverse",
    kicker="No retirar — instrucciones de manejo",
    title="Silla de Ruedas El&eacute;ctrica · Manejo y Vuelo",
    sn_serial="N.º de serie", sn_weight="425 lb (193 kg)", sn_owner="Propietario:",
    qrlabel="Instrucciones completas",
    rules_h="Cinco reglas — lea antes de tocar esta silla",
    rules="""
    <li><b>Mant&eacute;ngala en posici&oacute;n vertical.</b> Nunca la acueste de lado, sobre el respaldo ni de punta. El asiento es r&iacute;gido: no se pliega y se da&ntilde;ar&aacute; si se carga de costado.</li>
    <li><b>Lev&aacute;ntela &uacute;nicamente por el bastidor met&aacute;lico s&oacute;lido de la base</b>, debajo del asiento. Nunca por los apoyabrazos, el reposapi&eacute;s, el joystick, el reposacabezas, el respaldo ni las <b>palancas amarillas</b> de rueda libre.</li>
    <li><b>Apague la silla en el joystick antes de moverla.</b> Luego use el modo de rueda libre (derecha). Nunca la empuje contra los motores.</li>
    <li><b>Use la rueda libre solo en terreno plano.</b> La rueda libre libera los frenos: en cualquier pendiente, una silla de 425 lb se va sola y no se puede detener a mano.</li>
    <li><b>Las bater&iacute;as permanecen en la silla.</b> Son de gel selladas, no derramables. No las desconecte, retire ni descargue.</li>""",
    battery="""<b>DECLARACI&Oacute;N DE BATER&Iacute;A PARA EL MOSTRADOR:</b> Dos bater&iacute;as NF-22 de 12 voltios <b>de gel selladas (no derramables)</b>, instaladas de f&aacute;brica en una bandeja cerrada, con los bornes protegidos. <b>Esta silla no lleva bater&iacute;a de litio.</b> Seg&uacute;n 49 CFR 175.10(a)(15) y 14 CFR 382.127, las bater&iacute;as no derramables pueden permanecer instaladas y conectadas; el transportista no debe retirarlas, desconectarlas ni descargarlas.""",
    specs_h="Especificaciones",
    specs="""
      <tr><td class="k">Peso total</td><td><b>425 lb / 193 kg</b></td></tr>
      <tr><td class="k">Ancho</td><td>24 pulg — las ruedas motrices son el punto m&aacute;s ancho; los apoyabrazos no sobresalen</td></tr>
      <tr><td class="k">Largo</td><td>39 pulg con el reposapi&eacute;s plegado hacia arriba</td></tr>
      <tr><td class="k">Altura</td><td>40 pulg sin el reposacabezas (se retira antes de viajar)</td></tr>
      <tr><td class="k">Altura libre al suelo</td><td>2.7 pulg — requiere rampa; no sube un bordillo</td></tr>
      <tr><td class="k">Asiento</td><td>TRU-Balance 3 con inclinaci&oacute;n, reclinaci&oacute;n y elevaci&oacute;n de 12 pulg — <b>r&iacute;gido, no se pliega</b></td></tr>
      <tr><td class="k">Bater&iacute;as</td><td>2 × 12 V NF-22 de gel, ~38 lb cada una, dentro de la base</td></tr>
""",
    apart_h="Qu&eacute; se desmonta — y qu&eacute; no",
    apart="""<p style="margin-bottom:3px">El propietario prepara la silla antes de entregarla: <b>reposacabezas retirado, joystick girado hacia adentro y asegurado, reposapi&eacute;s plegado hacia arriba.</b> Llega al avi&oacute;n lista para cargar.</p>
    <ul class="n">
      <li><b>Nada m&aacute;s en esta silla se desmonta para el transporte.</b> No retire el asiento, el respaldo, los apoyabrazos, los actuadores de inclinaci&oacute;n/reclinaci&oacute;n, la columna de elevaci&oacute;n, las ruedas ni las bater&iacute;as.</li>
      <li>El <b>respaldo est&aacute; atornillado al bastidor</b> — sin pasador ni palanca. No se pliega ni se abate. <b>No lo fuerce.</b></li>
      <li>Los apoyabrazos son de <b>ancho fijo</b>. Moverlos no hace la silla m&aacute;s angosta: el ancho es 24 pulg, medido en las ruedas motrices.</li>
      <li>El joystick <b>no se quita r&aacute;pidamente</b>. Va girado hacia adentro y asegurado. Es la pieza que se da&ntilde;a con m&aacute;s facilidad: nada debe presionar contra &eacute;l.</li>
    </ul>
    <div class="quote">Del fabricante: &ldquo;No intente levantar ni mover la silla o el sistema de asiento por ninguna de sus piezas desmontables, incluidos los apoyabrazos, los soportes delanteros, los cojines, el respaldo, las cubiertas o el control. Use &uacute;nicamente componentes s&oacute;lidos y no desmontables del bastidor.&rdquo;</div>""",
    secure_h="Sujeci&oacute;n en la bodega — use los cuatro puntos de anclaje",
    secure="""
      <li>Esta silla tiene <b>cuatro puntos de anclaje identificados</b> — dos delanteros y dos traseros, en la base, marcados con <b>s&iacute;mbolos de ancla</b>. <b>Use los cuatro.</b> No improvise correas alrededor de los tubos del bastidor.</li>
      <li>Est&iacute;bela <b>en posici&oacute;n vertical, sobre las ruedas</b>, mirando hacia adelante. No apile carga sobre el asiento, el respaldo ni el joystick.</li>
      <li><b>Nunca sujete una correa a:</b> las palancas amarillas de rueda libre, los apoyabrazos, el reposapi&eacute;s, el joystick, el reposacabezas, el respaldo, las ruedas ni ninguna pieza ajustable o desmontable.</li>
      <li>Deje las palancas de rueda libre <b>ARRIBA</b> (modo de conducci&oacute;n) para que los frenos sujeten.</li>
      <li><b>Nunca eleve el asiento</b> mientras la silla est&eacute; sujeta para el transporte.</li>""",
    free_h="Moverla sin motor — modo de rueda libre",
    free="""
      <li>Lleve la silla a <b>terreno plano</b>. Nadie sentado en ella.</li>
      <li><b>Apague la silla</b> en el joystick, o el control mostrar&aacute; un c&oacute;digo de error.</li>
      <li>Localice las <b>dos palancas amarillas de rueda libre</b> — una en cada motor, al centro de la silla, detr&aacute;s de las ruedas motrices. <b>Baje ambas palancas.</b></li>
      <li>Empuje desde el <b>bastidor de la base</b>. Dos personas. Nunca empuje el respaldo, el joystick, los apoyabrazos ni el reposapi&eacute;s.</li>
      <li>Ya colocada, <b>suba ambas palancas</b> para volver a acoplar los motores y restablecer los frenos. Confirme que ambas est&eacute;n arriba.</li>""",
    free_warn="<b>Palancas abajo = sin frenos.</b> 425 lb se ir&aacute;n solas en cualquier rampa o pendiente y no se pueden detener a mano.",
    ret_h="Devoluci&oacute;n de la silla",
    ret="""
      <li>Devu&eacute;lvala <b>en la puerta del avi&oacute;n</b> — el propietario no puede caminar y no tiene otra movilidad.</li>
      <li>Confirme que <b>ambas palancas de rueda libre est&eacute;n arriba</b> antes de que el propietario se siente.</li>
      <li>Devuelva todas las piezas que se hayan retirado, incluido el reposacabezas.</li>
      <li>Informe cualquier da&ntilde;o <b>antes</b> de que el propietario salga de la puerta de embarque.</li>""",
    contact_h="Contactos",
    c_owner="propietario", c_owner_note="Llame primero para cualquier asunto de esta silla",
    c_backup="contacto alterno", c_backup_note="Si no logra comunicarse con el propietario",
    rights_h="Derechos del propietario — 14 CFR Parte 382",
    rights="""
      <li><b>§ 382.125</b> — Las sillas de ruedas tienen <i>prioridad de estiba en la bodega de equipaje sobre cualquier otra carga</i>, y deben devolverse <i>lo m&aacute;s cerca posible de la puerta del avi&oacute;n</i>.</li>
      <li><b>§ 382.127</b> — No se puede exigir el retiro de una bater&iacute;a no derramable etiquetada por el fabricante; el transportista no debe desconectar una bater&iacute;a no derramable dentro de su carcasa, ni descargar las bater&iacute;as.</li>
      <li><b>§ 382.129</b> — El pasajero puede entregar <b>instrucciones escritas</b> de desmontaje y montaje, que el transportista debe seguir en la medida de lo posible. <b>Esta tarjeta es esa instrucci&oacute;n escrita.</b> El equipo debe devolverse <i>en las mismas condiciones en que se recibi&oacute;</i>.</li>""",
    footer="Manual del fabricante: quantumrehab.com/pdf/owners-manuals/us_uk_au_q6_edge_2.0_2.0x_3_2.0hd_series_om.pdf · Quantum Rehab, 401 York Ave, Duryea PA 18642 · Fabricada en 2023, entregada el 13 dic 2023 · Escanee el c&oacute;digo QR para las instrucciones completas. · <b>Imprimir a doble cara, girando por el borde LARGO</b>, para que las marcas coincidan.",
)

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

for name, data in (("sheet-en", EN), ("sheet-es", ES)):
    html = TEMPLATE.format(css=CSS.replace("%(zoom)s", data["zoom"]), **data)
    open(f"{name}.html", "w").write(html)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={name}.pdf", f"{name}.html"],
                   capture_output=True)
    pages = subprocess.run(["pdfinfo", f"{name}.pdf"], capture_output=True, text=True).stdout
    print(name, [l for l in pages.split("\n") if l.startswith("Pages")])

subprocess.run(["pdfunite", "sheet-en.pdf", "sheet-es.pdf", "Wheelchair Handling Sheet.pdf"], check=True)
print("merged ->", os.path.getsize("Wheelchair Handling Sheet.pdf"), "bytes")
