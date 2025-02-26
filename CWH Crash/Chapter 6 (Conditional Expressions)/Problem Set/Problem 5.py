# Write a program which finds out whether a given name is present in the list or not.

names = ["Keshav", "Sherkhan", "Mayur", "Sid", "Kurkura", "Sanju", "Shadow"]
name = input("Enter a name: ")
if name.title() in names:
  print(f"\"{name}\" is present in the list of names.")
else:
    print(f"\"{name}\" is not present in the list of names.")
