# Write a program to filter a list of numbers which are divisible by 5.
print(list(filter(lambda x: (x % 5 == 0), [25, 5, 35, 2, 4])))
