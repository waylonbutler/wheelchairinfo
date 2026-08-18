# Wheelchair Airline Card — complete set

Everything for the Quantum Q6 Edge 3 handling card: the hosted page, the printed
sheet, the sticker, and the source to regenerate all three.

**Live page:** <https://waylonbutler.github.io/wheelchairinfo/>
**Repo:** `waylonbutler/wheelchairinfo`

---

## The four files you actually touch

| File | What to do with it |
|---|---|
| **`index.html`** | Upload to the GitHub repo. This is the page the QR code opens. Self-contained — every diagram and photo is embedded, so it is the *only* file the repo needs. |
| **`Wheelchair Handling Sheet.pdf`** | Print double-sided (**flip on LONG edge**), laminate, punch at the red target, hang on the chair. Page 1 English, page 2 Spanish. |
| **`Wheelchair QR Sticker.pdf`** | Print page 1 (6×3 in) and stick it on the back of the seat back. Page 2 is a 4×2 in fallback. |
| **`HOSTING-SETUP.md`** | Printing steps, lamination and punch instructions, pre-flight checklist, and the list of facts verified on the chair rather than assumed. Read this one first. |

## Syncing

- **To Drive:** drop this whole folder in. It is the complete archive.
- **To the repo:** upload `index.html` only.

Keep the two in step. If the printed card and the live page disagree, the card
is the one in the handler's hands.

---

## `source/` — for regenerating

Only needed if something about the chair changes. All wording lives in plain
Python dictionaries at the top of each `build_*.py`, English and Spanish side by
side, so a text change is a one-line edit.

| File | Produces |
|---|---|
| `build_page.py` | `index.html` — bilingual, images embedded as data URIs |
| `build_sheet.py` | `Wheelchair Handling Sheet.pdf` — 2 pages, mirrored punch targets |
| `build_sticker.py` | `Wheelchair QR Sticker.pdf` — 6×3 in and 4×2 in |
| `annotate_controller.py` | `img-controller.jpg` — callouts on the controller |
| `annotate_breaker.py` | `img-breaker.jpg` — callouts on the circuit breaker |
| `make-qr.py` | `qr.png` — only if the URL ever changes |
| `rebuild.sh` | Runs all of the above and copies results up a level |

```bash
cd source
bash rebuild.sh
```

Requires Python 3 with `pillow` and `qrcode`, plus a headless Chromium for the
PDFs (path is set at the top of each build script — adjust if yours differs).

### Assets

- `img-freewheel`, `img-brackets`, `img-points-iso`, `img-points-plan` — figures
  from the Quantum owner's manual.
- `ql.jpg` → `img-controller.jpg` — the controller, unannotated and annotated.
- `chair.jpg` → `img-breaker.jpg` — photo of this chair, and the cropped
  circuit-breaker view built from it.

---

## Three things that are easy to break

**The punch targets on the sheet.** English and Spanish use different scale
factors to fit one page each, so the target is positioned *outside* the scaled
layout. If you change the layout, re-verify the two marks still align before
laminating — they should agree within a hundredth of an inch.

**The QR error correction.** Set to Q (25%), not H (30%). The current URL at H
pushes the module size too small to scan reliably through laminate. If the URL
gets longer, re-check module size rather than assuming it still works.

**No wiring detail, on purpose.** An earlier draft showed the manufacturer's
electrical diagram with the battery harness and quick-release connectors. It was
removed deliberately: this page is read by strangers handling the chair, and
showing them the wiring invites tinkering. The circuit breaker is the only
electrical item shown, because pressing it is the one safe recovery action. If
you ever add electrical content back, keep that line in mind.
