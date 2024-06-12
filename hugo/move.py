import os

def process_markdown_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 处理每一行
    processed_lines = []
    in_section = False
    for line in lines:
        if line.strip() == '-----':
            in_section = True
        if in_section:
            # 1. 如果行末有两个空格，删除这两个空格
            if line.endswith('  \n'):
                line = line[:-3] + '\n'
            # 2. 如果行末有一个空格，删除该空格
            elif line.endswith(' \n'):
                line = line[:-2] + '\n'
            # 3. 如果一行没有文字，则清空该行的所有内容
            if line.strip() == '':
                line = '\n'
        processed_lines.append(line)

    return processed_lines

def rename_old_file(file_path):
    directory, filename = os.path.split(file_path)
    old_filename = os.path.join(directory, f'old_{filename}')
    os.rename(file_path, old_filename)
    return old_filename

def write_processed_file(file_path, processed_lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)

def process_all_markdown_files():
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory):
        if filename.endswith('.md'):
            file_path = os.path.join(current_directory, filename)
            # 处理文件内容
            processed_lines = process_markdown_file(file_path)
            # 重命名旧文件
            rename_old_file(file_path)
            # 写入处理后的内容到原文件名
            write_processed_file(file_path, processed_lines)

if __name__ == '__main__':
    process_all_markdown_files()