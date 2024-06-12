import os

def modify_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            # Construct paths
            original_file = os.path.join(directory, filename)
            new_filename = f"new_{filename}"
            new_file = os.path.join(directory, new_filename)

            # Copy original file to new file with prefix
            with open(original_file, 'r', encoding='utf-8') as original:
                with open(new_file, 'w', encoding='utf-8') as modified:
                    under_line = False
                    first_line = True
                    for line in original:
                        if line.strip() == '-----':
                            under_line = True
                            modified.write(line)
                        elif under_line:
                            if first_line:
                                modified.write(line)
                                first_line = False
                            elif line.strip() == '':
                                modified.write('　  \n')  # Add placeholder line
                            elif line.strip().startswith('###'):
                                modified.write(line.rstrip() + '\n')  # Remove trailing spaces for ### lines
                            else:
                                modified.write(line.rstrip() + '  \n')  # Add two spaces at the end of other lines
                        else:
                            modified.write(line.rstrip() + '\n')  # Ensure there is no extra empty line at the end

def main():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    modify_markdown_files(script_directory)

if __name__ == "__main__":
    main()