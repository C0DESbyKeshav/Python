# Write a python program to rename a file to "renamed_by_python.txt"

# To achieve this, we first have to create another file and copy all the contents of the existing old file to the another file and then delete the existing old file.

with open("11_file.txt") as file:
    content = file.read()
with open("11_renamed_by_python.txt", "w") as file:
    file.write(content)

# To delete the old file: import os (for files) OR import shutil (for directories)

import os
os.remove("11_file.txt")
print("File renamed successfully!")
