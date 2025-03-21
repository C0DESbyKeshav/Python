f = open("file3.txt")
# print(f.readlines())  # returns the contents of the file as a list where each line being the consecutive element of the list
# print(type(f.readlines()))

print()

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()
