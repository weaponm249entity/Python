import os
import json

def get_directory_structure(root_path):
    dir_name = os.path.basename(root_path)
    structure = {
        "directory_name": dir_name,
        "path": root_path,
        "files": [],
        "subdirectories": []
    }
    with os.scandir(root_path) as entries:
        for entry in entries:
            if entry.is_file():
                structure["files"].append(entry.name)
            elif entry.is_dir():
                structure["subdirectories"].append(get_directory_structure(entry.path))
    return structure
target_directory = "/home/revenant/Github/" 
output_filename = "file_structure.json"

print(f"Scanning directory: {os.path.abspath(target_directory)}...")
file_data = get_directory_structure(target_directory)

print("Saving to JSON file...")
with open(output_filename, 'w', encoding='utf-8') as json_file:
    json.dump(file_data, json_file, indent=4, ensure_ascii=False)

print(f"Done! Data saved to '{output_filename}'.")