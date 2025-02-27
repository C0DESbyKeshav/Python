# Write a program to greet all the person names stored in a list 'l' and which starts with 'R'

l = ["Keshav", "Ridhima", "Robin", "rahul", "Parth", "Sujal", "Rohan", "Gauri", "Sherkhan", "ram"]

for item in l:
    if (item[0].lower() == 'r'):
        print(f"おはよう {item} !!")
