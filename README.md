# image_tools

Small image-prep utilities (consolidated from former top-level `change_dpi`, `rename_images`, `move_images` projects). Each subfolder is standalone; install with `pip install -r <sub>/requirements.txt` (needs Pillow; each pins `pillow==12.2.0`, and the root `requirements.txt` lists unpinned `pillow` for all three).

## dpi/
- **dpi_resize_exact.py** — resizes PNGs to an exact 3600×4800 px (12"×16" @ 300 DPI), stretching to fit. Edit `input_folder` / `output_folder` at the top. Converts to RGBA, saves PNG with 300-DPI metadata into `output_folder` (created if missing); a file that fails is reported and skipped. Currently reads `~/Documents/Websites/altmerch.store/RAW` and writes the absolute `/Users/as/Documents/Websites/altmerch.store/changed_DPI`.
- **dpi_fit_canvas.py** — scales artwork proportionally and centers it on a 300-DPI canvas with a background color (no distortion). Edit the config block. Takes `.png`/`.jpg`/`.jpeg` from `~/Documents/Websites/altmerch.store/Sweet Poison`; the canvas is 3600×4800 px (12"×16"), black by default (`background_color`). Two known bugs (see TODO): `output_folder` is joined onto the input folder with an unexpanded `~`, so output lands in a literal `Sweet Poison/~/Documents/…/output_ready_for_print` folder; and a JPEG input stops the run, because the RGBA canvas cannot be saved as JPEG.

## rename/
- **rename_for_print.py** — batch-renames images to `sweet_poison_001`, `_002`, … continuing from the highest existing index in the target folder. Edit `SOURCE_DIR` / `TARGET_DIR` / `BASE_NAME`. Files are renamed **in place** in `SOURCE_DIR` (`.jpg .jpeg .png .webp .tiff`, sorted by name); `TARGET_DIR` (`…/Sweet Poison/ready_for_print`) is only read for the highest index. Both folders must exist, and the run stops at the first name collision.

## move/
- **move_small_images.py** — moves images ≤200×200 px into a `Delete` subfolder (cleanup of thumbnails/junk). Edit `source_folder`. Shows a macOS notification when done.
- **move_small_images.workflow** — Automator Quick Action wrapper for the same task. Note: its shell step runs `~/Documents/Tech/scripts/move_images.py`, not the script in this folder.

> Note: input/output paths are hardcoded at the top of each script — edit them per use. Since 2026-10-11 the `dpi/` and `rename/` scripts point at `~/Documents/Websites/altmerch.store/...` (RAW, Sweet Poison, changed_DPI, ready_for_print); `move/` points at `~/Downloads/Pictures/...`. None are lab-relative paths. The store folder itself currently lives at `~/Documents/Business/Merch/altmerch.store`, so check the path exists before a run.
