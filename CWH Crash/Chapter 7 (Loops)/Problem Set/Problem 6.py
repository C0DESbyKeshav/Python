# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number: "))

fact = 1

if(num >= 0):
    for i in range(1, num + 1):
        fact = fact * i
    print(f"Factorial of {num} = {fact}")
else:
    print("Factorial is not defined for negative numbers.")
