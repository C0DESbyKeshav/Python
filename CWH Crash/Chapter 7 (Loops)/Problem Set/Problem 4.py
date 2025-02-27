# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))

if (num == 1):
    print("1 is neither prime nor composite number.")
elif(num > 0):
    for i in range(2, num):
        if(num % i == 0):
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print("Prime and composite numbers are only defined for natural numbers.")
