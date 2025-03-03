# Write a python function to remove a given word from a list and strip it at the same time.


def rs(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = []
print("Enter three words:")
for i in range(0, 3):
    l.append(input())
print(l)
word = input("Enter the word to be stripped from the list:")
print(rs(l, word))
