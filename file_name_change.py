import os
def rename_files_with_spaces(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if ' ' in filename:
                new_filename = filename.replace(' ', '_')
                old_file = os.path.join(root, filename)
                new_file = os.path.join(root, new_filename)
                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} -> {new_file}")

directory_path = "/path/to/your/directory"
rename_files_with_spaces(directory_path)
