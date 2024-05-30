import os
import json
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from PIL import Image
except ImportError:
    install("Pillow")
    from PIL import Image

repo_owner = "infinity-MSFS"
repo_name = "assets"
branch = "master"

links = {}

def generate_jsdelivr_url(file_path):
    return f"https://cdn.jsdelivr.net/gh/{repo_owner}/{repo_name}@{branch}/{file_path}"

output_file = "jsdeliver_links.json"
if os.path.exists(output_file):
    os.remove(output_file)

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".png"):
            png_path = os.path.join(root, file)
            webp_path = os.path.splitext(png_path)[0] + ".webp"
            
            try:
                png_image = Image.open(png_path)
                png_image.save(webp_path, 'WEBP')
                print(f"Converted {png_path} to {webp_path}")
            except Exception as e:
                print(f"Failed to convert {png_path}: {e}")
                continue

            relative_webp_path = os.path.relpath(webp_path, ".")
            relative_webp_path = relative_webp_path.replace("\\", "/")
            url = generate_jsdelivr_url(relative_webp_path)
            links[relative_webp_path] = url

with open(output_file, "w") as f:
    json.dump(links, f, indent=4)

print(f"JSON file generated: {output_file}")