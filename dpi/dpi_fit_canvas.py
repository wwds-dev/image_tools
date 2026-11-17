import os
from PIL import Image

# === CONFIG ===
input_folder = os.path.expanduser("~/Documents/lab/websites/altmerch.store/Sweet Poison")
output_folder = os.path.join(input_folder, "~/Documents/lab/websites/altmerch.store/Sweet Poison/output_ready_for_print")

# Print specs
target_dpi = (300, 300)
target_width_in  = 12
target_height_in = 16
target_px = (target_width_in * 300, target_height_in * 300)

# Background color: (0,0,0,255)=black; (255,255,255,255)=white; (0,0,0,0)=transparent
background_color = (0, 0, 0, 255)

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    with Image.open(input_path) as img:
        img = img.convert("RGBA")

        # Compute proportional scale
        scale = min(target_px[0] / img.width, target_px[1] / img.height)
        new_size = (int(img.width * scale), int(img.height * scale))
        resized = img.resize(new_size, Image.LANCZOS)

        # Make new print canvas
        canvas = Image.new("RGBA", target_px, background_color)

        # Center artwork
        offset = ((target_px[0] - new_size[0]) // 2, (target_px[1] - new_size[1]) // 2)
        canvas.paste(resized, offset, resized)

        # Save with correct DPI
        canvas.save(output_path, dpi=target_dpi)

        print(f"✅ {filename}: {canvas.width}x{canvas.height}px ({target_width_in}x{target_height_in}in @ 300 DPI)")