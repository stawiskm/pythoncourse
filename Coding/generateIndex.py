import os

def list_files(startpath):
    with open("FileIndex.md", "w") as f:
        f.write("# File Index\n\n")
        for root, dirs, files in os.walk(startpath):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f"{indent}- **{os.path.basename(root)}/**\n")
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                if not file.startswith('.'):  # Skip hidden files
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, startpath)
                    f.write(f"{subindent}- [{file}]({relative_path})\n")

list_files('.')