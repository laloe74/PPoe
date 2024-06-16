import os

def modify_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            # Construct paths
            original_file = os.path.join(directory, filename)
            new_filename = f"new_{filename}"
            new_file = os.path.join(directory, new_filename)

            print(f"Processing file: {original_file}")

            try:
                # Step 1: Copy original file to new file
                with open(original_file, 'r', encoding='utf-8') as original:
                    lines = original.readlines()
                    if not lines:
                        print(f"Original file {original_file} is empty or could not be read.")
                    else:
                        print(f"Original file {original_file} has {len(lines)} lines.")
                    with open(new_file, 'w', encoding='utf-8') as modified:
                        for line in lines:
                            modified.write(line)
                            print(f"Copied line: {line.strip()}")

                print(f"Copied {len(lines)} lines to {new_file}")

                # Step 2: Modify the new file
                with open(new_file, 'r', encoding='utf-8') as modified:
                    content = modified.readlines()
                    if not content:
                        print(f"New file {new_file} is empty after copying.")
                    else:
                        print(f"New file {new_file} has {len(content)} lines after copying.")

                with open(new_file, 'w', encoding='utf-8') as modified:
                    under_line = False
                    first_line = True
                    for line in content:
                        print(f"Processing line: {line.strip()}")
                        if line.strip() == '-----':
                            under_line = True
                            modified.write(line)
                            print("Found '-----'")
                        elif under_line:
                            if first_line:
                                modified.write(line)
                                print(f"Writing first line under '-----': {line.strip()}")
                                first_line = False
                            elif line.strip() == '':
                                modified.write('　  \n')  # Add placeholder line
                                print("Writing placeholder line")
                            elif line.strip().startswith('###'):
                                modified.write(line.rstrip() + '\n')  # Remove trailing spaces for ### lines
                                print("Processed '###' line")
                            else:
                                modified.write(line.rstrip() + '  \n')  # Add two spaces at the end of other lines
                                print("Processed regular line")
                        else:
                            modified.write(line.rstrip() + '\n')  # Ensure there is no extra empty line at the end
                            print(f"Writing line above '-----': {line.strip()}")
                print(f"Modification complete for {new_file}")

            except Exception as e:
                print(f"Error processing file {original_file}: {e}")

def main():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    print(f"Script directory: {script_directory}")
    modify_markdown_files(script_directory)

if __name__ == "__main__":
    main()