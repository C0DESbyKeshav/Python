# Write a program to find out whether a file is identical and matches the content of another file
with open("09_file1.txt") as file:
    content1 = file.read()
with open("09_file2.txt") as file:
    content2 = file.read()

if content1 == content2:
    print("The files are identical and has the same content.")
else:
    print("The files are not identical or do not have the same content.")
