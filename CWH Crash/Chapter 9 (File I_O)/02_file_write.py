
# * Writing Files in Python
# In order to write to a file, we first open it in 'write' mode or 'append' mode after which, we use the python's f.write() method to write to the file.

f1 = open("file2.txt", 'w')  # Opens the file in write mode

# Writing into the opened file 'file1.txt'
f1.write("Name of all the users:\n")

f1 = open("file2.txt", 'a')  # Opens the file in append mode
f1.write("Keshav\n")
f1.write("Sukii\n")
f1.write("Ridhav\n")

f1 = open("file2.txt")  # Opening the file in read mode (by default)
print(f1.read())  # Read the contents of the opened file 'file2.txt'

# Never forget to close the file
f1.close()
