# Write a program to make a copy of a text file "this.txt".
with open("08_this.txt") as file:
    content = file.read()
with open("08_copy_this.txt", "w") as file:
    file.write(content)
