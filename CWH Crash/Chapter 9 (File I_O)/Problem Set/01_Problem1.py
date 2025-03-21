# Write a program to read the text from a given file "01_poem.txt" and find out whether it contains the word 'darr'.
bool = False
with open("01_poem.txt") as file:
    for line in file:
        for word in line.split():
            if word == "darr":
                bool = True;
if bool == True:
    print("'darr' is present in the given poem.")
else:
    print("'darr' is not present in the given poem.")
