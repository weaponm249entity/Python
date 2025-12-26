import os
import json

def get_directory_structure(root_path):
    """
    Recursively scans a directory and builds a dictionary representing
    the structure of files and subdirectories.
    """
    # Get the name of the current folder
    dir_name = os.path.basename(root_path)
    
    # Initialize the dictionary structure for this folder
    # We use a standard format: Name, Files (list), and Subdirectories (list of dicts)
    structure = {
        "directory_name": dir_name,
        "path": root_path,
        "files": [],
        "subdirectories": []
    }

    try:
        # os.scandir is faster and more efficient than os.listdir for this
        with os.scandir(root_path) as entries:
            for entry in entries:
                if entry.is_file():
                    # If it's a file, add just the name to the files list
                    structure["files"].append(entry.name)
                elif entry.is_dir():
                    # If it's a directory, RECURSION happens here.
                    # We call the function again on the subfolder.
                    structure["subdirectories"].append(get_directory_structure(entry.path))
                    
    except PermissionError:
        # Handle cases where the script doesn't have permission to access a folder
        structure["error"] = "Permission Denied"

    return structure

# --- CONFIGURATION ---
# Replace this with the directory you want to scan
target_directory = "/home/revenant/Github/"  # "." means the current folder where this script is running
output_filename = "file_structure.json"

# --- EXECUTION ---
print(f"Scanning directory: {os.path.abspath(target_directory)}...")
file_data = get_directory_structure(target_directory)

print("Saving to JSON file...")
with open(output_filename, 'w', encoding='utf-8') as json_file:
    # indent=4 makes the JSON human-readable (pretty-printed)
    json.dump(file_data, json_file, indent=4, ensure_ascii=False)

print(f"Done! Data saved to '{output_filename}'.")