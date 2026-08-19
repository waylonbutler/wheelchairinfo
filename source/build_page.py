#!/usr/bin/env python3
"""Build the self-contained bilingual wheelchair info page (index.html)."""
import base64, os

def b64(path):
    mime = "image/jpeg" if path.lower().endswith((".jpg", ".jpeg")) else "image/png"
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()

IMGS = {
    "freewheel": (b64("img-freewheel.png"), 611 / 760),
    "brackets": (b64("img-brackets.png"), 532 / 760),
    "iso": (b64("img-points-iso.png"), 713 / 655),
    "plan": (b64("img-points-plan.png"), 874 / 530),
    "breaker": (b64("img-breaker.jpg"), 636 / 760),
    "ctrl": (b64("img-controller.jpg"), 864 / 760),
}

IMG_CSS = "\n".join(
    f".fig-{k}{{padding-top:{r*100:.2f}%;background-image:url({d})}}"
    for k, (d, r) in IMGS.items()
)

# ---------------------------------------------------------------- content ----

EN = """
<header class="top">
  <div class="kicker">Do not remove — handling instructions</div>
  <h1>Power Wheelchair<br>Handling &amp; Airline Information</h1>
  <p class="sub">Quantum Rehab Q6 Edge 3 · Serial <strong>JE733123218020</strong> · Owner: Waylon Butler</p>
</header>

<div class="band">
  <h2>Five rules — please read before touching this chair</h2>
  <ol>
    <li><strong>Keep it upright at all times.</strong> Never lay it on its side, its back, or its end. The seat is rigid — it does not fold flat, and side-loading will damage the seating system.</li>
    <li><strong>Lift only by the solid metal frame of the power base</strong>, below the seat. Never by the armrests, footplate, joystick, headrest, seat back, or the yellow freewheel levers.</li>
    <li><strong>Turn the power OFF at the joystick before moving it.</strong> Then use freewheel mode (below) and push by the two poles on the back of the seat. Do not force it against the motors.</li>
    <li><strong>Only put it in freewheel on level ground.</strong> Freewheel releases the brakes. On any slope the chair will roll away on its own.</li>
    <li><strong>The batteries stay in the chair.</strong> They are sealed, non-spillable gel-cell batteries. Do not disconnect, remove, or drain them.</li>
  </ol>
</div>

<div class="okband">
  <h2>Battery statement for check-in</h2>
  <p style="margin:0">This chair uses <strong>two 12-volt NF-22 sealed gel-cell (non-spillable) batteries</strong>, factory-installed, enclosed in the battery tray with terminals protected. There is <strong>no lithium battery</strong> on this chair.</p>
  <p style="margin:8px 0 0">Under <strong>49 CFR 175.10(a)(15)</strong> and <strong>14 CFR 382.127</strong>, non-spillable batteries may remain installed and connected, and carriers <strong>must not</strong> remove, disconnect, or drain them.</p>
</div>

<h2>Chair specifications</h2>
<table>
  <tr><th>Make / model</th><td>Quantum Rehab Q6 Edge 3, mid-wheel drive power base</td></tr>
  <tr><th>Serial number</th><td>JE733123218020 · manufactured 2023</td></tr>
  <tr><th>Total weight</th><td><strong>425 lbs (193 kg)</strong> as configured</td></tr>
  <tr><th>Width</th><td><strong>24 in (61 cm)</strong> — the drive wheels are the widest point. The armrests do not extend past them.</td></tr>
  <tr><th>Length</th><td>39 in (99 cm) with the footplate folded up</td></tr>
  <tr><th>Height</th><td>40 in (102 cm) with the headrest removed. The owner removes the headrest before travel.</td></tr>
  <tr><th>Ground clearance</th><td>2.7 in (69 mm) at the battery tray — needs a ramp, will not clear a curb</td></tr>
  <tr><th>Seating system</th><td>TRU-Balance 3 power tilt, recline, and 12 in power seat lift. <strong>Rigid — does not fold or collapse.</strong></td></tr>
  <tr><th>Seat / back</th><td>17 in wide × 20 in deep seat; 17 in × 23 in back. ROHO Hybrid Elite SR air cushion.</td></tr>
  <tr><th>Batteries</th><td>Two 12 V NF-22 sealed gel-cell, non-spillable, ~38 lbs each, installed in the base</td></tr>
  <tr><th>Charger</th><td>8-amp off-board charger — travels with the owner, not with the chair</td></tr>
</table>

<h2>What comes apart — and what does not</h2>
<p>The owner prepares the chair before handing it over: <strong>headrest removed, joystick swung in and secured, footplate folded up.</strong> It arrives at the aircraft ready to load.</p>
<ul>
  <li><strong>Nothing else on this chair comes apart for transport.</strong> Do not remove the seat, seat back, armrests, tilt or recline actuators, seat lift column, wheels, or batteries.</li>
  <li><strong>The seat back is bolted to the frame.</strong> It does not fold, flip forward, or drop out of the way. There is no pin and no release lever — <strong>do not try to force it down.</strong> (Verified on this chair, not assumed from the model.)</li>
  <li>The armrests are <strong>fixed-width</strong>. Moving them does not make the chair narrower — 24 in is the width, measured at the drive wheels.</li>
  <li>The joystick is <strong>not quickly removable</strong>. It is swung in and secured. It is the most easily damaged part of the chair; nothing should press against it.</li>
</ul>
<blockquote>From the manufacturer's manual: “Do not attempt to lift or move your power chair or seating system by any of its removable parts, including the armrest(s), front rigging(s), seat cushions, seatback, shrouds, or controller. Use only solid, non-removable frame components.”</blockquote>

<h2>Moving the chair without power (freewheel mode)</h2>
<p>Freewheel lets you push the chair by hand. It also <strong>releases the brakes completely</strong>.</p>
<ol>
  <li>Bring the chair to <strong>level ground</strong> and make sure nobody is seated in it.</li>
  <li><strong>Turn the power off</strong> at the joystick. Skipping this will throw a controller error code.</li>
  <li>Find the two <strong>yellow freewheel levers</strong> — one on each drive motor, at the middle of the chair behind the drive wheels. <strong>Push both levers down.</strong></li>
  <li>Push using the <strong>two upright poles on the back of the seat</strong> — they are there to be used as push handles. Two people. <strong>Push only; do not lift by them.</strong> Never push or pull by the joystick, the armrests, the headrest, or the footplate.</li>
  <li>When in position, <strong>pull both levers back up</strong> to re-engage the motors and restore the brakes. Confirm both are up before leaving the chair.</li>
</ol>
<figure><div class="fig fig-freewheel"></div><figcaption>Levers <strong>down</strong> = freewheel, motors disengaged, no brakes. Levers <strong>up</strong> = drive mode, brakes holding. On this chair the levers are <strong>yellow</strong>. <span class="src">Quantum Rehab owner's manual, figure 2</span></figcaption></figure>
<div class="warnbox"><strong>Warning:</strong> With the levers down, the chair has no brakes and weighs 425 lbs. On a ramp or an incline it will roll away and cannot be stopped by hand.</div>

<h2>The controller — turning the chair on and off</h2>
<p>The control unit is the joystick on the <strong>left armrest</strong>, on a swing-away mount.</p>
<figure><div class="fig fig-ctrl"></div><figcaption>Q-Logic 3 controller. <span class="src">Manufacturer image, shown for identification.</span></figcaption></figure>
<ol class="legend">
  <li><strong>On/off toggle</strong>, on the left side of the controller. <strong>Push it forward to turn the system on. Push it back to turn it off.</strong></li>
  <li><strong>Drive mode</strong> — the leftmost round button, marked <strong>1</strong>.</li>
  <li><strong>Green indicator and screen.</strong> Lit means the system is on. Dark means it is off.</li>
</ol>
<ul>
  <li><strong>The chair should travel powered OFF.</strong> Push the toggle back and confirm the green indicator and screen go dark.</li>
  <li><strong>If the joystick gets bumped while the system is on, the chair can drive itself.</strong> That is the reason it travels off, and the reason nothing should rest against the joystick.</li>
  <li><strong>Turning the power off does not release the brakes.</strong> The brakes stay engaged. Releasing them is a separate action — the yellow freewheel levers, above.</li>
  <li>If the system was switched on and the chair will not drive, it may be out of drive mode. Press button <strong>1</strong>. Do not drive this chair — this is here only so you can recognise the state and tell the owner.</li>
  <li>Do not use the joystick or its bracket as a handhold or a lift point. The manufacturer lists them as non-load-bearing.</li>
</ul>
<h3>If it will not power on after transport</h3>
<p>The <strong>main circuit breaker</strong> may have tripped. It is the small round button on the side of the power base, directly <strong>below the EDGE 3 logo</strong>. Let the chair rest about a minute, <strong>press the button back in</strong>, then switch the controller on. If it trips again straight away, stop and call the owner.</p>
<figure><div class="fig fig-breaker"></div><figcaption><strong>1</strong> — main circuit breaker reset, below the EDGE 3 logo. <strong>2</strong> — one of the two yellow freewheel levers. <strong>Nothing else in this area should be touched.</strong> <span class="src">Photograph of this chair.</span></figcaption></figure>

<h2>Securing the chair — use the four tie-down points</h2>
<p>This chair has <strong>four labeled securement points</strong> built into the power base — two front, two rear — marked with <strong>anchor symbols</strong>. These are the only correct attachment points.</p>
<ul>
  <li><strong>Use all four.</strong> Do not improvise straps around frame tubes when the labeled points are right there.</li>
  <li>Stow <strong>upright, wheels down</strong>, facing forward. Do not stack cargo on the seat, the back, or the joystick.</li>
  <li><strong>Never attach a strap to</strong> the yellow freewheel levers, armrests, footplate, joystick, headrest, seat back, wheels, or any adjustable or removable part.</li>
  <li>Leave the freewheel levers <strong>up</strong> (drive mode) so the brakes hold, unless you are actively rolling the chair.</li>
  <li><strong>Never raise or elevate the seat</strong> while the chair is secured for transport.</li>
</ul>
<figure><div class="fig fig-brackets"></div><figcaption>The securement brackets are the flat looped tabs low on the power base, 2 of 4 shown. <span class="src">Quantum Rehab owner's manual, figure 12</span></figcaption></figure>
<figure><div class="fig fig-iso"></div><figcaption>All four points in use — front straps angled forward and out, rear straps angled back. <span class="src">Quantum Rehab owner's manual, figure 13</span></figcaption></figure>
<figure><div class="fig fig-plan"></div><figcaption>Plan view. Front tie-downs anchor <strong>wider</strong> than the chair for stability; rear tie-downs anchor directly behind the rear points. <span class="src">Quantum Rehab owner's manual, figure 13</span></figcaption></figure>

<h2>Returning the chair</h2>
<ul>
  <li>Return it <strong>at the aircraft door</strong> — the owner cannot walk and has no other mobility.</li>
  <li>Confirm <strong>both freewheel levers are up</strong> before the owner transfers in.</li>
  <li>Return every part that came off the chair, including the headrest.</li>
  <li>If any part is missing or damaged, tell the owner <strong>before</strong> they leave the gate area.</li>
</ul>

<h2>If the chair is damaged</h2>
<ol>
  <li>Report it to the airline <strong>at the airport, before leaving</strong>, and get a written damage report.</li>
  <li>Photograph the damage at the gate.</li>
  <li>Under <strong>14 CFR 382.129</strong>, the carrier must return the device in the condition in which it was received.</li>
</ol>

<h2>Contacts</h2>
<div class="contact">
  <div class="who">Waylon Butler — owner</div>
  <div class="role">Call first for anything involving this chair</div>
  <a class="tel" href="tel:+16317729702">+1 (631) 772-9702</a>
</div>
<div class="contact">
  <div class="who">Danielle Butler — backup contact</div>
  <div class="role">If the owner cannot be reached</div>
  <a class="tel" href="tel:+17039678487">+1 (703) 967-8487</a>
</div>

<h2>Owner's rights under 14 CFR Part 382</h2>
<ul>
  <li><strong>§ 382.125</strong> — Wheelchairs get <em>priority for stowage in the baggage compartment over other cargo and baggage</em>, and must be returned <em>as close as possible to the door of the aircraft</em>.</li>
  <li><strong>§ 382.127</strong> — A manufacturer-labeled non-spillable battery <strong>may not be required to be removed</strong>. Carriers <em>must not</em> disconnect a non-spillable battery enclosed in a case, and <em>must not drain batteries</em>.</li>
  <li><strong>§ 382.129</strong> — The passenger may <strong>provide written directions</strong> for disassembly and reassembly, and the carrier must follow them to the greatest extent feasible. <em>This page is that written direction.</em> The device must be returned <em>in the condition in which you received it</em>.</li>
</ul>

<h2>Full documentation</h2>
<p>Manufacturer owner's manual, Q6 Edge 2.0 / 2.0x / <strong>3</strong> / 2.0HD series:<br>
<a href="https://www.quantumrehab.com/pdf/owners-manuals/us_uk_au_q6_edge_2.0_2.0x_3_2.0hd_series_om.pdf">quantumrehab.com — owner's manual (PDF)</a></p>
<p>TRU-Balance 3 power positioning system, basic operation instructions:<br>
<a href="https://www.quantumrehab.com/pdf/basic-operation-instructions/us_tru-balance_3_power_positioning_systems_boi.pdf">quantumrehab.com — TRU-Balance 3 instructions (PDF)</a></p>

<footer>Quantum Rehab, 401 York Avenue, Duryea, PA 18642 · Serial JE733123218020 · delivered 13 Dec 2023. Diagrams reproduced from the Quantum Rehab owner's manual for handling reference.</footer>
"""

ES = """
<header class="top">
  <div class="kicker">No retirar — instrucciones de manejo</div>
  <h1>Silla de Ruedas Eléctrica<br>Manejo e Información de Vuelo</h1>
  <p class="sub">Quantum Rehab Q6 Edge 3 · N.º de serie <strong>JE733123218020</strong> · Propietario: Waylon Butler</p>
</header>

<div class="band">
  <h2>Cinco reglas — lea antes de tocar esta silla</h2>
  <ol>
    <li><strong>Manténgala en posición vertical en todo momento.</strong> Nunca la acueste de lado, sobre el respaldo ni de punta. El asiento es rígido: no se pliega, y cargarla de costado dañará el sistema de asiento.</li>
    <li><strong>Levántela únicamente por el bastidor metálico sólido de la base</strong>, debajo del asiento. Nunca por los apoyabrazos, el reposapiés, el joystick, el reposacabezas, el respaldo ni las palancas amarillas de rueda libre.</li>
    <li><strong>Apague la silla en el joystick antes de moverla.</strong> Luego use el modo de rueda libre (abajo) y empuje por los dos postes del respaldo. No la empuje contra los motores.</li>
    <li><strong>Use la rueda libre solo en terreno plano.</strong> La rueda libre libera los frenos. En cualquier pendiente, la silla se irá sola.</li>
    <li><strong>Las baterías permanecen en la silla.</strong> Son de gel selladas, no derramables. No las desconecte, retire ni descargue.</li>
  </ol>
</div>

<div class="okband">
  <h2>Declaración de batería para el mostrador</h2>
  <p style="margin:0">Esta silla usa <strong>dos baterías NF-22 de 12 voltios, de gel selladas (no derramables)</strong>, instaladas de fábrica, dentro de la bandeja cerrada y con los bornes protegidos. Esta silla <strong>no lleva batería de litio</strong>.</p>
  <p style="margin:8px 0 0">Según <strong>49 CFR 175.10(a)(15)</strong> y <strong>14 CFR 382.127</strong>, las baterías no derramables pueden permanecer instaladas y conectadas, y el transportista <strong>no debe</strong> retirarlas, desconectarlas ni descargarlas.</p>
</div>

<h2>Especificaciones de la silla</h2>
<table>
  <tr><th>Marca / modelo</th><td>Quantum Rehab Q6 Edge 3, base con tracción central</td></tr>
  <tr><th>N.º de serie</th><td>JE733123218020 · fabricada en 2023</td></tr>
  <tr><th>Peso total</th><td><strong>425 lb (193 kg)</strong> en su configuración actual</td></tr>
  <tr><th>Ancho</th><td><strong>24 pulg (61 cm)</strong> — las ruedas motrices son el punto más ancho. Los apoyabrazos no sobresalen.</td></tr>
  <tr><th>Largo</th><td>39 pulg (99 cm) con el reposapiés plegado hacia arriba</td></tr>
  <tr><th>Altura</th><td>40 pulg (102 cm) sin el reposacabezas. El propietario lo retira antes de viajar.</td></tr>
  <tr><th>Altura libre al suelo</th><td>2.7 pulg (69 mm) en la bandeja de baterías — requiere rampa; no sube un bordillo</td></tr>
  <tr><th>Sistema de asiento</th><td>TRU-Balance 3 con inclinación, reclinación y elevación eléctrica de 12 pulg. <strong>Rígido: no se pliega.</strong></td></tr>
  <tr><th>Asiento / respaldo</th><td>Asiento de 17 pulg de ancho × 20 pulg de fondo; respaldo de 17 × 23 pulg. Cojín de aire ROHO Hybrid Elite SR.</td></tr>
  <tr><th>Baterías</th><td>Dos de 12 V NF-22, gel sellado, no derramables, ~38 lb cada una, dentro de la base</td></tr>
  <tr><th>Cargador</th><td>Cargador externo de 8 A — viaja con el propietario, no con la silla</td></tr>
</table>

<h2>Qué se desmonta — y qué no</h2>
<p>El propietario prepara la silla antes de entregarla: <strong>reposacabezas retirado, joystick girado hacia adentro y asegurado, reposapiés plegado hacia arriba.</strong> Llega al avión lista para cargar.</p>
<ul>
  <li><strong>Nada más en esta silla se desmonta para el transporte.</strong> No retire el asiento, el respaldo, los apoyabrazos, los actuadores de inclinación o reclinación, la columna de elevación, las ruedas ni las baterías.</li>
  <li><strong>El respaldo está atornillado al bastidor.</strong> No se pliega, no se abate hacia adelante ni se retira. No hay pasador ni palanca de liberación — <strong>no intente forzarlo.</strong> (Verificado en esta silla, no supuesto por el modelo.)</li>
  <li>Los apoyabrazos son de <strong>ancho fijo</strong>. Moverlos no hace la silla más angosta: el ancho es 24 pulg, medido en las ruedas motrices.</li>
  <li>El joystick <strong>no se quita rápidamente</strong>. Va girado hacia adentro y asegurado. Es la pieza que se daña con más facilidad; nada debe presionar contra él.</li>
</ul>
<blockquote>Del manual del fabricante: “No intente levantar ni mover la silla o el sistema de asiento por ninguna de sus piezas desmontables, incluidos los apoyabrazos, los soportes delanteros, los cojines, el respaldo, las cubiertas o el control. Use únicamente componentes sólidos y no desmontables del bastidor.”</blockquote>

<h2>Mover la silla sin motor (modo de rueda libre)</h2>
<p>La rueda libre permite empujar la silla a mano. También <strong>libera los frenos por completo</strong>.</p>
<ol>
  <li>Lleve la silla a <strong>terreno plano</strong> y asegúrese de que nadie esté sentado en ella.</li>
  <li><strong>Apague la silla</strong> en el joystick. Si no lo hace, el control mostrará un código de error.</li>
  <li>Localice las dos <strong>palancas amarillas de rueda libre</strong> — una en cada motor, al centro de la silla, detrás de las ruedas motrices. <strong>Baje ambas palancas.</strong></li>
  <li>Empuje usando los <strong>dos postes verticales del respaldo</strong> — están para usarse como agarraderas. Dos personas. <strong>Solo empuje; no levante la silla por ellos.</strong> Nunca empuje ni jale por el joystick, los apoyabrazos, el reposacabezas ni el reposapiés.</li>
  <li>Ya colocada, <strong>suba ambas palancas</strong> para volver a acoplar los motores y restablecer los frenos. Confirme que ambas estén arriba antes de dejar la silla.</li>
</ol>
<figure><div class="fig fig-freewheel"></div><figcaption>Palancas <strong>abajo</strong> = rueda libre, motores desacoplados, sin frenos. Palancas <strong>arriba</strong> = modo de conducción, frenos activos. En esta silla las palancas son <strong>amarillas</strong>. <span class="src">Manual Quantum Rehab, figura 2</span></figcaption></figure>
<div class="warnbox"><strong>Advertencia:</strong> Con las palancas abajo, la silla no tiene frenos y pesa 425 lb. En una rampa o pendiente se irá sola y no se puede detener a mano.</div>

<h2>El control — encender y apagar la silla</h2>
<p>La unidad de control es el joystick en el <strong>apoyabrazos izquierdo</strong>, sobre un soporte abatible.</p>
<figure><div class="fig fig-ctrl"></div><figcaption>Control Q-Logic 3. <span class="src">Imagen del fabricante, mostrada para identificación.</span></figcaption></figure>
<ol class="legend">
  <li><strong>Interruptor de encendido/apagado</strong>, en el lado izquierdo del control. <strong>Empújelo hacia adelante para encender. Empújelo hacia atrás para apagar.</strong></li>
  <li><strong>Modo de conducción</strong> — el botón redondo del extremo izquierdo, marcado con <strong>1</strong>.</li>
  <li><strong>Indicador verde y pantalla.</strong> Encendidos significa que el sistema está activo. Apagados significa que está apagado.</li>
</ol>
<ul>
  <li><strong>La silla debe viajar APAGADA.</strong> Empuje el interruptor hacia atrás y confirme que el indicador verde y la pantalla se apaguen.</li>
  <li><strong>Si el joystick recibe un golpe con el sistema encendido, la silla puede moverse sola.</strong> Por eso viaja apagada, y por eso nada debe apoyarse contra el joystick.</li>
  <li><strong>Apagar la silla no libera los frenos.</strong> Los frenos siguen aplicados. Liberarlos es una acción distinta: las palancas amarillas de rueda libre, arriba.</li>
  <li>Si el sistema está encendido y la silla no avanza, puede estar fuera del modo de conducción. Presione el botón <strong>1</strong>. No conduzca esta silla — esto se indica solo para que reconozca el estado y avise al propietario.</li>
  <li>No use el joystick ni su soporte como agarradera ni como punto de levante. El fabricante los indica como piezas que no soportan carga.</li>
</ul>
<h3>Si no enciende después del transporte</h3>
<p>Puede haberse disparado el <strong>disyuntor principal</strong>. Es el botón redondo pequeño en el costado de la base, justo <strong>debajo del logotipo EDGE 3</strong>. Deje reposar la silla alrededor de un minuto, <strong>vuelva a presionar el botón</strong> y encienda el control. Si se dispara otra vez de inmediato, deténgase y llame al propietario.</p>
<figure><div class="fig fig-breaker"></div><figcaption><strong>1</strong> — disyuntor principal, debajo del logotipo EDGE 3. <strong>2</strong> — una de las dos palancas amarillas de rueda libre. <strong>No toque nada más en esta zona.</strong> <span class="src">Fotografía de esta silla.</span></figcaption></figure>

<h2>Sujeción de la silla — use los cuatro puntos de anclaje</h2>
<p>Esta silla tiene <strong>cuatro puntos de anclaje identificados</strong> en la base — dos delanteros y dos traseros — marcados con <strong>símbolos de ancla</strong>. Son los únicos puntos correctos de sujeción.</p>
<ul>
  <li><strong>Use los cuatro.</strong> No improvise correas alrededor de los tubos del bastidor cuando los puntos identificados están ahí.</li>
  <li>Estíbela <strong>en posición vertical, sobre las ruedas</strong>, mirando hacia adelante. No apile carga sobre el asiento, el respaldo ni el joystick.</li>
  <li><strong>Nunca sujete una correa a</strong> las palancas amarillas de rueda libre, los apoyabrazos, el reposapiés, el joystick, el reposacabezas, el respaldo, las ruedas ni ninguna pieza ajustable o desmontable.</li>
  <li>Deje las palancas de rueda libre <strong>arriba</strong> (modo de conducción) para que los frenos sujeten, salvo mientras esté rodando la silla.</li>
  <li><strong>Nunca eleve el asiento</strong> mientras la silla esté sujeta para el transporte.</li>
</ul>
<figure><div class="fig fig-brackets"></div><figcaption>Los soportes de anclaje son las lengüetas planas con argolla, en la parte baja de la base; se muestran 2 de 4. <span class="src">Manual Quantum Rehab, figura 12</span></figcaption></figure>
<figure><div class="fig fig-iso"></div><figcaption>Los cuatro puntos en uso — correas delanteras hacia adelante y afuera, correas traseras hacia atrás. <span class="src">Manual Quantum Rehab, figura 13</span></figcaption></figure>
<figure><div class="fig fig-plan"></div><figcaption>Vista superior. Los anclajes delanteros se fijan <strong>más anchos</strong> que la silla para dar estabilidad; los traseros, directamente detrás de los puntos traseros. <span class="src">Manual Quantum Rehab, figura 13</span></figcaption></figure>

<h2>Devolución de la silla</h2>
<ul>
  <li>Devuélvala <strong>en la puerta del avión</strong> — el propietario no puede caminar y no tiene otra movilidad.</li>
  <li>Confirme que <strong>ambas palancas de rueda libre estén arriba</strong> antes de que el propietario se siente.</li>
  <li>Devuelva todas las piezas que se hayan retirado, incluido el reposacabezas.</li>
  <li>Si falta alguna pieza o hay daños, informe al propietario <strong>antes</strong> de que salga de la puerta de embarque.</li>
</ul>

<h2>Si la silla sufre daños</h2>
<ol>
  <li>Repórtelo a la aerolínea <strong>en el aeropuerto, antes de salir</strong>, y obtenga un informe de daños por escrito.</li>
  <li>Fotografíe los daños en la puerta de embarque.</li>
  <li>Según <strong>14 CFR 382.129</strong>, el transportista debe devolver el equipo en las mismas condiciones en que lo recibió.</li>
</ol>

<h2>Contactos</h2>
<div class="contact">
  <div class="who">Waylon Butler — propietario</div>
  <div class="role">Llame primero para cualquier asunto de esta silla</div>
  <a class="tel" href="tel:+16317729702">+1 (631) 772-9702</a>
</div>
<div class="contact">
  <div class="who">Danielle Butler — contacto alterno</div>
  <div class="role">Si no logra comunicarse con el propietario</div>
  <a class="tel" href="tel:+17039678487">+1 (703) 967-8487</a>
</div>

<h2>Derechos del propietario — 14 CFR Parte 382</h2>
<ul>
  <li><strong>§ 382.125</strong> — Las sillas de ruedas tienen <em>prioridad de estiba en la bodega de equipaje sobre cualquier otra carga</em>, y deben devolverse <em>lo más cerca posible de la puerta del avión</em>.</li>
  <li><strong>§ 382.127</strong> — No se puede exigir el retiro de una batería no derramable etiquetada por el fabricante. El transportista <em>no debe</em> desconectar una batería no derramable dentro de su carcasa, ni <em>descargar las baterías</em>.</li>
  <li><strong>§ 382.129</strong> — El pasajero puede <strong>entregar instrucciones escritas</strong> de desmontaje y montaje, que el transportista debe seguir en la medida de lo posible. <em>Esta página es esa instrucción escrita.</em> El equipo debe devolverse <em>en las mismas condiciones en que se recibió</em>.</li>
</ul>

<h2>Documentación completa</h2>
<p>Manual del propietario, serie Q6 Edge 2.0 / 2.0x / <strong>3</strong> / 2.0HD:<br>
<a href="https://www.quantumrehab.com/pdf/owners-manuals/us_uk_au_q6_edge_2.0_2.0x_3_2.0hd_series_om.pdf">quantumrehab.com — manual del propietario (PDF, en inglés)</a></p>
<p>Sistema TRU-Balance 3, instrucciones básicas de operación:<br>
<a href="https://www.quantumrehab.com/pdf/basic-operation-instructions/us_tru-balance_3_power_positioning_systems_boi.pdf">quantumrehab.com — instrucciones TRU-Balance 3 (PDF, en inglés)</a></p>

<footer>Quantum Rehab, 401 York Avenue, Duryea, PA 18642 · N.º de serie JE733123218020 · entregada el 13 dic 2023. Diagramas reproducidos del manual del propietario de Quantum Rehab como referencia de manejo.</footer>
"""

# ------------------------------------------------------------------- page ----

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Power Wheelchair — Handling Instructions</title>
<meta name="description" content="Airline and baggage handling instructions for a Quantum Q6 Edge 3 power wheelchair. Serial JE733123218020.">
<style>
  :root{
    --ink:#12161c; --muted:#4a5461; --line:#d9dee5; --bg:#ffffff;
    --alert:#a4161a; --alert-bg:#fdf0f0; --alert-line:#e8b4b6;
    --ok:#1b5e4a; --ok-bg:#eef6f2; --ok-line:#b7d9cb;
    --note-bg:#f4f6f9;
  }
  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{margin:0;background:var(--bg);color:var(--ink);
    font:17px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  .wrap{max-width:780px;margin:0 auto;padding:0 18px 64px}
  .langbar{position:sticky;top:0;z-index:10;background:#fff;border-bottom:1px solid var(--line);
    margin:0 -18px 18px;padding:9px 18px;display:flex;gap:8px;align-items:center}
  .langbar button{font:600 14px/1 inherit;padding:8px 16px;border:1px solid var(--line);
    background:#fff;color:var(--muted);border-radius:999px;cursor:pointer}
  .langbar button[aria-pressed="true"]{background:var(--ink);color:#fff;border-color:var(--ink)}
  header.top{border-bottom:3px solid var(--ink);padding-bottom:14px;margin-bottom:22px}
  .kicker{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:700}
  h1{font-size:29px;line-height:1.15;margin:6px 0 8px;letter-spacing:-.01em}
  .sub{font-size:16px;color:var(--muted);margin:0}
  h2{font-size:20px;margin:34px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line);letter-spacing:-.01em}
  h3{font-size:16.5px;margin:22px 0 6px;letter-spacing:-.005em}
  ol.legend{list-style:none;padding-left:0;margin:0 0 16px;counter-reset:cl}
  ol.legend li{position:relative;padding-left:36px;margin-bottom:10px;counter-increment:cl}
  ol.legend li::before{content:counter(cl);position:absolute;left:0;top:2px;
    width:25px;height:25px;border-radius:50%;background:var(--alert);color:#fff;
    font:700 14px/25px -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    text-align:center}
  p{margin:0 0 12px}
  ul,ol{margin:0 0 12px;padding-left:22px}
  li{margin:0 0 7px}
  .band{background:var(--alert-bg);border:2px solid var(--alert-line);border-left:8px solid var(--alert);
    border-radius:6px;padding:16px 18px;margin:0 0 22px}
  .band h2{color:var(--alert);border:0;margin:0 0 10px;padding:0;font-size:19px}
  .band ol{margin:0;padding-left:20px}
  .band li{margin-bottom:9px}
  .okband{background:var(--ok-bg);border:1px solid var(--ok-line);border-left:8px solid var(--ok);
    border-radius:6px;padding:14px 18px;margin:0 0 20px}
  .okband h2{color:var(--ok);border:0;margin:0 0 8px;padding:0;font-size:18px}
  .warnbox{background:var(--alert-bg);border:1px solid var(--alert-line);border-radius:6px;
    padding:12px 16px;margin:0 0 16px}
  blockquote{margin:0 0 16px;padding:12px 16px;background:var(--note-bg);
    border-left:4px solid #8b95a1;font-style:italic;font-size:16px}
  table{width:100%;border-collapse:collapse;margin:0 0 16px;font-size:15.5px}
  th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
  th{width:40%;font-weight:600;color:var(--muted)}
  figure{margin:0 0 20px}
  .fig{width:100%;height:0;background-repeat:no-repeat;background-size:100% auto;
    background-position:center;border:1px solid var(--line);border-radius:6px;background-color:#fff}
  figcaption{font-size:14.5px;color:var(--muted);margin-top:7px;line-height:1.45}
  .src{display:block;font-size:12.5px;opacity:.75;margin-top:2px}
  .contact{background:var(--note-bg);border:1px solid var(--line);border-radius:6px;padding:14px 16px;margin:0 0 14px}
  .contact .who{font-weight:700;font-size:16px}
  .contact .role{color:var(--muted);font-size:14px;margin-bottom:6px}
  .contact .fine{font-size:14px;color:var(--muted);margin-top:4px}
  a{color:#0b4f8a}
  a.tel{font-size:22px;font-weight:700;text-decoration:none;display:inline-block;padding:2px 0}
  footer{margin-top:40px;padding-top:14px;border-top:1px solid var(--line);font-size:13.5px;color:var(--muted)}
  [hidden]{display:none}
  @media print{
    body{font-size:11pt}
    .wrap{max-width:none;padding:0}
    .langbar{display:none}
    h2{page-break-after:avoid}
    .band,.okband,table,figure{page-break-inside:avoid}
    a{color:#000;text-decoration:none}
  }
__IMGCSS__
</style>
</head>
<body>
<div class="wrap">
  <div class="langbar">
    <button id="b-en" aria-pressed="true" onclick="setLang('en')">English</button>
    <button id="b-es" aria-pressed="false" onclick="setLang('es')">Espa&ntilde;ol</button>
  </div>
  <div id="en">__EN__</div>
  <div id="es" hidden>__ES__</div>
</div>
<script>
function setLang(l){
  var other = l === 'en' ? 'es' : 'en';
  document.getElementById(l).hidden = false;
  document.getElementById(other).hidden = true;
  document.getElementById('b-' + l).setAttribute('aria-pressed', 'true');
  document.getElementById('b-' + other).setAttribute('aria-pressed', 'false');
  document.documentElement.lang = l;
  window.scrollTo(0, 0);
}
if ((navigator.language || '').toLowerCase().indexOf('es') === 0) { setLang('es'); }
</script>
</body>
</html>
"""

out = PAGE.replace("__IMGCSS__", IMG_CSS).replace("__EN__", EN).replace("__ES__", ES)
open("index.html", "w").write(out)
print("index.html ->", os.path.getsize("index.html"), "bytes")
