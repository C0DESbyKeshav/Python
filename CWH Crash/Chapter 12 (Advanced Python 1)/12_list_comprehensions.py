# List comprehension is an elegant way to create lists based on existing lists.

myList = [25, 1, 4, 3, 35]

squaredList = []
for item in myList:
    squaredList.append(item ** 2)
print(squaredList)

# The elegant way to do this
squaredList1 = [item ** 2 for item in myList]
# It will take each element of the myList, square it, and then will append them to the squaredList1 one by one.
print(squaredList1)
