import os
import re
from pathlib import Path

# ---------------- CONFIG ----------------
SOURCE_DIR = Path("/Users/as/Documents/lab/websites/altmerch.store/Sweet Poison")
TARGET_DIR = Path("/Users/as/Documents/lab/websites/altmerch.store/Sweet Poison/ready_for_print")

BASE_NAME = "sweet_poison"   # change if needed
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tiff"}
PADDING = 3  # 001, 002, 003 ...
# ----------------------------------------


def get_highest_index(folder: Path) -> int:
    pattern = re.compile(rf"{re.escape(BASE_NAME)}_(\d+)", re.IGNORECASE)
    max_index = 0

    for file in folder.iterdir():
        if file.is_file():
            match = pattern.search(file.stem)
            if match:
                max_index = max(max_index, int(match.group(1)))

    return max_index


def main():
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(f"Source folder not found: {SOURCE_DIR}")

    if not TARGET_DIR.exists():
        raise FileNotFoundError(f"Target folder not found: {TARGET_DIR}")

    current_index = get_highest_index(TARGET_DIR)
    print(f"Highest existing index in ready_for_print: {current_index}")

    images = sorted(
        [
            f for f in SOURCE_DIR.iterdir()
            if f.is_file()
            and f.suffix.lower() in IMAGE_EXTENSIONS
            and f.parent != TARGET_DIR
        ]
    )

    if not images:
        print("No images found to rename.")
        return

    for image in images:
        current_index += 1
        new_name = f"{BASE_NAME}_{str(current_index).zfill(PADDING)}{image.suffix.lower()}"
        new_path = image.with_name(new_name)

        if new_path.exists():
            raise FileExistsError(f"File already exists: {new_path}")

        image.rename(new_path)
        print(f"Renamed: {image.name} → {new_name}")

    print("Renaming completed successfully.")


if __name__ == "__main__":
    main()