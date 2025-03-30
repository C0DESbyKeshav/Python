# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

try:
    num = int(input("Enter a number: "))
    table = [(num * i) for i in range(1, 11)]
    print(table)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
