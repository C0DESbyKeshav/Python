# The 'enumerate' function adds counter to an iterable and returns it.

l = [25, 1, 4, 3, 35]

index = 0
for item in l:
    print(f"The item number {index} is ", item)
    index += 1
    # Prints the item of the list with index

print("\n")

# This can be simplified by using enumerate function
for indexNo, element in enumerate(l):
    print(f"The item number {indexNo} is ", element)
    # Prints the item of the list with index
