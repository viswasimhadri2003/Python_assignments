#Question 1

import os

def find_largest_file(directory):
    max_size = 0
    largest_file = None
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            
            if file_size > max_size:
                max_size = file_size
                largest_file = file_path
    
    return largest_file, max_size

directory_path = r"C:\Users\Adithya Charya\Desktop\python classes"
file_name, file_size = find_largest_file(directory_path)

print(f"The largest file is: {file_name}")
print(f"Size: {file_size} bytes")

#Question 2

import os

def read_and_write_files(source_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as out_file:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as in_file:
                        out_file.write(f"--- Content of {file_path} ---\n")
                        out_file.writelines(in_file.readlines())
                        out_file.write("\n\n")
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

# Set your directory and output file path
source_directory = r"C:\Users\Adithya Charya\Desktop\python assignments"
output_file_path = "c.txt"

read_and_write_files(source_directory, output_file_path)
print(f"All files' contents are written to {output_file_path}")