#!/usr/bin/env python3
import os
import shutil
from PIL import Image
import subprocess

# Define source and destination folders
source_folder = os.path.expanduser("~/Downloads/Pictures/Cyberpunk")
destination_folder = os.path.expanduser("~/Downloads/Pictures/Cyberpunk/Delete")  # Moves small images here

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Define max width and max height
max_width, max_height = 200, 200  # Only images ≤ 200x200 pixels will be moved
moved_files = 0  # Counter for matched files

# Process each file in the folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # Skip non-image files
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".tiff", ".bmp")):
        continue

    try:
        with Image.open(file_path) as img:
            width, height = img.size

            # Move images that are SMALLER than or EQUAL TO 200x200 pixels
            if width <= max_width and height <= max_height:
                shutil.move(file_path, destination_folder)
                moved_files += 1
                print(f"Moved: {filename} (Resolution: {width}x{height})")

    except Exception as e:
        print(f"Skipping {filename}: {e}")

# Show a popup if no files were moved
if moved_files == 0:
    subprocess.run(['osascript', '-e', 'display notification "No images found under 200x200 pixels." with title "Image Processing Done"'])
else:
    subprocess.run(['osascript', '-e', f'display notification "{moved_files} images moved to Delete folder!" with title "Image Processing Done"'])
