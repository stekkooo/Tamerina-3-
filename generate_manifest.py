import os
import json

mods_folder = "mods"

mods = []

for file in os.listdir(mods_folder):
    if file.endswith(".jar"):
        mods.append({
            "name": file
        })

manifest = {
    "version": "1.0",
    "mods": mods
}

with open("manifest.json", "w") as f:
    json.dump(manifest, f, indent=4)

print("Manifest creato!")
