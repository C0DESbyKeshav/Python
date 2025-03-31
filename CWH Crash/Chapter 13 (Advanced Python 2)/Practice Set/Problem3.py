# A list contains the multiplication table of 7. Write a program to convert it to a vertical string of same numbers.

# Using List Comprehension to create a list containing the multiplication table of 7.
table = [str(7 * i) for i in range(1, 11)]
# converting each element into a string so that it works well with the join() function.

# To convert the list into a vertical string.
print("\n".join(table))
