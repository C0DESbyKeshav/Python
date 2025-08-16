# A program to print the factorial of a user-entered number.

num = int(input("Enter a number: "))
fact = 1
i = 1
if (num >= 0):
    while i <= num:
        fact = fact * i
        i = i + 1
    print(f"Factorial of {num} = {fact}")
else:
    print("Factorial is not defined for negative numbers.")
    
