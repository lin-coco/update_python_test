import os

def list_files_in_directory(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            file_paths.append(relative_path)
    return file_paths

# 使用示例
directory = "app"
files = list_files_in_directory(directory)
for file in files:
    print(file)