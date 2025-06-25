# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and keys as their names. Assume that the names are unique.
dict = {}
for i in range(1, 5):
    print("Friend", i)
    name = input("Enter your name: ")
    lang = input("Enter your favourite Language: ")
    dict.update({name:lang})
    print("\n")
print(dict)
