# The best way to open and close the file automatically is the with statement
with open ("file3.txt") as f:
    print(f.read())
# Don't need to write f.close() as it is done automatically.
