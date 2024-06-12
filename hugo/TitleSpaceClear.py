import os
import shutil

def process_markdown_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                original_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, f"new_{file}")
                # 复制原文件
                shutil.copy2(original_file_path, new_file_path)
                # 处理复制后的文件
                process_file(new_file_path)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        if line.startswith("###"):
            # 删除行末尾的所有空格
            processed_lines.append(line.rstrip() + '\n')
            print(f"Processed line: {line.rstrip()}")
        else:
            processed_lines.append(line)

    # 写回处理后的内容到文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)
    print(f"Processed file: {file_path}")

if __name__ == "__main__":
    directory = "/Users/laloe74/project/PPoe/Hugo"
    process_markdown_files(directory)