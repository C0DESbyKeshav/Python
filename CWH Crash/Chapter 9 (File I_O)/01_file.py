# The random-access memory is volatile, and all its contents are lost once a program terminates in order to persist the data forever, we use files.
# A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.
# RAM --> Volatile, HDD --> Non-Volatile

''' Types of Files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)
'''

# Python has a lot of functions for reading, updating and deleting files.

# * Opening a File
# Python has an open() function for opening files. It takes 2 parameters: filename and mode.
# open("filename", "mode_of_opening")

f1 = open("file1.txt")  # Opens the file 'file1.txt'. By default the mode is read 'r'.
data = f1.read()  # read() function reads the contents of the file 'file1.txt and assigns it to variable 'data'.
print(data)
f1.close()  # Closes the file. Won't throw an error if skipped but always a good practice to close the file after done working on it.

print()

# Shortened Method:
f2 = open("file1.txt")
print(f2.read())
f2.close()

print()

# We can also specify the number of characters in read() function
f3 = open("file1.txt")
print(f3.read(6))  # Reads and prints first 6 characters
f3.close()

print()

# * Other Methods to Read the File
# We can also use the readline() function to read one full line at a time.
f4 = open("file1.txt")
print(f4.readline())  # Reads one complete line from the file
f4.close()

# * Modes of Opening a File
'''
r --> open for reading
w --> open for writing
a --> open for appending
+ --> open for updating

'rb' will open for read in binary mode
'rt' will open for read in text mode
'''
