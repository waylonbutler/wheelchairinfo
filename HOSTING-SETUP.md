# Wheelchair handling card — reference and upkeep

**Live page:** <https://waylonbutler.github.io/wheelchairinfo/>
**Repo:** `waylonbutler/wheelchairinfo` · **Status:** live, current, QR codes point to it.

## What's in this set

| File | What it is |
|---|---|
| `index.html` | The page the QR code opens. Bilingual (English / Español toggle), fully self-contained — every diagram and photo is embedded, no external files. |
| `Wheelchair Handling Sheet.pdf` | 8.5×11, two pages. Page 1 English, page 2 Spanish. Print double-sided, laminate, punch, hang on the chair. |
| `Wheelchair QR Sticker.pdf` | **Page 1 is 6×3 in** — the one to use. Page 2 is a 4×2 in compact fallback. Both are 2:1 landscape to fit the flat panel on the seat back. |
| `README.md` | File-by-file overview and syncing notes. |
| `make-qr.py` | Regenerates `qr.png` if the URL ever changes. |
| `build_page.py` / `build_sheet.py` / `build_sticker.py` | Generators. All text lives in plain Python dicts at the top, English and Spanish side by side. |
| `annotate_controller.py` | Redraws the numbered callouts on the controller photo. |
| `annotate_breaker.py` | Redraws the numbered callouts on the circuit-breaker photo. |
| `rebuild.sh` | Runs every generator above and copies the results up a level. |

The whole folder — page, PDFs, docs, and `source/` — lives in the GitHub repo
now; it's the complete archive, not just a place to drop `index.html`.

---

## Printing the sheet

Designed as a laminated hang tag.

1. Print **double-sided**, and in the printer dialog choose **flip on LONG edge** (a.k.a. "long-edge binding"). Short-edge flip rotates the back 180° and the two punch targets end up at opposite corners.
2. Print at **100% / "Actual size"** — not "Fit to page," which shrinks everything and moves the punch marks.
3. **Check before laminating:** hold the sheet up to a light. The red target on the front should sit directly over the one on the back. They're at 0.80 in from the side edge and 0.66 in from the bottom on both sides.
4. **Scan-test the QR with your phone** while it's still bare paper. Verifying the file is not the same as verifying your printer.
5. **Laminate**, leaving the full sealed border — don't trim close.
6. **Punch through the target** with a standard ¼ in single-hole punch. The printed circle is sized so the punch takes most of it away.
7. **Attach with a zip tie or split ring**, not string — string abrades and the tag walks. A metal eyelet adds durability.

Print a fresh copy each trip. A legible card gets read; a weathered one gets ignored.

## Printing the sticker

Use **page 1 (6×3 in)** — QR, English, and Spanish in three columns, full rule set. Page 2 (4×2 in) is the fallback if the space is tighter than expected.

Print at **100% / "Actual size"** on full-sheet label stock and cut to the border, or on cardstock and laminate. A 6×3 fits inside a standard **4×6 laminating pouch** with room to seal on all four sides.

Best placement: the **back of the seat back**, where a handler sees it before they lift. A second copy on the **side of the power base near the yellow freewheel levers** puts the instructions where the hands go.

**Scan-test it before it goes on.**

---

## Keeping it current

**Small text change:** in the repo, click `index.html` → pencil icon → edit → **Commit changes**. Live in about a minute.

**Change that should hit the page *and* the printed pieces:** edit the matching `build_*.py`, run `bash source/rebuild.sh` to regenerate everything, then `git add`, commit, and push both the source change and the regenerated `index.html` / PDFs. Keeping the generators in the repo alongside their outputs is what stops the page and the card from drifting apart.

**If the URL ever changes:**

```bash
pip install "qrcode[pil]"
python make-qr.py https://NEW-URL/
python build_sheet.py
python build_sticker.py
```

Use a **static** QR (encodes the URL directly), never a "dynamic" tracking QR from a service that can expire or start charging.

---

## Before each flight

- Call the airline's disability desk 48+ hours ahead. Give them **425 lbs**, **24″ W × 39″ L × 40″ H**, and **sealed gel-cell, non-spillable, no lithium**. Ask them to confirm the aircraft's cargo door clears those dimensions.
- Bring **two printed copies** of the sheet: one stays on the chair, one goes to the gate agent.
- Prep the chair: **headrest off, joystick swung in and secured, footplate folded up, power off** (toggle back, green indicator dark).
- **Photograph the chair from four sides at the gate** before handing it over. Timestamped photos are what settle a damage claim.
- If anything is damaged, get a **written** damage report at the airport before you leave.

## Verified on the chair, not assumed

- **Freewheel levers are yellow**, not red as the generic diagrams suggest.
- **24 in is the width at the drive wheels.** The armrests do not extend past them and are fixed — moving them narrows nothing.
- **39 in length** is with the footplate folded up.
- **The seat back is bolted to the frame.** No detent pin, no release lever. It does not fold or flip forward, despite the TRU-Balance 3 manual describing that as an option. The card says so explicitly so nobody tries to force it.
- **The joystick is not quickly removable** — it swings in and gets secured.
