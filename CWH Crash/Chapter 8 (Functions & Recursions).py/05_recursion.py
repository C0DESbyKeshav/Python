# Recursion should always have a base condition or else it throws an error.

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)


n = int(input("Enter a number: "))
print(f"Factorial of {n} is : {factorial(n)}")    
