#!/usr/bin/env bash
# Regenerate every deliverable from source, then copy results up one level.
# Run from inside this source/ folder:  bash rebuild.sh
set -e
python3 annotate_controller.py     # numbered callouts on the controller photo
python3 annotate_breaker.py        # numbered callouts on the circuit-breaker photo
python3 build_page.py              # -> index.html
python3 build_sheet.py             # -> Wheelchair Handling Sheet.pdf
python3 build_sticker.py           # -> Wheelchair QR Sticker.pdf
cp index.html "Wheelchair Handling Sheet.pdf" "Wheelchair QR Sticker.pdf" ..
echo "Done. Updated files are in the parent folder."
