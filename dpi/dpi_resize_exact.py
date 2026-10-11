import os
from PIL import Image

# === CONFIG ===
input_folder = os.path.expanduser("~/Documents/Websites/altmerch.store/RAW")
# Specified your absolute output path directly
output_folder = "/Users/as/Documents/Websites/altmerch.store/changed_DPI"
target_dpi = (300, 300)

# Set your final print size in inches
target_width_in = 12
target_height_in = 16

# Convert inches to pixels (12" * 300 = 3600px | 16" * 300 = 4800px)
target_px = (target_width_in * 300, target_height_in * 300)

# === CREATE OUTPUT FOLDER ===
os.makedirs(output_folder, exist_ok=True)

# === PROCESS ===
print(f"🚀 Processing images from: {input_folder}")
print(f"📂 Saving output to: {output_folder}\n")

for filename in os.listdir(input_folder):
    # 1. Check for PNG extension
    if filename.lower().endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 2. SAFETY: Skip the output directory if it exists inside the input folder
        if os.path.abspath(input_path) == os.path.abspath(output_folder):
            continue

        try:
            with Image.open(input_path) as img:
                img = img.convert("RGBA")
                
                # Resize to exact dimensions (LANCZOS for high-quality downsampling/upsampling)
                resized = img.resize(target_px, Image.Resampling.LANCZOS)
                
                # Save with metadata for 300 DPI
                resized.save(output_path, "PNG", dpi=target_dpi)
                print(f"✅ Processed: {filename}")
                
        except Exception as e:
            print(f"❌ Failed: {filename} – Error: {e}")

print(f"\n🎯 Done! Your 300 DPI files are ready in: {output_folder}")