''' Write a program to print the contents of a directory using the os module.
Search online for the function which does that. '''

import os

# Specify the directory you want to list
directory_path = "."  # Replace with your directory path

# Check if the path exists
if os.path.exists(directory_path):
    # Get the list of files and directories
    contents = os.listdir(directory_path)

    # Print the contents
    print("Contents of the directory:")
    for item in contents:
        print(item)
else:
    print(f"The directory {directory_path} does not exist.")
