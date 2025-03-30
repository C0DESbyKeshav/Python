# Write a program to open 3 files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with(open("1.txt") as f1, open("2.txt") as f2, open("3.txt") as f3):
        print("All the files opened successfully.")
except:
    print("One or more files are missing.")
    print("Please check again if all the files are present or not.")
