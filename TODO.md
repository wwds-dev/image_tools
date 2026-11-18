# image_tools — TODO

> **Legend** — priority `P0` critical · `P1` high · `P2` normal · `P3` low
> categories `security` `bug` `feature` `performance` `design` `docs` `testing` `infra` `research`
> owner `@me` (needs you — accounts, keys, money, judgement) · `@ai` (Claude can do this)

---

## v1 — current

- [ ] `P1` `bug` `@ai` **Every path is hardcoded at the top of every script.** `input_folder`, `output_folder`, `SOURCE_DIR`, `TARGET_DIR`, `BASE_NAME`, `source_folder` — all edited by hand before each run, and all pointing at external `~/Documents/Business/…` and `~/Downloads/…` folders. Replace with `argparse`.
- [x] `P1` `bug` `@me` `dpi/` and `rename/` pointed at a different altmerch.store folder than the real one. Resolved 2026-11-17: the store moved to `~/Documents/lab/websites/altmerch.store` and the scripts point there.
- [ ] `P1` `bug` `@ai` `dpi_fit_canvas.py` builds `output_folder` as `os.path.join(input_folder, "~/Documents/lab/websites/…/output_ready_for_print")`; the `~` is never expanded, so output lands in a literal `Sweet Poison/~/Documents/lab/websites/altmerch.store/Sweet Poison/output_ready_for_print` folder inside the input folder.
- [ ] `P1` `bug` `@ai` `dpi_fit_canvas.py` accepts `.jpg`/`.jpeg` but saves the RGBA canvas under the original name; Pillow refuses RGBA as JPEG (`OSError`), and with no try/except the whole run stops at the first JPEG.
- [ ] `P2` `bug` `@ai` `move_small_images.workflow` runs `~/Documents/Tech/scripts/move_images.py`, not `move/move_small_images.py` from this repo. Point it at the repo copy.
- [ ] `P1` `bug` `@ai` `move_small_images.py` moves files into a `Delete` subfolder with no dry-run and no undo. Add `--dry-run` before it eats something.
- [ ] `P1` `bug` `@ai` **`rename_for_print.py` cannot be re-run, and keeps no record of the old names.** It renames in place in `SOURCE_DIR` but reads the next index only from `TARGET_DIR` (`rename_for_print.py:36,47-57`), so its own output (`sweet_poison_001.png`, still in the source folder) is picked up again and the next run stops with `FileExistsError` on the first file (verified on a scratch copy); when new files sort after the old ones it renames some and then stops half-way. Original filenames are lost with no mapping and no `--dry-run`. Write an `old → new` log (CSV) first, skip files already matching `BASE_NAME_\d+`, and compute the index from both folders.
- [ ] `P1` `bug` `@ai` **Hard rule: no `/Users/...` paths.** `dpi_resize_exact.py:7`, `rename_for_print.py:6-7` hardcode `/Users/as/...`; the other scripts use `~`. Fold into the argparse item, but at minimum use `Path.home()`.
- [ ] `P2` `bug` `@ai` **Scripts overwrite silently, and `dpi_resize_exact.py`'s safety check does nothing.** Both DPI scripts save over an existing file of the same name (`dpi_fit_canvas.py:35`, `dpi_resize_exact.py:35`); the "skip the output directory" test at `dpi_resize_exact.py:27` compares a file path with a folder path and can never be true. `dpi_fit_canvas.py` also runs at import (no `main()` guard) and creates its output folder (the literal `~` one) before looping. Add skip-if-exists or `--overwrite`, and a `main()`.
- [ ] `P2` `bug` `@ai` **The Automator workflow could not work even if repointed.** `~/Documents/Tech/scripts/move_images.py` does not exist on this machine (verified), the Run Shell Script step has `inputMethod` 0 (stdin) and passes no folder, and `move_small_images.py` has no argument for one. Do this after the argparse item: pass the selected folder as `"$@"` and call the repo script by a stable path.
- [ ] `P3` `bug` `@ai` `move_small_images.py` creates `Delete` before checking the source (`move_small_images.py:10,13`), so a wrong `source_folder` raises `FileNotFoundError` after making an empty folder in `~/Downloads`; check the source first.
- [ ] `P2` `bug` `@ai` `rename_for_print.py` continues from the highest existing index in the target folder — no test covers what happens with gaps, non-matching filenames, or a collision
- [ ] `P2` `testing` `@ai` No tests anywhere in the project. Start with the rename indexer, which is the one with real logic.
- [ ] `P2` `design` `@ai` Three subfolders each with their own `requirements.txt`, all of which are just Pillow. One venv would do.
- [ ] `P3` `feature` `@ai` `dpi_resize_exact.py` stretches to fit and distorts; warn when the source aspect ratio differs from 3:4
- [ ] `P3` `docs` `@ai` Document the 3600×4800 @ 300 DPI target in terms of the print sizes it is for, not just the pixel count

## v2 — if it grows

- [ ] `P2` `feature` `@ai` A single `image_tools` CLI with `dpi`, `rename` and `move` subcommands
- [ ] `P3` `feature` `@ai` Lab Hub already vendors these under *Prepare Images* — make that the primary interface and keep the scripts as the engine
- [ ] `P3` `feature` `@ai` Progress output on large batches; currently silent until done
