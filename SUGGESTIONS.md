# image_tools — Suggestions

Status: `IDEA` · `CONSIDERING` · `PLANNED` · `DONE` · `REJECTED`

---

## Open

| # | Suggestion | Category | Effort | Status |
|---|---|---|---|---|
| 1 | `argparse` on all five scripts, replacing hand-edited constants | bug | S | PLANNED |
| 2 | `--dry-run` on `move_small_images.py` before it deletes something wanted | bug | XS | PLANNED |
| 3 | One `image_tools` CLI with `dpi` / `rename` / `move` subcommands | design | M | CONSIDERING |
| 4 | Tests for the rename indexer — gaps, collisions, non-matching names | testing | S | PLANNED |
| 5 | One shared venv instead of three `requirements.txt` files that all say Pillow | design | XS | CONSIDERING |
| 6 | Aspect-ratio warning before a distorting stretch | feature | S | CONSIDERING |
| 7 | Progress output on large batches | design | XS | IDEA |
| 8 | Treat Lab Hub's *Prepare Images* tab as the primary interface | design | M | IDEA |
| 9 | Fix `dpi_fit_canvas.py`: expand the output path properly and flatten to RGB before saving JPEGs | bug | XS | PLANNED |
| 10 | Point the Automator workflow at `move/move_small_images.py` instead of `~/Documents/Tech/scripts/move_images.py` | bug | XS | PLANNED |

## Done

| Suggestion | When |
|---|---|
| Consolidated from three top-level projects (`change_dpi`, `rename_images`, `move_images`) into one repo | Jun 2026 |
| Automator Quick Action wrapper for `move_small_images` | Jun 2026 |

## Rejected

| Suggestion | Why |
|---|---|
