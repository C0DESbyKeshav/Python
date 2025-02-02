print(" LIST ".center(200, '-'))
print("\n")

# * LISTS
# Python lists are containers to store a set of values of any data type.
list = ["Apple", "Grapes", 3, 5.1, False, True, "Keshav"]
print("List 'list': ", list)
print("\nElement of list at index 0: ", list[0])
list[0] = "Banana"  # UNLIKE STRINGS, LISTS ARE MUTABLE.
print("Element of list at index 0 after changing the content: ", list[0])

print("\n")
print(" LIST SLICING ".center(200, '-'))

# * LIST SLICING
# List slicing is same as string slicing.
print("\nList Slicing from 1 to 5: ", list[1:5])  # excluding 5

print("\n")
print(" LIST METHODS ".center(200, '-'))

# * LIST METHODS
# NOTE: List methods affects the original / previous list unlike string's methods.

l1 = [3, 21, 0, 193, 5.6, -6, 89]
print("\nList 'l1': ", l1)

l1.sort()  # updates the list to [-6, 0, 3, 5.6, 21, 89, 193]
# This function only works on the lists having all numerical values.
print("\nAfter sorting the list: ", l1)

l1.reverse()  # updates the list to [193, 89, 21, 5.6, 3, 0, -6]
print("\nAfter reversing the list 'l1': ", l1)
list.reverse()  # updates the list to ['Keshav', True, False, 5.1, 3, 'Grapes', 'Banana']
print("After reversing the list 'list': ", list)

l1.append(8)  # appends 8 at the end of the list.
print("\nAfter appending 8 to the list 'l1': ", l1)
list.append("Python")  # appends 'Python' at the end of the list.
print("After appending \"Python\" in the list 'list': ", list)

l1.insert(3, 86)  # this will add 86 at index 3.
print("\nAfter inserting 86 at index 3 in the list 'l1': ", l1)
list.insert(4, 11)  # this will add 11 at index 4.
print("After inserting 11 at index 4 in the list 'list': ", list)

l1.pop(2)  # this will delete element at index 2 and return its value.
print("\nAfter popping the element at index 2 in the list 'l1': ", l1)
list.pop(2)  # this will delete element at index 2 and return its value.
print("After popping the element at index 2 in the list 'list': ", list)

l1.remove(89)  # this will remove 89 from the list.
print("\nAfter removing 89 from the list 'l1': ", l1)
list.remove(3)  # this will remove 3 from the list.
print("After removing 3 from the list 'list': ", list)

# This function only works on the lists having all numerical values.
print("\nAll the numbers in the list sums up to: ", sum(l1))
