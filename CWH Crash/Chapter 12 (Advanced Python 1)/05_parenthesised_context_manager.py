# You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager.
with (open ("file1.txt") as f1, open ("file2.txt") as f2): 
    print(f1.read())
    print("\n", f2.read())

# If one of the files fails to open, the context manager will automatically close all open files.
