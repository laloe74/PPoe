# python /Users/laloe74/project/PPoe/md_fix/md_fix.py

import os

def process_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    is_processing = False

    for line in lines:
        line_content = line.rstrip('\n')
        if line_content.startswith("-----"):
            is_processing = True
        if is_processing:
            if line_content:
                processed_lines.append(line_content + "  ")
            else:
                processed_lines.append("　  ")
        else:
            processed_lines.append(line_content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(processed_lines))

def process_all_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            input_file = os.path.join(directory, filename)
            output_file = os.path.join(directory, f"p_{filename}")
            process_markdown(input_file, output_file)
            print(f"Processed {input_file} and saved as {output_file}")

if __name__ == "__main__":
    directory = "/Users/laloe74/project/PPoe/md_fix"
    process_all_markdown_files(directory)