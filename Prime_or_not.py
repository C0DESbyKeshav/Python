# A program to check whether the user-entered number is prime or not.

num = int(input("Enter a number: "))

count = 0

if(num > 0):
    for i in range(2, num + 1):
        if(num % i == 0):
            count = count + 1
else:
    print("Prime and composite numbers are only defined for natural numbers.")

if count == 1:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
