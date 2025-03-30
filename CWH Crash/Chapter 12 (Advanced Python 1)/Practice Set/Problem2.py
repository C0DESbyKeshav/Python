# Write a program to print third, fifth and seventh element from a list using enumerate function.

myList = ['I', "once", "loved", 'a', "flower", "so", "much", "that", "instead", "of", "picking", "it", 'I', "left", "it", "alone"]

for index, item in enumerate(myList):
    if index in [2, 4, 6]:
        print(item)
