# image_tools

Small image-prep utilities (consolidated from former top-level `change_dpi`, `rename_images`, `move_images` projects). Each subfolder is standalone; install with `pip install -r <sub>/requirements.txt` (needs Pillow).

## dpi/
- **dpi_resize_exact.py** — resizes PNGs to an exact 3600×4800 px (12"×16" @ 300 DPI), stretching to fit. Edit `input_folder` / `output_folder` at the top.
- **dpi_fit_canvas.py** — scales artwork proportionally and centers it on a 300-DPI canvas with a background color (no distortion). Edit the config block.

## rename/
- **rename_for_print.py** — batch-renames images to `sweet_poison_001`, `_002`, … continuing from the highest existing index in the target folder. Edit `SOURCE_DIR` / `TARGET_DIR` / `BASE_NAME`.

## move/
- **move_small_images.py** — moves images ≤200×200 px into a `Delete` subfolder (cleanup of thumbnails/junk). Edit `source_folder`. Shows a macOS notification when done.
- **move_small_images.workflow** — Automator Quick Action wrapper for the same task.

> Note: input/output paths are hardcoded at the top of each script — edit them per use. They point at external `~/Documents/Business/...` and `~/Downloads/...` folders, not lab-relative paths.
