# If names of 2 friends are same; what will happen to the program in Problem 6 ?
dict = {'Sherkhan': 'Python',
        'Sherkhan': 'BrainFuck'}
for i in range(3, 5):
    print("Friend", i)
    name = input("Enter your name: ")
    lang = input("Enter your favourite Language: ")
    dict.update({name:lang})
    print("\n")
print(dict)

# * Conclusion:
'''If a dictionary has two keys of the same name, then only one of those keys is considered.
The decision of choosing one of the value from the two values having same key names is done by: The last updated key value is considered.'''
