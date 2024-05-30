import os
import json

repo_owner = "infinity-MSFS"
repo_name = "groups"
branch = "main"


links = {}

def generate_jsdelivr_url(file_path):
    return f"https://cdn.jsdelivr.net/gh/{repo_owner}/{repo_name}@{branch}/{file_path}"

    
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".png"):
            relative_path = os.path.relpath(os.path.join(root, file), ".")
            relative_path = relative_path.replace("\\", "/")
            url = generate_jsdelivr_url(relative_path)
            links[relative_path] = url
            
            
output_file = "jsdeliver_links.json"
with open(output_file, "w") as f:
    json.dump(links, f, indent = 4)
    
print(f"JSON file generated: {output_file}")