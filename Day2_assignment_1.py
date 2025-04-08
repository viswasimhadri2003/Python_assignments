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

