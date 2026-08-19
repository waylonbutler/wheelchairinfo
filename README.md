# Wheelchair Airline Card — complete set

Everything for the Quantum Q6 Edge 3 handling card: the hosted page, the printed
sheet, the sticker, and the source to regenerate all three.

**Live page:** <https://waylonbutler.github.io/wheelchairinfo/>
**Repo:** `waylonbutler/wheelchairinfo`

---

## The four files you actually touch

| File | What to do with it |
|---|---|
| **`index.html`** | Upload to the GitHub repo. This is the page the QR code opens, and it holds the full detail. Self-contained — every diagram and photo is embedded, so it is the *only* file the repo needs. |
| **`Wheelchair Handling Sheet.pdf`** | Print double-sided (**flip on LONG edge**), laminate, punch at the red target, hang on the chair. Page 1 English, page 2 Spanish. |
| **`Wheelchair QR Sticker.pdf`** | One sticker, **4 × 2.5 in**. Print at 100% and put it on the back of the seat back. |
| **`HOSTING-SETUP.md`** | Printing steps, lamination and punch instructions, pre-flight checklist, and the facts verified on the chair rather than assumed. Read this one first. |

## Syncing

- **To Drive:** drop this whole folder in. It is the complete archive.
- **To the repo:** upload `index.html` only.

---

## How the three pieces divide the work

They are not three versions of the same thing. Each has one job.

- **Sticker** — read in two seconds by someone already reaching for the chair. Four lines, big type.
- **Sheet** — read in about thirty seconds by a handler in a cargo hold, possibly in bad light. Six numbered steps, plain words, roughly an 8th-grade reading level. No regulations, no model numbers, no manufacturer detail.
- **Web page** — read by whoever needs the whole story: airline staff at a desk, a repair tech, or you. Specs, photos, CFR citations, the controller, the circuit breaker.

**If you edit the printed pieces, keep them plain.** Detail belongs on the page. A card that reads like a legal notice gets skipped, and a skipped card protects nothing.

---

## `source/` — for regenerating

All wording lives in plain Python dictionaries at the top of each `build_*.py`,
English and Spanish side by side, so a text change is a one-line edit.

| File | Produces |
|---|---|
| `build_page.py` | `index.html` — bilingual, images embedded as data URIs |
| `build_sheet.py` | `Wheelchair Handling Sheet.pdf` — 2 pages, mirrored punch targets |
| `build_sticker.py` | `Wheelchair QR Sticker.pdf` — 4 × 2.5 in |
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

## Four things that are easy to break

**The punch targets on the sheet.** English and Spanish are scaled independently
to fit one page each, so the target is positioned *outside* the scaled layout. If
you change the layout, re-verify the two marks still align before laminating —
they should agree within a hundredth of an inch.

**The QR error correction.** Set to Q (25%), not H (30%). The current URL at H
pushes the module size too small to scan reliably through laminate. If the URL
gets longer, re-check module size rather than assuming it still works.

**No wiring detail, on purpose.** An earlier draft showed the manufacturer's
electrical diagram with the battery harness and quick-release connectors. It was
removed deliberately: this page is read by strangers handling the chair, and
showing them the wiring invites tinkering. The circuit breaker is the only
electrical item shown, because pressing it is the one safe recovery action.

**The push handles are push-only.** The two upright poles on the back of the seat
are the correct place to push from. They are not lift points, and the wording on
all three pieces says push, never lift. Keep that distinction if you reword it.
